import copy
import random


class Hat:
    def __init__(self, **colors):
        self.contents = []
        for color, count in colors.items():
            self.contents += [color] * count

    def __repr__(self):
        return f"{self.contents}"

    def __str__(self):
        return f"{self.contents}"

    def draw(self, num_balls):
        # If the number of balls to draw is zero or negative, return an empty list
        balls = []
        if num_balls <= 0:
            return balls
        # If the number of balls to draw exceeds the available number of balls, return all the balls
        if num_balls <= len(self.contents):
            balls = random.sample(self.contents, num_balls)

            for ball in balls:
                self.contents.remove(ball)
        # If the number of balls to draw exceeds the available number of balls, return all the balls
        # and clear all the balls in the hat
        else:
            balls = self.contents[:]
            self.contents.clear()

        return balls


def experiment(hat, expected_balls: dict, num_balls_drawn, num_experiments):
    success = 0
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        balls = hat_copy.draw(num_balls_drawn)
        balls_dict = {}
        for ball in balls:
            balls_dict[ball] = balls_dict.get(ball, 0) + 1
        is_success = True
        for color, count in expected_balls.items():
            if balls_dict.get(color, 0) < count:
                is_success = False
                break
        if is_success:
            success += 1

    return success / num_experiments


if __name__ == '__main__':
    hat = Hat(blue=3, red=1, green=3)
    print(hat)
    print(hat.draw(7))
