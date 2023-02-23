import environ
import os
import enum


class RabbitsConst(enum.Enum):
    RABBITS_PER_CAGE_SET = (1,2,3,4,5,6,7,8,9,10,11,12,)
    BATCH_RANGE_VALID = (1,2,3,4,5,6,7,8,9,10,11,12,)
    

def reset_autoincrement_sql_tables():
    sql_result = str(os.environ.get('SQL_SENTENCE'))
    return sql_result.replace(","," ")

def reset_autoincrement_sql_customusers():
    sql_result = str(os.environ.get('SQL_SENTENCE_CUSTOM_USER'))
    return sql_result.replace(","," ")

def reset_autoincrement_sql_rabbit_status():
    sql_result = str(os.environ.get('SQL_SENTENCE_RABBIT_STATUS'))
    return sql_result.replace(","," ")

def reset_autoincrement_sql_rabbit_breeds():
    sql_result = str(os.environ.get('SQL_SENTENCE_RABBIT_BREEDS'))
    return sql_result.replace(","," ")
  
