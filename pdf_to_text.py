import os
import pdfplumber
import re



# Directory containing the country folders
base_directory = "/Users/gr2757/Dropbox/global taxation/Outputs"

# Iterate over each country folder
for country_folder in os.listdir(base_directory):
    country_directory = os.path.join(base_directory, country_folder)
    
    # Ensure that the item in the country directory is a folder
    if os.path.isdir(country_directory):
        # Iterate over the PDF files in the country folder
        for root, dirs, files in os.walk(country_directory):
            for name in files:
                if name.endswith(".pdf"):  # Ensure we only process PDF files
                    pdf_path = os.path.join(root, name)
                    with open(pdf_path, "rb") as f:
                        pdf = pdfplumber.open(f)
                        page_length = len(pdf.pages)
                        
                        # Path to the directory for text files
                        text_directory = os.path.join(country_directory, "text_files")
                        
                        # Create the directory if it doesn't exist
                        if not os.path.exists(text_directory):
                            os.makedirs(text_directory)
    
                        # New file name for the text file
                        new_file_name = os.path.join(text_directory, name[:-4] + "_text.txt")
                        
                        # Country name extraction
                        country_name = (name[:-9])
                        country_name = country_name.upper()
                        country_pattern = re.compile(r'\b\d+\s*' + country_name + r'\b' + r'|' + r'\b' + country_name + r'\s*\d+\b')
    
                        # Open the new text file
                        with open(new_file_name, "w+") as new_file:
                            for Ind in range(page_length):
                                page_object = pdf.pages[Ind]
                                text = page_object.extract_text()
                                
                                # Get rid of header countries and pages
                                text = re.sub(country_pattern, '', text)
    
                                new_file.write(text)
                        
                        pdf.close()  # Close the PDF file once done processing
