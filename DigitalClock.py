# import tkinter and time module
import tkinter as tk
import time


# create function to get time
def tick():
    time_string = time.strftime("%H:%M:%S")
    clock.config(text=time_string)
    # call tick() after every 200 micro seconds to display updated time
    clock.after(200, tick)


root = tk.Tk()
# create label to display time on window
clock = tk.Label(root, font=("time", 100, "bold"), bg="cyan")
clock.pack()
# call tick() function for clock label
tick()
root.mainloop()
