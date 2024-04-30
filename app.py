import streamlit as st
from dotenv import load_dotenv
load_dotenv()
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain import hub
from langchain_core.output_parsers import StrOutputParser
OPENAI_API_KEY=st.secrets["OPENAI_API_KEY"]

prompt = hub.pull("kanxu/tiktokscriptwriter")
llm = ChatOpenAI(
    model="gpt-4-turbo",
    temperature=0.8

)

# prompt = ChatPromptTemplate.from_messages([
# #     ("system","""You are a professional scriptwriter. Take the user's input and transform into a short, catchy TikTok script suitable for engaging a wide audience. The script should be structured as follows:

# # - **Hook**: Start with a compelling opening line to grab attention.
# # - **Content**: Break down the main points into concise, impactful statements.
# # - **Call to Action**: End with a motivating call to action that encourages viewer interaction.

# # Ensure the script is formatted in bullet points and tailored to resonate with a TikTok audience, making it both memorable and sharable.
# #      """),
# ("system","""
# # Role 
# 		Act as MrBeast script writer, who writes short and engaging scripts for  MrBeast that helps him gain thousands of subscribers.
		
# 	# Task 
# 		Take the essay of topic given by the user and generate a script for engaging, informative video script about it. Make the content clear, concise and easy to understand for a general audience. 
# 		Use this step by step process to ensure your script is top-notch:
# 		1. Hook the viewer with an attention-grabbing opening line
# 		2. Briefly explain the key concepts or ideas related to the topic
# 		3. Add 1-2 fascinating facts or statistics to illustrate the importance of the topic this is the most important
# 		4. Give 1-2 ways it can impact the users day to day life
# 		5. Describe the main takeaway or action viewers should remember
# 		6. End with powerful closing line that reinforces the message
# 		7. Review the entire script for conciseness and flow
#         8.Put the answer in same format as example and make it under 40 seconds and label hook, content, intresting facts , call to action and all of them time stamped
 
	
# 	# Specifics
# 		 - Script should hold the strong attention of the user by relating to them.
# 		 - Your message should call the user to action. 
# 		 - It should impact the life of the user.
# 		 - The script should be polarising so that different user can have                      different reaction to the same script.
# 		 - Script should invoke some kind of emotional reaction from the user. 
		 
# 	# Context:
# 		Our Company provides scripts to top tiktokers and content creator in the world. We have receive a high volume of demand to write scripts. Your role is to come up with the highly addicting and attention grabbing scripts to contribiute the growth of the user and for the sucess of the company.
		
# 	# Tools
# 		1. Knowledge base of MrBeast's Youtube transcripts to be used when writing this script.

# 	# Examples 
# 		1:What if earth was the size of Jupiter?
# 			00:00:00.080 --> 00:00:02.440
# 			What if earth was the size of Jupiter?
			
# 			00:00:02.441 --> 00:00:04.721
# 			Jupiter is insanely big,
			
# 			00:00:04.722 --> 00:00:09.761
# 			11 times wider than earth and capable of fitting 13 Earths inside it.
			
# 			00:00:09.762 --> 00:00:13.261
# 			These are real scale models of the earth and Jupiter.
			
# 			00:00:13.720 --> 00:00:17.160
# 			Kind of scary how big Jupiter really is.
			
# 			00:00:17.161 --> 00:00:21.401
# 			For starters, gravity would be 11 times stronger than it currently is,
			
# 			00:00:21.402 --> 00:00:24.561
# 			meaning if you weigh around 80 kg here on earth,
			
# 			00:00:24.562 --> 00:00:28.161
# 			you would weigh nearly eight pun on this new super earth.
			
# 			00:00:28.162 --> 00:00:30.201
# 			Since the earth would be so much bigger,
			
# 			00:00:30.202 --> 00:00:32.521
# 			assuming our rotation speed stayed the same,
			
# 			00:00:32.522 --> 00:00:36.961
# 			a single day on earth would now last 269 hours.
			
# 			00:00:36.962 --> 00:00:38.681
# 			And perhaps most terrifyingly,
			
# 			00:00:38.682 --> 00:00:41.721
# 			the asteroid belt would be pulled towards the super earth
			
# 			00:00:41.722 --> 00:00:43.621
# 			due to the intense pull of gravity,
			
# 			00:00:43.760 --> 00:00:47.480
# 			causing the surface to be constantly bombarded by huge
			
# 			00:00:47.481 --> 00:00:49.721
# 			asteroid collisions. On the bright side, though,
			
# 			00:00:49.722 --> 00:00:52.081
# 			our moon would likely be torn apart
			
# 			00:00:52.082 --> 00:00:54.241
# 			and made into these beautiful rings.
			
# 			00:00:54.242 --> 00:00:57.935
# 			So if you did survive, at least you'd have a nice view.

	
# 		2. What happens every second on earth:
# 			00:00:00.000 --> 00:00:04.120
# 			I wanna show you what happens in just one second here on earth. Ready?
			
# 			00:00:04.121 --> 00:00:06.801
# 			Four babies are born and two people die.
			
# 			00:00:06.802 --> 00:00:09.281
# 			2.5 million emails are sent
			
# 			00:00:09.282 --> 00:00:12.921
# 			and nearly 100,000 images are uploaded to Instagram.
			
# 			00:00:12.922 --> 00:00:17.601
# 			28 football fields worth of trees is cut down due to deforestation.
			
# 			00:00:17.602 --> 00:00:20.761
# 			Light travels around the globe more than seven times.
			
# 			00:00:20.762 --> 00:00:23.321
# 			And in the 20 seconds you've been watching this video,
			
# 			00:00:23.322 --> 00:00:26.281
# 			the earth has received enough solar power from the sun
			
# 			00:00:26.282 --> 00:00:30.081
# 			to charge your phone for nearly 20 million years.
			
# 			00:00:30.082 --> 00:00:32.241
# 			And it goes even deeper than that.
			
# 			00:00:32.242 --> 00:00:35.881
# 			The earth has travelled 230 km through the galaxy
			
# 			00:00:35.882 --> 00:00:37.841
# 			every second in this video.
			
# 			00:00:37.842 --> 00:00:39.321
# 			And during the length of this video,
			
# 			00:00:39.322 --> 00:00:42.901
# 			Jeff Bezos has made over $100,000.
			
# 			00:00:43.280 --> 00:00:44.489
# 			Seems fair, right?


# 	# Notes:
# 		 - Always tailor your responses to specific needs and context of the user's query.
# 		 - Avoid making any generic scripts and be more creative and edgy.
# 		 - Ensure that story has context.
	 
	 

# """),



#     ("human","{input}")
# ])
outputParser=StrOutputParser()
chain= prompt | llm | outputParser
print("ok")
def cutMyScript(user_input):
    response =chain.invoke({"question":user_input})
    return response
if "response" not in st.session_state:
     st.session_state["response"]=""

user_input=st.sidebar.text_area(label="Paste your script",height=300)
 
if st.sidebar.button("Cut the Script") :
     if user_input!=" ":
          st.sidebar.write("Please type something")
     st.session_state["response"]=cutMyScript(user_input)
text_result=st.text_area(label="Script",value=st.session_state["response"],height=450)
 
 