import os
import openai

openai.api_key = "API-KEY"

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

prompt = "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: "
conversation = ""

def openai_create(prompt):
    i = 1
    while(i != 0):
        question = input("Humano: ")
        conversation = "\nHumano:" + question + "\nAI:"
        response = openai.Completion.create(
            engine = "davinci",
            prompt = prompt,
            temperature = 0.9,
            max_tokens = 150,
            top_p = 1,
            frequency_penalty = 0,
            presence_penalty = 0.6,
            stop = ["\n", " Humano:", " AI:"]
        )
        answer = response.choices[0].text.strip()
        conversation += answer
        print("AI: " + answer + "\n")

openai_create(prompt)
