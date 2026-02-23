from app.config.database import db

print("Dialect:", db.dialect)
print("Tables:", db.get_usable_table_names())