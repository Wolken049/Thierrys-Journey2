import os
from dotenv import load_dotenv
from mysql.connector import connect

load_dotenv()

#connecting Database

def get_db_connection():
    try:
        return connect(
            host = os.getenv("DB_HOST"),
            user = os.getenv("DB_User"),
            password = os.getenv("DB_Pass"),
            database = os.getenv("DB_Immigration")
        )
    except Exception as e:
        print(f"Error connecting to MySQL: {e}")
        return None

mydb = get_db_connection()

#Global Consonants

DEFAULT_FONT = ("Times New Roman", 20)
DEFAULT_COLOUR = "#000000"
FORM_SIZE = "700x650"
LIST_HEIGHT = 3


ValidVisa = ["STUDENT", "WORK", "TOURIST"]
ValidReasonOfTravel = ["WORK", "SCHOOL", "TOURING", "CHAPERONE"]

#Creating the GUI



SEX = ["MALE", "FEMALE"]
VISA = ["STUDENT", "WORK", "TOURIST"]

def get_cities():
    if not mydb:
        return {}
    cursor = mydb.cursor()
    cursor.execute("SELECT City_ID, City_Name FROM City_Table")
    return {row[1]: row[0] for row in cursor.fetchall()}

def get_schools(city_id = None):
    if not mydb:
        return {}
    cursor = mydb.cursor()
    if city_id:
        cursor.execute("SELECT School_ID, School_Name FROM School_Table FROM City_ID = %s", (city_id,))
    else:
        cursor.execute ("SELECT School_ID, School_Name FROM School_Table FROM City_ID")
    return {row[1]: row[0] for row in cursor.fetchall()}