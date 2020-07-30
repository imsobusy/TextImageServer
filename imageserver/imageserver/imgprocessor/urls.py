from django.urls import path 
from imgprocessor import views 

urlpatterns = [
    path('image/', views.request_make_image), 
    path('image/<int:request_id>', views.generate_client_image)
]