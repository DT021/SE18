import psycopg2

def adduser(username, password, email):
	conn = psycopg2.connect(dbname="gyesfxht", user="gyesfxht", password="VwftaOkFDwF2LoGElDUxJ7i4kjJyALvy", host="stampy.db.elephantsql.com", port="5432")
	cur = conn.cursor()
	cur.execute('INSERT INTO home_user ("username", "password", "email", "leagueID0", "leagueID1", "leagueID2", "leagueID3") VALUES (%s, %s, %s, %s, %s, %s, %s)', (username, password, email, 0, 1 ,2, 3))
	conn.commit()
	conn.close()
adduser("hehe", "haha", "hoohoo@gmail.com")