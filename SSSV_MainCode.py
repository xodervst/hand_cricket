# This is the code for Hand Cricket Mini Project done by Kushagra and Vaibhav.
# ------------------------------------------------------------------------This part is coded by Vaibhav Singh Tomar-------------------------------------------------------------
# At first we will import the necessary function modules.
import random
# random module is imported for the random computer inputs
from sssv_functionmodule import print_stars
from sssv_functionmodule import player_name_in_stars
from sssv_functionmodule import final_result
# Above three functions are imported from the functions_used file that we created.

# We define a function writing_in_file which will take three parameteres ,first the name of txt file in which we want to write, second no of balls as integer and runs as integer.


def wriing_in_file(file_name, balls, runs):
    file_name.write(str(balls))
    file_name.write(" : ")
    file_name.write(str(runs))
    file_name.write('\n')


# Now we will start with try and except, as if user is giving correct inputs code will work otherwise the try block will end and except block will start.
try:
    # match is a dummy variable created to continue the loop untill it becomes false.
    match = True
    # At first it will take player_name as input
    player_name = input("Please enter your name: ",)
    # t is taken to print equal stars so as the output looks good.
    t = len(player_name)
    # In starting best score of user is set to 0. It will subsequently store the highest score among all the scores.
    best_user = 0
    # In starting best score of computer is set to 0. It will subsequently store the highest score among all the scores.
    best_comp = 0
    # list is created so that if computer wins the toss it can choose randomely between Batting and Bowling.
    l = ["Batting", "Bowling"]
    user_total_runs = {}
    # This empty dictionary is created to store user score in different matches and it will be shown at the end like this:
    # Your last 2  matches score are as given below:
    #{1: 31, 2: 45}
    file_of_runs = open("run_by_ball.txt", mode='w')
    # A txt file is created to store run per ball .
    i = 0
    # i=0 is a dummy variable which is et to 0 initially and it will be incremented by 1 per ball. So, it will show the no, of balls.
    while(match):
        # A loop is created which will write the run_by_ball file as runs scored in each ball.
        i += 1
        file_of_runs.write('Match: ')
        file_of_runs.write(str(i))
        file_of_runs.write('\n')
        # Above three line of code will store as the folloeing: ball no: runs scored on that ball
        scores_of_user = open("final_scores_till_now.txt", "r")
        # A new file is opened in which all previous scores of user is stored. And it is opened for read operation.
        # The below loop will go through each score and will check if the score in current match is highest among all or not. If it will be highest then it will change the best_score with the new highest score.
        for lines in scores_of_user.readlines():
            scored_runs = int(lines.strip())
            if(best_user < scored_runs):
                best_user = scored_runs
        scores_of_user.close()
        # The file is closed.

        scores_of_comp = open("runs_given_by_user_per_match.txt", "r")
        # A new file is opened in which all previous scores of computer is stored. And it is opened for read operation.
        # The below loop will go through each score and will check if the score in current match is highest among all or not. If it will be highest then it will change the best_score with the new highest score.
        for lines in scores_of_comp.readlines():
            scored_runs = int(lines.strip())
            if(best_comp < scored_runs):
                best_comp = scored_runs
        scores_of_comp.close()
        # The file is closed.
        toss_computer = random.randrange(1, 6)
        # it will give toss_computer a random input from 1 to 6.

