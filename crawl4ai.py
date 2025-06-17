from dotenv import load_dotenv
import os

load_dotenv(verbose=True)

print(os.getenv("test"))
