from django.db import models

# Create your models here.

"""
Below we have inherrited models.Model so that whatever we write in the class can be verified 
that it will work with a database that django already works with. In the class we sepcify all 
the different fields that will become attributes of the Article table (like the CREATE TABLE query in SQL)


"""

class Article(models.Model):
    title = models.TextField()
    content = models.TextField()
    