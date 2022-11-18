from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render

from xhtml2pdf import pisa

def render_to_pdf(template_src, context_dict):
    """
    renders a document to pdf using a template
    """
    if context_dict is None:
        context_dict = {}
    template = get_template(template_src)
    html = template.render(context_dict)
    # turkishchars=["ı","ş","ğ"]
    # englishchars=[",","s","g"]
    htmls = html.replace("ı","i").replace("ş","s").replace("İ","I").replace("ğ","g").replace("Ğ","G").replace("Ş","S")
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(htmls.encode("UTF-8")), result,
                            encoding='UTF-8')
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None 