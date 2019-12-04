import tkinter as tk
from tkinter import ttk
import random
import os.path
from PIL import ImageTk, Image

LARGE_FONT= ("Verdana", 12,'bold')
image_paths = ['img0.gif', 'img1.gif', 'img2.gif', 'img3.gif', 'img4.gif', 'img5.gif', 'img6.gif', 'img7.gif', 'img8.gif', 'img9.gif', 'img10.gif']

#def donothing(var=''):
 #   pass
class Hangman(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        #self.title("Hangman")
        self.frames = {}
        for F in (HomePage, PlayPage, RecordPage):
            frame = F(container, self)
            self.minsize(100,100)
            self.geometry("900x480")
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="news")
        self.show_frame(HomePage)

    def show_frame(self, page):
        if page == PlayPage:
            self.title("Hangman")
        elif page == RecordPage:
            self.title("Player record")
        else:
            self.title("Hangman Game. Play and have Fun!!!")
        frame = self.frames[page]
        frame.tkraise()
    def quit(self):
        self.destroy()
        
class HomePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        img = Image.open('img/hang.png')
        img= ImageTk.PhotoImage(img)
        self.panel = tk.Label(self, image = img)
        self.panel.image =img
        self.panel.pack(pady = 10)
        
        button = tk.Button(self, text="Play", bg ="skyBlue",fg="Black",width=12,height= 1,font=('Helvetica','20'),command=lambda: controller.show_frame(PlayPage))
        button.configure(relief = 'flat')
        button.pack(pady = 10)
        
        button2 = tk.Button(self, text="Record", bg ="skyBlue",fg="Black",width=12,height=1,font=('Helvetica','20'),command=lambda: controller.show_frame(RecordPage))
        button2.configure(relief = 'flat')
        button2.pack(pady = 10)

