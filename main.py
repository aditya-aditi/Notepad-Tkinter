import tkinter as tk
from tkinter.filedialog import askopenfilename


# Event handlers
def open_file():
    """
    Open a file
    """
    global text_editor_txt
    filename = tk.filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if filename == '':
        return
    else:
        text_editor_txt.delete("1.0", tk.END)
        with open(filename, "r") as f:
            text_editor_txt.insert(tk.END, f.read())


def save_file():
    """
    Save a file
    """
    global text_editor_txt
    filename = tk.filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    # text_editor_txt.delete("1.0", tk.END)
    with open(filename, "w") as f:
        f.write(text_editor_txt.get("1.0", tk.END))


# Tkinter Code
# Create a new window
window = tk.Tk()
window.title("Notepad")

# Configure the row and column
window.columnconfigure(1, weight=1)
window.rowconfigure(0, weight=1)

# Create a frame to display the buttons
frame_btn = tk.Frame(width=80)
frame_btn.grid(column=0, sticky="ns")

# Create a open button which will open the text files
open_btn = tk.Button(master=frame_btn, text="Open", command=open_file)
open_btn.pack(padx=10, pady=10)

# Create a save button which will save the text files
save_btn = tk.Button(master=frame_btn, text="Save As...", command=save_file)
save_btn.pack(padx=10, pady=10)

# Create a area where user can write
text_editor_txt = tk.Text(font=8)
text_editor_txt.grid(column=1, row=0, sticky="nsew")

window.mainloop()
