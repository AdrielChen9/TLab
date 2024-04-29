import tkinter as tk
from tkinter import filedialog

from getInstrument import open_file,extract_data, save_to
from template import * 


# Main window
root = tk.Tk()
root.title("Extract Instrument Method From Raw MS Files")

# Frame for buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Buttons
open_button = tk.Button(button_frame, text="Open File", command=lambda :open_file(file_label))
open_button.grid(row=0, column=0, padx=5)

extract_button = tk.Button(button_frame, text="Extract", command=lambda: extract_data(message_label, instrument_method_preview))
extract_button.grid(row=0, column=1, padx=5)

save_to_button = tk.Button(button_frame, text="Save to", command=lambda: save_to(message_label))
save_to_button.grid(row=0, column=2, padx=5)

template_button = tk.Button(button_frame, text="Upload template", command=lambda: select_template(template_display))
template_button.grid(row=0, column=3, padx=5)

fill_template_button = tk.Button(button_frame, text="Fill template", command=lambda: read_template(instrument_method_preview, template_display, filled_template))
fill_template_button.grid(row=0, column=4, padx=5)

save_template_button = tk.Button(button_frame, text="Save template", command=lambda: save_filled_template(filled_template))
save_template_button.grid(row=0, column=5, padx=5)

# Display of the current file name
file_label = tk.Label(root, text="Current File Paths:")
file_label.pack()

# Message display
message_label = tk.Label(root, text="Messages:")
message_label.pack()

#Text display for Instrument Methods 
instrument_method_preview = tk.Text(root, height=30, width=30, wrap=tk.NONE)
instrument_method_preview.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

template_display = tk.Text(root, height=30, width=30, wrap=tk.NONE)
template_display.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

filled_template = tk.Text(root, height=30, width=30, wrap=tk.NONE)
filled_template.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

#Main loop
root.mainloop()
