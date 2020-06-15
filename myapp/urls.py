from django.urls import path
from .views import *


urlpatterns = [
    path('', homeView, name="home"),
    path('product-sofa/', sofaView, name="product-sofa"),
    path('product-curtain/', curtainView, name="product-curtain"),
    path('about-us/', aboutUsView, name="about-us"),
    path('contact-us/', contactUsView, name="contact-us"),
    #path('upload/', uploadView, name="upload"),
]
