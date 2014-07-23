import requests
from decorators import HttpOptionsDecorator, VoolksAPIAuthRequired
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.template.loader import render_to_string
from django_xhtml2pdf.utils import generate_pdf
from app import settings
from os import urandom
import json
import StringIO
import ho.pisa as pisa 

@HttpOptionsDecorator
@VoolksAPIAuthRequired
def xhtml2pdf(request):

    url = ""
    htmlsrc = ""
    
    if request.META["REQUEST_METHOD"] == "POST":
        htmlsrc = request.POST.items()[0][0]
    else:
        request.GET['url']
        r = requests.get(url, verify=False)
        htmlsrc = r.text

    html = render_to_string('blank.html', {'html': htmlsrc},
                            context_instance=RequestContext(request))
            
    if request.META["REQUEST_METHOD"] == "POST":
        filename = str(urandom(16).encode('hex')) + ".pdf"
        result = open('/var/www/pdf.voolks.com/media/' + filename, 'wb') 
        pdf = pisa.pisaDocument(StringIO.StringIO(
            html.encode("UTF-8")), result)
        result.close()
        url = "/media/" + filename
        return HttpResponse(json.dumps({'url': url}), content_type="application/json"); 
    else:
        result = StringIO.StringIO()
        pdf = pisa.pisaDocument(
                StringIO.StringIO(html.encode('ascii', 'xmlcharrefreplace')),
                result, link_callback=link_callback)
        return HttpResponse(result.getvalue(), mimetype='application/pdf')


def link_callback(uri, rel):
    if uri.find('http') != -1:
        return uri
    return os.path.join(settings.MEDIA_ROOT, uri.replace(settings.MEDIA_URL, ""))
