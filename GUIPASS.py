import tkinter as tk
import random
import string
def generate_password(length=12, uppercase=True, lowercase=True, digits=True, special_chars=True):
    characters = ''
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if digits:
        characters += string.digits
    if special_chars:
        characters += string.punctuation
    if not characters:
        print("Error: At least one character type must be selected.")
        return None
    password = ''.join(random.choice(characters) for _ in range(length))

        #text widget editing
    result_text.config(state="normal")
        #clear previous content
    result_text.delete("1.0",tk.END)
        #insert new text
    result_text.insert(tk.END,password)
        #disable text widget
    result_text.config(state="disabled")
def start():
    #retrieve text from input field
    password_length=int(length_entry.get())
    include_uppercase=uppercase_var.get()
    include_lowercase=lowercase_var.get()
    include_digits=digits_var.get()
    include_special_chars=special_chars_var.get()
    generate_password(
    length=password_length,
    uppercase=include_uppercase,
    lowercase=include_lowercase,
    digits=include_digits,
    special_chars=include_special_chars)    
    
#create main window
root=tk.Tk()
root.title("GUI EXAMPLE")
root.geometry("500x600")
#widgets
length_label=tk.Label(root,text="enter number")
length_label.pack()
#input field
length_entry=tk.Entry(root)
length_entry.pack()
#button
button=tk.Button(root,text="Getx text" ,command=start)
button.pack()
#check box
uppercase_var=tk.BooleanVar(value=True)
uppercase=tk.Checkbutton(root,text="include upper case",variable=uppercase_var)
uppercase.pack()

lowercase_var=tk.BooleanVar(value=True)
lowercase=tk.Checkbutton(root,text="include lower case",variable=lowercase_var)
lowercase.pack()

digits_var=tk.BooleanVar(value=True)
digits=tk.Checkbutton(root,text="include digits",variable=digits_var)
digits.pack()

special_chars_var=tk.BooleanVar(value=True)
special_chars=tk.Checkbutton(root,text="include special_chars",variable=special_chars_var)
special_chars.pack()
#text widget
result_text=tk.Text(root,wrap="word",height=5,state="disabled")
result_text.pack()

#run the application
root.mainloop()
