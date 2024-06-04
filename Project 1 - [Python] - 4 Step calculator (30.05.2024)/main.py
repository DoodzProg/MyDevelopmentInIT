import customtkinter

# Init main window
root = customtkinter.CTk()
root.title("Calculatrice")
root.geometry("400x600")

# Variable to store the expression
expression = ""

# Update expression in the text entry box
def update_expression(value):
    global expression
    expression += str(value)
    input_text.set(expression)

# Evaluate final expression
def evaluate_expression():
    global expression
    try:
        result = str(eval(expression))  # evaluate expression
        input_text.set(result)  # display result
        expression = result  # update expression with result
    except:
        input_text.set("ERROR")  # invalid expression
        expression = ""

# Function to clear the expression
def clear_expression():
    global expression
    expression = ""
    input_text.set("")

# Input text box
input_text = customtkinter.StringVar()
input_frame = customtkinter.CTkFrame(root)
input_frame.pack(pady=20)

input_entry = customtkinter.CTkEntry(input_frame, textvariable=input_text, font=("Helvetica", 28), width=380, justify='right')
input_entry.grid(row=0, column=0, ipady=10)

# Frame for buttons
button_frame = customtkinter.CTkFrame(root)
button_frame.pack()

# Buttons for digits
digits = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('0', 4, 1)
]

for (digit, row, column) in digits:
    button = customtkinter.CTkButton(button_frame, text=digit, command=lambda d=digit: update_expression(d), width=80, height=80)
    button.grid(row=row, column=column, padx=5, pady=5)

# Buttons for operations
operations = [
    ('+', 1, 3), ('-', 2, 3), ('×', 3, 3), ('÷', 4, 3)
]

for (op, row, column) in operations:
    button = customtkinter.CTkButton(button_frame, text=op, command=lambda o=op: update_expression(o if o != '×' and o != '÷' else '*' if o == '×' else '/'), width=80, height=80)
    button.grid(row=row, column=column, padx=5, pady=5)

# Buttons Clear and Equal
clear_button = customtkinter.CTkButton(button_frame, text="C", command=clear_expression, width=80, height=80)
clear_button.grid(row=4, column=0, padx=5, pady=5)

equal_button = customtkinter.CTkButton(button_frame, text="=", command=evaluate_expression, width=80, height=80)
equal_button.grid(row=4, column=2, padx=5, pady=5)

# Start
root.mainloop()
