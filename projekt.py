from tkinter import *
from random import *

class Ucenje_racunanja():
    x=0
    y=0
    
    def __init__(self,master):
        self.a=DoubleVar(master,value=randint(1,50))
        polje_a=Label(master,textvariable=self.a)
        polje_a.grid(row=1,column=0)
        Label(master,text="operacija").grid(row=1,column=1)
        # Glavni menu
        menu = Menu(master)
        master.config(menu=menu) # Dodamo menu

        # Naredimo podmenu "Datoteka"
        datoteka_menu = Menu(menu)
        menu.add_cascade(label="Datoteka", menu=datoteka_menu)
        datoteka_menu.add_command(label="Shrani",command=self.shrani)
        datoteka_menu.add_command(label="Izhod", command=master.destroy)
        
        self.b=DoubleVar(master,value=randint(1,50))        
        polje_b=Label(master,textvariable=self.b)        
        polje_b.grid(row=1,column=2)
        Label(master,text="=").grid(row=1,column=3)
        self.d=DoubleVar(master,value=0)        
        polje_d=Entry(master,textvariable=self.d)        
        polje_d.grid(row=1,column=4)
        Label(master,text="Pravilen rezultat:").grid(row=2,column=0)
        self.c=DoubleVar(master,value=0)        
        polje_c=Label(master,textvariable=self.c)        
        polje_c.grid(row=2,column=1,columnspan=4)
        gumb_seštevanje=Button(master,text="seštevanje",command=self.seštevanje)
        gumb_seštevanje.grid(row=0,column=1)
        gumb_počisti=Button(master,text="počisti",command=self.počisti)
        gumb_počisti.grid(row=0,column=0)
        gumb_odštevanje=Button(master,text="odštevanje",command=self.odstevanje)
        gumb_odštevanje.grid(row=0,column=2)
        gumb_množenje=Button(master,text="množenje",command=self.mnozenje)
        gumb_množenje.grid(row=0,column=3)
        self.napis_spodaj = StringVar(value="")
        napis = Label(master, textvariable=self.napis_spodaj)
        napis.grid(row=4, column=0, columnspan=4)
        
    def seštevanje(self):
        self.c.set(int(self.a.get())+int(self.b.get()))
        x=self.c.get()
        y=self.d.get()
        if int(x)==y:
            self.napis_spodaj.set("Pravilno")
        else:
            self.napis_spodaj.set("Narobe")
    def odstevanje(self):
        self.c.set(int(self.a.get())-int(self.b.get()))
        x=self.c.get()
        y=self.d.get()
        if int(x)==y:
            self.napis_spodaj.set("Pravilno")
        else:
            self.napis_spodaj.set("Narobe")

    def mnozenje(self):
        self.c.set(int(self.a.get())*int(self.b.get()))
        x=self.c.get()
        y=self.d.get()
        if int(x)==y:
            self.napis_spodaj.set("Pravilno")
        else:
            self.napis_spodaj.set("Narobe")
            
    def počisti(self):
        self.a.set(randint(1,50))
        self.b.set(randint(1,50))
        self.c.set(0)
        self.d.set(0)
        self.napis_spodaj.set("")
        

    def shrani(self):
        ime=filedialog.asksaveasfilename()
        with open(ime,"wt",encoding="utf8") as f:
            if int(self.c.get())==self.d.get():
                f.write(str("Tvoj rezultat je pravilen, cestitam :D")+"\n"+"Kar pridno vadi naprej :)")
            else:
                f.write(str("Tvoj rezultat je zal napacen :(")+"\n"+"Poskusi znova :D")
                
root=Tk()
aplikacija=Ucenje_racunanja(root)
root.mainloop()
