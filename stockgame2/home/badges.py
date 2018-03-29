from pinax.badges.base import Badge, BadgeAwarded
from pinax.badges.registry import badges
from .models import Transaction
	class SalesBadge(Badge):
		slug = "sales"
		levels = [
			"Bronze",
			"Silver",
			"Gold",
		]
		events = [
			"stocks_sold",
		]
		multiple = False
	# MAKE NEW THING IN PLAYER TRACKING SELLS
		def award(self, **state):
			player = state["player"]
			sales = Transaction.objects.filter(leagueID=player.leagueID, isBuy=False,playerID=player.playerID).count()
			if sales > 10:
				player.userID.points = player.userID.points + 5	
				return BadgeAwarded(level=3)
			elif sales > 5:
				player.userID.points = player.userID.points + 3
				return BadgeAwarded(level=2)
			elif sales > 3:
				player.userID.points = player.userID.points + 1
				return BadgeAwarded(level=1)


	badges.register(PointsBadge)