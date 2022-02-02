class FTeam:

    def __init__(self, win, lose, draw, goals, missed):
        self.win = win
        self.lose = lose
        self.draw = draw
        self.goals = goals
        self.missed = missed

    def result(self, goals, missed):
        if goals > missed:
            self.win += 1
            print(f"Команда выиграла со счётом {goals}:{missed}")
            return self.win

        elif goals == missed:
            self.draw += 1
            print(f"Команда сыграла вничью со счётом {goals}:{missed}")
            return self.draw

        else:
            self.lose += 1
            print(f"Команда проиграла со счётом {goals}:{missed}")
            return self.lose

    def points(self, win, draw):
        point = self.win * 3 + self.draw
        print(f'У команды сейчас {point} очков')

    def difference(self, goals, missed):
        dif = self.goals - self.missed
        print(f'Разница забитых/пропущенных сейчас составляет - {dif}')


class FTeam2(FTeam):
    def total(self, win, lose, draw):
        tot = self.win + self.lose + self.draw
        print(f'Общее количество матечей команды - {tot} ')

