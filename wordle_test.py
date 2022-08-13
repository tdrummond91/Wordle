# The code to test
from wordle import *
import unittest   # The test framework



game = Wordle()

def testValidWord() -> None:
        assert game.isValidWord("cater") == True
        
def testNotValidWord() -> None:
        assert game.isValidWord("cat") == False


