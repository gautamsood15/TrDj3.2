""" 
    To render HTML pages 
"""
import random
from django.http import HttpResponse

from articles.models import Article

def home_view(request):
    """
    take in a request (Django sends request)
    Return HTML as a response (We pick to return the response)
    """
    
    name = "Justin"     # hard coded    
    random_id = random.randint(1,4)   # pseudo random
    

    # Django Database
    article_obj = Article.objects.get(id=random_id)
    




    # Django Templates

    H1_STRING = f"""
    <h1>Hello {article_obj.title} (id: {article_obj.id})!</h1>
    """
    P_STRING = f"""
    <p>Hello {article_obj.content}!</p>
    """


    HTML_STRING = H1_STRING + P_STRING
    return HttpResponse(HTML_STRING)