from rest_framework import serializers


class StatisticSerializer(serializers.Serializer):
    stat1 = serializers.CharField()
    stat2 = serializers.CharField()
    stat3 = serializers.CharField()


class RankSerializer(serializers.Serializer):
    rank1 = serializers.ListField()
    rank2 = serializers.ListField()
    rank3 = serializers.ListField()
    rank4 = serializers.ListField()
    rank5 = serializers.ListField()
    rank6 = serializers.ListField()
    rank7 = serializers.ListField()
    rank8 = serializers.ListField()

# class RankkSerializer(serializers.Serializer):
#     rank = serializers.JSONField()