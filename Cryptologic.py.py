#CS-230 Project- Apeksha
# A program to guess the random scrambled word from the wordlist

import random
from random import shuffle       #to use the function shuffle in the program

inputfile = open("wordList.txt", "r")         #syntax to open the input file 
file = inputfile.readlines()                  #reads every line of the input file

wordlist = []             #initializing an empty wordlist

for i in range(len(file)):             #loop condition - the range is the whole file 
	s = file[i].strip("\n")     #strip function - removes the new line between the words(since words are given one at a line)
	wordlist.append(s)          #append function - adds words to the wordlist(every word since it's a loop)

randomNumber = random.randint(0, len(wordlist))      #choosing a random number first 
randomWord = wordlist[randomNumber]                  # whatever word is there in the index(random number), is stored in the variable randomWord
 
letterlist = []            #another empty list to store the letters of the selected random word

for c in randomWord:           #for every letter in randomWord
	letterlist.append(c)       #adds letter wise letter to the letterlist
shuffle(letterlist)                #shuffles the letters inside the list 
letterlist=''.join(letterlist)  # joining the letters with ' '
letterlist=letterlist.upper()   #converts every letter into uppercase
 
print("Welcome to CRYPTO-LOGIC!")
print("Try to guess the scrambled word, one letter at a time!")
print("Scrambled word: "+ letterlist)  # the shuffled letters 
print()
print()

condition = True     #Initializing the condition as true 
#Initializing the variables
incorrect=0      
guessedlet = ""
i=0

while condition== True:       #the loop executes until the condition is true, in our case, it terminates when it meets the fals condition which is below
        
   guessedletter =  str(input("Enter your guess..."))           #prompts the user to guess a letter

   if(guessedletter== randomWord[i]):        #if the first letter matches with the letter at index i=0, then...
        i=i+1                               #updates the value of index by 1
        guessedlet += guessedletter         #this is to store the correct letters already guessed
        print("Incorrect guess:",incorrect)
        print("Letters already guessed:",guessedlet.upper())        #prints the incorrect answers and letters already guessed each time.
        print()
              
   else :                #if the user guesses incorrect letter
        incorrect += 1    #updates the incorrect guesses every time by 1       
        print("Incorrect guess:",incorrect)
        print("Letters already guessed:",guessedlet.upper())
        print()
          
   if i==len(randomWord) :        #when the value of i(index) is equal to the length of the random word, the condition is false and hence the program terminates
        condition = False 
        
   
print("Congratulations!You found the word after",incorrect," incorrect guesses!")       #prints the final message

#End of program
