import tkinter as tk
import math
import random
import sys
class Saper:
    def __init__(self):
    
        #init
        self.guziki = []
        self.liczba_kolumn = 15
        self.liczba_rzędów = 15
        self.trudność=0
        self.poziomy=["Łatwy", "Średni", "Trudny", "Bombowy"]
        self.rząd=-1
        self.kolumna=0
        self.X=1024
        self.Y=1024
        self.XY=str(self.X)+"x"+str(self.Y)
        self.bomby=[]
        self.kolory_tła=["light salmon", "light blue", "LightGoldenrodYellow", "light green", "LavenderBlush", "MistyRose", "PaleTurquoise"]
        self.Bg = random.choice(self.kolory_tła)
        self.nazwy=[]
        self.sprawdzono=[]
        self.oflagowano=[]
        self.kolory=["grey", "blue", "green", "red", "dark blue", "purple", "dark green", "dark red", "dark cyan", "black",]
        self.font="Sylfaen"
        self.ilość_bomb=2
        self.mnożniki=[0.07, 0.15, 0.25, 0.4]
        self.root=tk.Tk()
        self.root.title("Saper")
        self.root.geometry(self.XY)
        self.root.configure(bg=self.Bg)
        self.żyje=True
        self.wyjście_guzik=tk.Button(self.root, text="Wyjście", font=(self.font, 17), bg="black", fg=self.Bg, command=sys.exit)
        self.wyjście_guzik.place(x=6, y=5)
        self.ustaw_menu()
        self.root.attributes("-fullscreen", True)
        self.root.mainloop()
    #funkcje
        
    def reset(self):
        self.guziki = []
        self.bomby = []
        self.oflagowano = []
        self.nazwy = []
        self.sprawdzono = []
        self.żyje=True
        
        self.koniec.place_forget()
        self.koniec_guzik.place_forget()
        self.plansza.place_forget()
        self.ustaw_menu()
        
        
        
    def łatwiej(self):
        self.trudność = self.trudność-1
        if self.trudność<0:
            self.trudność=3
        self.poziom.config(text=self.poziomy[self.trudność])
    def trudniej(self):
        self.trudność = self.trudność+1
        if self.trudność>3:
            self.trudność=0
        self.poziom.config(text=self.poziomy[self.trudność])
    def ustaw_menu(self):
  
        self.menu = tk.Frame(self.root, width=self.X, height=self.Y, bg=self.Bg)
        self.menu.place(relx=0.5, rely=0.5, anchor="center")

        self.saper_napis = tk.Label(self.menu, text="Saper", font=(self.font, 85), bg=self.Bg)
        self.saper_napis.place(x=512,y=100, anchor="center")

        self.pytanie1 = tk.Label(self.menu, text="Podaj liczbę rzędów:", font=(self.font, 30), bg=self.Bg)
        self.pytanie1.place(x=100,y=300)
        self.pytanie2 = tk.Label(self.menu, text="Podaj liczbę kolumn:", font=(self.font, 30), bg=self.Bg)
        self.pytanie2.place(x=100,y=350)

        self.entry_y = tk.Entry(self.menu, font=(self.font, 22))
        self.entry_y.place(x=480, y=310)
        self.entry_x = tk.Entry(self.menu, font=(self.font, 22))
        self.entry_x.place(x=480, y=360)

        self.poziom = tk.Label(self.menu, text=self.poziomy[self.trudność], bg=self.Bg, font=(self.font, 40))
        self.poziom.place(x=512, y=500, anchor="center")

        self.guzik_łatwiej=tk.Button(self.menu, text="<", bg="black", fg=self.Bg, font=(self.font, 40), command=self.łatwiej)
        self.guzik_łatwiej.place(x=300, y=450)
        self.guzik_trudniej=tk.Button(self.menu, text=">", bg="black", fg=self.Bg, font=(self.font, 40), command=self.trudniej)
        self.guzik_trudniej.place(x=645, y=450)

        self.guzik_start = tk.Button(self.menu, text="Graj", bg="black", fg=self.Bg, font=(self.font, 70), command=self.Graj)
        self.guzik_start.place(x=512, y=710, anchor="center")
        
        self.błąd = tk.Label(self.menu, text=" ", bg=self.Bg, font=(self.font, 20))
        self.błąd.place(x=300, y=900)
    
    def Graj(self):
        self.liczba_rzędów = int(self.entry_y.get())
        self.liczba_kolumn = int(self.entry_x.get())
        print(self.liczba_rzędów, self.liczba_kolumn)
        if 1 < self.liczba_kolumn < 30:
            if 1 < self.liczba_rzędów < 16:
                self.start()
            else:
                self.błąd.config(text="Podaj poprawną ilość kolumn!!")
        else:
            self.błąd.config(text="Podaj poprawną ilość rzędów!!")
            
            
            
    def start(self):
        print("start")
        self.menu.place_forget()
        
        self.plansza = tk.Frame(self.root)
        self.plansza.place(relx=0.5, rely=0.5, anchor="center")
        self.ilość_bomb=math.ceil(self.liczba_rzędów*self.liczba_kolumn*self.mnożniki[self.trudność])
        #generowanie bomb
        for i in range (self.liczba_rzędów):
            rząd_bomb=[]
            for j in range (self.liczba_kolumn):
                rząd_bomb.append(False)
            self.bomby.append(rząd_bomb)
        
        for i in range (self.ilość_bomb):
            while True:
                p = random.randint(0, self.liczba_rzędów-1)
                q = random.randint(0, self.liczba_kolumn-1)
                if self.bomby[p][q] == False:
                    self.bomby[p][q] = True
                    print("zastawione!")
                    break
            
        
        #miejsca na flagi
        for i in range (self.liczba_rzędów):
            rząd_oflagowano=[]
            for j in range (self.liczba_kolumn):
                rząd_oflagowano.append(False)
            self.oflagowano.append(rząd_oflagowano)
        
        #lista odkrytych
        for i in range (self.liczba_rzędów):
            rząd_sprawdzono=[]
            for j in range (self.liczba_kolumn):
                rząd_sprawdzono.append(False)
            self.sprawdzono.append(rząd_sprawdzono)
            
        #lista nazw
        for i in range(self.liczba_rzędów):
            rząd_nazwa=[]
            for j in range(self.liczba_kolumn):
                B = 0
                #krawędzie
                if 0 <= i-1 < self.liczba_rzędów and self.bomby[i-1][j]==True:
                    B = B+1
                if 0 <= i+1 < self.liczba_rzędów and self.bomby[i+1][j]==True:
                    B = B+1
                if 0 <= j+1 < self.liczba_kolumn and self.bomby[i][j+1]==True:
                    B = B+1
                if 0 <= j-1 < self.liczba_kolumn and self.bomby[i][j-1]==True:
                    B = B+1
                #rogi
                if 0 <= i-1 < self.liczba_rzędów and 0 <= j-1 < self.liczba_kolumn and self.bomby[i-1][j-1]==True:
                    B = B+1
                if 0 <= i+1 < self.liczba_rzędów and 0 <= j-1 < self.liczba_kolumn and self.bomby[i+1][j-1]==True:
                    B = B+1
                if 0 <= i+1 < self.liczba_rzędów and 0 <= j+1 < self.liczba_kolumn and self.bomby[i+1][j+1]==True:
                    B = B+1
                if 0 <= i-1 < self.liczba_rzędów and 0 <= j+1 < self.liczba_kolumn and self.bomby[i-1][j+1]==True:
                    B = B+1
                rząd_nazwa.append(B)
            self.nazwy.append(rząd_nazwa)
        print(self.nazwy)
                    
        for i in range(self.liczba_rzędów):
            for j in range(self.liczba_kolumn):
                if self.bomby[i][j]==True:
                    self.nazwy[i][j]="9"
      
        
        
        
        
        #generowanie pola   
        for h in range (self.liczba_rzędów):
            for g in range(self.liczba_kolumn):
                pole = tk.Label(self.plansza, text="     ", font=(self.font, 35),)
                pole.grid(row = h, column = g, sticky="nsew")
                
        #generowanie nazw
        for h in range (self.liczba_rzędów):
            for g in range(self.liczba_kolumn):
                numerek=int(self.nazwy[h][g])
                widok = tk.Label(self.plansza, text=str(numerek), fg=self.kolory[numerek], font=(self.font, 30),)
                widok.grid(row = h, column = g, sticky="nsew")
                
        for i in range(self.liczba_rzędów):
            for j in range(self.liczba_kolumn):
                if self.bomby[i][j] == True:
                    obraz_bomby = tk.Label(self.plansza, text="💣", font=(self.font, 30))
                    obraz_bomby.grid(row = i, column = j, sticky="nsew")
                    
        for i in range(self.liczba_rzędów):
            for j in range(self.liczba_kolumn):
                if self.nazwy[i][j] == 0:
                    puste_pole = tk.Label(self.plansza, text=" ", font=(self.font, 30))
                    puste_pole.grid(row = i, column = j, sticky="nsew")
                    
        for h in range (self.liczba_rzędów):
            rząd_guzików=[]
            for g in range(self.liczba_kolumn):
                guzik = tk.Button(self.plansza, text="", command=lambda h=h, g=g: self.klik(h,g))
                guzik.bind("<Button-3>", lambda e, h=h, g=g: self.flaga(h,g))
                guzik.grid(row = h, column = g, sticky="nsew")
                rząd_guzików.append(guzik)
            self.guziki.append(rząd_guzików)
        
        self.wyjście_guzik.lift()

            
    #funkcje rozgrywki  
    def wygrana(self):
        sprawdzenie=0
        if self.bomby==self.oflagowano:
            for i in range (self.liczba_rzędów):
                for j in range (self.liczba_kolumn):
                    if self.oflagowano[i][j] != self.sprawdzono[i][j]:
                        sprawdzenie = sprawdzenie+1
            if sprawdzenie == self.liczba_kolumn*self.liczba_rzędów:
                print("wygrałeś!")
                self.koniec = tk.Label(self.root, text="Wygrałeś!", font=(self.font, 40), bg=self.Bg)
                self.koniec.place(x=160, y=750)
                self.koniec.lift()
                self.koniec_guzik = tk.Button(self.root, text="Zagraj ponownie", font=(self.font, 40), bg="black", fg=self.Bg, command=self.reset)
                self.koniec_guzik.place(x=90, y=850)
                
    def przegrana(self):
        print("bum bum")
        self.koniec = tk.Label(self.root, text="Przegrałeś!", font=(self.font, 40), bg=self.Bg)
        self.koniec.place(x=160, y=750)
        self.koniec.lift()
        self.koniec_guzik = tk.Button(self.root, text="Zagraj ponownie", font=(self.font, 40), bg="black", fg=self.Bg, command=self.reset)
        self.koniec_guzik.place(x=90, y=850)
        
    def flaga(self, a, b):
        if self.oflagowano[a][b] == False:
            print("Flaga!", a,b)
            self.guziki[a][b].config(text="🚩", font=(self.font, 22))
            self.oflagowano[a][b] = True
        elif self.oflagowano[a][b] == True:
            print("zdejmujemy", a,b)
            self.guziki[a][b].config(text=" ")
            self.oflagowano[a][b] = False
        self.wygrana()
        
    def klik(self,a,b):
        if self.bomby[a][b] == True and self.oflagowano[a][b] == False and self.żyje==True:
            self.guziki[a][b].grid_remove()
            self.żyje=False
            self.przegrana()
        elif self.bomby[a][b] == False and self.oflagowano[a][b] == False and self.żyje==True:
            self.sprawdz(a,b)
            self.wygrana()
            print("żyjemy")
               
    def sprawdz(self,a,b):
        if self.bomby[a][b] == False and self.sprawdzono[a][b]==False and self.oflagowano[a][b]==False:
            self.guziki[a][b].grid_remove()
            self.sprawdzono[a][b]=True
            if self.nazwy[a][b]==0:
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if not (dx==0 and dy==0):
                            if 0 <= a+dx <= self.liczba_rzędów-1 and 0 <= b+dy <= self.liczba_kolumn-1:
                                self.sprawdz(a+dx, b+dy)
                 
gra = Saper()



