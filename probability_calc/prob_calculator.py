import copy
from math import perm
import random
from unittest.main import TestProgram
# Consider using the modules imported above.

class Hat:
    
    def __init__(self, **args):
        contents = []
        # temp = []
        for key in args:
            for value in range(args[key]):
                contents.append(key)          
        self.contents = contents

    # draw method that accepts an argument indicating the number of balls to draw from the hat
    def draw(self, num_balls):
        contents = self.contents
        draw = []

        if num_balls >= (len(contents)-1):
            return contents
        else:
            for i in range(num_balls):
                choice = random.choice(self.contents)
                draw.append(choice)
                index = self.contents.index(choice)
                del self.contents[index]
        self.contents = contents

        return draw


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    bad = 0

    for n in range(num_experiments):
        exp = copy.deepcopy(hat)
        balls = exp.draw(num_balls_drawn)
        for v in expected_balls.keys():
            count = 0
            for x in range(len(balls)):
                if balls[x] == v:
                    count += 1
            if count < expected_balls[v]:
                bad += 1
                break
            
    return 1 - bad /num_experiments