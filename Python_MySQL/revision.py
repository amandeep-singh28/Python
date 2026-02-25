import mysql.connector as connector

class StudentDB:
    def __init__(self):
        self.con = connector.connect(
            host = "localhost",
            user = "root",
            password = "aman",
            database = "collegedb"
        )
        query1 = """
        CREATE TABLE IF NOT EXISTS students(
            student_id INT PRIMARY KEY,
            name VARCHAR(30),
            age INT
        )
        """
        curr = self.con.cursor()
        curr.execute(query1)
        self.con.commit()
        print("Table student already exists")
    def insert_value(self):
        try:
            query = """
            INSERT INTO students (student_id, name, age)
            VALUES (3, "Ranveer", 19)
            """
            curr = self.con.cursor()
            curr.execute(query)
            self.con.commit()
            print("Record inserted successfully")
        except Exception:
            print("Record Already present")
    def fetch_data(self):
        query = """
        SELECT * FROM students
        """
        curr = self.con.cursor()
        curr.execute(query)
    
        print(curr.fetchone())
        print(curr.fetchmany(2))
        print(curr.fetchall())


db = StudentDB()
db.insert_value()
db.fetch_data()