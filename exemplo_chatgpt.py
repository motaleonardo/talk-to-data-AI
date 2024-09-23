import openai
import os
from dotenv import load_dotenv, find_dotenv

#Set your API key
load_dotenv(find_dotenv())
openai.api_key = os.getenv("OPENAI_API_KEY")

#Function to send a question to GPT-4o-mini

def ask_chatgpt(question: str):
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": question}
        ]
    )
    #Extrating the actual content message from the response
    return response.choices[0].message.content

#Asking the question:
question = "A Zapflow vai abrir escritorio em Moscow?"
answer = ask_chatgpt(question)

#print the response
print(f"Resposta do ChatGPT: {answer}")
