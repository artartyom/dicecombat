import numpy as np

class Dice:

    def __init__(self, num_sides):
        self.sides=int(num_sides)
        self.lastroll=[[],0]

    def roll(self, n = 1):
        self.lastroll=[[],0]
        for n in range(n):
            roll = np.random.randint(1, self.sides + 1)
            self.lastroll[0].append(roll)
            self.lastroll[1] += roll
        return self.lastroll

def open_dicebox():
    global dicebox
    dicebox = {"d3":Dice(3),
                "d4":Dice(4),
                "d6":Dice(6),
                "d8":Dice(8),
                "d10":Dice(10),
                "d12":Dice(12),
                "d20":Dice(20),
                "d100":Dice(100)}

def roll(rollexpr):
    if "+" in rollexpr:
        dice, bonus = rollexpr.split('+')
    elif "-" in rollexpr:
        dice, bonus = rollexpr.split('-')
    else:
        dice, bonus = (rollexpr, 0)
    
    if dice[0] != "d":
        dice_num=int(dice[:dice.find("d")])
        dice=dice[dice.find("d"):]
    
    if not dice in dicebox.keys():
        dicebox[dice] = Dice(dice[1:])

    result = dicebox[dice].roll(int(dice_num))
    result[1] += int(bonus)

    return result

def discard_lowest(data_in, n = 1):
        data_out = [[],0]
        data_out[0] = data_in[0][:]
        data_out[1] = data_in[1] - sum(data_in[0])
        for iter in range(n):
            data_out[0].remove(min(data_out[0]))
    
        data_out[1] += sum(data_out[0])
        return data_out

def discard_highest(data_in, n = 1):
        data_out = [[],0]
        data_out[0] = data_in[0][:]
        data_out[1] = data_in[1] - sum(data_in[0])
        for iter in range(n):
            data_out[0].remove(max(data_out[0]))
    
        data_out[1] += sum(data_out[0])
        return data_out