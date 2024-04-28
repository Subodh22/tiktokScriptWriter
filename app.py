import streamlit as st
from dotenv import load_dotenv
load_dotenv()
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI


llm = ChatOpenAI(
    model="gpt-3.5-turbo"

)

prompt = ChatPromptTemplate.from_messages([
    ("system","You are a friendly assistant named max"),
    ("human","{input}")
])

chain= prompt | llm
print("ok")
response =chain.invoke({"input":"What is your name"})

st.write(response["content"])