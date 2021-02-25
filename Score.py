# Greed is a dice game where you roll up to five dice to accumulate
# points.  The following "score" function will be used calculate the
# score of a single roll of the dice.
#
# A greed roll is scored as follows:
#
# * A set of three ones is 1000 points
#
# * A set of three numbers (other than ones) is worth 100 times the
#   number. (e.g. three fives is 500 points).
#
# * A one (that is not part of a set of three) is worth 100 points.
#
# * A five (that is not part of a set of three) is worth 50 points.
#
# * Everything else is worth 0 points.
#
#
# Examples:
#
# score([1,1,1,5,1]) => 1150 points
# score([2,3,4,6,2]) => 0 points
# score([3,4,5,3,3]) => 350 points
# score([1,5,1,2,4]) => 250 points
#
# More scoring examples are given in the tests below:
#
# Your goal is to write the score method.

def score(dice):
    # You need to write this method
    result = 0
    aux = []
    NUMBER_OF_DICE_FACES = 7

    for i in range(NUMBER_OF_DICE_FACES): aux.append((i, dice.count(i)))
    for i, ni in aux:
        while ni > 0:
            if ni > 2:
                if i == 1:
                    result += 1000
                else:
                    result += i * 100
                ni -= 3
            else:
                if i == 1:
                    result += 100 * ni
                elif i == 5:
                    result += 50 * ni
                ni = 0
    return result
