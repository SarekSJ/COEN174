from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
from sqlalchemy.orm import relationship, backref, sessionmaker
from tabledef import *
from datetime import datetime
import os
from pprint import pprint

app = Flask(__name__)

Session = sessionmaker(bind=engine)
s = Session()


@app.route('/')
def home():
    if not session.get('logged_in'):
        isLoggedIn = True
    else:
        isLoggedIn = False
    return redirect(url_for('table_screen'))

@app.route('/login_screen', methods=['POST'])
def show_login_screen():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def do_admin_login():
    POST_USERNAME = str(request.form['username'])
    POST_PASSWORD = str(request.form['password'])

    query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]))
    result = query.first()
    if result:
        session['username'] = POST_USERNAME
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return home()

@app.route('/add_row', methods=['POST'])
def add_row(isLoggedIn=False):
    POST_SCHOOL = str(request.form['school'])
    POST_SCHOOL_COURSE = str(request.form['school_course'])
    POST_SCU_COURSE = str(request.form['scu_course'])
    POST_DETERMINATION = str(request.form['determination'])
    # POST_ADVISOR = str(request.form['advisor'])

    s.add(Course(POST_SCHOOL, POST_SCHOOL_COURSE, POST_SCU_COURSE, POST_DETERMINATION, session['username'], datetime.now()))
    s.commit()
    return redirect(url_for('table_screen'))

@app.route("/logout")
def logut():
    session['logged_in'] = False
    return home()


@app.route("/delete/<int:id>", methods=['POST'])
def delete_row(id, isLoggedIn=false):
    row = s.query(Course).filter(Course.id == id).delete()
    s.commit()
    return redirect(url_for('table_screen'))

@app.route("/edit/<int:id>", methods=['POST'])
def edit_row(id, isLoggedIn=false):
    POST_SCHOOL = str(request.form['school'])
    POST_SCHOOL_COURSE = str(request.form['school_course'])
    POST_SCU_COURSE = str(request.form['scu_course'])
    POST_DETERMINATION = str(request.form['determination'])
    POST_ADVISOR = str(request.form['advisor'])

    s.query(Course).filter(Course.id == id).update({"school": POST_SCHOOL, "school_course": POST_SCHOOL_COURSE, "scu_course": POST_SCU_COURSE, "determination": POST_DETERMINATION, "advisor": POST_ADVISOR})
    s.commit()
    return redirect(url_for('table_screen'))

@app.route("/add_user", methods=['POST'])
def add_user():
    POST_USERNAME = str(request.form['username'])
    POST_PASSWORD = str(request.form['password'])

    s.add(User(POST_USERNAME, POST_PASSWORD))
    s.commit()
    session['logged_in'] = True
    return table_screen(True)

@app.route("/display_edit_page/<int:id>", methods=['POST'])
def display_edit_page(id):
    row = s.query(Course).filter(Course.id == id).one()
    advisors = s.query(User).all()
    # for advisor in advisors:
    #     print(advisor['username'])
    return render_template('edit_row.html', row=row, advisors=advisors)

@app.route('/table')
def table_screen(isLoggedIn=False):
    if not session.get('logged_in'):
        isLoggedIn = False
    else:
        isLoggedIn = True
    items = s.query(Course).all()
    return render_template('table.html', items=items, isLoggedIn=isLoggedIn)

if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(host='0.0.0.0', port=8000)


# if __name__ == '__main__':
#     app.run()
