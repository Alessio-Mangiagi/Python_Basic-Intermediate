from django.urls import path

from . import views

app_name = "chatbot_api"

urlpatterns = [
    path("chat/", views.chat_endpoint, name="chat"),
    path("chat/stream/", views.chat_stream_endpoint, name="chat_stream"),
    path("health/", views.health_check, name="health"),
    path("history/", views.chat_history, name="history"),
]
