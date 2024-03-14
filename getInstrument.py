from pymsfilereader import MSFileReader
import os

def main():
    # Path to the RAW file relative to the script's location
    raw_file_path = os.path.join(os.path.dirname(__file__), 'files', 'rawfile1.raw')
    
    # Path for the output file
    outfile = os.path.join(os.path.dirname(__file__), 'files', 'rawfile1.txt')
    
    # Open the RAW file
    
    rawfile = MSFileReader(raw_file_path)
    try: 
        # Select the MS instrument
        rawfile.GetInstMethod()
        
        # Get the instrument method
        # instrument_method = rawfile.GetInstrumentMethod(1)
        instrument_method = rawfile.GetInstMethod()
        
        # Write the instrument method to the output file
        with open(outfile, "w") as text_out:
            text_out.write(instrument_method)
    finally: 
        rawfile.Close() 

if __name__ == "__main__":
    main()
