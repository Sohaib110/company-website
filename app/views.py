from django.shortcuts import render
from app.models import GeneralInfo

from django.db import connection
def write_sql_queries_to_file(file_path):
    with open(file_path, 'w') as file:
        queries = connection.queries
        for query in queries:
            sql= query['sql']
            file.write(f"{sql}\n")


# Create your views here.
def index(request):
    
    
    
    
    #all_records = GeneralInfo.objects.all()
    #print(all_records)
    
    
    
    
    
    
    file_path = 'sql_queries.txt'
    write_sql_queries_to_file(file_path)
    context={}
    return render(request, 'index.html', context) 
    