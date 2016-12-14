# Simple finds

1. Find all baseball leagues
"leagues": League.objects.filter(sport = "Baseball")
2. Find all womens' leagues
"leagues": League.objects.raw('SELECT * FROM leagues_league WHERE name LIKE "%women%" '),
3. Find all leagues where sport is any type of hockey
"leagues": League.objects.raw('SELECT * FROM leagues_league WHERE sport LIKE "%hockey%" '),
4. Find all leagues where sport is something OTHER THAN football
"leagues": League.objects.raw('SELECT * FROM leagues_league WHERE sport NOT LIKE "%football%" '),
5. Find all leagues that call themselves "conferences"
"leagues": League.objects.raw('SELECT * FROM leagues_league WHERE name LIKE "%conference%" '),
6. Find all leagues in the Atlantic region
"leagues": Team.objects.raw('SELECT * FROM leagues_team WHERE location LIKE "%Connecticut%" ')
7. Find all teams based in Dallas
"teams": Team.objects.filter(location = "Dallas"),
8. Find all teams named the Raptors
"teams": Team.objects.filter(team_name = "Raptors"),
9. Find all teams whose location includes "City"
"teams": Team.objects.raw('SELECT * FROM leagues_team WHERE location LIKE "%city%" '),
10. Find all teams whose names begin with "T"
"teams": Team.objects.raw('SELECT * FROM leagues_team WHERE team_name LIKE "T%" '),
11. Return all teams, ordered alphabetically by location
"teams": Team.objects.raw('SELECT * FROM leagues_team ORDER BY location ASC')
12. Return all teams, ordered by team name in reverse alphabetical order
		"teams": Team.objects.raw('SELECT * FROM leagues_team ORDER BY location DESC')
13. Find every player with last name "Cooper"
		"players": Player.objects.raw('SELECT * FROM leagues_player WHERE last_name LIKE "%cooper%" ')
14. Find every player with first name "Joshua"
		"players": Player.objects.raw('SELECT * FROM leagues_player WHERE first_name LIKE "%joshua%" ')
15. Find every player with last name "Cooper" EXCEPT FOR Joshua
	"players": Player.objects.raw('SELECT * FROM leagues_player WHERE first_name NOT LIKE "%joshua%" AND last_name LIKE "%cooper%" ')
16. Find all players with first name "Alexander" OR first name "Wyatt"
		"players": Player.objects.raw('SELECT * FROM leagues_player WHERE first_name LIKE "Alexander" OR first_name LIKE "Wyatt" ')
