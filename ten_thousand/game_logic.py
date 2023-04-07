import random
from collections import Counter

"""
(TODO)
1. Define a GameLogic class

2. Handle calculating score for dice roll
    - Add calculate_score static method to GameLogic class.
    - The input to calculate_score is a tuple of integers that represent a dice roll.
    - The output from calculate_score is an integer representing the roll’s score according to rules of game

3. Handle rolling dice
    - Add roll_dice static method to GameLogic class.
    - The input to roll_dice is an integer between 1 and 6.
    - The output of roll_dice is a tuple with random values between 1 and 6.
    - The length of tuple must match the argument given to roll_dice method.
"""


class GameLogic:

    # def __init__(self):
    #     self.score = 0

    score_combinations = {
        "1": 100,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 50,
        "6": 0,
        "3 of a kind": {
            "1": 1000,
            "2": 200,
            "3": 300,
            "4": 400,
            "5": 500,
            "6": 600
        },
        "4 of a kind": {
            "1": 2000,
            "2": 400,
            "3": 600,
            "4": 800,
            "5": 1000,
            "6": 1200
        },
        "5 of a kind": {
            "1": 3000,
            "2": 600,
            "3": 900,
            "4": 1200,
            "5": 1500,
            "6": 1800
        },
        "6 of a kind": {
            "1": 4000,
            "2": 800,
            "3": 1200,
            "4": 1600,
            "5": 2000,
            "6": 2400
        },
        "straight": 1500,
        "3 pairs": 1500,
    }

    @staticmethod
    def roll_dice(n):
        """
        Rolls n number of dice
        :param n: number of dice
        :return: a tuple with random values between 1 and 6
        """

        dice = []
        for _ in range(n):
            dice.append(random.randint(1, 6))
        return tuple(dice)

    @staticmethod
    def calculate_score(combination):
        """
        Calculates the score depending on the combination of 6 randomly generated numbers in a tuples
        :param combination: tuple of 6 integers representing different dice combinations
        :return: An integer representing a score
        """

        total_score = 0
        counts = Counter(combination)

        if sorted(combination) == [1, 2, 3, 4, 5, 6]:
            total_score += GameLogic.score_combinations['straight']
            return total_score
        # if counts == Counter({1: 3, 2: 3}):
        #     total_score += GameLogic.score_combinations['3 of a kind'][str(1)] + \
        #                    GameLogic.score_combinations['3 of a kind'][str(2)]
        #     return total_score
        if len(counts.most_common()) >= 2 and counts.most_common()[0][1] == 3 and counts.most_common()[1][1] == 3:
            total_score = GameLogic.score_combinations['3 of a kind'][str(counts.most_common()[0][0])] \
                          + GameLogic.score_combinations['3 of a kind'][str(counts.most_common()[1][0])]
            return total_score
        # if counts == Counter({1: 3, 2: 3}):
        #     total_score += GameLogic.score_combinations['3 of a kind'][str(1)] + GameLogic.score_combinations['3 of a kind'][str(2)]
        #     return total_score
        if len(counts) == 3 and all(count == 2 for count in counts.values()):
            total_score += GameLogic.score_combinations['3 pairs']
            return total_score

        # counts = Counter(combination)
        # if sorted(combination) == [1, 2, 3, 4, 5, 6]:
        #     total_score += GameLogic.score_combinations['straight']
        #     return total_score
        # if counts == Counter({1: 3, 2: 3}):
        #     total_score += GameLogic.score_combinations['3 of a kind'][str(1)] * 2
        #     return total_score
        # if counts == Counter({1: 2, 2: 2, 3: 2}):
        #     total_score += GameLogic.score_combinations['3 pairs']
        #     return total_score
   # so we need to verify len 6, quantity of 1st most common is 3, quantity of the 2nd most common is also 3, then add the scores

        for key in ['6 of a kind', '5 of a kind', '4 of a kind', '3 of a kind']:
            for value in combination:
                if combination.count(value) >= int(key[0]):
                    total_score += GameLogic.score_combinations[key][str(value)]
                    combination = [x for x in combination if x != value]
                    if key == '6 of a kind':
                        combination = []
                    break
        for value in combination:
            total_score += GameLogic.score_combinations[str(value)]
        print(total_score)
        return total_score


if __name__ == "__main__":
    pass
