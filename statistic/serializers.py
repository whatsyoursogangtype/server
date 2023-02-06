from rest_framework import serializers


class StatisticSerializer(serializers.Serializer):
    stat1 = serializers.CharField()
    stat2 = serializers.CharField()
    stat3 = serializers.CharField()
