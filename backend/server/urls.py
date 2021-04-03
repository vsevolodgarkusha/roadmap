from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .api import ModuleViewSet, TopicViewSet, SubTopicViewSet


router = DefaultRouter()
router.register('module', ModuleViewSet)
router.register('topic', TopicViewSet)
router.register('subtopic', SubTopicViewSet)


urlpatterns = [
    path('api/', include(router.urls))
]
