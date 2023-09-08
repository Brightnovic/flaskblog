from mysql import connector
def get_connection():
    try:
        db = connect(
            host="localhost",
            port=3306,
            user="root",
            password="",
            database="flask-blog"
        )
        if db.is_connected(): 
            print("database connection")
        
    except Exception as e:
        print("database error")