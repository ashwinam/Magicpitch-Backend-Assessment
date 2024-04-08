from djoser.views import UserViewSet as BaseUserViewSet
from django.contrib.auth import get_user_model

from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status

from .serializers import UserSerializer

User = get_user_model()


class UserViewSet(BaseUserViewSet):

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({'id': serializer.data.get('id'), 'message': 'User Registered Successfully.'}, status=status.HTTP_201_CREATED, headers=headers)

    @action(["get"], detail=False)  # return the current user details
    def me(self, request, *args, **kwargs):
        self.get_object = self.get_instance
        if request.method == "GET":
            return self.retrieve(request, *args, **kwargs)

    @action(['get'], detail=False)  # for referral endpoint
    def referral(self, request, *args, **kwargs):
        queryset = User.objects.filter(referred_by=request.user)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = UserSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
