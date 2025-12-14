# create_tables.py
from database import Base, engine
import models  # ensures all models are loaded

Base.metadata.create_all(bind=engine)
print("All tables created successfully!")
