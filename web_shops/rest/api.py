from rest_framework import viewsets
from django.contrib.auth.models import User
from .seriallizers import UserSerializer




#это что бы потмо в урлах черех route отобразить эту страницу
#Вот так
# router = routers.DefaultRouter()
# router.register('users', UserViewSet)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer