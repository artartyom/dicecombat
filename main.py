import dice
dice.initiate_dicebox()

class Character:

    def __init__(self, name, stats = [0, 0, 0]):
        if stats == [0, 0, 0]:
            self.stats = [discarddice.roll]
        self.name = name

    def generate(self, statdie = 6, dicerolls = 4, discards = 1):
        stat_die = Dice(statdie)
        for stat in self.stats:
            stat_die.roll(dicerolls)
            for discard in range(discards):
                self.stats[stat] = stat_die.discard_lowest()
            print(stat + " : " + str(self.stats[stat][1]))
    
    def.alive(self):
