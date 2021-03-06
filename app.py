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

@app.route('/new_user_screen', methods=['POST'])
def show_add_user_screen():
    return render_template('new_user_screen.html')

@app.route('/login', methods=['POST'])
def do_admin_login():
    POST_USERNAME = str(request.form['username']).strip()
    POST_PASSWORD = str(request.form['password'])

    query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]))
    result = query.first()
    if result:
        session['username'] = POST_USERNAME
        session['logged_in'] = True
        if (POST_USERNAME == 'Atkinson'):
            session['admin'] = True
    else:
        flash('wrong password!')
    return home()

@app.route('/add_row', methods=['POST'])
def add_row(isLoggedIn=False):
    POST_SCHOOL = str(request.form['school']).strip()
    POST_COUNTRY = str(request.form['country']).strip()
    POST_SCHOOL_COURSE = str(request.form['school_course']).strip().upper()
    POST_SCU_COURSE = str(request.form['scu_course']).strip().upper()
    POST_DETERMINATION = str(request.form['determination']).strip()
    POST_DESCRIPTION = str(request.form['description']).strip()

    s.add(Course(POST_SCHOOL, POST_COUNTRY,POST_SCHOOL_COURSE, POST_SCU_COURSE, POST_DETERMINATION, session['username'], datetime.now(), POST_DESCRIPTION))
    s.commit()
    return redirect(url_for('table_screen'))

@app.route("/logout")
def logut():
    session['logged_in'] = False
    session['admin'] = False
    return home()


@app.route("/delete/<int:id>", methods=['POST'])
def delete_row(id, isLoggedIn=false):
    row = s.query(Course).filter(Course.id == id).delete()
    s.commit()
    return redirect(url_for('table_screen'))

@app.route("/table/edit/<int:id>", methods=['POST'])
def edit_row(id, isLoggedIn=false):
    POST_SCHOOL = str(request.form['school']).strip()
    POST_SCHOOL_COURSE = str(request.form['school_course']).strip().upper()
    POST_SCU_COURSE = str(request.form['scu_course']).strip().upper()
    POST_DETERMINATION = str(request.form['determination']).strip()
    POST_ADVISOR = str(request.form['advisor']).strip()
    POST_DESCRIPTION = str(request.form['description']).strip()

    s.query(Course).filter(Course.id == id).update({"school": POST_SCHOOL, "school_course": POST_SCHOOL_COURSE,
                                                    "scu_course": POST_SCU_COURSE, "determination": POST_DETERMINATION,
                                                    "advisor": POST_ADVISOR, "date":datetime.now(), "description": POST_DESCRIPTION})
    s.commit()
    return redirect(url_for('table_screen'))

@app.route("/add_user", methods=['POST'])
def add_user():
    POST_USERNAME = str(request.form['username']).strip()
    POST_PASSWORD = str(request.form['password'])

    s.add(User(POST_USERNAME, POST_PASSWORD))
    s.commit()
    return table_screen(True)

@app.route("/display_edit_page/<int:id>", methods=['POST'])
def display_edit_page(id):
    r = s.query(Course).filter(Course.id == id).one()

    advisors = s.query(User).all()
    items = s.query(Course).all()
    # for advisor in advisors:
    #     print(advisor['username'])
    return render_template('edit_row.html', r=r, items=items, advisors=advisors, isLoggedIn=True)

@app.route('/table')
def table_screen(isLoggedIn=False):
    session['is_search'] = False
    if not session.get('logged_in'):
        isLoggedIn = False
    else:
        isLoggedIn = True
    items = s.query(Course).all()
    countries = []
    for country in s.query(Course).distinct(Course.country):
        if country.country not in countries:
            countries.append(country.country)
    schools = []
    for school in s.query(Course).distinct(Course.school):
        if school.school not in schools:
            schools.append(school.school)
    return render_template('table.html', items=items, countries = countries, schools=schools, isLoggedIn=isLoggedIn)

@app.route('/table/search_scu_course/', methods=['POST'])
def search_scu_course(isLoggedIn=false):
    search = str(request.form['search']).strip().upper()
    count = str(request.form['country']).strip()
    scho = str(request.form['school']).strip()
    countries = []
    for country in s.query(Course).distinct(Course.country):
        if country.country not in countries:
            countries.append(country.country)
    schools = []
    for school in s.query(Course).distinct(Course.school):
        if school.school not in schools:
            schools.append(school.school)
    session['is_search'] = True
    items = s.query(Course).filter(or_(Course.scu_course.like(search), Course.country.like(count),
                                   Course.school.like(scho))).all()
    return render_template('table.html', items=items, countries = countries, schools=schools)


if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(host='0.0.0.0', port=8000)
