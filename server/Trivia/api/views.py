from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import UserSerializer
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404


@api_view(["POST"])
def signup(request):

    #linking it with serializer.py, whatever user tries to signup they need to provide 'field' from that doc
    #which includes username, password, and email (id is always there by default)
    serializer = UserSerializer(data = request.data)
 
    #Check if the provided data is valid, then save the validated data to create a new user
    if serializer.is_valid():
        user = serializer.save()

        #make sure password is hashed for security purpose
        user.set_password(request.data['password'])
        user.save()

        #create an authentication token for the new user, 
        #By associating the token with user, token can be used for authenticating API requests made by user.
        token = Token.objects.create(user = user)

        #Return the token and user data (id, username, password, email) in the response
        return Response({"token": token.key, "user": serializer.data} )

    #Return validation errors if the data is invalid
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def login(request):

    #Retrieve user based on provided username
    user = get_object_or_404(User, username = request.data['username'])

    #check if the inserted password is correct, if not return error
    if not user.check_password(request.data['password']):
        return Response ({"error": "Invalid credentials"}, status= status.HTTP_400_BAD_REQUEST) 
    
    #create or retrieve token for the user
    token, created = Token.objects.get_or_create(user=user)

    #serialized user instances 
    serializer = UserSerializer(instance=user)

    #return token and userdata in response
    return Response({"token": token.key, "user": serializer.data} )


from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

@api_view(["POST"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])

def test_token(request):
    return Response("passed for {}".format(request.user.username))


from .models import Quiz
from .serializer import QuizSerializer

@api_view(["GET"])
def get_quiz(request):
    quiz = Quiz.objects.all() #get everything from the quiz object (database)
    serializer = QuizSerializer(quiz, many=True) #serailze the data 
    return Response(serializer.data) #return the serialzed data
