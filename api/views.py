from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework import status
from api.models import User, ActivityPeriod
from api.serializers import UserSerializer, ActivityPeriodSerializer



@api_view(['GET', 'POST', 'DELETE'])
def user_list(request):
    if request.method == 'GET' :
        user = User.objects.all()
        user_serializer = UserSerializer(user, many=True)
        return JsonResponse(user_serializer.data, safe=False)

    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = User.objects.all().delete()
        return JsonResponse({'message': '{} Users were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

 
 
@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):
    try:
        user = User.objects.get(pk=pk)
        if request.method == 'GET':
            user_serializer = UserSerializer(user)
            return JsonResponse(user_serializer.data)
        elif request.method == 'PUT':
            user_data = JSONParser().parse(request)
            user_serializer = UserSerializer(user, data=user_data)
            if user_serializer.is_valid():
                user_serializer.save()
                return JsonResponse(user_serializer.data)
            return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        elif request.method == 'DELETE': 
            user.delete() 
            return JsonResponse({'message': 'User was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

    except User.DoesNotExist: 
        return JsonResponse({'message': 'The user does not exist'}, status=status.HTTP_404_NOT_FOUND) 


        
@api_view(['GET'])
def user_activity(request):
    if request.method == 'GET' :
        users = list(User.objects.all())
        useractivity = []
        for user in users:
            acr =  list(ActivityPeriodSerializer(ActivityPeriod.objects.filter(user=user), many=True).data)
            k={}
            k = dict(UserSerializer(user).data)
            k["activity_periods"] = acr
            useractivity.append(k)
    
    return JsonResponse(useractivity, safe=False, json_dumps_params={'indent': 4})
