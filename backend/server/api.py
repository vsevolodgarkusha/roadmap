from rest_framework.viewsets import ModelViewSet

from .models import Module, Topic, SubTopic
from .serializers import ModuleSerializer, TopicSerializer, SubTopicSerializer


class ModuleViewSet(ModelViewSet):

    queryset = Module.objects.all()
    serializer_class = ModuleSerializer


class TopicViewSet(ModelViewSet):

    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class SubTopicViewSet(ModelViewSet):

    queryset = SubTopic.objects.all()
    serializer_class = SubTopicSerializer

