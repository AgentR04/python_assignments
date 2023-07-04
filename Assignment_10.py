# 1) Implement the tkinter and webbrowser module
import tkinter as tk
import webbrowser

# 3) Also display the user entered text in the command prompt with message of navigating to "..." whichever site you chooses
def DisplayNavigation():
    s = e.get()
    url = f"https://open.spotify.com/search/{s}"
    print("Navigating to", url)
    webbrowser.open(url)

# 2) create a gui for taking input from the user and create a button to navigate to a browser site.
root = tk.Tk()
root.title("Spotify")
# root.configure(bg="black")

l = tk.Label(root, text="Enter a song or artist:",
             font=("Times New Roman",15),
             width=30,
             height=2,
             )
l.grid()

e = tk.Entry(root, 
             width=30,)
e.grid()

b = tk.Button(root, text="Search",
            font=("Times New Roman",10),
            width=20,
            height=2,
            activebackground="#1DB954",
            command=DisplayNavigation)
b.grid()

b=tk.Button(root,
            text="Exit",
            font=("Times New Roman",10),
            width=20,
            height=2,
            activebackground="#1DB954",
            command=root.destroy)
b.grid()

root.mainloop()
