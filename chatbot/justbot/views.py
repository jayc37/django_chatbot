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
def get_data(request):
    if request.method == "GET":
        userText = str(request.GET.get('data'))
        logging.info(userText)
        message_chatbot = handle_response_code(userText)
        logging.error(type(userText))
    return message_chatbot