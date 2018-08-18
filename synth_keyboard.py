import tkinter as tk
from functools import partial
import pygame
import time

pygame.mixer.init()

#to fix:

#make list of keys into a dic of octaves
def _generateoctlist(lok):
    assert len(lok)%12==0
    l=len(lok)
    lmod=l//12
    a=dict()
        
    for x in range(lmod):
        a[x]=[lok[y+12*x] for y in range(12)]
    return a
            

def split(listo):
    assert len(listo)==12
    seplist=[1,0,1,0,1,1,0,1,0,1,0,1]

    white=list()
    for x in range(12):
        if seplist[x]:
            white.append(listo[x])

    black=list()
    for x in range(12):
        if not seplist[x]:
            black.append(listo[x])

    return(white, black)


class keyboard:#7 white keys and 5 black ones

    def __init__(self, masterframe, keys, directory):
        self.synthframe = tk.Frame(masterframe)
        self.whitenames = split(keys)[0]
        self.blacknames = split(keys)[1]
        self.listofkeys = [str(directory)+x+'.wav' for x in self.whitenames]            #directory of white keys
        self.listofblackkeys = [str(directory)+x+'.wav' for x in self.blacknames]       #directory of black keys
        self.whitebutt = ['a','s','d','f','g','h','j']                                  #which keyboard key plays white buttons
        self.blackbutt = ['w','e','t','z','u']                                          #which keyboard key plays black buttons
        self.bbb = [1, 1, 0, 1, 1, 1, 0]                                                #black button binary,where black buttons go
        self._makekeyboard()
        
        
        #bind keyboard keys to laptop keys
        for i in range(len(self.whitenames)):
            masterframe.bind(str(self.whitebutt[i]),partial(self._clicked,i))

        for i in range(len(self.blacknames)):
            masterframe.bind(str(self.blackbutt[i]),partial(self._blackclicked,i))
            

    def _clicked(self,a,_event=None):
        pygame.mixer.Sound(self.listofkeys[a]).play()

    def _blackclicked(self,a,_event=None):
        pygame.mixer.Sound(self.listofblackkeys[a]).play()

    def _makekeyboard(self):
        for i in range(len(self.listofkeys)):
            tk.Button(self.synthframe, text=self.whitenames[i]+'\n'+self.whitebutt[i],\
                      anchor='s', pady=30,highlightbackground='white', command=partial(self._clicked,i))\
                      .grid(row=0, column=i*3, rowspan=2, columnspan=3, sticky='nsew');

        counter=0
        for i in range(len(self.listofkeys) - 1):
            if self.bbb[i]:
                tk.Button(self.synthframe, text=self.blacknames[counter]+'\n'+self.blackbutt[counter],\
                          anchor='s', pady=30 ,highlightbackground='black', command=partial(self._blackclicked,counter))\
                          .grid(row=0, column=(i*3)+2, rowspan=1, columnspan=2, sticky='nsew')
                counter+=1

        #give the buttons weight
        for i in range(len(self.whitenames) * 3):     
            self.synthframe.columnconfigure(i, weight=1)

        for i in range(2):
            self.synthframe.rowconfigure(i, weight=1)
        
        
        

    def pack(self):
        self.synthframe.pack(side= tk.RIGHT, fill=tk.BOTH, expand=1)

    def destroy(self):
        self.synthframe.destroy()


#class to move octaves
class assoct:
    def __init__(self,masterframe,lok,directory): #lok = list of keys, mod 12=0 and put in dict of octlists
        self.masterframe=masterframe
        self.directory=directory
        
        self.octlist=_generateoctlist(lok)
        self.octkeys=list(self.octlist.keys())
        self.keyboard=keyboard(masterframe=self.masterframe, keys=self.octlist[self.octkeys[-1]//2], directory=self.directory)
        self.schluessel=self.octkeys[-1]//2
        self.schlmax=self.octkeys[-1]
        self.schlmin=self.octkeys[0]

        self.keyboard.pack()
        
    def octaveup(self):
        if self.schluessel==self.schlmax:
            pass
        else:
            self.keyboard.destroy()
            self.schluessel+=1
            self.keyboard=keyboard(masterframe=self.masterframe,keys=self.octlist[self.schluessel], directory=self.directory)
            self.keyboard.pack()
            
    def octavedown(self):
        if self.schluessel==self.schlmin:
            pass
        else:
            self.keyboard.destroy()
            self.schluessel-=1
            self.keyboard=keyboard(masterframe=self.masterframe, keys=self.octlist[self.schluessel], directory=self.directory)
            self.keyboard.pack()

#test
if __name__ == "__main__":
    
    root=tk.Tk()
    root.geometry('700x400')

    

    direc='/Users/nol975/Desktop/tiny-piano00/Piano-'

    
    white=['A4','A5','D#4','D#5','C1','F#5','C3']
    blacks=['F#3','D#3','C4','C5','C5']
    mix=white+blacks +['A4']*12
    
    c=assoct(masterframe=root, lok=mix, directory=direc)

    a=tk.Button(text='up', command=c.octaveup())
    a.pack(anchor='n')

    b=tk.Button(text='down', command=c.octavedown())
    b.pack(anchor='e')
    
    '''
    c.octaveup()
    
    c.octavedown()

    
    
    print(c.keyboard)
    c.octavedown()
    print(c.keyboard)
    '''
