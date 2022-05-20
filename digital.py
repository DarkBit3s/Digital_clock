#import reqiure packages
import tkinter as tk
import time

# creating a root window to work on it
root = tk.Tk()
root.title("Digital clock")
root.iconphoto(False, tk.PhotoImage(file='clock2.png'))

# defining our function to update the clock value
def update_clock():
	hours = time.strftime("%I")
	minutes = time.strftime("%M")
	seconds = time.strftime("%S")
	am_pm = time.strftime("%p")
	time_text = hours + ":" + minutes + ":" + seconds + " " + am_pm
	clock_label.config(text=time_text)
	clock_label.after(1000,update_clock)
	

# creating a label to display it to window
clock_label = tk.Label(root,text="00:00:00",font="Helvetica 72 bold",fg='white',bg='black')

update_clock()

clock_label.pack()

root.mainloop()
