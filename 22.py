games = ['CS', 'FIFA', 'Kabaddi', 'Hockey', 'Cricket']

for game in games:
    print(game)
    print()
    print(games.index(game)+1,game)
    print()

for game in games[:3]:
    print(game)