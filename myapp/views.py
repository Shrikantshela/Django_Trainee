from django.http import JsonResponse
from django.contrib.auth.models import User

def create_user_view(request):
    username = "testuser"  # Change as needed

    if not User.objects.filter(username=username).exists():
        user = User.objects.create(username=username)
        return JsonResponse({"message": "User created successfully!"})
    else:
        return JsonResponse({"message": "User already exists!"})

