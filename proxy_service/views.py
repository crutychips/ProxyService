import json
from django.conf import settings
import redis
import httpx

from django.http import JsonResponse, HttpResponse

def proxy_view(request):
    redis_client = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0)
    
    # Load routing rules from Redis
    rules = json.loads(redis_client.get('routing_rules'))
    
    # Find the target URL using provided routing rules
    target_url = rules.get(request.path, "http://default-legacy-service-url.com")
    
    # Forward the request to target service and return response
    response = httpx.request(request.method, target_url, data=request.body)
    
    return HttpResponse(content=response.content, status=response.status_code)
