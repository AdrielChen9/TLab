from pymsfilereader import MSFileReader
import tkinter as tk
from tkinter import filedialog
import os 

current_files = []
extracted_info = []

def open_file(file_label):
    current_files.clear()
    initial_dir = os.getcwd()
    file_paths = filedialog.askopenfilenames(initialdir=initial_dir, filetypes=[("RAW file", "*.raw")], multiple=True)

    if file_paths:
        current_files.extend(file_paths)
        update_file_label(file_label)

def update_file_label(file_label):
    file_label.config(text="Current File Paths:\n" + "\n".join("\u2022 " + file_path for file_path in current_files))

def extract_data(message_label, instrument_method_preview):
    if not current_files:
        message_label.config(text="Messages: No file selected")
        return

    for file in current_files:
        try:
            rawfile = MSFileReader(file)
            instrument_method = rawfile.GetInstMethod()
            rawfile.Close()
            extracted_info.append(instrument_method)

            for item in extracted_info: 
                instrument_method_preview.insert(tk.END, item + "\n")

        except Exception as e:
            error = f"Error extracting data from {file}: {e}"
            message_label.config(text=f"Messages: {error}")
            return

    message_label.config(text="Message: Instrument Method Successfully Extracted")

def save_to(message_label): 
    if not current_files or not extracted_info:  #if nothing is selected
        message_label.config(text="Messages: Nothing selected.")
    else:     
        output_folder = filedialog.askdirectory(title="Select Output Folder")
        if output_folder:
            for file_path, instrument_method in zip(current_files, extracted_info):
                file_name = os.path.basename(file_path)
                output_file_path = os.path.join(output_folder, f"{file_name}_instrument_method.txt")
                with open(output_file_path, "w") as output_file:
                    output_file.write(str(instrument_method))

        message_label.config(text="Messages: Data extraction completed.")

def get_current_files():
    return current_files

def get_extracted_info():
    return extracted_info