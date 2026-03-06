from flask import Blueprint, request, jsonify
from app.services.query_service import ask_question

api = Blueprint("api", __name__)

@api.route("/ask-whatsapp", methods=["POST"])
def ask_whatsapp():
    print("hello",request)
    question = request.json.get("question")
    answer = ask_question(question)
    return jsonify({"answer": answer})

@api.route("/ask-voice", methods=["POST"])
def ask_voice():
    question = request.json.get("question")
    answer = ask_question(question)
    return jsonify({"answer": answer})

# @api.route("/tasks", methods=["GET"])
# def get_tasks():
#     limit = request.args.get("limit", default=10, type=int)
#     try:
#         tasks = fetch_task_data(limit=limit)
#         return jsonify(tasks)
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# @api.route("/query-tasks", methods=["POST"])
# def query_tasks():
#     sql_query = request.json.get("query")
#     if not sql_query:
#         return jsonify({"error": "No query provided in the 'query' field."}), 400
#     try:
#         results = run_custom_task_query(sql_query)
#         return jsonify(results)
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

