import tkinter as tk
from tkinter import ttk, PhotoImage, Entry, messagebox
from PIL import Image, ImageTk
import csv

# Create a main window
root = tk.Tk()
root.title("MRT Fast")
root.geometry("1280x720")

# Set column 0 width
root.grid_columnconfigure(0, minsize=900)
# Set column 1 width
root.grid_columnconfigure(1, minsize=380)

# Set row weight and column weights to make them expand with the window
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Create title
title_column_0 = tk.Label(root, text="MRT Fast Best FE05", font=("Arial", 70), anchor="n", borderwidth=2, relief="solid", padx=0, pady=5)
title_column_0.grid(row=0, column=0, sticky="nsew")

title_column_1 = tk.Label(root, text="CALCULATE", font=("Arial", 35), anchor="n", borderwidth=2, relief="solid", padx=10, pady=50)
title_column_1.grid(row=0, column=1, sticky="nsew")

# Create Text
text_0 = tk.Label(root, text="WHO :", font=("Arial", 20), anchor="center")
text_0.grid(row=0, column=1, sticky="nw", padx=10, pady=150)

text_1 = tk.Label(root, text="START :", font=("Arial", 20), anchor="center")
text_1.grid(row=0, column=1, sticky="nw", padx=10, pady=200)

text_2 = tk.Label(root, text="END :", font=("Arial", 20), anchor="center")
text_2.grid(row=0, column=1, sticky="nw", padx=10, pady=250)


# Create Entry field
who = ["kid", "scholar", "nomanal person", "elderly"]
option_who = tk.StringVar()
entry_field_who = ttk.Combobox(root, textvariable=option_who, values=who, font=("Arial", 20), state="readonly", width=15)

