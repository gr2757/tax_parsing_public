# tax_parsing_public

### The first file to run is the better_split_pdf.ipynb which is a jupyter notebook that splits all the pdf files into countries and years.

The “year_page_gap” list of lists deals with the gap between what page the pdf is on and what number is on the page of the pdf. This was hard coded by hand, just went to a page on the pdf to see what the number on the page is. After that it is all about finding the table of contents to find page numbers and split up the pdf into countries.  Then the program standardizes the names of a few different countries, so the generated pdfs go into the right country folders. Some are shortening of names, “China, Republic” into just “China”. Lastly the program creates the pdf files to be from the start of the first page of a country to the start of the next county. 

### The second file to run is the better_pdf_to_text.ipynb which is also a notebook. It converts the individual pdf files into txt files.

This program runs a terminal command to turn the pdfs into text files in a way that keeps the whitespace structure. It requires a program called "pdftotext" from “xpdfreader”. All you need is the path of the pdftotext program and the directory
of all the files that need to be converted. 

### The third file to run is the whitespace_table_extract.ipynb which iterates through every txt file to extract all the tax rates into one csv.

This is the most complicated program, there is a lot of hard coding for a few countries and some for just a single instance. Titles of the different tax rates were very important to add to the name of the tax rate. They were also difficult to determine algorithmically, so they were determined by looping through all the lines of text that could have been a title, and making a list of titles. I added to this list from trial and errors, sometimes I’d see a rate that looked wrong in the .csv file and added it to the list of titles. 

There are a few things that the code does to turn the text into pure variables. It takes multi rates into just the max value, such as “10/15/20” into “20” and “5 to 10” as just “10”. For a few countries it will turn “-” into 0, or whitespace depending on how we interpret the tax rate by manually looking at the full text of the pdf file.  It was possible for one tax rate to have multiple titles, so there would be a stacking of titles, such as “Withholding (Dividends) (Resident) Individual 10”. There at most would be up to 3 titles for one tax rate. Also, any title that has an associated footnote such as “(a)”, will be pushed on to any rate that has it. 

In 2010 there was a change in whitespace, one page would have a lot less leading whitespace than the next page. So I used some standard points of the second page to remove the leading whitespace, and when that wasn’t possible I simply hardcoded certain countries. 
