from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET', 'PUT', 'DELETE', 'POST'])
def index(request):
    try:
        calculate = eval(request.POST['query'])
        return Response({'status':'success','data':{'query': request.POST['query'], 'result':calculate}})
    except Exception as e:
        return Response({'status':'error', 'message':str(e)})