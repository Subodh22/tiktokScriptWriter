import streamlit as st
from dotenv import load_dotenv
load_dotenv()
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
OPENAI_API_KEY=st.secrets["OPENAI_API_KEY"]

llm = ChatOpenAI(
    model="gpt-3.5-turbo"

)

prompt = ChatPromptTemplate.from_messages([
    ("system","You are a friendly assistant named max"),
    ("human","{input}")
])
outputParser=StrOutputParser()
chain= prompt | llm | outputParser
print("ok")
response =chain.invoke({"input":"What is your name"})

st.write(response)