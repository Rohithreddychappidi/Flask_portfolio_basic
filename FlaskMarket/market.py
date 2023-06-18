from flask import Flask, render_template,request
from flask_mysqldb import MySQL
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'flask@123'
app.config['MYSQL_DB'] = 'contactdb'

mysql = MySQL(app)
@app.route('/')
def home_page():
    return render_template('home.html',)
@app.route('/user')
def abouut_page():
    return render_template('user.html')

@app.route('/website')
def web_page():
    return render_template('user.html')

@app.route('/contact',methods=['POST','GET'])
def cont_page():
    if request.method == 'POST':
        name = request.form['name']
        phone =request.form['phone']
        email =request.form['email']
        description=request.form['description']
        cur =mysql.connection.cursor()
        cur.execute("INSERT INTO contpage(name,phone,email,description) VALUES(%s,%s,%s,%s)",(name,phone,email,description))
        mysql.connection.commit()
        cur.close()
        return "success"
    return render_template('user.html')
