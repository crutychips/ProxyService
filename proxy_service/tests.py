from django.test import TestCase, Client

class ProxyTest(TestCase):
    def test_proxy_view(self):
        client = Client()
        response = client.get('/endpoint1')
        self.assertEqual(response.status_code, 200)
