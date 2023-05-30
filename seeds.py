from models import Author, Qoutes
import connect
import json
from datetime import datetime
from dateutil import parser

with open('authors.json', 'r', encoding= 'utf-8') as f:
    authors = json.load(f)

with open('quotes.json', 'r', encoding= 'utf-8') as f:
    quotes = json.load(f) 


for i in authors:
   parser.parse(i["born_date"]).date()
   s = datetime.strptime(i["born_date"], '%B %d, %Y')
   Author(fullname=i["fullname"], born_date= s 
        , born_location=i["born_location"], description=i["description"]).save()
    
 
    
for i in quotes:
    author = Author.objects(fullname=i['author']).first()
    if author:
        Qoutes(tags=i['tags'], authors=author, quote=i['quote']).save()
        
    


