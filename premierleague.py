class Team:
    def __init__(self, name, played, won, drawn, lost, gf, ga):
        self.name = name
        self.played = played
        self.won = won
        self.drawn = drawn
        self.lost = lost
        self.gf = gf
        self.ga = ga

    @property
    def gd(self):
        return self.gf - self.ga

    @property
    def points(self):
        return self.won * 3 + self.drawn


teams = [
    Team("Arsenal", 38, 28, 5, 5, 88, 43),
    Team("Man City", 38, 29, 6, 3, 94, 33),
    Team("Liverpool", 38, 24, 8, 6, 85, 40),
    Team("Chelsea", 38, 21, 11, 6, 76, 38),
    Team("Aston Villa", 38, 18, 12, 8, 70, 45),
    Team("Manhester United", 38, 16, 10, 12, 65, 50),
    Team("Tottenham", 38, 15, 11, 12, 60, 55),
    Team("West Ham", 38, 14, 10, 14, 55, 50),
    Team("brighton", 38, 12, 14, 12, 50, 45),
    Team("bournmouth", 38, 10, 12, 16, 45, 60),
]

# Sort
teams.sort(key=lambda x: (x.points, x.gd), reverse=True)

# Print table
for t in teams:
    print(f"{t.name:12} Pts: {t.points} GD: {t.gd}")
