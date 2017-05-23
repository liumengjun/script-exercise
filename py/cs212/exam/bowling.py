"""
UNIT 1: Bowling:

You will write the function bowling(balls), which returns an integer indicating
the score of a ten-pin bowling game.  balls is a list of integers indicating 
how many pins are knocked down with each ball.  For example, a perfect game of
bowling would be described with:

    >>> bowling([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10])
    300

The rules of bowling are as follows:

(1) A game consists of 10 frames. In each frame you roll one or two balls,
except for the tenth frame, where you roll one, two, or three.  Your total
score is the sum of your scores for the ten frames.
(2) If you knock down fewer than ten pins with your two balls in the frame,
you score the total knocked down.  For example, bowling([8, 1, 7, ...]) means
that you knocked down a total of 9 pins in the first frame.  You score 9 point
for the frame, and you used up two balls in the frame. The second frame will
start with the 7.
(3) If you knock down all ten pins on your second ball it is called a 'spare'
and you score 10 points plus a bonus: whatever you roll with your next ball.
The next ball will also count in the next frame, so the next ball counts twice
(except in the tenth frame, in which case the bonus ball counts only once).
For example, bowling([8, 2, 7, ...]) means you get a spare in the first frame.
You score 10 + 7 for the frame; the second frame starts with the 7.
(4) If you knock down all ten pins on your first ball it is called a 'strike'
and you score 10 points plus a bonus of your score on the next two balls.
(The next two balls also count in the next frame, except in the tenth frame.)
For example, bowling([10, 7, 3, ...]) means that you get a strike, you score
10 + 7 + 3 = 20 in the first frame; the second frame starts with the 7.

保龄球的计分，每一局总共有十格，每一格里面有一球或两球。
共有十支球瓶，要尽量在两球之内把球瓶全部击倒，
如果第一球就把全部的球瓶都击倒了，也就是“STRIKE”，画面出现“X”，就算完成一格了，所得分数就是10分再加下两球的倒瓶数，
但是如果第一球没有全倒时，就要再打一球，如果剩下的球瓶全都击倒，也就是“SPARE”，画面出现“/”，也算完成一格，所得分数为10分再加下一格第一球的倒瓶数，
但是如果第二球也没有把球瓶全部击倒的话，那分数就是第一球加第二球倒的瓶数，再接着打下一格。
依此类推直到第十格。
但是第十格有两球或三球，第十格时如果第一球或第二球将球瓶全部击倒时，可再加打第三球。
"""


def bowling(balls):
    "Compute the total score for a player's game of bowling."
    ## bowling([int, ...]) -> int
    total = 0
    for frame in range(10):
        score, balls = score_frame(balls)
        total += score
    return total


def score_frame(balls):
    "Return two values: (score_for_this_frame, remaining_balls)."
    n_used, n_scoring = (
        (1, 3) if balls[0] == 10  # strike
        else (2, 3) if balls[0] + balls[1] == 10  # spare
        else (2, 2)  # open frame
    )
    return (sum(balls[:n_scoring]), balls[n_used:])


def test_bowling():
    assert 0 == bowling([0] * 20)
    assert 20 == bowling([1] * 20)
    assert 80 == bowling([4] * 20)
    assert 190 == bowling([9, 1] * 10 + [9])
    assert 300 == bowling([10] * 12)
    assert 200 == bowling([10, 5, 5] * 5 + [10])
    assert 11 == bowling([0, 0] * 9 + [10, 1, 0])
    assert 12 == bowling([0, 0] * 8 + [10, 1, 0])
    assert 20 == bowling([0, 0] * 9 + [10, 10, 0])
    assert 30 == bowling([0, 0] * 8 + [10, 10, 0])
    assert 168 == bowling(
        [9, 1, 0, 10, 10, 10, 6, 2, 7, 3, 8, 2, 10, 9, 0, 9, 1, 10])
    assert 24 == bowling([10, 3, 4] + [0] * 17)
    assert 168 == bowling(
        [10, 7, 3, 7, 2, 9, 1, 10, 10, 10, 2, 3, 6, 4, 7, 3, 3])
    assert 133 == bowling(
        [1, 4, 4, 5, 6, 4, 5, 5, 10, 0, 1, 7, 3, 6, 4, 10, 2, 8, 6])
    assert 16 == bowling([5, 5, 3, 0] + [0, 0] * 8)
    assert 200 == bowling([5, 5] + [10, 5, 5] * 5)
    assert 20 == bowling([0, 0] * 9 + [10, 5, 5])
    print('tests pass')


test_bowling()
