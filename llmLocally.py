import os
import requests
import json
import ollama
from ollama import chat

if __name__ == "__main__":
    number_of_questions = 2
    number_of_questions_asked = 0

    while number_of_questions_asked < number_of_questions:
        prompt = str(input("Enter a question: "))
        data = {
            "model": "llama3.1",
            "messages": [
                {"role": "system", "content": "You are a tourist guide. Answer the question as concisely as possible with the most relevant information."},
                {"role": "user", "content": prompt}
            ],
            "stream": False,
            "temperature": 0.7
        }
        url = "http://localhost:11434/api/chat"
        response = requests.post(url, json=data)

        response_json = json.loads(response.text)

        ai_reply = response_json['message']['content']

        print(ai_reply)
        number_of_questions_asked += 1
        