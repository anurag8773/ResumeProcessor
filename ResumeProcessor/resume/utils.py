import re
import PyPDF2
import docx

def extract_text_from_file(file):

    file_extension = file.name.split('.')[-1].lower()
    
    if file_extension == 'pdf':
        return extract_text_from_pdf(file)
    elif file_extension == 'docx':
        return extract_text_from_docx(file)
    else:
        return ""

def extract_text_from_pdf(file):

    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() or ""
    return text

def extract_text_from_docx(file):

    doc = docx.Document(file)
    text = ""
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text

def clean_text(text):

    text = text.replace('\n', ' ').replace('\r', '')
    return text

def extract_name(text):

    match = re.search(r'^[A-Za-z]+', text)
    return match.group(0) if match else None

def extract_email(text):

    match = re.search(r'[\w\.-]+@[\w\.-]+', text)
    return match.group(0) if match else None

def extract_phone(text):

    match = re.search(r'(\+?\d{1,2}\s?)?(\(?\d{1,4}\)?[\s\-]?)?[\d\s\-]{10,}', text)
    return match.group(0) if match else None

def process_resume_file(file):

    text_content = extract_text_from_file(file)  
    text_content = clean_text(text_content)  

    first_name_last_name = extract_name(text_content)
    email = extract_email(text_content)
    phone = extract_phone(text_content)

    if first_name_last_name and email and phone:
        return {
            "first_name": first_name_last_name.split()[0], 
            "email": email,
            "mobile_number": phone,
        }
    
    return {"detail": "Could not extract data from the resume."}
