""" 
    To render HTML pages 
"""

from django.http import HttpResponse

HTML_STRING = """
<h1>Hello World</h1>
"""

def home(request):
    """
    take in a request (Django sends request)
    Return HTML as a response (We pick to return the response)
    """
    return HttpResponse(HTML_STRING)