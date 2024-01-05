
pip install openai==0.28

import os
import openai

openai.api_key = <<your key here>>

import pandas as pd



def summarizepaper(text):
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
        {
          "role": "assistant",
          "content": "Your role is that of a learning assistant, specifcally helping high school students understand\
          advanced research papers and in simple terms. You will be provided with the introductory first half of \
          the full paper text text and your task is to provide a one paragraph explanation, in simple terms at the \
          level of a high school junior, of what this paper is about."
        },
        {
          "role": "user",
          "content": text
        }
      ],
      temperature=0,
      max_tokens=256,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )
    #print(response.choices[0])
    return response.choices[0]["message"]["content"]

def paperglossary(text):
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
        {
          "role": "assistant",
          "content": "Your role is that of a learning assistant, specifcally helping high school students understand\
          advanced research papers and in simple terms. You will be provided with the \
          the full paper text text and your task to list all the technical terms with a definition or short description\
          of what the term means. Please stick to scientific terms only. You tend to give terms like author manuscript\
          or stuff like that but dont. I dont care about the author manuscript and anything todo with the NIH. Focus only on the scientific terms related to the content of the paper"
        },
        {
          "role": "user",
          "content": text
        }
      ],
      temperature=0,
      max_tokens=256,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )
    #print(response.choices[0])
    return response.choices[0]["message"]["content"]

def worksuggestions(text):
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
        {
          "role": "assistant",
          "content": "Your role is that of a learning assistant, specifcally helping high school students understand\
          advanced research papers and in simple terms. You will be provided with the summary text of the paper and\
          you must then provide suggestions on:\
          1. What, if anything, can a student do at home or high school lab to explore this particular research. \
          Please also list the type of equipment I would need.\
          2. What opportunities (labs or research programs including summer high school programs) they can look at for further\
          research internships in that area. Please list specific programs at specific institutions, versus telling me that I should\
          look at local universities etc."
        },
        {
          "role": "user",
          "content": text
        }
      ],
      temperature=0,
      max_tokens=2048,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )
    #print(response.choices[0])
    return response.choices[0]["message"]["content"]


def researchers(text):
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
        {
          "role": "assistant",
          "content": "Your role is that of a learning assistant, specifcally helping high school students understand\
          advanced research papers and in simple terms. You will be provided with the summary of the paper and\
          you must then provide me 3-4 researchers, other than the paper authors, that work in that specific area and along\
          with their affilitations. Tell me specifically why you think each one is relevant. Finally, please make sure you \
          provide me a *diverse* set of researchers - by location, gender, type of institution etc"
        },
        {
          "role": "user",
          "content": text
        }
      ],
      temperature=0,
      max_tokens=512,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )
    #print(response.choices[0])
    return response.choices[0]["message"]["content"]



papersummary=summarizepaper(paperfirst)

papersummary

print(paperglossary(paperfirst))

print(worksuggestions(papersummary))

print(researchers(authors+papersummary))