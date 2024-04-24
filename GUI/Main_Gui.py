import tkinter as tk
from tkinter import filedialog


from getInstrument import open_file,extract_data, save_to


# Main window
root = tk.Tk()
root.title("Extract Instrument Method From Raw MS Files")

# Frame for buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Buttons
open_button = tk.Button(button_frame, text="Open File", command=lambda :open_file(file_label))
open_button.grid(row=0, column=0, padx=5)
extract_button = tk.Button(button_frame, text="Extract", command=lambda: extract_data(message_label, text_preview))
extract_button.grid(row=0, column=1, padx=5)

save_to_button = tk.Button(button_frame, text="Save to", command=lambda: save_to(message_label))
save_to_button.grid(row=0, column=2, padx=5)

# Display of the current file name
file_label = tk.Label(root, text="Current File Paths:")
file_label.pack()

# Message display
message_label = tk.Label(root, text="Messages:")
message_label.pack()

#text display 
text_preview = tk.Text(root, height=30, width=30, wrap=tk.NONE)
text_preview.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# x_scrollbar = tk.Scrollbar(root, orient=tk.HORIZONTAL, command=text_preview.xview)
# x_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
# text_preview.config(xscrollcommand=x_scrollbar.set)


# Main loop
root.mainloop()
