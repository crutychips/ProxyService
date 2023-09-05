from django.apps import AppConfig
from django.conf import settings
import redis
import json
import os

class ProxyServiceConfig(AppConfig):
    name = 'proxy_service'
    label = "PS"
    path = ""

    def ready(self):
        # Ensure we're only executing in development mode
        #if os.environ.get('DJANGO_SETTINGS_MODULE') == 'proxy_service.settings':
        self.load_rules_to_redis()

    def load_rules_to_redis(self):
        # Load the routing rules into Redis when the app starts
        with open('rules.json', 'r') as f:
            rules = json.load(f)
        
        redis_client = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0)
        redis_client.set('routing_rules', json.dumps(rules))