class PlayPage(tk.Frame):

    
    def __init__(self, parent, controller):
        self.score = 0
        # Life remain
        self.chances = 10
        self.lst_words = []
        self.lst_wordsGuessed = []
        self.arrAvailabelMask = []
        self.words = self.getWord()

        tk.Frame.__init__(self, parent)
        self.config(bg="white")
        firstImg = Image.open('img/'+ image_paths[10])
        firstImg = firstImg.resize((200, 200), Image.ANTIALIAS)
        firstImg= ImageTk.PhotoImage(firstImg)
        self.panel = tk.Label(self, image = firstImg)
        self.panel.image = firstImg
        self.panel.place(x=20, y=20)

        self.lbResult = tk.Label(self, text="", bg ="white",fg = "red", font=("Verdana", 16,'bold'))
        self.lbResult.place(x= 400, y= 190)

        self.lbLife = tk.Label(self, text="LIFE REMAINING : 10", bg ="white",fg = "red", font=("Tahoma", 12,'bold'))
        self.lbLife.place(x=20, y=230)
        
        lbScore = tk.Label(self, text="SCORE:", bg ="white",fg = "red", font=("Verdana", 16,'bold','underline'))
        lbScore.place(x=20, y=278)
        self.lbPoins = tk.Label(self, text="0", bg ="white",fg = "red", font=("Verdana", 25,'bold'))
        self.lbPoins.place(x=40, y=306)
        
        # For test
        # self.words = "AABCDA"
        # print(self.getAvailabelLetters('A'))
        self.drawGuessWord()
        self.drawKeyboard()

        # Draw button
        button1 = tk.Button(self, text="BACK", font=('Tahoma','13'), command=lambda: controller.show_frame(HomePage))
        button1.place(x=40, y=435)

        self.button2 = tk.Button(self, text="PLAY AGAIN", font=('Tahoma','13'), command=lambda: self.showBtnPlayAgain())

        button3 = tk.Button(self, text="QUIT", font=('Tahoma','13'), command=lambda: controller.quit())
        button3.place(x=800, y=435)
    
    # Draw guess cell
    def drawGuessWord(self):
        self.btn_guess = [0 for x in range(len(self.words))]
        wordposition = int((int(self.winfo_screenwidth()/2 - self.winfo_reqwidth()/2)- (len(self.words)* 58))/2) + 254/2
        for col in range(len(self.words)):
            self.btn_guess[col] = tk.Button(self, text="_",bg="lightgrey", fg="Black",width=3,height=1,font=('Helvetica','20'))
            self.btn_guess[col].place(x= wordposition + (58 * col), y=90)
    def clearGuessWord(self):
        for col in range(len(self.words)):
            if self.btn_guess[col].winfo_ismapped():
                self.btn_guess[col].place_forget()
    # Draw keyboard 3x9
    def drawKeyboard(self):
        self.btn = [0 for x in range(27)] 
        for idx in range(27):
            if idx == 26:
                self.btn[idx] = tk.Button(self,bg = "skyBlue",width=3,height=1,font=('Helvetica','20'))
            else:
                self.btn[idx] = tk.Button(self,text = chr(idx + 65),bg = "skyBlue",fg ="Black",width=3,height=1,font=('Helvetica','20'),command= lambda idx1=idx: self.Play(idx1))
            if idx <= 8:
                self.btn[idx].place(x = 190 + (58 *(idx + 1)),y = 250)
            elif idx >= 9 and idx <= 17:
                    self.btn[idx].place(x = 190 + (58 *(idx  - 8)),y = 306)
            elif idx >= 18:
                self.btn[idx].place(x = 190 + (58 *(idx  - 17)),y = 362)

    def disableKeyboard(self):
        for x in range(27):
            self.btn[x]["state"] = "disabled"

    def enableKeyboard(self):
        for x in range(27):
            self.btn[x]["state"] = "normal"

    def showBtnPlayAgain(self):
        if self.button2.winfo_ismapped():
            self.button2.place_forget()
            self.PlayAgain()
        else:
            self.button2.place(x=380, y=435)
    def PlayAgain(self):
        self.enableKeyboard()
        print("Play again!!!")
        self.chances = 10
        self.score = 0
        self.lbPoins["text"] = str(self.score)
        #txt = "LIFE REMAINING: " + str(self.chances)
        self.lbLife.configure(text = ("LIFE REMAINING: " + str(self.chances)))
        self.clearGuessWord()
        self.words = self.getWord()
        self.drawGuessWord()
        for col in range(len(self.words)):
            self.btn_guess[col]["text"] = "_"

    def PlayNextLevel(self):
        self.enableKeyboard()
        print("Play next!!!")
        self.chances = 10
        #txt = "LIFE REMAINING: " + str(self.chances)
        self.lbLife.configure(text = ("LIFE REMAINING: " + str(self.chances)))
        self.clearGuessWord()
        self.words = self.getWord()
        self.drawGuessWord()
        for col in range(len(self.words)):
            self.btn_guess[col]["text"] = "_"
    # Play
    def Play(self, idxButton):
        numCorrectChar = 0
        self.lbResult.configure(text ="")
        character = self.getLetter(idxButton)
        # print("letter guess :" + character)
        self.getAvailabelLetters(character)
        #print(self.arrAvailabelMask)
        if character in self.words: #Its checks whether the albpbet is there in the answer
            for i in range(len(self.words)):
                if character == self.words[i]:
                    self.btn_guess[i]["text"] = character
            for i in range(len(self.arrAvailabelMask)):
                if self.arrAvailabelMask[i] == '*':
                    numCorrectChar = numCorrectChar + 1
            if numCorrectChar == len(self.arrAvailabelMask):
                self.score = self.score + 1
                self.lbPoins["text"] = str(self.score)
                #Win
                self.result(False)
                self.PlayNextLevel()
        else:
            self.chances = self.chances - 1
            #print(self.chances)
            if self.chances == 0:
                # 1 Disable keyboard
                # 2 Show button replay
                # 3 Play again
                # GameOver
                self.result(True)
                for i in range(len(self.arrAvailabelMask)):
                    if self.arrAvailabelMask[i] != '*':
                        self.btn_guess[i].configure(text = self.arrAvailabelMask[i], fg = "red")
                self.disableKeyboard()
                self.showBtnPlayAgain()

                #txt = "LIFE REMAINING: " + str(self.chances)
                self.lbLife.configure(text = ("LIFE REMAINING: " + str(self.chances)))
                self.drawHangman(self.chances)
                # Save txt
                # inputDialog = ShowDialog(self)
                # self.wait_window(inputDialog.top)
                self.showMessage()
            #txt = "LIFE REMAINING: " + str(self.chances)
            self.lbLife.configure(text = ("LIFE REMAINING: " + str(self.chances)))
            self.drawHangman(self.chances)

    def showMessage(self):
        self.top = tk.Toplevel(self)
        self.top.geometry('250x100')
        # top.overrideredirect(True)
        myLabel = tk.Label(self.top, text='Enter your username below')
        myLabel.pack()
        self.myEntryBox = tk.Entry(self.top)
        self.myEntryBox.pack(pady = 10)
        self.mySubmitButton = tk.Button(self.top, text='Submit', command= lambda: self.Savetxt(self.myEntryBox.get()))
        self.mySubmitButton.pack()
    def Savetxt(self, name):
        print(name, self.score)
        fp = open('txt/record.txt', "a")
        fp.write(name + '-'+ str(self.score)+'\r')
        fp.close()
        self.top.destroy()
    # Check whether word have been guessed
    def isWordGuessed(self, word):
        try:
            self.lst_wordsGuessed.index(word)
            return True
        except ValueError as e:
            return False
    
    # Get random word from .txt
    def getWord(self):
        with open('txt/words.txt') as fp:
           line = fp.readline()
           while line:
               self.lst_words.append(line.strip())
               line = fp.readline()
        fp.close()
        #Remove word have been guessed
        rWord = random.choice(self.lst_words)
        if self.isWordGuessed(rWord):
            self.lst_words.remove(rWord)
            rWord = random.choice(self.lst_words)
        #self.lst_words.remove(rWord)
        self.lst_wordsGuessed.append(rWord)
        self.arrAvailabelMask = list(rWord)
        print("Word Guess: " + rWord)
        return rWord
        
    # Get ra tu doan
    def getLetter(self, idxButton):
        self.btn[idxButton]["state"] = "disabled"
        return chr(idxButton + 65)

    
    # Khi thua get ra cac tu con lai
    #print(self.getAvailabelLetters('A'))
    def getAvailabelLetters(self, guessLetter):
        arrWord = list(self.words)
        indexPosList = []
        indexPos = 0
        while True:
            try:
                # Search for item in list from indexPos to the end of list
                indexPos = arrWord.index(guessLetter, indexPos)
                # Add the index position in list
                indexPosList.append(indexPos)
                indexPos += 1
            except ValueError as e:
                break
        # '*' '*' 'B' 'C' 'D' '*'
        for x in indexPosList:
            self.arrAvailabelMask[x] = '*'
    
    # Display hangman picture
    def drawHangman(self, chances):
        image = Image.open('img/'+ image_paths[chances])
        image = image.resize((200, 200), Image.ANTIALIAS)
        imgnew = ImageTk.PhotoImage(image)
        self.panel.configure(image=imgnew)
        self.panel.image = imgnew

    # Display message win or lose
    def result(self, gameOver):
        if gameOver == True:
            #print("Game Over!")
            self.lbResult.configure(text ="GAME OVER!!!")
        else:
            #print("Win")
            self.lbResult.configure(text ="GOOD JOB!!!")
class RecordPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        topframe = tk.Frame(self)
        topframe.pack(side = "top",padx = 10, pady = 10, fill = tk.X)

        searchframe = tk.Frame(self)
        searchframe.pack(side = "top",padx = 10, fill = tk.X)
        
        self.tree = ttk.Treeview(topframe, selectmode='browse')
        self.tree.pack(side="left",fill = "both" ,expand=True)
        self.vsb = ttk.Scrollbar(topframe, orient="vertical", command=self.tree.yview)
        self.vsb.pack(side='right', fill='y')
        self.initTreeview()
        self.lst_record = []
        self.lst_record = self.loadScore()
        for x in self.lst_record:
            self.tree.insert("", 'end', text="L1", values=(x["name"], x["score"]))

        tk.Label(searchframe, text="Enter name",font=('Tahoma','12')).pack(side = "left", padx = 10)
        self.key = tk.StringVar()
        self.entryKey = tk.Entry(searchframe, width= 55 ,font=('Tahoma','12'), textvariable = self.key).pack(side = "left",padx = 10)
        btnSearch = tk.Button(searchframe, text="Search", width = 15, font=('Tahoma','10'), command=lambda: self.searchByName(self.key.get()))
        btnSearch.pack(side = "left",padx = 3)
        btnRefresh = tk.Button(searchframe, text="Refresh", width = 15, font=('Tahoma','10'), command=lambda: self.searchRefresh())
        btnRefresh.pack(side = "left",padx = 3)
        button1 = tk.Button(self, text="BACK", font=('Tahoma','13'), command=lambda: controller.show_frame(HomePage))
        button1.place(x=40, y=420)
        button2 = tk.Button(self, text="QUIT", font=('Tahoma', '13'), command=lambda: controller.quit())
        button2.place(x=800, y=420)
        self.lbResult = tk.Label(self, text="", bg="white", fg="red", font=("Verdana", 16, 'bold'))
        self.lbResult.place(x=400, y=190)


    def loadScore(self):
        lst_data = []
        if os.path.isfile('txt/record.txt'):
            try:
                with open('txt/record.txt') as fp:
                    line = fp.readline()
                    while line:
                        name = line.strip().split("-")[0]
                        score = line.strip().split("-")[1]
                        recordDict ={
                            "name" : name,
                            "score" : score
                        }
                        lst_data.append(recordDict)
                        line = fp.readline()
                fp.close()
                rsList = sorted(lst_data, key=lambda k: k['name'])
            except ValueError as e:
                print(e)
                fp.close()
                return None
        return rsList

    def initTreeview(self):
        self.tree.configure(yscrollcommand=self.vsb.set)
        self.tree["columns"] = ("1", "2")
        self.tree['show'] = 'headings'
        self.tree.column("1", width=500, anchor='c')
        self.tree.column("2", width=320, anchor='c')
        self.tree.heading("1", text="Name")
        self.tree.heading("2", text="Score")
    def clearTreeview(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
    def searchByName(self, name):
        self.clearTreeview()
        self.lbResult.configure(text=" ")
        check = True
        for x in self.lst_record:
            if x["name"] == name:
                self.tree.insert("",'end',text="L1",values=(x["name"], x["score"]))
                check = False
        if check:
            self.lbResult.configure(text="Invalid name!!!")


    def searchRefresh(self):
        global key
        self.lbResult.configure(text=" ")
        self.key.set("")
        self.clearTreeview()
        for x in self.lst_record:
            self.tree.insert("",'end',text="L1",values=(x["name"], x["score"]))
app = Hangman()
app.mainloop()
