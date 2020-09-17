 # CRYPTOLOGIC
##
## Project Summary
In this game, the letters of a randomly-selected dictionary word are scrambled, and the player is challenged to guess the original word, letter by letter, while making as few incorrect guesses as possible.

## Language used 
**PYTHON**
##

## Downloading and installing Python  
 
**Step 1 :  Download Python** -
To start, go to python.org/downloads and then click on the button to download the latest version of Python.
##
**Step 2: Run the .exe file** -
Next, run the .exe file that you just downloaded:
##
**Step 3 :  Install Python** -
You can now start the installation of Python by clicking on Install Now.
Follow the instructions and the setup will be completed.

 
## Running a code in Python 
 
You can run a code in Python via the Python IDLE.
A quick way to find your Python IDLE on Windows is by clicking on the Start menu. You should then see the IDLE under “Recently added”.
After the Python shell screen opens, you can go to File, click on New File, and paste/write your code there.
Then, you have to save your code and then you can compile and run from the menu or simply press F5.

 
## Game Logic  
1. The list of words is read from the attached **"wordlist.txt"** file, one at a time, adding each word to a list. There is a total of 300 random dictionary words in this file: 
100 are six letters long, 100 are seven letters long, and the last 100 are eight or more letters long. Each word is on a separate line of the file. 

2. A secret word is chosen at random from the word list, splatted it into a list of individual letters, and then created a scrambled copy of this list, with the letters randomly shuffled.
Python's **"shuffle()"** function is used for this; we can import this function from the **"random"** module. Also, Python’s **“randint()”** function is imported from the
“random” module  to make the task of selecting the random target word in the list much easier than using the generic “rand()” function. 

3. A welcome message is printed with a brief explanation of the game for the player.

4. Then, the scrambled word is printed, along with the number of incorrect guess(es) and any correct letter(s) the player has guessed so far.  

5. The player is prompted to guess a letter, and the player's input is compared with the next letter of the secret word. If the player's guess is different, the program 
increases the "incorrect guesses" counter by one; if it is the same, it appends the letter to the list of correctly guessed letters.

6. The step 4 and 5 is repeated until the number of correctly guessed letters is equal to the length of the secret word. At that point, the game is over, and the program displays the completed word, along with a message indicating the number of incorrect guess(es) the player made.


## An example of what the output of a complete game looks like:
   (The player's input is shown in bold)
