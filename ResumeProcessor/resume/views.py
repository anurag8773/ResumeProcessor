from rest_framework.response import Response
from rest_framework.decorators import api_view
from .utils import process_resume_file 

@api_view(['POST'])
def extract_resume(request):
    """API view to extract data from the resume."""
    
    if 'resume' not in request.FILES:
        return Response({"detail": "No resume file provided."}, status=400)
    
    file = request.FILES['resume']
    
    extracted_data = process_resume_file(file)

    if isinstance(extracted_data, dict) and "first_name" in extracted_data and "email" in extracted_data and "mobile_number" in extracted_data:
        return Response(extracted_data)
    else:
        return Response({"detail": "Could not extract data from the resume."}, status=400)
