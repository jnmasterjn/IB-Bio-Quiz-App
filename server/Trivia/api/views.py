from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["POST"])
def login(request):
    return Response({"login?"})


@api_view(["POST"])
def signup(request):
    return Response({"signup?"})


@api_view(["GET"])
def test_token(request):
    return Response({"token?"})