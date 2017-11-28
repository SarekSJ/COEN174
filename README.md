# COEN174
Team 6
Kelsey Pasco, Sarek Sotelo Jimenez, Ellen Tseng
11/28/17

Setting up the Course Equivalency App

Hey there! Welcome to our instruction guide on how to install and run the Course Equivalency Web App. This was a fun project to make and getting it to run is even more fun!

Procedure: 
==========
1. First, you’re going to want to make sure you’re all set up with a MySql account. If you haven’t set one up, make sure you talk to Lantz Johnson at the ECC. (<lantz@engr.scu.edu>) He’ll hook it up. 


2. Once you have a MySql account, make sure you run the `setup mysql5` in the terminal. This is crucial to setting up your MySql. 


3. Now that your MySql is all set, we can get started with the fun stuff. This app doesn’t use too many python packages, but it does use a few. We’ll be installing those in this step.


3a. The first package you’ll want is flask. To download this, just run `pip install flask --user` in the terminal.


3b.The second package will be your gateway to the MySql database through the code. For this, you’ll want to run `pip install mysql-python --user` as well as `pip install sqlalchemy --user`. 

4. Next we’re going to create a database within your MySql server. First, log into your server using `mysql -h dbserver.engr.scu.edu -p -u <username> <db_name>`, making sure to exchange the <> for your own information. Once logged in, run the following command: `CREATE DATABASE <DATABASENAME>;` Replace <DATABASENAME> with whatever you want your database to named. (Team6NineFifteen might be a good idea for a database name). 


Remember your MySql information! Now we’re going to be connecting our flask app to the MySql database we just created. Open our code and go into the *engine.py* file. Once opened, replace the values in between tags with your own information. 

Once you’ve done all that, you’re going to want to create some dummy data to give you an account to log in with. To do this, run `python make_dummy_data.py` in the terminal and you’ll have set up three accounts (Atkinson, Fang, Figueira) and a few course evaluations too.


And that’s it! All you need to do now is run `python app.py` in order to launch the flask app. Check it out by typing in 0.0.0.0:8000 into your web browser.
