from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('openai/', views.query_view, name='query'), 
]

websocket_urlpatterns = [
   re_path(r'listen', consumers.TranscriptConsumer.as_asgi()),
]