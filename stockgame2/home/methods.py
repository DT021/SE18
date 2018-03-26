import psycopg2


def getdashboardinfo(userid):
	#current_user = request.user
	conn = psycopg2.connect(dbname="gyesfxht", user="gyesfxht", password="VwftaOkFDwF2LoGElDUxJ7i4kjJyALvy", host="stampy.db.elephantsql.com", port="5432")
	cur = conn.cursor()
	cur.execute('SELECT * from "home_player" WHERE "userID_id" = %s', [userid])
	x = cur.fetchall()
	print(x)

#getdashboardinfo(1)
