#* Library Imports
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from django_eventstream import send_event
import time
import os

#* Relative imports
from .common_ws_utils import WSUtils
from .utils.keras.keras_model import KerasModel

#* Global variable
KERAS_OBJECT = KerasModel()
class HttpDemoClass(APIView):
    
    def get(self, request, format=None):
        
        user_name  = request.query_params.get('user_name') #get Username
        
        if user_name == 'A':
            state = -1
        elif user_name == 'B':
            state = 0
        elif user_name == 'C':
            state = 1
        else:
            state = 2
        
        return Response({"state":state},status=200)
    
class UpdateClass(APIView):

    def get(self, request):
        user_name  = request.query_params.get('user_name') #get Username
            
        ws_obj = WSUtils()
        
        time.sleep(3)
        ws_obj.send_message(username=user_name,message=1)
        time.sleep(5)
        ws_obj.send_message(username=user_name,message=2)
        
        time.sleep(1)
        ws_obj.send_message(username=user_name,message=1)
        
        time.sleep(2)
        ws_obj.send_message(username=user_name,message=2)
        
        
        return HttpResponse("<h2>Status: Complete</h2>")
    
class SendEvent(APIView):
    
    def get(self, request):
        user = request.query_params.get('user')
        if not user: user = 0
        for i in range(10):
            send_event(f"{user}", 'message', {'text': f'hello world {i}'})
            time.sleep(1)
        
        return HttpResponse("<h2>Status: Complete</h2>")
    
class ExecutePipeline(APIView):
    
    def get(self, request):
        user = request.query_params.get('user')
        # epochs = request.query_params.get('epochs', 150)
        # batch_size = request.query_params.get('batch_size', 10)
        
        KERAS_OBJECT.executePipeline(user=user) #, epoch=epochs, batch_size=batch_size)
        
        return HttpResponse("<h2>Status: Complete</h2>")