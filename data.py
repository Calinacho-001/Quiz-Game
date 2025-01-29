import requests
from config import *

# Fetch quiz questions from Open Trivia Database API
response = requests.get("https://opentdb.com/api.php?", params=PARAMETERS)
response.raise_for_status()
data = response.json()
question_data = data["results"]