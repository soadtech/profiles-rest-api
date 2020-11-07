from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API view"""

    def get(self, request, format=None):
        """Return a list of APIVIEWS features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Give you the most control over you application logic',
            'Is mapped manually to URLS'
        ]

        return Response({'message': 'Hellow!', 'an_apiview': an_apiview})
