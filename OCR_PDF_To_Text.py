import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from pdf2image import convert_from_path
import re

import pytesseract
from pdf2image import convert_from_path

def ocr_pdf_to_text(input_pdf, output_txt):
    # Convert PDF pages to images
    images = convert_from_path(input_pdf)
    
    # Initialize a string to hold all the text
    full_text = ""
    
    # Perform OCR on each image
    for image in images:
        text = pytesseract.image_to_string(image)
        full_text += text + "\n"  # Add a newline after each page's text
    
    # Write the extracted text to a text file
    with open(output_txt, "w") as text_file:
        text_file.write(full_text)

# Example usage
input_pdf = r"demo\Test notes test.pdf"  # Path to your PDF file
output_txt = r"demo\test.txt"  # Path to save the output text file

ocr_pdf_to_text(input_pdf, output_txt)
