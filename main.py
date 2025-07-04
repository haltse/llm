import os
import sys
from google import genai
from dotenv import load_dotenv
print(sys.argv)

if len(sys.argv) > 1:
    print(sys.argv[1])
else:
    print("No argument provided!")
    exit(1)

user_prompt = sys.argv[1]
messages = [
    genai.types.Content(role="user", parts=[genai.types.Part(text=user_prompt)]),
]




load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")


client = genai.Client(api_key=api_key)
response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents=messages,
)

usage_metadata = response.usage_metadata
print(response.text)
if len(sys.argv) <= 2:
    pass
else:
    if sys.argv[2] =='--verbose':
        print(f'User prompt: {sys.argv[1]}\nPrompt tokens: {usage_metadata.prompt_token_count}\nResponse tokens: {usage_metadata.candidates_token_count}')
   
 

 