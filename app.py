import json
from flask import Flask
from flask import request

app = Flask(__name__)

tasks = {
    0: {
        "id": 0,
        "Description": "Wash Dishes",
        "Done": False
    },
    1: {
        "id": 1,
        "Descriotion": "Finish projects",
        "Done": False
    }
}
tasks_id_counter = 2
@app.route("/")
@app.route("/tasks/")
def get_tasks():
    res={
        "Success": True,
        "data": list(tasks.values())
    }
    
    return json.dumps(res), 200

@app.route("/tasks/", method=["POST"])
def create_task():
    global tasks_id_counter
    body = json.loads(request.data)
    description = body.get("description", "no description")
    task = {"id": tasks_id_counter, "description": description, "done": False}
    tasks[tasks_id_counter] = task
    tasks_id_counter += 1
    return json.dumps({"success": True, "data": task}), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
