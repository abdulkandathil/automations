import requests 
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("prompt", help="The prompt to sent to OpenAI")
parser.add_argument("filename", help="Filename to with python code need to be saved.")
args = parser.parse_args()


openai_api_endpoint = "https://api.openai.com/v1/chat/completions"
openai_api_key = os.getenv("OPENAI_API_KEY")

request_headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + openai_api_key
}

request_data = {
    "model": "gpt-3.5-turbo",
    "messages": [{
        "role": "user", 
        "content": f"Write a python code to {args.prompt}, only code"
        }],
    "temperature": 0.7
}

response = requests.post(openai_api_endpoint, headers=request_headers, json=request_data)

if response.status_code == 200:
    response_text = (response.json()["choices"][0]["message"]["content"])
    with open(args.filename, "w") as file:
        file.write(response_text)
else:
    print(f"Request failed with response code {str(response.status_code)}")