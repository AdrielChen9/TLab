import tkinter as tk
from tkinter import filedialog

#The various dicts for the template 
masterscan_dict = {} 
charge_stage_dict = {} 
ddmsn_dict = {}

#Selects the dict to be filled out based on what the current section is (determined from 'line') 
def match(current_dict, line): 
    match current_dict: 
        case 'Scan MasterScan':
            fill_out_dict(masterscan_dict, line)
        case 'Filter ChargeState':
            fill_out_dict(charge_stage_dict, line)
        case 'Scan ddMSnScan':
            fill_out_dict(ddmsn_dict,line)
        case "": 
            pass
        case _: 
            pass  

#Adds the key-value pair to the respective dict based on the line 
def fill_out_dict(dict, line): 

    if '=' in line:
        try: #for lines key = value 
            key, value = line.strip().split(' = ')
            dict[key.strip()] = value.strip()
        except ValueError: 
            try:  #for lines key =value or key= value 
                parts = line.split('=')
                reformat = ' = '.join(parts) 
                key, value = reformat.strip().split(' = ')
                dict[key.strip()] = value.strip() 
            except ValueError:  #for lines with key = "nothing"
                key= line.strip()
                dict[key] = ""
    else: #for section titles, everything lese
        key = line.strip()
        dict[key] = ""

#Determines which section we are in
def read_instrument_lines_from_file(filename):

    #determines which section we are in ; ignores everything else
    with open(filename, 'r') as file:
        current_dict_name = "" 
        for line in file:
            if 'Scan MasterScan' in line: 
                current_dict_name = 'Scan MasterScan'
            elif 'Filter ChargeState' in line: 
                current_dict_name = 'Filter ChargeState'
            elif 'Scan ddMSnScan' in line: 
                current_dict_name = 'Scan ddMSnScan'  
            elif '=' not in line:  # no '=' means section title, so skip them if it isn't any of the 3 above
                current_dict_name = ''
            match(current_dict_name, line)

    return 1

#Select the instrument method to be read
def select_instrument_method():
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Prompt user to select a file
    file_path = filedialog.askopenfilename(title="Select the instrument method file(in .txt)")

    if file_path:
        return file_path
    else:
        print("No file selected.")
        return None

#Select the template file you want filled out 
def select_template(additional_text_preview): 
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Prompt user to select a file
    file_path = filedialog.askopenfilename(title="Select the template file (in .txt form)")

    if file_path:
        with open(file_path, 'r', encoding='utf-8') as file:
            template_content = file.read()
        additional_text_preview.delete('1.0', tk.END)
        additional_text_preview.insert(tk.END, template_content)
        
        return file_path
    else:
        print("No file selected.")
        return None

#Reads the template, fills it, then returns a filled out template as a separate txt
def read_template(textFile):
    # Read the text from the file
    with open('template.txt', 'r', encoding='utf-8') as file:
        text = file.read()

    # Split the text into sections
    sections = text.split('#')

    # Initialize filled sections
    filled_sections = []

    # Fill in the blanks for each section
    for section in sections[1:]:  # Skip first empty element
        section_name, section_text = section.split('\n', 1)
        section_dict = None
    
        if section_name.strip() == 'MasterScan':
            section_dict = masterscan_dict
        elif section_name.strip() == 'Charge state':
            section_dict = charge_stage_dict
        elif section_name.strip() == 'DDMSN':
            section_dict = ddmsn_dict
        
        if section_dict:
            filled_section = section_text.format(**section_dict)
            filled_sections.append(filled_section)

    #printing out 
    output_file = 'filled_out_text.txt'
    with open(output_file, 'w') as file:
        for section in filled_sections:
            x= f"{section.strip()}"
            file.write(x)

def main():

    #select the template  
    template_file = select_template()
    if not template_file:
        return

    #select the instrument method     
    instrument_file = select_instrument_method()
    if not instrument_file:
        return 
    
    #fill out the dicts 
    read_instrument_lines_from_file(instrument_file)

    #fill out the template and return 
    read_template(template_file) 

# main()