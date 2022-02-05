from rest_framework import filters, status
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from posts.models import Follow
from .serializers import FollowListSerializer, FollowPostSerializer


class FollowView(ListCreateAPIView):
    authentication_classes = (JWTAuthentication,)
    serializer_class = FollowListSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        user = self.request.user
        return Follow.objects.filter(user__username=user.username)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        is_empty = len(request.data) != 0
        if is_empty and request.data['following'] != request.user.username:
            context = {
                'request': self.request,
            }
            serializer = FollowPostSerializer(data=request.data,
                                              context=context)
            if serializer.is_valid(raise_exception=True):
                serializer.save(user=request.user)
                return Response(serializer.data,
                                status=status.HTTP_201_CREATED)

            return Response(serializer.data,
                            status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_400_BAD_REQUEST)
