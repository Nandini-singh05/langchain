from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langserve import add_routes

import os
from secret_key import GROQ_API_KEY
os.environ["GROQ_API_KEY"] = GROQ_API_KEY

system_template = "Translate the following to {language}."
prompt = ChatPromptTemplate.from_messages([
    ("system", system_template),
    ("user", '{text}')
])

model = ChatGroqmodel = ChatGroq()

parser = StrOutputParser()

chain = prompt | model | parser

app = FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A simple translation tool using langchain.",
)

add_routes(
    app,
    chain,
    path='/chain'
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)