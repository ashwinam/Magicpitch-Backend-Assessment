from djoser.views import UserViewSet as BaseUserViewSet
from rest_framework.response import Response
from rest_framework import status


class UserViewSet(BaseUserViewSet):

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({'id': serializer.data.get('id'), 'message': 'User Registered Successfully.'}, status=status.HTTP_201_CREATED, headers=headers)
