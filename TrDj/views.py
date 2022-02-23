""" 
    To render HTML pages 
"""
import random
from django.http import HttpResponse



def home_view(request):
    """
    take in a request (Django sends request)
    Return HTML as a response (We pick to return the response)
    """
    
    name = "Justin"
    number = random.randint(10,1233123)

    # Django Database



    # Django templates

    H1_STRING = f"""
    <h1>Hello {name} - {number}!</h1>
    """
    P_STRING = f"""
    <p>Hello {name} - {number}!</p>
    """


    HTML_STRING = H1_STRING + P_STRING
    return HttpResponse(HTML_STRING)