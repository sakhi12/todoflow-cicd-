from flask import Flask, jsonify, request

app = Flask(__name__)
todos = []


@app.route("/")
def home():
    return jsonify({"status": "TodoFlow CI/CD is running!"})


@app.route("/todos", methods=["GET"])
def get_todos():
    return jsonify(todos)


@app.route("/todos", methods=["POST"])
def add_todo():
    data = request.get_json()
    if not data or "task" not in data:
        return jsonify({"error": "task is required"}), 400
    todo = {"id": len(todos) + 1, "task": data["task"], "done": False}
    todos.append(todo)
    return jsonify(todo), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
