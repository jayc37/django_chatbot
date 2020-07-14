from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests, os
from django.views.decorators.csrf import csrf_exempt
from .models import Conversation
import logging
from src.handledata import handle_response_code

def Home(request):
    return render(request, "justbot/index.html",{})


@csrf_exempt
def get_bot_response(request):
    try:
        if request.method == "GET":
            userText = str(request.GET.get('data',None))
            logging.info(userText)
            message_chatbot = handle_response_code(userText)
            logging.error('#'*10)
        return JsonResponse(message_chatbot)
    except Exception as e:
            logging.error('###############################'*10)
            logging.error('<views.py>' + str(e))
        
        