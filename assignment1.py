import tkinter as tk
from tkinter import messagebox

# Initialize the main window
root = tk.Tk()
root.title("Library Management System")
root.geometry("400x400")

# Initialize a list to store books
book_list = []

# Function to add a new book
def add_book():
    book = entry_book.get()
    if book:
        book_list.append(book)
        entry_book.delete(0, tk.END)
        update_book_list()
    else:
        messagebox.showwarning("Input Error", "Please enter a book name")

# Function to update the listbox with the current book list
def update_book_list():
    listbox_books.delete(0, tk.END)
    for index, book in enumerate(book_list, start=1):
        listbox_books.insert(tk.END, f"{index}. {book}")

# Function to delete a selected book
def delete_book():
    selected_book = listbox_books.curselection()
    if selected_book:
        index = selected_book[0]
        del book_list[index]
        update_book_list()
    else:
        messagebox.showwarning("Selection Error", "Please select a book to delete")

# Widgets to add books
label_book = tk.Label(root, text="Enter book name:")
label_book.pack(pady=10)

entry_book = tk.Entry(root)
entry_book.pack(pady=5)

button_add = tk.Button(root, text="Add Book", command=add_book)
button_add.pack(pady=5)

# Listbox to display books
label_book_list = tk.Label(root, text="Books in Library:")
label_book_list.pack(pady=10)

listbox_books = tk.Listbox(root, height=10, width=50)
listbox_books.pack(pady=10)

# Button to delete a book
button_delete = tk.Button(root, text="Delete Book", command=delete_book)
button_delete.pack(pady=5)

# Function to exit the application
def exit_app():
    root.quit()

# Exit button
button_exit = tk.Button(root, text="Exit", command=exit_app)
button_exit.pack(pady=5)

# Start the Tkinter event loop
root.mainloop()
