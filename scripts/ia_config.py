import os
from dotenv import load_dotenv

class IaConfig :
    def __init__(self):
        load_dotenv()
        self.ia_api_key = os.getenv('OPENAI_API_KEY')
    def get_ia_api_key(self):
        return self.ia_api_key
    