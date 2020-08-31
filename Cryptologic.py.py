#Cryptologic- Apeksha
 

import random
from random import shuffle       

inputfile = open("wordList.txt", "r")         
file = inputfile.readlines()                  

wordlist = []             

for i in range(len(file)):               
	s = file[i].strip("\n")      
	wordlist.append(s)           

randomNumber = random.randint(0, len(wordlist))       
randomWord = wordlist[randomNumber]                  
 
letterlist = []             

for c in randomWord:            
	letterlist.append(c)        
shuffle(letterlist)                  
letterlist=''.join(letterlist)   
letterlist=letterlist.upper()    
 
print("Welcome to CRYPTO-LOGIC!")
print("Try to guess the scrambled word, one letter at a time!")
print("Scrambled word: "+ letterlist)   
print()
print()

condition = True      
incorrect=0      
guessedlet = ""
i=0

while condition== True:        
        
   guessedletter =  str(input("Enter your guess..."))            
   if(guessedletter== randomWord[i]):        
        i=i+1                                
        guessedlet += guessedletter          
        print("Incorrect guess:",incorrect)
        print("Letters already guessed:",guessedlet.upper())        
        print()
              
   else :                 
        incorrect += 1          
        print("Incorrect guess:",incorrect)
        print("Letters already guessed:",guessedlet.upper())
        print()
          
   if i==len(randomWord) :         
        condition = False 
        
   
print("Congratulations!You found the word after",incorrect," incorrect guesses!")        

#End of program
