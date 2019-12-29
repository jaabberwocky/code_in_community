class WordList:
    words = set()
    used = set()

    def __init__(self, path):
        f = open(path, "r")
        for line in f:
            self.words.add(line.strip()) 
    
    def checkWord(self, word):
        if word in used:
            print("You typed a word that has been typed before.")
            return False
        else:
            return word.strip() in self.words
    