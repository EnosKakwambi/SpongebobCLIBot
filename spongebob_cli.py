#!/usr/bin/env python3
"""
Example: One-shot call to ai.sooners.us using gemma3:4b model.

Requires:
  pip install requests python-dotenv
"""

import os
import requests
from dotenv import load_dotenv

print("Loading....")

# Load API key and base URL from ~/.soonerai.env
load_dotenv(os.path.join(os.path.expanduser("~"), ".soonerai.env"))

API_KEY = os.getenv("SOONERAI_API_KEY")
BASE_URL = os.getenv("SOONERAI_BASE_URL", "https://ai.sooners.us").rstrip("/")
MODEL = os.getenv("SOONERAI_MODEL", "gemma3:4b")

if not API_KEY:
    raise RuntimeError("Missing SOONERAI_API_KEY in ~/.soonerai.env")

# Prepare API request
url = f"{BASE_URL}/api/chat/completions"
payload = {
    "model": MODEL,
    "messages": [
        {"role": "system", "content": "You are SpongeBob SquarePants. Speak cheerfully and use ocean humor."},
    ],
    "temperature": 0.6,
}

#Maximum conversation pairs
MAX_PAIRS=5

#keep asking user for input until they say bye
while True:
    user_input = input("You: ")
    if user_input.strip().lower() in ("bye", "quit"):
        print("Ending Chat.")
        break

        #save transcript
        #with open("chat_log.txt", "a", encoding="utf-8") as f:
        #    for msg in payload["messages"]:
        #        f.write(f"{msg['role'].upper()}: {msg['content']}\n")


    #append newest user message
    payload["messages"].append({"role": "user", "content": user_input   })

    #keep only the most recent MAX_PAIRS system+user pairs
    trimmed = []
    system_count = 0
    for m in reversed(payload["messages"]):
        if m["role"] == "user":
            system_count += 1
        trimmed.append(m)

        #keep speak like spongebob instruction on top
        if system_count == MAX_PAIRS:
            trimmed.append({"role": "system", "content": "You are SpongeBob SquarePants. Speak cheerfully and use ocean humor."})
            break
    payload["messages"]=list(reversed(trimmed))

    #send to model
    response = requests.post(
        url,
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
        },
        json=payload,
        timeout=60,
    )

    # Display result
    if response.status_code == 200:
        data = response.json()
        reply = data["choices"][0]["message"]["content"]
        print("SpongeBob:", reply)
        payload["messages"].append({"role": "assistant", "content": reply})
    else:
        print(f"Error {response.status_code}: {response.text}")