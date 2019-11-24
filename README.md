# SE18
# This is a guide on how to start the program.
# Make sure you have 64-bit Python installed on your computer. 
Windows: https://www.python.org/downloads/windows/
MAC: https://www.python.org/downloads/mac-osx/
LINUX: https://www.python.org/downloads/source/
# 0.) run: pip install requirements.txt
# 1.)Go to cmd for windows and terminal for Mac and make sure you are in the stockgame2 directory. 
# 2.)If you are using a windows computer type:windowsvenv\Scripts\activate
# 2 alt.) If you are using a mac type:source macvenv/bin/activate
# 3.)Type:python manage.py runserver
# 4.)Go to browser and go to http://localhost:8000
# 5.)If you do no see any styles or pictures on that localhost:8000, then go to SE18/stockgame2/stockgame/settings.py and scroll all the way down until you see STATICFILES_DIRS. Read the comments under that.

Sample usernames and passwords to login:
Username: SEDemo		Password: pwdpwdpwd
Username: safa			Password: pwdpwdpwd

Leagues to Join:
Username: SoftwareEngineering	Password: pwd
Username: League of Friendship 	Password: pwd

Can also create new username and leagues

To run tests, set up Testing Database:
1. Download the windows postgresql client https://www.enterprisedb.com/downloads/postgres-postgresql-downloads
I used PSQL 10
2. Install it, set up your postgres superuser account, make sure the port number is 5432
3. Alright so it should start the psql service in the background, if not let me know
4. Go to settings.py and comment out the HOST setting under DATABASES and change to ‘HOST’: ‘localhost’ (this is so you can swap between the two depending on whether you wish to use the prod version of the site or the test.
5.So here is where things get a little hairy, add the psql bin folder to your PATH environment variables (mine is C:\Program Files\PostgreSQL\10\bin)
	(you can do this in cmd with ‘set PATH=%PATH%;C:\[PATH]’)
6. Open the command line and run:
psql -U postgres -c "CREATE ROLE <database_name> LOGIN NOSUPERUSER INHERIT CREATEDB CREATEROLE;"
7. It should say something like role created
8. Now run 
psql -U postgres -c “ALTER USER <database_name> WITH PASSWORD '<database_pwd>';”
9. It should say something like user altered
10. Launch into the venv like you would be running manage.py runserver
11. Instead run ‘manage.py test home.unit_tests’ or ‘manage.py test home.inttests’


See SE18/inttests for integration testing README
See SE18/unit_tests for unit testing README

see sources.txt for authors information

All images are located under stockgame2/home/static/home2

See database configuration in stockgame2/stockgame/settings.py

Hosted website: titantrading.herokuapp.com  



