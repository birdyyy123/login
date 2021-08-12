from flask import Flask, render_template, flash, request, redirect
from flask_mysqldb import MySQL, MySQLdb
import yaml

app = Flask(__name__)


db = yaml.load(open("db.yaml"))
app.config['MYSQL_HOST'] = db["mysql_host"]
app.config['MYSQL_USER'] = db["mysql_user"]
app.config['MYSQL_DB'] = db["mysql_db"]

mysql = MySQL(app)

############ สมัครสมาชิก ########################################

@app.route("/register", methods = ["GET", "POST"])
def reg():
    if request.method == "POST":
        userdental = request.form
        UID = userdental["username"]
        Upass = userdental["password"]
        Fname = userdental["Fname"]
        Lname = userdental["Lname"]
        DEmail = userdental["email"]
        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("SELECT * FROM dentaluser WHERE UID = %s",(UID,))
        user = cur.fetchone()
        if user is None :
            cur.execute("INSERT INTO dentaluser(UID, Upass, Fname, Lname, DEmail) VALUES(%s, %s, %s, %s, %s)", (UID, Upass, Fname, Lname, DEmail))
            mysql.connection.commit()
            cur.close()
        else:
            return "error"
    return render_template('register.html')

############ สมัครสมาชิก ########################################

############ เข้าสู่ระบบ ########################################

@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        userdental = request.form
        UID = userdental["username"]
        Upass = userdental["password"]
        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("SELECT * FROM dentaluser WHERE UID = %s",(UID,))
        user = cur.fetchone()
        if user is None :
            return "error"
        else:
            cur.execute("SELECT * FROM dentaluser WHERE Upass = %s",(Upass,))
            Upass = cur.fetchone()
            if Upass is None:
                return "error"
            else:
                return render_template('home.html')
    return render_template('login.html')

############ เข้าสู่ระบบ ########################################

if __name__ == "__main__":
    app.run(debug=True)