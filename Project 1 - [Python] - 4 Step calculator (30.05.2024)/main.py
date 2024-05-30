import customtkinter

# Initialize main window
root = customtkinter.CTk()
root.title("Display A/B")
root.geometry("300x200")

# Function to display "A"
def display_a():
    label.configure(text="A")

# Function to display "B"
def display_b():
    label.configure(text="B")

# Create a label to display "A" or "B"
label = customtkinter.CTkLabel(root, text="", font=("Helvetica", 42)) # Police and size of text display
label.pack(pady=50) #

# Create buttons to change with "A" or "B"
button_a = customtkinter.CTkButton(root, text="Display A", command=display_a)
button_a.pack(side="left", padx=10, pady=10)

button_b = customtkinter.CTkButton(root, text="Display B", command=display_b)
button_b.pack(side="right", padx=10, pady=10)

# Start the main application
root.mainloop()
