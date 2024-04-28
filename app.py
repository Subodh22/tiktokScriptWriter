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
    ("system","""You are a professional scriptwriter. Take the user's input and transform into a short, catchy TikTok script suitable for engaging a wide audience. The script should be structured as follows:

- **Hook**: Start with a compelling opening line to grab attention.
- **Content**: Break down the main points into concise, impactful statements.
- **Call to Action**: End with a motivating call to action that encourages viewer interaction.

Ensure the script is formatted in bullet points and tailored to resonate with a TikTok audience, making it both memorable and sharable.
     """),
    ("human","{input}")
])
outputParser=StrOutputParser()
chain= prompt | llm | outputParser
print("ok")
def cutMyScript(user_input):
    response =chain.invoke({"input":user_input})
    return response
user_input=st.text_area(label="input",height=200)

if st.button("transform") :
     if user_input!=" ":
          st.write("Please type something")
     response=cutMyScript(user_input)
     st.write(response)
 
# st.write(response)