# Our toss formula is like this. First User will give input as "TOM" or "JERRY". Then again user will give an input between [1,6] and we have already taken a input from computer between [1,6]. So if user has selected TOM and user input+computer input is even then the user wins the toss and if usser has selected JERRY and user input+computer input is odd then the user wins the toss and in any other case user loses.
        while True:
            # Here we take "TOM" or "JERRY" input from the user.
            toss_user1 = input("Choose TOM or JERRY: ",)
            if toss_user1 == 'TOM' or toss_user1 == 'JERRY':
                break
            # Here we check for error, if user gives input other than TOM or JERRY, it will say invalid input.
            print("You have given an invalid input. Please try again.")

        while True:
            # Here we take user input between [1,6].
            toss_user = int(input("Give any number between 1 and 6: ",))
            if(toss_user <= 6 and toss_user >= 1):
                break
            # Here we check foir error. If user gives input other than the range [1,6], it will give an error message.
            print("You have given an invalid input. Please try again.")

        print("Computer choose: ", toss_computer)
        # The above line prints the computer's choice.
        if ((toss_user+toss_computer) % 2 == 0 and toss_user1 == "TOM") or ((toss_user+toss_computer) % 2 != 0 and toss_user1 == "JERRY"):
            # This is the case when user wins toss.
            print('Congratulations You won the toss')
            flag = True  # flag is True if user eins toss.
            print("Now, choose batting or bowling")
            while True:
                # Now it will ask user to select Batting or Bowling.
                choice = input(
                    "input 'Batting' to choose bat first or 'Bowling' to choose bowl first: ",)
                if(choice == 'Batting' or choice == 'Bowling'):
                    break
                # Here it checks for error if the user gives invalid input, it will show an error message.
                print("You have entered any wrong or invalid input. Please try again.")
            print("You selected:", choice)

        else:
            flag = False  # flag is false if user loses toss.
            print('Sorry You lost the toss')
            # This will randomely choose Batting or Bowlig for computer.
            choice = random.choice(l)
            print('Computer selected', choice)

# The below variables are ccreated and set to zero in the starting of the match. These variables will be incremented accordingly as the match starts.
        # This counts the no. of balls in first inning.
        first_inning_balls = 0
        # This counts the no. of balls in second innings.
        second_inning_balls = 0
        # This counts the user score.
        user_score = 0
        # This counts the computer score.
        computer_score = 0
        # This counts the no. of sixes hit by user.
        user_sixes = 0
        # This counts the no. of fours hit by user.
        user_fours = 0
        # This counts the no. of sixes hit by computer.
        computer_sixes = 0
        # This counts the no. of fours hit by computer.
        computer_fours = 0
        # This counts the no. of half century hit by user.
        halfcentury_user = 0
        # This counts the no. of century hit by user.
        century_user = 0
        # This counts the no. of half century hit by computer.
        halfcentury_computer = 0
        # This counts the no. of century hit by computer.
        century_computer = 0

        if (flag == True and choice == "Batting") or (flag == False and choice == 'Bowling'):
            # This is the case when user wins toss and choose Batting or user lose toss and Computer choose Bowling
            print("Your Batting Starts")
            flag1 = 0  # flag1 is 0 for first inning.
            while flag1 == 0:
                # This loop will take batting input from user Untill flag1=0.
                first_inning_balls += 1
                while True:
                    user_input = int(
                        input("Give any input between 1 and 6: ",))

                    if(user_input <= 6 and user_input >= 1):
                        # It checks for error whether the batting input is in the range [1,6] or not.
                        break
                    print("You have given an invalid input. Please try again.")

                comp_input = random.randint(1, 6)
                # It gives random integer in range[1,6] to computer input
                if user_input == comp_input:
                    # According to our game if user input is same as computer input user is out. So it will stop the first inning.
                    print("Bad Luck You are OUT")
                    # flag1=1 this signifies the starting of second inning.
                    flag1 = 1
                    break
                else:
                    # if user input is not same as computer input . It adds the user input into the user score.
                    user_score += user_input
                    if(user_input == 4):
                        user_fours += 1  # It counts for the no of fours hit.
                    elif(user_input == 6):
                        # It counts for the number of sixes hit.
                        user_sixes += 1

                    if(user_score >= 50 and halfcentury_user == 0):
                        # It checks if user hits half century and congratulates.
                        print("Congrats", player_name,
                              "! You have completed a half century in this match.")
                        # It counts no of half century hit by the user.
                        halfcentury_user = 1
                    if(user_score >= 100 and century_user == 0):
                        # It checks if user hits century and congratulates.
                        print("Congrats", player_name,
                              "! You have completed a century in this match.")
                        # It counts no of half century hit by the user.
                        century_user = 1
                    if(best_user < user_score):
                        # It updates the highest score of user in its whole carrier.
                        best_user = user_score
                    print("Your Score:", user_score)
                    wriing_in_file(
                        file_of_runs, first_inning_balls, user_input)
                    # This stores the run per ball.

            # The below code will print the data of first inning.
            strike_rate = (user_score/first_inning_balls)*100
            player_name_in_stars(player_name)
            print(user_score, "        ", first_inning_balls, "            ", round(
                strike_rate, 2), "          ", user_fours, "         ", user_sixes, "       ", best_user)
            print_stars(64+t)
            print("*")
            print("Now Computer will bat")
            while flag1 == 1 and computer_score <= user_score:
                # Now second inning starts and the loop will continue unless the computer is out or it croses the user score.
                # It counts the no of balls in second inning.
                second_inning_balls += 1
                while True:
                    user_input = int(
                        input("Give any input between 1 and 6: ",))
                    if(user_input <= 6 and user_input >= 1):
                        break
                    # It checks for error in the bowling input given by user.
                    print("You have given an invalid input. Please try again.")

                comp_input = random.randint(1, 6)
                # It gives random batting input for computer.
                if user_input == comp_input:
                    # According to our algorithm if user input = computer input. It is out.
                    print("Bravo! Computer is out")
                    flag1 = 2  # flag1=2 signifies end of second inning.
                    break
                else:
                    # if user input is not equal to computer input the code will come to else block.
                    if(comp_input == 4):
                        # it counts for no of fours hit by computer.
                        computer_fours += 1
                    elif(comp_input == 6):
                        # it counts for no of 6 hit by computer.
                        computer_sixes += 1
                    computer_score += comp_input
                    if(computer_score >= 50 and halfcentury_computer == 0):
                        print(
                            "Congrats Computer has completed a half century in this match.")
                        halfcentury_computer = 1
                        # This counts if computer hits half century and congratulates.
                    if(computer_score >= 100 and century_computer == 0):
                        print(
                            "Congrats! Computer has completed a century in this match.")
                        century_computer = 1
                        # This counts if computer hits century and congratulates.
                    if best_comp < computer_score:
                        best_comp = computer_score
                        # This updates the best carrier score of computer if present score is greater than the previous scores.

                    # This prints the computer score
                    print("Computer's Score:", computer_score)

            # This calculates the strike rate for computer.
            strike_rate = (computer_score/second_inning_balls)*100
            # The below 5 line code will give all the data for the second innings.
            player_name_in_stars('Computer')
            print(computer_score, "        ", second_inning_balls, "             ", round(
                strike_rate, 2), "         ", computer_fours, "         ", computer_sixes, "       ", best_comp)
            print_stars(72)
            print("*")

