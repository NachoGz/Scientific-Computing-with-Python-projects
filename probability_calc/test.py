from math import perm
import prob_calculator
prob_calculator.random.seed(95)
# hat = prob_calculator.Hat(blue=4, red=2, green=6)

hat = prob_calculator.Hat(blue=3,red=2,green=6)
probability = prob_calculator.experiment(hat=hat, expected_balls={"blue":2,"green":1}, num_balls_drawn=4, num_experiments=10)
actual = probability
expected = 0.272
print(actual)
print(expected)


