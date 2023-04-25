import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "7165358")

API_HASH = os.environ.get("API_HASH", "304228f1dc7b9c86ef1c8d83cdc5da85")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6190065172:AAGBbeYQqSdYHd7xokw9337q7SS0Lwlak80") 

FORCE_SUB = os.environ.get("FORCE_SUB", "Anime_complex") 

DB_NAME = os.environ.get("DB_NAME","EXONTESTMONGO")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://EXONTESTMONGO:EXONTESTMONGO@cluster0.bviw7ic.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/19467bbc490900f8a29ba.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', 6014086787 5347606696 1711005257 5858467322 1476517140 1858995207 917790252 6011680633 1245624597 1827695840 1172340595 1435293433 1649093710 1869271514 1380685014 1694138821 1122860241 5751548638

        },).split()]

PORT = os.environ.get("PORT", "443")
