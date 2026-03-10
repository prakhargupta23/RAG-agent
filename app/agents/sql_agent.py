from google import genai
from app.agents.prompt import SYSTEM_PROMPT
from app.config.database import fetch_data
import os
from dotenv import load_dotenv


load_dotenv()

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
def get_sql_query(question):
    
    prompt=SYSTEM_PROMPT["new_db1"]
    # print("this is prompt",prompt)
    response = client.models.generate_content(
        model="gemini-3.1-flash-lite-preview", contents=f"""Hi ,you are SAAR(Smart AI assistant for Railways){prompt},{question}, give your reply in a readable para format without any special characters"""
    )
    print("this is response",response)
    reply=response.text
    type_flag, content = reply.split(":", 1)

    if type_flag == "1":
        return content

    # elif type_flag == "2":
    #     sql_query = content
    #     # run SQL query
    #     sql_response = get_text_query(question)
    #     print("this is sql response",sql_response)
    #     return sql_response

    elif type_flag=="2":
        print("this is content",content)
        data=get_data_from_db(content)
        prompt=SYSTEM_PROMPT["test1"]
        response = client.models.generate_content(
            model="gemini-3.1-flash-lite-preview",
            contents=f"""Hi ,you are SAAR (Smart AI assistant for Railways)\n\nInstructions - {prompt}\n\nUser Query - {question}\n\nSQL Query - {content}\n\nData - {data}\n\nGive your reply in a readable paragraph format without special characters."""
        )
        return response.text

def get_text_query(question):
    prompt=SYSTEM_PROMPT["pfaPrompt"]
    response = client.models.generate_content(
        model="gemini-3.1-pro-preview", contents=f"""Hi ,you are SAAR(Samrt AI assistant for Railways){prompt},{question}, give your reply in a readable para format without any special characters"""
    )
    reply=response.text
    return reply

def get_data_from_db(query):
    data=fetch_data(query)
    print("this is data",data)
    return data