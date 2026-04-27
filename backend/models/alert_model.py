from config import db
from datetime import datetime

collection = db["alerts"]

# 🔹 Create alert (keep this)
def create_alert(data):
    alert = {
        "name": data["name"],
        "area": data["area"],
        "type": data["type"],
        "room": data.get("room", ""),
        "level": data["level"],
        "location": data["location"],
        "status": "active",
        "created_at": datetime.utcnow()
    }
    return collection.insert_one(alert)

# 🔹 Get all alerts (keep this)
def get_alerts():
    return list(collection.find({}, {"_id": 0}))

# 🔹 NEW: update alert status (generic)
def update_alert(name, status):
    return collection.update_one(
        {"name": name},
        {"$set": {"status": status}}
    )