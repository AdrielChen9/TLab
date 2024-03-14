
import tkinter as tk
from tkinter import filedialog
from pymsfilereader import MSFileReader
import os

current_files = []

def open_file():
    initial_dir = os.getcwd()
    file_paths = filedialog.askopenfilenames(initialdir=initial_dir, filetypes=[("RAW file", "*.raw")], multiple=True)

    if file_paths:
        current_files.extend(file_paths)
        update_file_label()

def update_file_label():
    file_label.config(text="Current File Paths:\n" + "\n".join("\u2022 " + file_path for file_path in current_files))

def extract_data():
    if not current_files:
        message_label.config(text="Messages: No file selected")
        return

    extracted_info = []
    for file in current_files:
        try:
            rawfile = MSFileReader(file)
            instrument_method = rawfile.GetInstMethod()
            rawfile.Close()
            extracted_info.append(instrument_method)
        except Exception as e:
            error = f"Error extracting data from {file}: {e}"
            message_label.config(text=f"Messages: {error}")
            return

    output_folder = filedialog.askdirectory(title="Select Output Folder")
    if output_folder:
        for file_path, instrument_method in zip(current_files, extracted_info):
            file_name = os.path.basename(file_path)
            output_file_path = os.path.join(output_folder, f"{file_name}_instrument_method.txt")
            with open(output_file_path, "w") as output_file:
                output_file.write(str(instrument_method))

    message_label.config(text="Messages: Data extraction completed.")

# Main window
root = tk.Tk()
root.title("Extract Instrument Method From Raw MS Files")

# Frame for buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Buttons
open_button = tk.Button(button_frame, text="Open File", command=open_file)
open_button.grid(row=0, column=0, padx=5)
extract_button = tk.Button(button_frame, text="Extract and Save Data To", command=extract_data)
extract_button.grid(row=0, column=1, padx=5)

# Display of the current file name
file_label = tk.Label(root, text="Current File Paths:")
file_label.pack()

# Message display
message_label = tk.Label(root, text="Messages:")
message_label.pack()

# Main loop
root.mainloop()
