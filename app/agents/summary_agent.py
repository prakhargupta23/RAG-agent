from google import genai
from app.agents.prompt import SYSTEM_PROMPT
from app.config.database import fetch_data
import os
from dotenv import load_dotenv
import requests
import json


load_dotenv()

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def get_summary(question, base64):
    # print("this is base64",base64[0:10])
    response = requests.post(
            "https://pdfocrazure.azurewebsites.net/ocr",
            data=json.dumps({"pdf": base64}),
            headers={"Content-Type": "application/json"},
            timeout=10
        )
    text = response.json().get("text")
    # print("this is text",text)
    
    
    prompt=f"Generate a summary of the given text, include all the key points, also the user query is {question} and the text is {text}"
    # print("this is prompt",prompt)
    response = client.models.generate_content(
        model="gemini-3.1-pro-preview", contents=f"""{prompt}, give your reply in a readable para format removing all # and - symbols"""
    )
    # print("this is response",response)
    reply=response.text
    return reply
