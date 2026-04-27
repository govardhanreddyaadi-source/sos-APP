from flask import Flask, request, jsonify
from flask_cors import CORS

from models.alert_model import create_alert, get_alerts, update_alert
from models.user_model import get_users

app = Flask(__name__)
CORS(app)

# 🔹 Create Alert
@app.route('/api/alert', methods=['POST'])
def create():
    data = request.json
    create_alert(data)
    return jsonify({"message": "Alert created"}), 201

# 🔹 Get Alerts
@app.route('/api/alerts', methods=['GET'])
def alerts():
    return jsonify(get_alerts())

# 🔹 Resolve Alert
@app.route('/api/resolve/<name>', methods=['PUT'])
def resolve(name):
    update_alert(name, "resolved")
    return jsonify({"message": "Resolved"})

# 🔹 Get Users
@app.route('/api/users', methods=['GET'])
def users():
    return jsonify(get_users())

if __name__ == '__main__':
    app.run(debug=True)
@app.route('/api/stats', methods=['GET'])
def stats():
    from config import db

    total = db.alerts.count_documents({})
    active = db.alerts.count_documents({"status": "active"})
    resolved = db.alerts.count_documents({"status": "resolved"})

    return {
        "total": total,
        "active": active,
        "resolved": resolved
    }
# 🔹 Accept alert
@app.route('/api/accept/<name>', methods=['PUT'])
def accept(name):
    from models.alert_model import update_alert
    update_alert(name, "accepted")
    return {"message": "Alert accepted"}

# 🔹 Resolve alert
@app.route('/api/resolve/<name>', methods=['PUT'])
def resolve(name):
    from models.alert_model import update_alert
    update_alert(name, "resolved")
    return {"message": "Alert resolved"}