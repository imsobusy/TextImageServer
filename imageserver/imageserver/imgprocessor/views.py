from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, FileResponse 
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from imgprocessor.models import ClientImageRequest, TextImageResponse
from imgprocessor.serializers import ClientImageRequestSerializer, TextImageResponseSerializer
from PIL import Image, ImageDraw, ImageFont


@csrf_exempt
def request_make_image(request):
    if request.method == 'GET':
        # 여기서 GET 이 하는 역할이 딱히 없는 듯 ... ? 
        imageRequest = ClientImageRequest.objects.all() 
        serializer = ClientImageRequestSerializer(imageRequest, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ClientImageRequestSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            # 성공 응답을 받으면 클라이언트 쪽에서 이미지를 받아오는 요청 날리기 
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

def generate_client_image(request, request_id):
    if request.method == 'GET':
        # read the title and content by image request id
        imageRequest = ClientImageRequest.objects.get(pk=request_id)
        title = imageRequest.title
        content = imageRequest.content
        
        #generate image on local machine
        result = generate_image_locally(title, content)
        if result == True : 
            # change this part to database operation 
            image_path='./sample_response.png'
            image_data = open(image_path, 'rb')
            # 서버 스토리지에 저장한 후 
            # TextImageResponseSerializer data 를 반환하는 식으로 변경할 것. 
            return HttpResponse(image_data, content_type="image/png")
    
        return JsonResponse(serializer.errors, safe=False)


def generate_image_locally(title, content):
    if title == "" or content == "":
        return False 

    else :
        image = Image.open('./imgprocessor/background.png')
        draw = ImageDraw.Draw(image)
        # english_font = ImageFont.truetype("arial.ttf", 48)
        korean_font=ImageFont.truetype("batang.ttc", 48)
        
        # 제목 위치, 색상, 텍스트 지정 
        (x, y) = (200, 50)
        color = 'rgb(0, 0, 0)'
        draw.text((x, y), title, fill=color, font=korean_font) #font 값도 줄 수 있음. 
        
        # 내용 위치, 색상, 텍스트 지정 
        (x, y) = (200, 150)
        color = 'rgb(100, 0, 0)'
        draw.text((x,y), content, fill=color, font=korean_font)
        image.save('sample_response.png', optimize= True, quality=100)
        return True