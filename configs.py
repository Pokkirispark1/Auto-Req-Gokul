from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "19517098"))
    API_HASH = getenv("API_HASH", "064100a1cb729dfb0436aaee64fd9d58")
    BOT_TOKEN = getenv("BOT_TOKEN", "6543058088:AAGZR8vUJd9tYIoUujdHAWHaMG3kgJTv_uU")
    FSUB = getenv("FSUB", "Joinbotupdatess")
    CHID = int(getenv("CHID", "-1002111150402"))
    SUDO = list(map(int, getenv("SUDO").split()))
    MONGO_URI = getenv("MONGO_URI", "")
    
cfg = Config()
