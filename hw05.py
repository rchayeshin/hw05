"""
Name: (Riley Chaye-Shin)
Peers: (add any collaborators)
References: (lecture slides, python tutor, textbook)
"""

def get_letter():
    """Asks for A, B, or C and returns it"""
    # remove the default return and add your code
    while True:
        #ask user for letter
        letter = input("Give a single uppercase letter:")
        #check that length of input is 1
        if len(letter) != 1:
            print("Error: it needs to be a single character.")
            continue
        #character must be A, B, or C
        if letter == "A" or letter == "B" or letter == "C":
            return letter
        else:
            print("Error: You provided the wrong character.")


def get_digit():
    """Asks for 1, 2, or 3 and returns it"""
    # remove the default return and add your code
    #asks user for digit
    while True:
        digit = input("Give an single number character: ")
        #check that input is only a digit
        if digit.isdigit() == False:
            print("Error: your input should be only digits.")
            continue
        #digit has to be 1, 2, or 3
        if digit == "1" or digit == "2" or digit == "3":
            return digit
        else:
            print("Error: a single digit needs to be in [1,3].")


def check_pattern(letter, digit, lst):
    """Prints the words that have the letter and then the digit"""
    # remove the default pass and add your code
    print("Strings with the pattern:")
    #read one word at a time
    for word in lst:
        #assume word does not have the pattern
        has_pattern = False
        for letter_position in range(len(word)):
            #digit_position comes after letter_position so digit will come later n word than letter
            for digit_position in range(letter_position + 1, len(word)):
                if word[letter_position] == letter and word[digit_position] == digit:
                    has_pattern = True
                    #pattern exists at leats onc time
                    
         #print the word once           
        if has_pattern == True:
            print(word, end=" ")
            #keeps everything on one line
    print()
    #to move to a new line after all the words

#  The function main is INCOMPLETE, you must finish it
# before you submit
def main ():
    """Reads a letter and number pair and searches for matches in list"""

    # The list inside of which we will search the user pair (DO NOT MODIFY)
    # -------------------------------------------------
    st_list = ["@C@2", "@2B", "A3", "C2C2", "AA@1", "@B@33",
    "B@2@", "@@C1", "1B@", "A@@2", "@A3@", "@1@A", "2AA@",
    "1B1B", "333B", "1@CC", "3@@C", "333C"]

    # TODO: Add your calls to get_letter, get_digit, and check_pattern
    # Inside a loop so that:
    #     After printing the results, a prompt appears requiring an input
    #          with the text: "Try Again? (y/n): "
    #     AND
    #          IF the user replies with 'y', the loop continues
    #          IF the user replies with anything else, the loop ends
    # ADD YOUR CODE UNDER THIS LINE
    # -------------------------------------------------
  
    #start with y so loop runs
    answer = "y"
    while answer == "y":
        letter = get_letter() #get an approved letter
        digit = get_digit() #get an approved digit
        check_pattern(letter, digit, st_list) #print matching words
        answer = input("Try Again? (y/n): ") #ask if user wnats to try again, if input isn't y, loop ends
        

    # -------------------------------------------------
    # No need to modify anything Below this line
    print("The End")
    

# Do not modify these two lines
if __name__ == "__main__":
    main()