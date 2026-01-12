from flask import Flask, jsonify

app = Flask(__name__)

# Mock railway schedule data
train_data = [
    {
        "train_name": "Godavari Express",
        "train_no": "12727",
        "from": "Visakhapatnam",
        "to": "Hyderabad",
        "seats_available": 42,
        "arrival": "10:30",
        "departure": "10:45"
    },
    {
        "train_name": "Konark Express",
        "train_no": "11020",
        "from": "Bhubaneswar",
        "to": "Mumbai",
        "seats_available": 18,
        "arrival": "14:00",
        "departure": "14:15"
    }
]

@app.route("/api/trains", methods=["GET"])
def get_trains():
    return jsonify(train_data)

if __name__ == "__main__":
    app.run(debug=True)
