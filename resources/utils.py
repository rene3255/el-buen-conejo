import environ
import os

def reset_autoincrement_sql_tables():
    sql_result = str(os.environ.get('SQL_SENTENCE'))
    return sql_result.replace(","," ")