import tkinter as tk
from tkinter import ttk
import time
import keyboard
import pydirectinput
import yaml

with open("skills.yaml", 'r') as file:
    skills = yaml.safe_load(file)

def on_closing():
    root.destroy()

# per skill cooldowns
cooldown = {}
progress = {}
last_time = time.time()

# gui elements
window_height = len(skills)*48
progress_bar = {}
button = {}
inkey_label = {}
outkey_label = {}

# make list of inkeys/outkeys to avoid infinite loops
inkeys = []
for k in skills:
    if 'inkey' in skills[k]:
        inkeys.append(skills[k]['inkey'])
outkeys = []
for k in skills:
    if 'outkey' in skills[k]:
        outkeys.append(skills[k]['outkey'])

# update progress bars ~60 times per second
def update():
    root.after(17, update)
    global last_time
    delta_time = time.time() - last_time
    last_time = time.time()
    for k in progress.keys():
        # increment progress timer
        if progress[k].get() < cooldown[k]:
            progress[k].set(progress[k].get() + delta_time)

def press_key(k):
    if k in skills:
        if 'outkey' in skills[k]:
            if skills[k]['outkey'] not in inkeys:
                pydirectinput.press(skills[k]['outkey'])
        reset_key(k)

def reset_key(k):
    if k in skills:
        progress[k].set(0)

# receive keyboard input
def on_key_event(e):
    if e.name in inkeys and e.event_type == 'down':
        for k in progress.keys():
            if progress[k].get() >= cooldown[k]:
                if 'inkey' in skills[k]:
                    if e.name == skills[k]['inkey']:
                        press_key(k)
                        break

keyboard.hook(on_key_event)

# create window
root = tk.Tk()
root.title("Everquest Macro")
root.geometry(f"220x{window_height}")  # Set the window size

def add_progress_bar(k, cd, row, col):
    progress[k] = tk.DoubleVar()
    progress[k].set(cd)
    cooldown[k] = cd
    progress_bar[k] = ttk.Progressbar(root, variable=progress[k], maximum=cooldown[k])
    progress_bar[k].grid(row=row,column=col+3,padx=2, pady=10)
    button[k] = tk.Button(root, text=k, command=lambda: reset_key(k))
    button[k].grid(row=row,column=col+1,padx=2, pady=10)
    if 'inkey' in skills[k]:
        inkey_label[k] = tk.Label(root, text=skills[k]['inkey'])
        inkey_label[k].grid(row=row,column=col,padx=2, pady=10)
    if 'outkey' in skills[k]:
        outkey_label[k] = tk.Label(root, text=skills[k]['outkey'])
        outkey_label[k].grid(row=row,column=col+2,padx=2, pady=10)
    
i = 0
for k in skills.keys():
    add_progress_bar(k, skills[k]['cooldown'], i, 0)
    i += 1

root.protocol("WM_DELETE_WINDOW", on_closing)

update()
root.mainloop()