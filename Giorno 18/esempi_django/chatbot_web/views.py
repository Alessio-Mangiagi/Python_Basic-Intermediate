from django.shortcuts import render


def chat_interface(request):
    """
    View per la pagina principale del chatbot
    """
    return render(request, "chatbot_web/chat.html")
