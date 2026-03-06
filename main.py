from flask import Flask
from app.api.routes import api
from app.agents.sql_agent import get_sql_query

app = Flask(__name__)
app.register_blueprint(api)

if __name__ == "__main__":
    app.run(debug=True)