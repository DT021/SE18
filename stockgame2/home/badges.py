from pinax.badges.base import Badge, BadgeAwarded
	from pinax.badges.registry import badges

	class PointsBadge(Badge):
		slug = "points"
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
			user = state["user"]
			points = user.get_profile().points
			if points > 10:
				return BadgeAwarded(level=3)
			elif points > 5:
				return BadgeAwarded(level=2)
			elif points > 3:
				return BadgeAwarded(level=1)


	badges.register(PointsBadge)