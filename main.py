# pip install --upgrade langchain langchain_google_genai streamlit

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain import LLMChain
from langchain import PromptTemplate

import streamlit as st
import os

os.environ['GOOGLE_API_KEY'] = st.secrets['AIzaSyAGMTsHdloiDYzRl2YzTmy8ly6dDvJ4wpw']

# Create prompt template for suggesting places
tour_template = "Give me places in {location} for {person} people to go on a {tourtype} tour in {month}, for {days} days on a budget of {budget} Indian rupees"

tour_prompt = PromptTemplate(template = tour_template, input_variables = ['location', 'person', 'tourtype', 'month', 'days', 'budget'])

# Initialize Google's Gemini model
gemini_model = ChatGoogleGenerativeAI(model = "gemini-1.5-flash-latest")

# Create LLM chain using the prompt template and model
tour_chain = tour_prompt | gemini_model

st.header("Travel Guide")

st.subheader("Generate travel ideas using Gen AI")

location= st.text("India/ International/ India & International")
person= st.number_input("Number of people going on the trip", min_value=1, max_value= 50, value=1, step=1)
tourtype= st.text("Type of tour- Family/ Romantic/ Adventure/ Relaxing/ Religious/ Wildlife/ Water activities/ Beach/ Mountain")
month= st.text("Which month do you plan to go")
days= st.number_input("Number of days of trip", min_value=1, max_value= 365, value=1, step=1)
budget= st.text("Budget Amount= ")

if st.button("Generate"):
    tours = tour_chain.invoke({"location": location,"person": person,"tourtpe": tourtype,"month": month,"days": days, "budget": budget})
    st.write(tours.content)
