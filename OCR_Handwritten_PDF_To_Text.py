import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from pdf2image import convert_from_path
import re

# Function to perform OCR on the entire PDF
def ocr_entire_pdf(input_pdf):
    images = convert_from_path(input_pdf)
    full_text = ""
    for image in images:
        full_text += pytesseract.image_to_string(image) + "\n"
    return full_text

# Function to split text by a custom marker and extract lecture titles
def split_text_and_extract_titles(full_text, marker_pattern):
    lectures = []
    matches = re.finditer(marker_pattern, full_text)
    
    last_end = 0
    for match in matches:
        title = match.group(1).strip()
        start = match.start()
        
        if last_end != 0:  # Skip the first match because it has no preceding content
            lectures[-1]["content"] = full_text[last_end:start].strip()
        
        lectures.append({"title": title, "content": ""})
        last_end = match.end()
    
    # Capture the content of the last lecture
    if lectures:
        lectures[-1]["content"] = full_text[last_end:].strip()
    
    return lectures

# Example workflow
input_pdf = r"C:\Users\devas\Sync\Test notes test.pdf"

# Step 1: Perform OCR
full_text = ocr_entire_pdf(input_pdf)

# Step 2: Define the marker pattern (using regex to capture the lecture title)
marker_pattern = r"### Lecture Start: (.*?) ###"

# Step 3: Split the text based on the marker and extract titles
lectures = split_text_and_extract_titles(full_text, marker_pattern)

# Step 4: Save each lecture into a separate text file with the lecture title as the filename
for lecture in lectures:
    # Create a safe filename by replacing spaces and other characters
    #lecture_filename = re.sub(r'[^\w\s-]', '', lecture["title"]).strip().replace(" ", "_") + ".txt"
    lecture_filename = r"C:\Users\devas\Sync\\test.txt"
    
    with open(lecture_filename, "w") as lecture_file:
        lecture_file.write(lecture["content"])