from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *

class AddStudentView(APIView):

    serializer_class = AddStudentSerializer
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)