from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from .serializers import StatisticSerializer
from user.models import User
from statistics import mode


class StatisticView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = StatisticSerializer

    def retrieve(self, request, *args, **kwargs):
        # request 유저
        user = self.get_object()
        # 총 유저
        total_user = User.objects.all()
        # request 유저의 타입과 전공
        user_type = user.sg_type
        user_major = user.major
        # request유저와 같은 타입인 유저
        user_type_user = total_user.filter(sg_type=user_type)
        # request 유저와 같은 타입이면서 같은 과인 유저
        user_type_major_user = user_type_user.filter(major=user_major)
        # request 유저와 같은 타입인 유저들의 전공의 최빈값
        mode_type = mode(list(user_type_user.values_list('major',flat=True)))

        instance = dict()
        instance['stat1'] = int(user_type_user.count() / total_user.count()*100)
        instance['stat2'] = mode_type
        instance['stat3'] = int(user_type_major_user.count() / user_type_user.count()*100)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
