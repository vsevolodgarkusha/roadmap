from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.conf import settings


class TimeStampedModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ('-created_at', )


class Block(TimeStampedModel):

    importance_choices = (
        (0, 'As an introduction'),
        (1, 'Learn anytime'),
        (2, 'Alternative option: pick this or recommended'),
        (3, 'Recommended')
    )

    title = models.CharField(max_length=150)
    short_description = models.CharField(max_length=200, blank=True)
    completed = models.BooleanField(default=False)
    importance = models.PositiveSmallIntegerField(default=3, choices=importance_choices)
    position_x = models.IntegerField(blank=True, null=True)
    position_y = models.IntegerField(blank=True, null=True)
    previous_block = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        abstract = True
        ordering = ('position_y', )


class Module(Block):
    pass


class Topic(Block):

    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='topics')


class SubTopic(Block):

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='sub_topics')
