import PyPDF2
import re

def extract_pages(pdf_path, start_page, end_page):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page_num in range(start_page - 1, end_page):  # Adjusting for zero-based index
            page = reader.pages[page_num]
            text += page.extract_text()
        return text

def save_text_to_file(text, filename):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)

def remove_page_numbers(text):
    # Remove common page number formats (customize as needed)
    text = re.sub(r'\d+\s*$', '', text)  # Page numbers at end of line
    return text

# Usage example
pdf_path = '/Users/markhuber/Downloads/Outlive.pdf'
# chunk_text_1 = extract_pages(pdf_path, 116, 144)  # Extract pages 1 to 50
# chunk_text_2 = extract_pages(pdf_path, 145, 182)  # Extract pages 1 to 50
# chunk_text_3 = extract_pages(pdf_path, 183, 212)  # Extract pages 1 to 50
# chunk_text = remove_page_numbers(chunk_text)

chunk_text_1 = extract_pages(pdf_path, 356, 384)  # Extract pages 1 to 50
chunk_text_2 = extract_pages(pdf_path, 385, 420)  # Extract pages 1 to 50
# chunk_text_3 = extract_pages(pdf_path, 314, 420)  # Extract pages 1 to 50
# print(chunk_text)

save_text_to_file(chunk_text_1, "book/extracted_text_chapter_16.txt")
save_text_to_file(chunk_text_2, "book/extracted_text_chapter_17.txt")
# save_text_to_file(chunk_text_3, "extracted_text_chapter_15.txt")
key = "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"
os.environ['OPENAI_API_KEY'] = key