# -----------------------------------------------This part is coded by Kushagra Srivastava----------------------------------------------------------------------------------
        elif (flag == True and choice == "Bowling") or (flag == False and choice == 'Batting'):
            # This is the case when user wins toss and choose Bowling or user lose toss and Computer choose Batting
            print("Computer bats first and your bowling starts")
            flag1 = 0  # flag1 = 0 for the first inning.
            while flag1 == 0:
                # This loop will take batting input from user Untill flag1=0.
                first_inning_balls += 1
                while True:
                    user_input = int(
                        input("Give any input between 1 and 6: ",))
                    if(user_input <= 6 and user_input >= 1):
                        break
                    # It checks for error whether the batting input is in the range [1,6] or not.
                    print("You have given an invalid input. Please try again.")

                comp_input = random.randint(1, 6)
                # It gives random integer in range[1,6] to computer input.
                if user_input == comp_input:
                    # According to our game if user input is same as computer input user is out. So it will stop the first inning.
                    print("Bravo! Computer is out")
                    # Calculates the strike rate for computer.
                    strike_rate = (computer_score/first_inning_balls)*100
                    # Prints all the data for the first inning.
                    player_name_in_stars("Computer")
                    print(computer_score, "        ", first_inning_balls, "             ", round(
                        strike_rate, 2), "         ", computer_fours, "         ", computer_sixes, "       ", best_comp)
                    print_stars(72)
                    print("*")
                    # flag1=1 signifies the starting of second inning.
                    flag1 = 1
                    print("Now Computer will bowl and you will bat.")
                    break
                else:
                    # If user input is not equal to computer input, the code will run into else block.
                    if(comp_input == 4):
                        # It counts for no. of fours hit by computer.
                        computer_fours += 1
                    elif(comp_input == 6):
                        # It counts for no. of sixes hit by computer.
                        computer_sixes += 1
                    computer_score += comp_input
                    # It increments computer score in each iteration.
                    if(computer_score >= 50 and halfcentury_computer == 0):
                        print(
                            "Congrats Computer has completed a half century in this match.")
                        # It checks if computer scores more than 50 and congratulates.
                        halfcentury_computer = 1

                    if(computer_score >= 100 and century_computer == 0):
                        print(
                            "Congrats! Computer has completed a century in this match.")
                        # It checks if computer scores more than 100 and congratulates.
                        century_computer = 1

                    if best_comp < computer_score:
                        best_comp = computer_score
                    print("Computer's Score:", computer_score)
                    # It checks if the present computer score is greater than the previous highest score by computer and if it is greater than previous score it updates the best score of computer.
            while flag1 == 1 and user_score <= computer_score:
                # Second inning starts and the loop goes on untill user is out or it crosses the computer score.
                while True:
                    user_input = int(
                        input("Give any input between 1 and 6: ",))
                    # It takes user input in range[1,6]
                    if(user_input <= 6 and user_input >= 1):
                        break
                    # It checks for error in input and gives error message in case of invalid input.
                    print("You have given an invalid input. Please try again.")
                second_inning_balls += 1
                # No of balls in second inning is incremented in each iteration.
                comp_input = random.randint(1, 6)
                # It gives computer a random input in the range [1,6]
                if user_input == comp_input:
                    # If user input is equal to computer input. User will be out according to our gaming rules.
                    print("Bad Luck You are OUT")
                    # print("Total user score:", user_score)
                    flag1 = 2  # This signifies the end of second innings.
                    break
                else:
                    # If user input is not equal to computer input, code runs into the else block and user score is incremented by user input.
                    user_score += user_input
                    if(user_input == 4):
                        # It counts no of fours hit by user.
                        user_fours += 1
                    elif(user_input == 6):
                        # It counts no of sixes hut by user.
                        user_sixes += 1
                    if(user_score >= 50 and halfcentury_user == 0):
                        print("Congrats", player_name,
                              "! You have completed a half century in this match.")
                        # It checks if user scores more than 50 and congratulates.
                        halfcentury_user = 1
                    if(user_score >= 100 and century_user == 0):
                        print("Congrats", player_name,
                              "! You have completed a century in this match.")
                        # It checks if user scores more than 100 and congratulates.
                        century_user = 1
                    if(best_user < user_score):
                        best_user = user_score
                        # It checks if the present user score is greater than the previous highest score by user and if it is greater than previous score it updates the best score of user.
                    print('Score:', user_score)
                    wriing_in_file(
                        file_of_runs, first_inning_balls, user_input)
                    # It writes the run per ball file.

            # It calculates the strike rate for user.
            strike_rate = (user_score/second_inning_balls)*100
            # The below code will print the data for the second innings.
            player_name_in_stars(player_name)
            print(user_score, "        ", second_inning_balls, "            ", round(
                strike_rate, 2), "          ", user_fours, "         ", user_sixes, "       ", best_user)
            t = len(player_name)
            print_stars(64+t)
            print("*")

        final_result(user_score, computer_score)
        # It uses final result function and gives the output as who wins or if the match draws.

        user_total_runs[i] = user_score
        # This stores in dictionary as Match Number : Score in that Match.
        score_of_user = open("final_scores_till_now.txt", "a")
        score_of_user.write(str(user_score))
        score_of_user.write("\n")
        score_of_user.close()
        # The above four line code will update the data of scores by user in all the previous matches.

        score_of_comp = open("runs_given_by_user_per_match.txt", "a")
        score_of_comp.write(str(computer_score))
        score_of_comp.write("\n")
        score_of_comp.close()
        # The above four line code will update the data of scores by computer in all the previous matches.
# ------------------------------------------------------------This part is coded by both---------------------------------------------------------------------------------------
        while True:
            # This loop will ask for if user wants to play another match or not.
            new_match = input(
                "Want another match? If yes then enter 'YES' and if no then enter 'NO': ",)
            if(new_match == 'NO'):
                # If user doesn't want to play another match, it will show the details for the previous matches.
                print("Your last", i, " matches score are as given below: ")
                print(user_total_runs)
                print("I hope you enjoyed the game", player_name, ", Bye!")
                # match becomes false so that new game doesn,t starts.
                match = False

                break
            elif(new_match != 'NO' and new_match != 'YES'):
                print("You have given an invalid input. Please give a valid input.")
                # If user gives invalid input it will show an error message.
            else:
                break
    file_of_runs.close()
    # The file is closed which stores run per ball.

except:
    # This is for the exception if the user gives wrong input in the starting.
    print("Sorry but you have given some wrong input.")
