[Program for Hand Cricket]
--------------------------

SSSV: [Vaibhav Singh Tomar, Kushagra Srivastava]

Project Files:
1. [handcricket.py]-
    This file includes main code that is necessary to run the program for desired outputs.
    It starts with importing random library in program. After that, we have imported some functions defined in other file which will come later and also, we have defined one function in main code itself.
    After defining and importing the function, we used try and except method for exceptional handling. 
    In try section, we have started with defining a Boolean expression named 'match' which is used to make a while loop which runs at least once.
    After that, we have taken player name as input. We defined some variables, list and dictionary as you can see in the code easily. 
    We opened a file named run_per_ball in write mode to store runs on any given ball.
    In next section, we have made our code in such a way so that firstly he takes the input between TOM and JERRY and then a number between 1 to 6. Then we perform a virtual toss in which
    if user wins the toss then the program asks him to choose between Batting or Bowling and if computer wins the toss then it randomly selects between Batting and Bowling.
    After this, we have created program such that innings of the match starts and user have asked to give input between 1 to 6 and computer randomly selects integer between 1 to 6.
    If user is batting and input given by user is equal to as selected by computer then user is declared to be out and computer starts batting and similarly it happens with computer if inning is first.
    After the end of any of the first or second inning, the program prints the name of player and then all the data about him like how many runs he have scored in how many balls.
    After the ending of second inning, a function is called which has given inputs as score of user and score of computer and the functions declares that who has won the match.
    Then the program asks the user for another match, if user says YES then whole code runs which is under the while loop and if user says NO then program stops running after printing previous matches scored
    which he has played after starting the code last time.
    We have used some extra features in this game which makes this game more beautiful like the Highscore of user and computer since from the starting of code for first time.
    It also counts that how many sixes and fours you have scored in the match.

2. [functions_used.py]-
    This file is used to contain the functions that are used in the main code. We have used functions contained in this file by importing the functions to main code.

3. [run_per_ball.txt]-
    This file is a txt file which is used to store runs scored on each ball. This file is capable of storing runs of matches which you have played after last time you have started the program freshy.

4. [run_given_by_user_per_match.txt]-
    This file is used to score runs given by users in a match since from the first start of the program and this file is used to calculate best score of computers in main program.

5. [final_scores_till_now.txt]-
    This file is used to store runs scored by user in matches he had played since from first start of the program and this file is used to calculate best score of users in main program.  


Sample Inputs:
Kushagra
TOM
4
Batting (if won the toss)
3
2
1
.... (until got out)
4
5
3
.... (until computer gets out or computer wins the match or match draw)

NO

