
from random import randint
from termcolor import colored
from typing import List
import os
import colorama

colorama.init()
absolutepath = os.path.abspath(__file__)
absolutepath = absolutepath[:-10] + "\\words\\wordle_list.txt"
print(absolutepath)

class Wordle:
  wordleWord: str = ""
  guessedWord: str = ""
  guessArray:List[str] = ['_','_','_','_','_']
  

  '''Initialization code for game'''
  def __init__(self) -> None:
    winner:bool = False
    initList:List[str] = []
    file = open(absolutepath, 'r')
    for items in file:
      if len(items) == 6:
        initList.append(items[:-1])
    file.close()

    seed: int = randint(0, len(initList)-1)
    self.wordleWord: str = initList[seed]
    

  '''colors letter based on color parameter passed'''
  def colorLetter(self, ltr:str="A", color:str="correct") -> str:
    testString:str = ""
    if color == "correct":
      testString = colored(ltr.upper(), 'white', 'on_green')
    elif color == "close":
      testString = colored(ltr.upper(), 'white', 'on_yellow')
    return testString

  '''If word matches index then change to green'''
  def correctWord(self) -> None:
    #guess -> goals --> _ u e s _
    guessArr:List[str] = [ltr for ltr in self.guessArray]
    wordleArr:List[str] = [ltr for ltr in self.wordleWord]
    #loop through each letter in word and compare to wordle
    for i in range(len(self.guessArray)):
      if guessArr[i] == wordleArr[i]:
        guessArr[i] = ""
        wordleArr[i] = "_"
        self.guessArray[i] = self.colorLetter(self.guessArray[i], "correct")
    
    for i in range(len(self.guessArray)):
      for j in range(len(self.guessArray)):
          if wordleArr[j] == guessArr[i]:
            wordleArr[j] = "_"
            self.guessArray[i] = self.colorLetter(self.guessArray[i], "close")
            break
        


  '''Prints guess out on screen'''
  def printGuess(self) -> None:
    print(' '.join(self.guessArray))

  '''Checks if word entered is in list'''
  def isValidWord(self, word) -> bool:
    if not len(word) == 5:
      return False
    try:
      file = open(absolutepath, 'r')
      for items in file:
        if items[:-1] == word:
          return True
      return False  
    finally:
      file.close()
    

  def submitWord(self, word) -> None:
    for i in range(len(word)):
      self.guessArray[i] = word[i]

  def isWinner(self) -> bool:
    return self.guessedWord == self.wordleWord

  '''Code that runs game using other definitions'''
  def play(self) -> bool:
    for i in range(6):

      self.guessedWord = input("enter word:\n")
      while not self.isValidWord(self.guessedWord):
        print("enter a valid word!\n")
        self.guessedWord = input("enter word:\n")
      
      self.submitWord(self.guessedWord)

      #enter code to decorate word if matches
      self.correctWord()
      self.printGuess()
      if self.isWinner():
        print("You win!!!")
        return True
    
    print("You Lose! Try again.")
    return False

  

#initialize game instance
game = Wordle()
#print(game.wordleWord)
game.play()

