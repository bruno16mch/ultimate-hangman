from random import randint

class Game(object):
    
    
    def __init__(self):
        self.output = []
        self.watch = []    
        self.master = ["packers","packets","packing","earings","earplug","abduction","acres",
    "adult", "advice", "brick", "calm", "cast", "chose", "claws", "coach"]
        
    def print_screen(self, text):
        self.output.append(text)
        
    def first(self):
        self.print_screen(" -----")
        self.print_screen("|")
        self.print_screen("|")
        self.print_screen("|")
        self.print_screen("|")
        self.print_screen("|")
        self.print_screen(" ---------- ")
    
    def second(self):
        self.print_screen(" -----")
        self.print_screen("|     |")
        self.print_screen("|")
        self.print_screen("|")
        self.print_screen("|")
        self.print_screen("|")
        self.print_screen(" ---------- ")
    
    def third(self):
        self.print_screen(" -----")
        self.print_screen("|     |")
        self.print_screen("|     O ")
        self.print_screen("|")
        self.print_screen("|")
        self.print_screen("|")
        self.print_screen(" ---------- ")
    
    def fourth(self):
        self.print_screen(" -----")
        self.print_screen("|     |")
        self.print_screen("|     O ")
        self.print_screen("|    /")
        self.print_screen("|")
        self.print_screen("|")
        self.print_screen(" ---------- ")
    
    def fifth(self):
        self.print_screen(" -----")
        self.print_screen("|     |")
        self.print_screen("|     O ")
        self.print_screen("|    /|")
        self.print_screen("|")
        self.print_screen("|")
        self.print_screen(" ---------- ")
    
    def sixth(self):
        self.print_screen(" -----")
        self.print_screen("|     |")
        self.print_screen("|     O ")
        self.print_screen("|    /|\\")
        self.print_screen("|")
        self.print_screen("|")
        self.print_screen(" ---------- ")
    
    def seventh(self):
        self.print_screen(" -----")
        self.print_screen("|     |")
        self.print_screen("|     O ")
        self.print_screen("|    /|\\")
        self.print_screen("|    /")
        self.print_screen("|")
        self.print_screen(" ---------- ")
    
    def eighth(self):
        self.print_screen(" -----")
        self.print_screen("|     |")
        self.print_screen("|     O ")
        self.print_screen("|    /|\\")
        self.print_screen("|    / \\")
        self.print_screen("|")
        self.print_screen(" ---------- ")
    
    
    def display(self, word):
        for y in word:
            self.watch.append("_")
    
    def play(self,x, user): 
        rand_word = randint(0, len(self.master)-1)
        
        
        run = [self.first, self.second, self.third, self.fourth, self.fifth, self.sixth, self.seventh, self.eighth]
        
        google = []
        user_word = []
        
        word = self.master[rand_word]
        position_list = []
        g = 0
        t = 0
        u = 0
        self.display(word)
        if x < len(run) - 1:
            #user = raw_input("Guess a Letter: ")
            char = word.find(user)
            
            #tray = "".join(watch)
            #right_guessed = tray.find(user)
            for i in self.watch:
                if i == user: #if the guessed letter was already guessed correctly
                    user = "!!@^"
            for u in google:
                if u == user:#if the letter was already guessed
                    user = "#&%^"
        
            if len(user) == 0: #if the user string is empty
                run[x]()
                self.print_screen("Type in one letter at a time")
                self.print_screen("  ".join(self.watch))
                self.print_screen("Letters you have guessed: %s" % google)
            elif user == word:
                run[x]()
                self.print_screen("Nice Job, You Guessed the Word!!")
                self.print_screen("The word was %s" % word)
                return ""
        
            elif user == "!!@^": #if the letter was already correctyl guessed
                run[x]()
                self.print_screen("You already got that one")
                self.print_screen("Try something else")
                self.print_screen("  ".join(self.watch))
                self.print_screen("Letters you have guessed: %s" % google)
        
            elif user == "#&%^": #if the letter was already guessed
                run[x]()
                self.print_screen("You already guessed that")
                self.print_screen("Try a different letter")
                self.print_screen("  ".join(self.watch))
                self.print_screen("Letters you have guessed: %s" % google)
        
            elif user == "quit":
                return ""
        
            elif char >= 0:     # if the guessed letter is right
                t += 1
                #watch.append(user) #adds the correctly guessed letter into a list
                horse = word.find(user)
                self.watch[horse] = user
        
                run[x]()
                self.print_screen("You got one!!")
                self.print_screen("  ".join(self.watch))
        
                if t == len(word): #game ends when the number of correct letters
                    self.print_screen("You Guessed It!!") #is the same as the number of letters in the word)
                    return ""
        
            elif char == -1: #incorrect guess
                self.print_screen("Try a different letter")
                x += 1
                run[x]()
                google.append(user)
                self.print_screen("  ".join(self.watch))
                self.print_screen("Letters you have guessed: %s" % google)
        
        
        
        
            else:
                self.print_screen("WE;FKLQMDS")
        
        
        
        self.print_screen("Game Over")
        self.print_screen("The word was %s" % word)
    
   
    
                     
    
    