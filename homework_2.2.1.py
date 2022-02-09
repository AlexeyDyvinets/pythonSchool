class FTeam:

    def __init__(self, win, lose, draw, goals, missed):
        self.win = win
        self.lose = lose
        self.draw = draw
        self.goals = goals
        self.missed = missed

    def add_result(self, goals, missed):
        self.goals += goals
        self.missed += missed
        if self.goals > self.missed:
            self.win += 1
            print(f"Команда выиграла со счётом {goals}:{missed}")
            return self.win

        elif self.goals == self.missed:
            self.draw += 1
            print(f"Команда сыграла вничью со счётом {goals}:{missed}")
            return self.draw

        else:
            self.lose += 1
            print(f"Команда проиграла со счётом {goals}:{missed}")
            return self.lose

    def points(self):
        point = self.win * 3 + self.draw
        print(f'У команды сейчас {point} очков')

    def difference(self):
        dif = self.goals - self.missed
        print(f'Разница забитых/пропущенных сейчас составляет - {dif}')


class FTeam2(FTeam):
    def __init__(self, win, lose, draw, goals, missed):
        super().__init__(win, lose, draw, goals, missed)

    def total(self):
        tot = self.win + self.lose + self.draw
        print(f'Общее количество матечей команды - {tot} ')


if __name__ == '__main__':
    ukr = FTeam(0, 0, 0, 0, 0)
    ukr.add_result(5, 1)
    print(ukr.goals, ukr.missed)
