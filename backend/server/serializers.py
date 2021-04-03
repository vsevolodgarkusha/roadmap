from rest_framework.serializers import ModelSerializer

from .models import Module, Topic, SubTopic


class ModuleSerializer(ModelSerializer):

    class Meta:
        model = Module
        fields = '__all__'


class TopicSerializer(ModelSerializer):

    class Meta:
        model = Topic
        fields = '__all__'


class SubTopicSerializer(ModelSerializer):

    class Meta:
        model = SubTopic
        fields = '__all__'

