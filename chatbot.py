import os
import requests
from bs4 import BeautifulSoup
import openai

# -----------------------------
# CONFIGURATION
# -----------------------------
openai.api_key = os.getenv("OPENAI_API_KEY")

WEBSITE_URL = "https://botpenguin.com/"
MAX_CONTEXT_LENGTH = 3000

# -----------------------------
# STEP 1: SCRAPE WEBSITE DATA
# -----------------------------
def scrape_website(url):
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    texts = []

    for tag in soup.find_all(["h1", "h2", "h3", "p", "li"]):
        text = tag.get_text(strip=True)
        if text:
            texts.append(text)

    content = " ".join(texts)
    return content[:MAX_CONTEXT_LENGTH]

# -----------------------------
# STEP 2: CHATGPT RESPONSE
# -----------------------------
def chat_with_website(context, user_query):
    prompt = f"""
You are a chatbot that answers questions strictly based on the website content below.

Website Content:
{context}

User Question:
{user_query}
"""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Answer only from the website content."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )

        return response.choices[0].message["content"].strip()

    except Exception:
        return f"I’m currently unable to fetch an AI response, but the website content has been processed for your query: '{user_query}'."


# -----------------------------
# STEP 3: CONSOLE CHATBOT
# -----------------------------
def start_chatbot():
    print("Fetching website data...")
    website_content = scrape_website(WEBSITE_URL)
    print("Chatbot ready! Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break

        reply = chat_with_website(website_content, user_input)
        print(f"Chatbot: {reply}\n")

# -----------------------------
# MAIN
# -----------------------------
if __name__ == "__main__":
    print("Script started...")

    if not openai.api_key:
        print("ERROR: OPENAI_API_KEY is not set.")
        exit(1)

    start_chatbot()
