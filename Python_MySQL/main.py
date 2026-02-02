import mysql.connector as connector

class AdmissionDB:
    def __init__(self):
        self.con = connector.connect(
            host = "localhost",
            user = "root",
            password = "aman",
            database = "new_db"
        )

        query1 = """
        CREATE TABLE IF NOT EXISTS students(
            student_id INT PRIMARY KEY AUTO_INCREMENT,
            name VARCHAR(30),
            email VARCHAR(30) UNIQUE,
            phone VARCHAR(15),
            city VARCHAR(20)
        )
        """
        query2 = """
        CREATE TABLE IF NOT EXISTS applications(
            application_id INT PRIMARY KEY,
            student_id INT,
            FOREIGN KEY (student_id) REFERENCES students(student_id),
            course VARCHAR(20),
            marks INT,
            status VARCHAR(30) DEFAULT "Pending",
            applied_date DATE
        )
        """
        curr = self.con.cursor()
        curr.execute(query1)
        curr.execute(query2)
        print("Table students and applications already exists")

    def add_student(self, name, email, phone, city):
        try:
            query = """
            INSERT INTO students (name, email, phone, city)
            VALUES (%s, %s, %s, %s)
            """
            cur = self.con.cursor()
            cur.execute(query, (name, email, phone, city))
            self.con.commit()
            print("Student inserted successfully")
        except Exception:
            print("Record Already present.")

    def apply_for_admission(self, application_id, student_id, course, marks, applied_date):
        try:
            query = """
            INSERT INTO applications (application_id, student_id, course, marks, applied_date)
            VALUES (%s, %s, %s, %s, %s)
            """
            cur = self.con.cursor()
            cur.execute(query, (application_id, student_id, course, marks, applied_date))
            self.con.commit()
            print("Admission Application inserted successfully")
        except Exception:
            print("Record Already present.")
    def view_all_applications(self):
        query = """
            SELECT * FROM applications
        """
        curr = self.con.cursor()
        curr.execute(query)

        rows = curr.fetchall()
        for row in rows:
            print(row)
    def update_status(self):
        query1 = """
            SELECT * FROM applications
        """
        curr = self.con.cursor()
        curr.execute(query1)
        
        print("Here are the details applications of all the students:")
        rows = curr.fetchall()
        for row in rows:
            print(row)
        id = int(input("Enter application id for whom you want to Approve or reject the application:"))

        query2 = """
            SELECT * FROM applications
            WHERE application_id = %s
        """
        curr.execute(query2, (id,))
        curr.fetchone()


        ans = input("Approved or Rejected??").lower()
        if ans == "approved":
            query3 = """
                UPDATE applications
                SET status = "Approved"
                WHERE application_id = %s
            """
            curr.execute(query3, (id,))
            self.con.commit()
            print("Record Updated Successfully")
        else:
            query4 = """
                UPDATE applications
                SET status = "Rejected"
                WHERE application_id = %s
            """
            curr.execute(query4, (id,))
            self.con.commit()
            print("Record Updated Successfully")
            
    def close(self):
        self.con.close()
        print("Database connection closed")


db = AdmissionDB()