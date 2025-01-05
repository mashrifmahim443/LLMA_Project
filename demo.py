import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

from langchain_groq import ChatGroq
llmaChatModel=ChatGroq(model="llama3-70b-8192")

responce=llmaChatModel.invoke("How are you doing today?")

print(responce)

for chunk in llmaChatModel.stream(
    "How are you doing today?"
):
    print(chunk, end="",flush=True)