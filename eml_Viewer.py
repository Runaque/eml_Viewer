import tkinter as tk
from tkinter import filedialog

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("EML files", "*.eml")])
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        text_area.delete(1.0, tk.END)
        text_area.insert(tk.END, content)

def clear_screen():
    text_area.delete(1.0, tk.END)

def save_as_txt():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'w', encoding='utf-8') as f:
            content = text_area.get(1.0, tk.END)
            f.write(content)

root = tk.Tk()
root.title("EML File Viewer")

# Create a frame for the buttons
button_frame = tk.Frame(root)
button_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

open_button = tk.Button(button_frame, text="Open .eml file", command=open_file)
open_button.pack(side=tk.LEFT, padx=5)

clear_button = tk.Button(button_frame, text="Clear screen", command=clear_screen)
clear_button.pack(side=tk.LEFT, padx=5)

save_button = tk.Button(button_frame, text="Save as .txt", command=save_as_txt)
save_button.pack(side=tk.RIGHT, padx=5)

# Text area to display the content
text_area = tk.Text(root, wrap=tk.WORD, bg='white', fg='black')
text_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

# Frame for the signature at the bottom
signature_frame = tk.Frame(root)
signature_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=5)

# Center the signature label within the frame
signature_label = tk.Label(signature_frame, text="Made in Antwerp by Runaque", bg='SystemButtonFace', fg='grey', font=('Helvetica', 10))
signature_label.pack(side=tk.LEFT, expand=True)
signature_label.pack(side=tk.RIGHT, expand=True)

root.mainloop()