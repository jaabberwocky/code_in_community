class WordList:
    words = set()
    used = set()
    last_word = None

    def __init__(self, path='word_list.txt'):
        '''
        Params:
            path - path to word list

        Returns:
            None
        '''
        with open(path) as f:
            line = f.readline()
            while line:
                self.words.add(line.strip().lower())
                line = f.readline()
        f.close()
    
    def checkWord(self, word):
        '''
            Checks word to see if valid.

            Params:
                word - word to be checked

            Returns:
                Boolean - true if valid
        '''
        word = word.strip()
        if self.last_word is not None:
            # rule #1: check whether first character is the same as the last character of previous word
            if self.last_word[-1] != word[0]:
                print("You didn't type a word starting with '{}'".format(self.last_word[-1]))
                return False
        # rule #2: check if word has been used before
        if word in self.used:
            print("You typed a word that has been typed before.")
            return False
        else:
            # rule #3: check if word is in the word list
            if word not in self.words:
                print("You didn't type a word found in word_list.txt")
                return False
            else:
                self.used.add(word)
                self.last_word = word
                return True
    
    def startGame(self):
        '''
            Loop to begin game and accepts user input.

            Params:
                None

            Returns:
                None
        '''
        while True:
            w = input("Please type a word:\t").lower()
            if self.checkWord(w):
                continue
            else:
                break
        return None

if __name__ == "__main__":
    wl = WordList()
    wl.startGame()
    