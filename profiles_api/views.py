from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    '''Test API View'''

    def get(self, request, format=None):
        """Return API Features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a tradional Django view',
            'Gives you the most control over your application logic',
            'Is mapped manually to urls'
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})