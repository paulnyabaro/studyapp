from django.http import JsonResponse


def get_routes(request): # A view that shows us all the routes in our API
    routes = [
        'GET /api',
        'GET /api/rooms',
        'GET /api/rooms/:id'
    ]
    return JsonResponse(routes, safe=False)
