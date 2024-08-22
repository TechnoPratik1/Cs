from os import environ 

class Config:
    API_ID = environ.get("API_ID", "25107334")
    API_HASH = environ.get("API_HASH", "15d3ebd2e07e8e2703500a906bd70b04")
    BOT_TOKEN = environ.get("BOT_TOKEN", "6513494927:AAHCD6RJ3tr-PrkDJOHslhPvX_23cRSkoPg") 
    BOT_SESSION = environ.get("BOT_SESSION", "BQBqRVIrbtgUqe6xKyzaZO-u4P5QhKTuugLxewuOkhJgIz4IxrvrL7y8vuD2ZYuurjQALPE8DIO-bRrm1F8P2ZS7gCgqbkMRrJiEgT3V73uujq1E401F90o5oY8XIZf3OUxnEG9tru-F838YstYMVKcXtyn3Yk2_y8a2Kjhd4CqylRpWAusWIC6FlvZ-s2V59N2g4wBugvCvCEYjyMJwaOkNW0SJyuxrzh-Q103MssPduoXK4Q5ROHaexByf0NugAuLvidQ23TBHSvZHhphIdSt77Kd0dZE5_jp2jKntrVN7X_ik6W8cgImNn7xmsXc7oA4vG1UaQuNk1ksNVYhs3AAAAAAWeVqMIA") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://Pratik:Pratik333@cluster0.ppnlq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '6032828610').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
