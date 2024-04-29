players = [
    {
        "name": "john",
        "position": "quarterback",
        "jerseyNo": "12",
        "stats": {
            "yards_gained": 250,
            "touchdowns": 2,
            "interceptions": 1
        }
    },
    {
        "name": "andy",
        "position": "defense",
        "jerseyNo": "06",
        "stats": {
            "tackles": 10,
            "sacks": 2
        }
    },
    {
        "name": "bob",
        "position": "offense",
        "jerseyNo": "15",
        "stats": {
            "receiving_yards": 150,
            "touchdowns": 1
        }
    }
]

positions = [player["position"] for player in players]
print("Player Positions: ", positions)

for player in players:
    if player["name"] == "andy":
        player["stats"]["receiving_yards"] = 200
        break

numOfplayers = len(players)

total_yards_gained = sum(player["stats"].get("yards_gained", 0) for player in players)
total_touchdowns  = sum(player["stats"].get("touchdown", 0) for player in players)

avg_yards_gained = total_yards_gained / numOfplayers
avg_touchdowns = total_touchdowns / numOfplayers

print("Average Yards Gained per Player: ", avg_yards_gained)
print("Average Touchdowns per Player: ", avg_touchdowns)
