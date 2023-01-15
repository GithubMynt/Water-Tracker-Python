import tkinter as tk 
from time import time
from data.data_functions import *
from PIL import ImageTk, Image

def return_amount():

    user_data = load_json()
    return user_data["cups_drank"]

# Set the width and length for the window 
root = tk.Tk()
length, width = 800, 800
root.geometry(f"{length}x{width}")
root.resizable(False, False)

# At the very top, I want to display the users number of cups of water drank
amount_display = tk.Label(root, text=f"Today, you have drank {return_amount()} cup(s) of water!", font=("Arial", 30), fg="#4b8ec4")
amount_display.pack()

# In the bottom left, I want to display how much one cup of water is 
cup_value = tk.Label(root, text="*One 'cup' of water is 8 ounces (around 240ml)", font=('Arial', 10), fg="black")
cup_value.pack(anchor="w", side="bottom")

# Functions that the buttons in the program will utilize
def addition():

    user_data = load_json()
    user_data["cups_drank"] += 1

    write_json(user_data)
    amount_display["text"] = f"Today, you have drank {return_amount()} cup(s) of water!"

    return 

def subtract():

    user_data = load_json()
    if user_data["cups_drank"] == 0:
        return 
    user_data["cups_drank"] -= 1

    write_json(user_data)
    amount_display["text"] = f"Today, you have drank {return_amount()} cup(s) of water!"

    return 

# Insert an image into the window, and center it. 
cup_logo = ImageTk.PhotoImage(Image.open("./images/cup.png"))
cup_label = tk.Label(root, image=cup_logo)
cup_label.place(x=length/2, y=width/2, anchor="center")

# Create button to +1 to the cups of water drank

# First create the custom image for the button 
add_button_img = ImageTk.PhotoImage(Image.open("./images/add_button.png"))
add_img_label = tk.Label(image=add_button_img)

add_button = tk.Button(root, text="+", image=add_button_img, command=addition, borderwidth=0)
add_button.pack(side="left", anchor="s", expand=True, pady=15)

# Create button to -1 to the cups of water drank 

# First create the custom image for the button 
minus_button_img = ImageTk.PhotoImage(Image.open("./images/minus_button.png"))
minus_img_label = tk.Label(image=minus_button_img)

subtract_button = tk.Button(root, text="-", image=minus_button_img, command=subtract, borderwidth=0)
subtract_button.pack(side="left", anchor="s", expand=True, pady=15)

# Loop the window
def main():

    user_data = load_json()

    if user_data["time_last_used"] is None or (time() - user_data["time_last_used"]) > 3600:
        user_data["cups_drank"] = 0
        user_data["time_last_used"] = time()

    write_json(user_data)

    root.mainloop()

if __name__ == "__main__":
    main()