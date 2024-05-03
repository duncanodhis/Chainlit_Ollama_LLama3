import chainlit as cl
import requests

# Ollama endpoint for generating responses
OLLAMA_ENDPOINT = "http://localhost:11434/api/generate"

@cl.on_chat_start
async def on_chat_start():
    await cl.Message(content="Welcome! Enter a question or topic, and I'll generate a response using Ollama.").send()

@cl.on_message
async def on_message(message):
    user_input = message.content  # Get the message from the user

    # Define the payload for Ollama with the user-provided prompt
    payload = {
        "model": "llama3",
        "prompt": user_input,  # Using user input as the prompt
        "stream": False,  # Set stream to False for a single response
    }

    # Send the POST request to the Ollama endpoint
    response = requests.post(OLLAMA_ENDPOINT, json=payload, headers={"Content-Type": "application/json"})

    # Check if the request was successful
    if response.status_code == 200:
        # If successful, extract the text content from the response
        response_content = response.json().get("response", "No response received")
        await cl.Message(content=response_content).send()
    else:
        # If there was an error, send the error message
        await cl.Message(content=f"Error: {response.status_code}, {response.text}").send()
