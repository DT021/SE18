Alright so right now elephantDB wont allow django to connect or create a test database when run in the test mode, I am looking into changing these settings, for now though, this is how I setup my machine for running test cases

1. Download the windows postgresql client https://www.enterprisedb.com/downloads/postgres-postgresql-downloads
I used PSQL 10
2. Install it, set up your postgres superuser account, make sure the port number is 5432
Alright so it should start the psql service in the background, if not let me know
3. Go to settings.py and comment out the HOST setting under DATABASES and change to ‘HOST’: ‘localhost’ (this is so you can swap between the two depending on whether you wish to use the prod version of the site or the test.
4. So here is where things get a little hairy, add the psql bin folder to your PATH environment variables (mine is C:\Program Files\PostgreSQL\10\bin)
	(you can do this in cmd with ‘set PATH=%PATH%;C:\[PATH]’)
5. Open the command line and run:
6. psql -U postgres -c "CREATE ROLE gyesfxht LOGIN NOSUPERUSER INHERIT CREATEDB CREATEROLE;"
7. It should say something like role created
8. Now run 
psql -U postgres -c “ALTER USER gyesfxht  WITH PASSWORD 'VwftaOkFDwF2LoGElDUxJ7i4kjJyALvy';”
It should say something like user altered
9. Launch into the venv like you would be running manage.py runserver
10. Instead run ‘manage.py test home.inttests’
Should run perfectly, if not message me with a screenshot or description of what it says
