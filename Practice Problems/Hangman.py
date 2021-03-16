import random as rand

print("Welcome to Hangman Game!")
print("Rules of the game:")
print("--------------------------------------------------------------------------------------------")
print("- A word is chosen by the computer and the player has to guess the word in limited attempts")
print("- As a hint, only vowels will be displayed for the word entered by player 1")

# Selecting a random word for computer from a txt file
file = open('../Test Data/sowpods.txt', 'r')
with open('../Test Data/sowpods.txt') as f:
    lines = f.read().splitlines()
chosenWordByComputer = rand.choice(lines)
print(chosenWordByComputer)  # Remove before code check-in


def HangManGame():
    noOfConsonantCharacters = 0
    noOfVowelCharacters = 0
    # Filtering out vowels and consonants present in computer selected word
    vowel_InChosenWord = list(filter(lambda vowel: vowel == 'A' or vowel == 'a' or
                                     vowel == 'E' or vowel == 'e' or vowel == 'I' or vowel == 'i'
                                     or vowel == 'O' or vowel == 'o' or vowel == 'U' or vowel == 'u', chosenWordByComputer))
    consonants_InChosenWord = list(filter(lambda consonant: consonant != 'A' and consonant != 'a' and
                                          consonant != 'E' and consonant != 'e' and consonant != 'I' and consonant != 'i'
                                          and consonant != 'O' and consonant != 'o' and consonant != 'U' and consonant != 'u', chosenWordByComputer))
    # Counting the number of vowels and consonants in the respective lists
    for index in consonants_InChosenWord:
        noOfConsonantCharacters = noOfConsonantCharacters + 1

    for index in vowel_InChosenWord:
        noOfVowelCharacters = noOfVowelCharacters + 1

    print(vowel_InChosenWord)  # Remove before code check-in
    print(consonants_InChosenWord)  # Remove before code check-in
    noOfRemainingAttempts = len(chosenWordByComputer)
    correctGuessesCounter = 0
    displayedString = " "
    inputLettersByUser = []
    indexesOfAvailableLetter = []
    correctLetterGuesses = []

    # Formatting string such that only vowels are displayed and instead of consonants, '_' will be displayed
    for letter in chosenWordByComputer:
        if letter in 'AEIOUaeiou':
            displayedString = displayedString + letter + " "
        else:
            displayedString = displayedString + "_ "

    while noOfRemainingAttempts != 0:
        print("Computer Chosen Word: "+displayedString)
        print("No of Remaining Attempts: {}\n".format(noOfRemainingAttempts))
        user_choice1 = input("Guess the consonant in the chosen word\n")
        inputLettersByUser.append(user_choice1)

        # Checking for duplicate user entry and storing it in a separate list
        alInputLettersByUser = ''.join(inputLettersByUser)
        duplicates = []
        for char in alInputLettersByUser:
            if alInputLettersByUser.count(char) > 1:
                if char not in duplicates:
                    duplicates.append(char)
        if user_choice1 in duplicates:
            print("This letter was previously entered by user. Please enter some other letter")

        else:
            # Checking whether the user's guessed word is present in the consonant list
            for test_letter in consonants_InChosenWord:
                if test_letter == user_choice1:
                    correctLetterGuesses.append(user_choice1)

            if user_choice1 in correctLetterGuesses:
                print("You guessed correctly!")
                for index in indexesOfAvailableLetter:
                    # Changing displayed string value after a correct guess
                    indexInDisplayedString = index * 2
                    displayedStringInList = list(displayedString)
                    displayedStringInList[indexInDisplayedString] = user_choice1
                    displayedString = "".join(displayedStringInList)

            else:
                print("Your guess was wrong :/")
                noOfRemainingAttempts = noOfRemainingAttempts - 1

        # Exiting the game if user has no remaining attempts
        if noOfRemainingAttempts == 0:
            print("Sorry you are out of attempts. GAME OVER!\nThe computer chosen word was :"+chosenWordByComputer)
            exit(0)

        # Exiting the game if user has guessed all consonant characters correctly
        if correctGuessesCounter == noOfConsonantCharacters:
            print("You have guessed all words correctly! Congratulations!\nThe word selected by computer was: "+chosenWordByComputer)
            exit(0)


HangManGame()
