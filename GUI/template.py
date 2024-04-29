import tkinter as tk
from tkinter import filedialog
from getInstrument import get_current_files, get_extracted_info 

#The various dicts for the template 
masterscan_dict = {} 
charge_stage_dict = {} 
ddmsn_dict = {}

#Select the template file you want filled out 
def select_template(message_label,template_display): 
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Prompt user to select a file
    file_path = filedialog.askopenfilename(title="Select the template file (in .txt form)")

    if file_path:
        with open(file_path, 'r', encoding='utf-8') as file:
            template_content = file.read()
        template_display.delete('1.0', tk.END)
        template_display.insert(tk.END, template_content)

        message_label.config(text="Message: Template selected")

        return file_path
    else:
        print("No file selected.")
        return None


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
def read_instrument_lines_from_file(instrument_method_preview):

    x = instrument_method_preview.get('1.0', tk.END)

    lines = x.split('\n')

    #determines which section we are in ; ignores everything else
    current_dict_name = "" 
    for line in lines:
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

#Reads the template, fills it, then returns a filled out template as a separate txt
def read_template(message_label, instrument_method_preview, template_display, filled_template):

    read_instrument_lines_from_file(instrument_method_preview)

    text = template_display.get('1.0', tk.END)

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


    for filled_section in filled_sections:
        filled_template.insert(tk.END, filled_section)
    
    message_label.config(text="Message: Template  filled")



def save_filled_template(message_label, filled_template):
    # Get the content from the additional_text Text widget
    text_content = filled_template.get('1.0', tk.END)

    # Prompt user to select a file name and location for saving
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
        title="Save Text File"
    )

    if file_path:
        # Write the content to the selected file
        try:
            with open(file_path, 'w') as file:
                file.write(text_content)
            message_label.config(text="Message: Template Saved")
        except Exception as e:
            print(f"Error occurred while saving file: {e}")
    else:
        print("Save operation cancelled.")

