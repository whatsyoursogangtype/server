from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from .serializers import StatisticSerializer, RankSerializer
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

class RankView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = RankSerializer

    def retrieve(self, request, *args, **kwargs):
        type_list = list(User.objects.all().values_list('sg_type',flat=True))
        types = {'커피브레이크','로욜라','X관랩실','취업지원팀','알바트로스탑','경의선숲길','빨간잠망경','서강포차'}
        
        instance = dict()
        for i in range(1,9):
            val_name = 'rank{}'.format(i)
            if not type_list:
                instance[val_name] = [None, None]
                continue
            mode_type = mode(type_list)
            mode_ratio = round(User.objects.filter(sg_type=mode_type).count()/User.objects.all().count()*100,2)
            instance[val_name] = [mode_type, mode_ratio]
            for j in type_list: 
                if j == mode_type: type_list.remove(mode_type)

        serializer = self.get_serializer(instance)
        return Response(serializer.data)
