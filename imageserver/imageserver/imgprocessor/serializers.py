from rest_framework import serializers
from imgprocessor.models import ClientImageRequest, TextImageResponse


class ClientImageRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientImageRequest
        fields = ['id', 'title', 'content', 'createdAt']

# 로컬에서 사진을 HTTP 응답으로 반환해 주는 경우 이 serializer 를 사용할 필요가 없음. 
# 나중에 원격 스토리지 사용 가능해지면, 그 때 url 과 함께 유저가 적은 title, content 등 도 같이 
# JSON 형식으로 해서 반환해 주는 걸로. 
# ex. {"imageUrl" : "www.aaaaa.com/bbb.jpg", "title" : "my awesome title", "content" : "my sample content"}
class TextImageResponseSerializer(serializers.ModelSerializer):
    imageUrl = serializers.SerializerMethodField('get_image_url')

    class Meta:
        model = TextImageResponse
        fields = ['id', 'title', 'content', 'createdAt', 'imageUrl']

    def get_image_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.image.url)