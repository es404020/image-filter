from django.urls import path
from . import views
from django.conf import  settings
from django.conf.urls.static import static
#urlConf
urlpatterns= [
    path('',views.say_hello),
    path('take', views.take),
    # static(settings.MEDIA_URL,settings.MEDIA_ROOT)
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)