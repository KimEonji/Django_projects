
# Create your views here.

from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def API(request):
    return Response("안녕하세요 api에 오신것을 환영합니다.")
