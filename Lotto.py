import random


class Dice:
    def roll(self):
        first = random.randint(1, 52)
        second = random.randint(1, 52)
        third = random.randint(1, 52)
        fourth = random.randint(1, 52)
        fifth = random.randint(1, 52)
        sixth = random.randint(1, 52)
        return first, second, third, fourth, fifth, sixth


dice = Dice()
print(dice.roll())