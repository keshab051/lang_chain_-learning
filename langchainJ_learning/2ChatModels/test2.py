from dotenv import load_dotenv
from pathlib import Path
import os

env_path = Path(__file__).resolve().parents[1] / ".env"

print("ENV PATH:", env_path)
print("ENV EXISTS:", env_path.exists())

load_dotenv(dotenv_path=env_path)

print("TOKEN:", os.getenv("HUGGINGFACEHUB_API_TOKEN"))

# from dotenv import dotenv_values
# from pathlib import Path

# env_path = Path(__file__).resolve().parents[1] / ".env"

# print(dotenv_values(env_path))
