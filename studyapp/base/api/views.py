from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET']) # Only requests allowed e.g 'GET', 'PUT', 'POST'
def get_routes(request): # A view that shows us all the routes in our API
    routes = [
        'GET /api',
        'GET /api/rooms',
        'GET /api/rooms/:id'
    ]
    return Response(routes)
