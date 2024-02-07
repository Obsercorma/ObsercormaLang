from assemblykey import AssemblyKey
from random import randint
from sympy import solve, Eq, symbols
class LetterKey:
    def __init__(self, letter:str, previousKey=None):
        self._letter = letter
        self.useNotPattern = False
        # code letter is the position of the letter in the latin alphabet
        self._codeLetter = ord(letter) - 96

        self.randomPatterns = [
            AssemblyKey.ADD_PATTERN,
            AssemblyKey.SUB_PATTERN,
            AssemblyKey.MUL_PATTERN,
            AssemblyKey.DIV_PATTERN
        ]
        self.selectedPattern = self.randomPatterns[randint(0, 3)]
        if not previousKey is None:
            if previousKey._codeLetter == self._codeLetter:
                print(f"Previous key: {previousKey._letter} - Current key: {self._letter} - CodeLetter: {self._codeLetter}")
                self.selectedPattern = self.randomPatterns[randint(0, 3)]
                while self.selectedPattern == previousKey.selectedPattern:
                    self.selectedPattern = self.randomPatterns[randint(0, 3)]
    
    def getPattern(self):
        return self.selectedPattern

    def calcFromPattern(self):
        """
        get the integer value from the selected pattern
        this integer value will haven't higher value than 26 (value>0 and value<27)
        """
        tmpCode = 0
        match self.selectedPattern:
            case AssemblyKey.ADD_PATTERN:
                a = randint(0, self._codeLetter)
                b = self._codeLetter - a
                return a, b
            case AssemblyKey.SUB_PATTERN:
                a = randint(0, self._codeLetter)
                b = self._codeLetter + a
                return a, b
            case AssemblyKey.MUL_PATTERN:
                for a in range(2, self._codeLetter):
                    if self._codeLetter % a == 0:
                        tmpCode = a
                        break
                if tmpCode == 0:
                    self.useNotPattern = True
                    tmpCode = 26 - self._codeLetter
                    firstKey = 0
                    for b in range(2, tmpCode+1):
                        if tmpCode % b == 0:
                            firstKey = b
                            break
                    assert firstKey != 0, "First key is 0"
                    secondKey = tmpCode // firstKey
                    assert secondKey != 0, "Second key is 0"
                    return firstKey, secondKey
                else:
                    firstKey = 0
                    for b in range(2, tmpCode+1):
                        if tmpCode % b == 0:
                            firstKey = b
                            break
                    assert firstKey != 0, "First key is 0"
                    secondKey = self._codeLetter // firstKey
                    assert secondKey != 0, "Second key is 0"
                    return firstKey, secondKey
            case AssemblyKey.DIV_PATTERN:
                m = randint(2, 9)
                firstKey = self._codeLetter * m
                secondKey = m
                return firstKey, secondKey
                    
        return 0, 0
            # case AssemblyKey.MUL_PATTERN:
            #     return (self._codeLetter // 4, self._codeLetter // 2)
            # case AssemblyKey.DIV_PATTERN:

    def __str__(self):
        return f"'{self._letter}' Pattern: {AssemblyKey.getInfoPattern(self.selectedPattern)} -> {self._codeLetter} - UseNotPattern: {self.useNotPattern}"


class Translater:
    def __init__(self, text:str):
        self.text = text.lower().replace(" ", "")
    
    def translate(self)->list[LetterKey]:
        translatedInObject = []
        for l in range(0, len(self.text)):
            translatedInObject.append(LetterKey(self.text[l], translatedInObject[l-1] if l > 0 else None))
        return translatedInObject

if __name__ == "__main__":
    translater = Translater("hello wworld")
    for letter in translater.translate():
        print(letter.calcFromPattern())
        print(letter)