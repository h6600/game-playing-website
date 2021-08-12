from flask import Flask,render_template,request,redirect,session
import mysql.connector
import os

app=Flask(__name__)
app.secret_key=os.urandom(24)

conn=mysql.connector.connect(host="remotemysql.com",user="2IjOg1pE8c",password="eq4V0VtofL",database="2IjOg1pE8c")
cursor=conn.cursor()

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/register')
def about():
    return render_template('register.html')

@app.route('/home')
def home():
    if 'user_id' in session:
        return render_template('home.html')
    else:
        return redirect('/')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/game1')
def game1():
    return render_template('game1.html')

@app.route('/game2')
def game2():
    return render_template('game2.html')

@app.route('/game3')
def game3():
    return render_template('game3.html')

@app.route('/game4')
def game4():
    return render_template('game4.html')


@app.route('/game5')
def game5():
    return render_template('game5.html')

@app.route('/game6')
def game6():
    return render_template('game6.html')


@app.route('/login_validation', methods=['POST'])
def login_validation():
    email=request.form.get('email')
    password=request.form.get('password')

    cursor.execute("""SELECT * FROM `emaillogin` WHERE `email` LIKE '{}' AND `password` LIKE '{}'"""
                   .format(email,password))
    users=cursor.fetchall()
    if len(users)>0:
        #session['user_id']=email[0][0]
        return redirect('/home')
    else:
        return redirect('/')

@app.route('/add_user',methods=['POST'])
def add_user():

    email=request.form.get('uemail')
    password=request.form.get('upassword')
    name = request.form.get('uname')
    age = request.form.get('uage')

    cursor.execute("""INSERT INTO `emaillogin` (`email`,`password`,`name`,`age`) VALUES ('{}','{}','{}','{}')"""
                   .format(email,password,name,age))
    conn.commit()
    return"USER REGISTERED SUCESSFULLY"

@app.route('/logout')
def logout():
    session.pop('user_id')
    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)







