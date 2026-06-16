@app.route("/todos", methods=["POST"])
def add_todo():
    data = request.get_json()
    if not data or "task" not in data:
        return jsonify({"error": "task is required"}), 400
    todo = {"id": len(todos) + 1, "task": data["task"], "done": False}
    todos.append(todo)
    return jsonify(todo), 201
