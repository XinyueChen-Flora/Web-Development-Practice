from email import message
import json
import os
from django.http import HttpResponse, JsonResponse
from django.conf import settings

def login(request):
    try:
        if request.method != "POST":
            raise Exception("error requestion method")

        data = request.body.decode()
        data = json.loads(data)
        print(data)

        nickname = data.get("nickname", "")
        if nickname == "":
            raise Exception("lack args")
        
        auth = nickname
        return JsonResponse({"status":1, "auth": auth})
    except Exception as e:
        return JsonResponse({"status":0, "message": str(e)})