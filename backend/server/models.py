from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.conf import settings


class TimeStampedModel(models.Model):

    class Meta:

        abstract = True
        ordering = ('-created_at', )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ItemBase(TimeStampedModel):
    class Meta:
        abstract = True

    title = models.CharField(max_length=150)

    def str(self):
        return self.title


class Materials(models.Model):

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id')


class Text(ItemBase):

    content = models.TextField(blank=True)


# Деревом файлов потом займусь
class File(ItemBase):

    file = models.FileField(upload_to='static', null=True, blank=True)


# Деревом файлов потом займусь
class Image(ItemBase):

    file = models.ImageField(upload_to='static', null=True, blank=True)


# Деревом файлов потом займусь
class Video(ItemBase):

    url = models.URLField()


class Block(TimeStampedModel):

    class Meta:

        abstract = True
        ordering = ('position_y', )

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
    next_block = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    materials = models.ManyToManyField(Materials, blank=True, related_name='block')


class Module(Block):

    pass


class Topic(Block):

    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='topics')


class SubTopic(Block):

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='sub_topics')
