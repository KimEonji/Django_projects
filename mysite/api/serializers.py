from rest_framework import serializers
from .models import CafeInfo, CafeKeyword

class cafe_info_Serializer(serializers.ModelSerializer):
    class Meta:
        model = CafeInfo
        fields=('중심장소','카페명','카페타입','별점','리뷰수','주소','영업시간','행정동')

class cafe_keyword_Serializer(serializers.ModelSerializer):
    class Meta:
        model = CafeKeyword
        fields=('카페명','키워드1','키워드2','키워드3')
