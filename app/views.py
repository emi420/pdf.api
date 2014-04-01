import requests
from django.shortcuts import render_to_response
from django_xhtml2pdf.utils import generate_pdf
from app import settings

def html2pdf(request):

   url = request.GET['url']
   r = requests.get(url, verify=False)
   resp = HttpResponse(content_type='application/pdf')   
   context = {}
   context['html'] = r.text
   result = generate_pdf('blank.html', file_object=resp, context=context)
   
   render_to_response(result, content_type="application/pdf")
