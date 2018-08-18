import tkinter as tk
import pygame
import synth_keyboard as sk

pygame.mixer.init()

# directory name where sounds are
direc = '/Users/nol975/Desktop/tiny-piano00/Piano-'

keys = ['A4', 'A5', 'D#4', 'D#5', 'C1', 'F#5', 'C3', 'F#3', 'D#3', 'C4', 'C5', 'C5']

# **********GUI**********

# main window
root = tk.Tk()
root.title('My cool synth')
root.geometry("600x350")

# label

synthphoto = tk.PhotoImage(file='/Users/nol975/Desktop/ferdis_synth.png')
synthphoto = synthphoto.zoom(2, 2)
top = tk.Frame(root).pack(side=tk.TOP)
synthtitle = tk.Label(top, text='test', image=synthphoto, bg='purple')
synthtitle.pack(fill=tk.X)

# keyboard
a = sk.keyboard(root, keys=keys, directory=direc)
a.pack()

# change octave
octave = tk.Frame(root)
octave.pack(fill=tk.Y, expand=0, anchor='w')
octaveswitch = tk.Label(octave, text='test', bg='pink').pack()
octaveswitch2 = tk.Label(octave, text='test', bg='pink').pack()


# Menu bar on top
menu = tk.Menu(root)
root.config(menu=menu)

submenu = tk.Menu(menu)
menu.add_cascade(label='File', menu=submenu)
submenu.add_command(label='Quit', command=root.destroy)


root.mainloop()
