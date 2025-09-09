import openai
from dotenv import load_dotenv
import os

load_dotenv()

client = openai.OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)

def call_api(prompt, options, context):
    """Simple provider that echoes the prompt with a prefix."""

    thread = client.beta.threads.create(messages=[
        {
            "role": "user",
            "content": context.get("vars", {}).get("question", "")
        }
    ],
    metadata={
        "user_id": "PromptfooTesting"
    })

    client.beta.threads.runs.create_and_poll(
        assistant_id="roger", 
        thread_id=thread.id,
        timeout=120,
    )

    # Get the messages in the thread
    messages = client.beta.threads.messages.list(thread.id)

    latest_assistant_message = []
    for message in messages.data:  # Check from most recent
        if message.role == "user":
            break
        else: 
            latest_assistant_message.insert(0, message.content[0].text)

    # Display the latest assistant message
    if latest_assistant_message:
        for msg in latest_assistant_message:
            response = msg
    else:
        response = None

    return {
        "output": response,
    }