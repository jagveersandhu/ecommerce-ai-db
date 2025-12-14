from langchain_community.utilities import SQLDatabase
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

db = SQLDatabase.from_uri(
    DATABASE_URL,
    include_tables=[
        "users",
        "categories",
        "products",
        "orders",
        "order_items",
        "reviews"
    ],
    sample_rows_in_table_info=2
)
