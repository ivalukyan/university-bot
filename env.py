import os
from dotenv import load_dotenv

load_dotenv()


class Telegram:
    def __init__(self):
        self.token = os.getenv('BOT_TOKEN')
        self.url = os.getenv('URL')
        self.admins = os.getenv('ADMINS')
        self.url_jurnal = os.getenv('URL_JURNAL')