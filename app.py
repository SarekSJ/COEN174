from flask import Flask, flash, redirect, render_template, request, session, abort
from sqlalchemy.orm import relationship, backref, sessionmaker
from tabledef import *
from courses_table import *
import os

app = Flask(__name__)

Session = sessionmaker(bind=engine)
s = Session()


@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return table_screen()
        # return "Hello Boss! <a href='/logout'>Logout</a>"

@app.route('/login', methods=['POST'])
def do_admin_login():
    POST_USERNAME = str(request.form['username'])
    POST_PASSWORD = str(request.form['password'])

    query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]) )
    result = query.first()
    if result:
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return home()

@app.route('/add_row', methods=['POST'])
def add_row():
    POST_SCHOOL = str(request.form['school'])
    POST_SCHOOL_COURSE = str(request.form['school_course'])
    POST_SCU_COURSE = str(request.form['scu_course'])
    POST_DETERMINATION = str(request.form['determination'])
    POST_ADVISOR = str(request.form['advisor'])

    s.add(Course(POST_SCHOOL, POST_SCHOOL_COURSE, POST_SCU_COURSE, POST_DETERMINATION, POST_ADVISOR, None))
    s.commit()
    return table_screen()

@app.route("/logout")
def logut():
    session['logged_in'] = False
    return home()


@app.route('/table')
def table_screen():
    items = s.query(Course).all();
    return render_template('table.html', items=items)


if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(host='0.0.0.0', port=8000)


# if __name__ == '__main__':
#     app.run()