start_station = []
option_start_station = tk.StringVar()
entry_field_start_station = ttk.Combobox(root, textvariable=option_start_station, values=start_station, font=("Arial", 20), state="readonly", width=14)
# Read data from CSV file
with open('mrt_station.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    start_station = [row[1] for row in reader if row[1] !="Station"]
# Populate start_station
entry_field_start_station['values'] = start_station 

end_station = []
option_end_station = tk.StringVar()
entry_field_end_station = ttk.Combobox(root, textvariable=option_end_station, values=end_station, font=("Arial", 20), state="readonly", width=16)
# Read data from CSV file
with open('mrt_station.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    end_station = [row[1] for row in reader if row[1] !="Station"]
# Populate end_station
entry_field_end_station['values'] = end_station

# Position of entry field
entry_field_who.grid(row=0, column=1, sticky="ne", padx=25, pady=150)

entry_field_start_station.grid(row=0, column=1, sticky="ne", padx=25, pady=200)

entry_field_end_station.grid(row=0, column=1, sticky="ne", padx=25, pady=250)

# Get image mrt map in to column 0 in main window
image_mrtmap = Image.open("mrt_map.png")
width, height = image_mrtmap.size
# Set new size of image
new_width = 900
new_height = (new_width / width) * height
resized_image_mrtmap = image_mrtmap.resize((new_width, int(new_height)), Image.LANCZOS)
# Create a PhotoImage from the resized image
resized_image_mrtmap = ImageTk.PhotoImage(resized_image_mrtmap)

# Get image mrt map in to column 1 in main window
image_mrtlogo = Image.open("mrt_logo.webp")
width, height = image_mrtlogo.size
# Set new size of image
new_width = 150
new_height = (new_width / width) * height
resized_image_mrtlogo = image_mrtlogo.resize((new_width, int(new_height)), Image.LANCZOS)
# Create a PhotoImage from the resized image
resized_image_mrtlogo = ImageTk.PhotoImage(resized_image_mrtlogo)

# # Get image mrt map in to column 1 in main window
image_fe = Image.open("FE.jpg")
width, height = image_fe.size
# Set new size of image
new_width = 170
new_height = (new_width / width) * height
resized_image_fe = image_fe.resize((new_width, int(new_height)), Image.LANCZOS)
# Create a PhotoImage from the resized image
resized_image_fe = ImageTk.PhotoImage(resized_image_fe)

# Create a edge of image
edge_mrtmap = tk.Label(root, image=resized_image_mrtmap, borderwidth=2, relief="solid")
edge_mrtmap.grid(row=0, column=0, sticky="sw", padx=0, pady=0)

edge_mrtlogo = tk.Label(root, image=resized_image_mrtlogo, borderwidth=0, relief="solid")
edge_mrtlogo.grid(row=0, column=1, sticky="se", padx=20, pady=2)

edge_fe = tk.Label(root, image=resized_image_fe, borderwidth=0, relief="solid")
edge_fe.grid(row=0, column=1, sticky="sw", padx=20, pady=30)

# Check to go to "Check List your ticket order" window
def show_selected_values():
    who = option_who.get()
    start = option_start_station.get()
    end = option_end_station.get()

    try:
        if not who and not start and not end:
            raise ValueError("Please select information.")
        if not who and not start:
            raise ValueError("Please select who you are and where your start.")
        if not who and not end:
            raise ValueError("Please select who you are and where your end.")
        if not start and not end:
            raise ValueError("Please select where your at start and where your end.")
        if not who:
            raise ValueError("Please select who you are.")
        if not start:
            raise ValueError("Please select where station is your stay.")
        if not end:
            raise ValueError("Please select where are you going.")
        if start == end:
            raise ValueError("Please check your at start and at end.")
        # Show text in "Check List your ticket order" window
        message = f"You are {who} who start at {start} and want to go to {end}."

        # Create a "Check List your ticket order" window
        checklist_window = tk.Toplevel(root)
        checklist_window.title("Check List your ticket order")
        # Set the size of the Toplevel window
        checklist_window.geometry("780x420")
        # Create a label to display the message
        text_check = tk.Label(checklist_window, text=message, font=("Arial", 14))

        # Position of message
        text_check.pack(anchor="nw")
        text_check.pack(padx= 10, pady=20)

        with open('Prices.csv', 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == start and row[1] == end :
                    if who == "nomanal person":
                        prices = f"You must pay {row[2]} {row[3]}."
                        prices = tk.Label(checklist_window, text=prices, font=("Arial", 14))
                        prices.pack(anchor="nw")
                        prices.pack(padx= 10, pady=0)
                    elif who == "scholar":
                        prices = f"You receive discount 10%, it must be pay {(int(row[2])*0.9)} {row[3]}."
                        prices = tk.Label(checklist_window, text=prices, font=("Arial", 14))
                        prices.pack(anchor="nw")
                        prices.pack(padx= 10, pady=0)
                    elif who == "kid" or "elderly":
                        prices = f"You receive discount 50%, it must be pay {int(row[2])*0.5} {row[3]}."
                        prices = tk.Label(checklist_window, text=prices, font=("Arial", 14))
                        prices.pack(anchor="nw")
                        prices.pack(padx= 10, pady=0)
                    

        # Import Prompay image
        image_path = "Prompay.png"
        try:
            image = Image.open(image_path)
        except IOError as e:
            raise ValueError(f"Error loading image: {e}")
        
        width, height = image.size
        new_width = 250
        new_height = (new_width / width) * height
        resized_image_prompay = image.resize((int(new_width), int(new_height)), Image.LANCZOS)
        # Create a PhotoImage from the resized image
        resized_image_prompay = ImageTk.PhotoImage(resized_image_prompay)

         # Create a edge of Prompay image
        image_label = tk.Label(checklist_window, image=resized_image_prompay, borderwidth=2, relief="solid")
        image_label.image = resized_image_prompay  # Keep a reference to avoid garbage collection
        image_label.pack(anchor="n", padx=10, pady=10)

         # Create a button to go back
        close_button = tk.Button(checklist_window, text="Go back to edit", command=checklist_window.destroy, font=("Arial", 14))
        close_button.pack(side="left", padx=10, pady=10)

        # Create a button to receive ticket
        receive_button = tk.Button(checklist_window, text="Receive ticket", command=open_ticket_window, font=("Arial", 14))
        receive_button.pack(side="right", padx=10, pady=10)

    except ValueError as e:
        # Display an error messagebox
        messagebox.showerror("Your order is not correct", str(e))

# Function to open a ticket window
def open_ticket_window():
    ticket_window = tk.Toplevel(root)
    ticket_window.title("Ticket")
    ticket_window.geometry("400x200")
    text_backtopay = tk.Label(ticket_window, text="Go back to pay me!", font=("Arial", 18))
    text_backtopay.pack()

# Button to show selected values
show_button_tocheck = tk.Button(root, text="Click me to pay", command=show_selected_values, font=("Arial", 16))
show_button_tocheck.grid(row=0, column=1, pady=10)

# Run the Tkinter main loop
root.mainloop()