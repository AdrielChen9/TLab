import tkinter as tk
from tkinter import filedialog

from getInstrument import open_file,extract_data, save_to
from template import * 

# Main frame
root = tk.Tk()
root.title("Instrument Method Extraction and Template Building From Raw MS Files")

# Frame for buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Labels for each row of buttons
label_row1 = tk.Label(button_frame, text="Instrument Method Actions: ")
label_row1.grid(row=0, column=0, columnspan=1)  # Spans across all three columns of buttons

label_row2 = tk.Label(button_frame, text="Template Actions: ")
label_row2.grid(row=1, column=0, columnspan=1)  # Spans across all three columns of buttons


# The buttons
open_button = tk.Button(button_frame, text="Select Instrument File", command=lambda :open_file(file_label))
open_button.grid(row=0, column=1, padx=5, pady= 10)

extract_button = tk.Button(button_frame, text="Extract Instrument Method", command=lambda: extract_data(message_label, instrument_method_display))
extract_button.grid(row=0, column=2, padx=5, pady= 10)

save_to_button = tk.Button(button_frame, text="Save to", command=lambda: save_to(message_label))
save_to_button.grid(row=0, column=3, padx=5, pady= 10)

template_button = tk.Button(button_frame, text="Upload Template", command=lambda: select_template(message_label,template_display))
template_button.grid(row=1, column=1, padx=5, pady= 10)

fill_template_button = tk.Button(button_frame, text="Fill Template", command=lambda: read_template(message_label, instrument_method_display, template_display, filled_template))
fill_template_button.grid(row=1, column=2, padx=5, pady= 10)

save_template_button = tk.Button(button_frame, text="Save Template to", command=lambda: save_filled_template(message_label, filled_template))
save_template_button.grid(row=1, column=3, padx=5, pady= 10)


# Display of the current file name
file_label = tk.Label(root, text="Current File Paths:")
file_label.pack()


# Message display
message_label = tk.Label(root, text="Messages:")
message_label.pack()


# Create a textbox with a heading 
def create_text_display_with_heading(parent, heading_text):
    # Create a frame to hold the text box and heading
    frame = tk.Frame(parent)
    frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Add a label for the heading
    heading_label = tk.Label(frame, text=heading_text, font=('Helvetica', 12, 'bold'))
    heading_label.pack(side=tk.TOP)

    # Add the text box
    text_box = tk.Text(frame, height=30, width=30, wrap=tk.NONE)
    text_box.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    return text_box

# Creating the textboxes and headings 
instrument_method_display = create_text_display_with_heading(root, "Instrument Method Display")
template_display = create_text_display_with_heading(root, "Template Display")
filled_template = create_text_display_with_heading(root, "Filled Template")

root.mainloop()
