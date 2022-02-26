from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView
from .serializers import CarSerializer, CommentsListSerializer, UsersSerializer
from .models import Car, Comments, User


class CarsDetailView(ModelViewSet):
    serializer_class = CarSerializer
    queryset = Car.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly, )

    @action(methods=['get', 'post', ], detail=True, serializer_class=CommentsListSerializer)
    def add_comment(self, request, *args, **kwargs):
        car = self.get_object()
        user = request.user
        serializer = CommentsListSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        comment = Comments.objects.create(
            user=user,
            car=car,
            comment=data['comment']
        )
        serializer = CommentsListSerializer(comment).data
        return Response(serializer, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class UsersView(ModelViewSet):
    serializer_class = UsersSerializer
    queryset = User.objects.all()



# class CommentsListView(ModelViewSet):
#     serializer_class = CommentsListSerializer
#     queryset = Comments.objects.all()


