import tkinter as tk
from tkinter import filedialog

def read_values_from_file(filename):
    dictionary = {}
    with open(filename, 'r') as file:
        for line in file:
            if '=' in line:
                try: 
                    key, value = line.strip().split(' = ')
                    dictionary[key.strip()] = value.strip()
                except ValueError: 
                    parts = line.split('=')
                    reformat = ' = '.join(parts) 
                    key, value = reformat.strip().split(' = ')
                    dictionary[key.strip()] = value.strip() 
            else:
                key = line.strip()
                dictionary[key] = ""
        print(dictionary)
    
    return dictionary

def fill_blank(text, values):
    for key, value in values.items():
        text = text.replace(f'{{{key}}}', value)
    return text

def select_file():
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Prompt user to select a file
    file_path = filedialog.askopenfilename(title="Select values.txt file")

    if file_path:
        return file_path
    else:
        print("No file selected.")
        return None

def main():
    # Select values.txt file using GUI
    values_file = select_file()
    if not values_file:
        return  # Exit if no file selected

    # Read values from the selected file
    values = read_values_from_file(values_file)

    # Read the pre-written text file
    text_file = 'template.txt'
    with open(text_file, 'r') as file:
        pre_written_text = file.read()

    # Fill in the blanks in the pre-written text with values from the dictionary
    filled_text = fill_blank(pre_written_text, values)

    # Output the filled text
    print(filled_text)

    # Optionally, write the filled text to a new file
    output_file = 'filled_text.txt'
    with open(output_file, 'w') as file:
        file.write(filled_text)

if __name__ == "__main__":
    main()
