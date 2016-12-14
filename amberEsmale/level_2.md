# ForeignKey Relationships

1. Find all teams in the Atlantic Soccer Conference
"teams": Team.objects.filter(league__name = "Atlantic Soccer Conference"),
2. Find all (current) players on the Boston Penguins
"players": Player.objects.filter(curr_team__team_name = "Penguins", curr_team__location = "Boston")
3. Find all (current) players in the International Collegiate Baseball Conference
"players": Player.objects.filter(curr_team__league__name = "International Collegiate Baseball Conference")
4. Find all (current) players in the American Conference of Amateur Football with last name "Lopez"
"players": Player.objects.filter(curr_team__league__name = "American Conference of Amateur Football", last_name = "Lopez")
5. Find all football players
"players": Player.objects.filter(curr_team__league__sport = "Football")
6. Find all teams with a (current) player named "Sophia"
"teams": Player.objects.filter(first_name = "Sophia")
<li>{{team.curr_team.location}} {{team.curr_team.team_name}}</li>
7. Find all leagues with a (current) player named "Sophia"
"leagues": Player.objects.filter(first_name = "Sophia"),
<li>{{league.curr_team.league.name}}</li>
8. Find everyone with the last name "Anderson" who DOESN'T (currently) play for the Phoenix Rays
"players": Player.objects.filter(last_name = "Anderson").exclude( curr_team__location = "Phoenix", curr_team__team_name = "Rays")
