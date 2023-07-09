import webbrowser
import tkinter as tk

def form():
    option = selected_option.get()
    
    if option == "Twitter Help":
        faq_url = "https://help.twitter.com/en"
    elif option == "Facebook Help":
        faq_url = "https://www.facebook.com/help"
    else:
        faq_url = ""
    
    if faq_url:
        webbrowser.open(faq_url)

root = tk.Tk()
root.title("Assignment 11")

label1 = tk.Label(root, text="Enter your Name:")
label1.grid()
 
entry = tk.Entry(root)
entry.grid()

label2 = tk.Label(root, text="Select FAQ page")
label2.grid()

selected_option = tk.StringVar()
selected_option.set("Twitter Help")
options = ["Twitter Help", "Facebook Help"]  
dropdown = tk.OptionMenu(root, selected_option, *options)
dropdown.grid()

submit_button = tk.Button(root, text="Submit", command=form)
submit_button.grid()

root.mainloop()
