from django.views import generic
from django.views.decorators.csrf import csrf_exempt
import json
import requests
import random
from django.utils.decorators import method_decorator
from django.http.response import HttpResponse
from django.shortcuts import render


def chat(request):
    context = {}
    return render(request, 'bot/chatbot.html', context)


def respond_to_websockets(message):
    jokes = {
     'age' : ["""I am your Assistant, You consider me same age of you.""",
                """Same age as of you."""],
     'who':    ["""Hello! I'm Elth. I'm your personal assistant.""",
                """  Hello! I'm Elth. I'm your personal assistant."""],
     'gender':   ["""Same as of you""",
                """I am Female."""] 
     }  

    result_message = {
        'type': 'text'
    }
    if 'age' in message['text']:
        result_message['text'] = random.choice(jokes['age'])
    
    elif 'who' in message['text']:
        result_message['text'] = random.choice(jokes['who'])
    
    elif 'gender' in message['text']:
        result_message['text'] = random.choice(jokes['gender'])

    elif message['text'] in ['hi', 'hey', 'hello']:
        result_message['text'] = "Hello to you too! Hello! I'm Elth. I'm your personal assistant."
    else:
        result_message['text'] = "I don't know any responses for that."

    return result_message
    
