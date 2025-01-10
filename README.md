# ResumeProcessor

A Django project that provides a REST API endpoint to extract the candidate's **first name**, **email**, and **mobile number** from resumes (PDF or Word documents).

## Table of Contents

1. [Project Setup](#project-setup)
2. [Database Configuration](#database-configuration)
3. [API Endpoint](#api-endpoint)
4. [Directory Structure](#directory-structure)
5. [Testing the API](#testing-the-api)
6. [Postman Collection](#postman-collection)
7. [Video Description](#video-description)
8. [Requirements](#requirements)

---

## Project Setup

1. Clone the repository to your local machine:

```bash
git clone https://github.com/anurag8773/ResumeProcessor
cd ResumeProcessor
```

2. Set up a virtual environment (optional but recommended):

```bash
python -m venv venv
```

3. Activate the virtual environment:

   - On macOS/Linux:

   ```bash
   source venv/bin/activate
   ```

   - On Windows:

   ```bash
   venv\Scripts\activate
   ```

4. Install project dependencies:

```bash
pip install -r requirements.txt
```

---

## Database Configuration

1. Ensure that PostgreSQL is installed and running on your local machine.

2. Create a PostgreSQL database for the project:

```bash
psql
CREATE DATABASE resume_processor_db;
CREATE USER your_db_user WITH PASSWORD 'your_db_password';
GRANT ALL PRIVILEGES ON DATABASE resume_processor_db TO your_db_user;
```

3. Update the `DATABASES` section in `ResumeProcessor/settings.py` to use the newly created database:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'resume_processor_db',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

4. Run database migrations:

```bash
python manage.py migrate
```

---

## API Endpoint

### Extract Resume Data

**POST** `/api/extract_resume/`

- **Description**: This endpoint accepts a resume file (PDF or Word document) and returns the candidate’s **first name**, **email**, and **mobile number** extracted from the resume.
- **Request Body**: A file upload containing a PDF or Word resume.

### Example Request (using cURL):

```bash
curl -X POST -F "resume=@/path/to/resume.pdf" http://127.0.0.1:8000/api/extract_resume/
```

### Response Format:

```json
{
    "first_name": "John",
    "email": "john.doe@example.com",
    "mobile_number": "123-456-7890"
}
```

---

## Directory Structure

The project has the following directory structure:

```
ResumeProcessor/
├── manage.py
├── ResumeProcessor/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── resume/
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── services.py
├── requirements.txt
└── README.md
```

- `ResumeProcessor/` - The root directory of the project.
- `manage.py` - A command-line utility for administrative tasks.
- `ResumeProcessor/settings.py` - Configuration settings for the project.
- `resume/` - The app that handles resume processing.
  - `models.py` - The database models, including the `Candidate` model.
  - `serializers.py` - Serializers for converting model instances to JSON.
  - `views.py` - Views for handling requests to extract data from resumes.
  - `services.py` - The business logic for parsing resumes.
  - `urls.py` - URL routing for the app.

---

## Testing the API

### Using Postman:

1. Open Postman and create a new `POST` request.
2. Set the URL to `http://127.0.0.1:8000/api/extract_resume/`.
3. In the "Body" tab, select "form-data", and upload a file under the key `resume`.
4. Click "Send". You should receive a JSON response with the extracted data.

### Using cURL:

You can also test the API using the following cURL command:

```bash
curl -X POST -F "resume=@/path/to/resume.pdf" http://127.0.0.1:8000/api/extract_resume/
```

### Expected Response:

```json
{
    "first_name": "John",
    "email": "john.doe@example.com",
    "mobile_number": "123-456-7890"
}
```

---

## Postman Collection

You can import the following Postman collection to test the API:

1. Download the [Postman collection JSON file](<your-postman-collection-url>).
2. Open Postman.
3. Click on "Import" and upload the downloaded file.
4. Use the imported collection to test the API.

---

## Video Description

For a step-by-step guide, watch the [video description](<your-video-url>), where we walk you through the setup, configuration, and testing of the API.

---

## Requirements

1. Python 3.8 or higher
2. PostgreSQL
3. Django 3.x or higher
4. Django REST Framework
5. Additional libraries: `python-docx`, `pypdf2`, `pdfplumber`

To install the required dependencies, run:

```bash
pip install -r requirements.txt
```

---

## Additional Notes

- You may need to adjust file permissions or configurations depending on your operating system and environment.
- Make sure that the resume file contains the expected data for proper parsing.
