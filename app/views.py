import requests
from decorators import HttpOptionsDecorator, VoolksAPIAuthRequired
from django.http import HttpResponse
from django.template import RequestContext
from django.template.loader import render_to_string
from django_xhtml2pdf.utils import generate_pdf
from app import settings
import StringIO
import ho.pisa as pisa 

@HttpOptionsDecorator
@VoolksAPIAuthRequired
def html2pdf(request):

    url = request.GET['url']
    r = requests.get(url, verify=False)

    html = render_to_string('blank.html', {'html': r.text},
                            context_instance=RequestContext(request))
    result = StringIO.StringIO()
    pdf = pisa.pisaDocument(
            StringIO.StringIO(html.encode('ascii', 'xmlcharrefreplace')),
            result, link_callback=link_callback)
    return HttpResponse(result.getvalue(), mimetype='application/pdf')


def link_callback(uri, rel):
    if uri.find('http') != -1:
        return uri
    return os.path.join(settings.MEDIA_ROOT, uri.replace(settings.MEDIA_URL, ""))
