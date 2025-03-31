from os import environ

API_ID = int(environ.get("API_ID", "27823209"))
API_HASH = environ.get("API_HASH", "1d693fcf3bfea119ca1d9057b08a4495")
BOT_TOKEN = environ.get("BOT_TOKEN", "")
OWNER_ID = int(environ.get("OWNER_ID", "6004928770"))
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002541046049"))
MONGO_DB_URI = environ.get("MONGO_DB_URI", "mongodb+srv://kalitgstringsession:kalitgstringsession@cluster0.rby7z6u.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
PORT = int(environ.get('PORT', 8080))
AUTH_CHANNELS = environ.get("AUTH_CHANNEL", "-1002327045567")
AUTH_CHANNELS = [int(channel_id) for channel_id in AUTH_CHANNELS.split(",")]
