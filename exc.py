from datetime import datetime
from models import Fitness

today = datetime.today().strftime("%Y-%m-%d")

db = Fitness()

item = (
    today,
    74,
    2100,
    "Chest and Triceps"
)

db.insert(item)

for item in db.read_all():
    print(item)