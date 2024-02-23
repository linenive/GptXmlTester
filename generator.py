import dotenv
import os
from openai import OpenAI
import logger

dotenv.load_dotenv(dotenv.find_dotenv())

client = OpenAI(
  api_key=os.environ.get("OPENAI_API_KEY"),
)

completion = client.chat.completions.create(
  model="gpt-4-1106-preview",
  messages=[
    {"role": "system", "content": "You are a poetic assistant in json, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ],
  response_format={"type": "json_object"},
)

print(completion.choices[0].message)

logger.export_log("generator", completion.choices[0].message.content)
