from langchain_community.utilities.sql_database import SQLDatabase
from langchain_community.agent_toolkits.sql.base import create_sql_agent
from llm import llm

DATABASE_URL = "postgresql://ecommerce_user:user@localhost:5432/ecommerce_db"

db = SQLDatabase.from_uri(DATABASE_URL)

agent = create_sql_agent(
    llm=llm,
    db=db,
    verbose=False,
    agent_type="openai-tools",  # works with Ollama too
)

FORBIDDEN = ["delete", "drop", "truncate", "update", "insert", "alter"]

def run_query(question: str):
    lower_q = question.lower()

    # HARD BLOCK destructive intent
    if any(word in lower_q for word in FORBIDDEN):
        return "Destructive queries are not allowed."

    result = agent.invoke({"input": question})
    return result["output"]
