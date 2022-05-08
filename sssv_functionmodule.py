# -----------------------------------------------------------------This part is coded by Kushagra Shrivastava--------------------------------------------------------------------------------------
# This is the function module which we will import and use in the original code.

# We define a function print_stars which can take one integer parameter i.e. how many stars we want to print.
def print_stars(n):
    while(n > 0):
        # end="" is used so that all stars are printedd in one line
        print("*", end="")
        n -= 1
    return

# We define a function player_name_in_stars, which take one string parameter. and it will give output as following:
# ******************************************player_name*********************************
# Runs       Balls       Strike Rate       Fours       Sixes       Carrier Best


def player_name_in_stars(player_name):
    print_stars(32)
    # here we have used the previous function print_stars
    print(player_name, end="")
    print_stars(32)
    print("*")
    print("Runs       Balls       Strike Rate       Fours       Sixes       Carrier Best")
    return

# We define a function final_result which have two parameter one os user score and second is computer score and it will give the result as whether the user wins, lose or draws the match.


def final_result(score_user, score_comp):
    if score_user > score_comp:
        print("Congratulations You won")
    elif score_user < score_comp:
        print("You lost!, Better luck next time")
    else:
        print("Match Drawn")
