from django.contrib import admin

from .models import  Module, Topic, SubTopic


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):

    list_display = ('title', 'importance', 'previous_block')


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):

    list_display = ('module', 'title', 'previous_block')
    list_filter = ('module', )


@admin.register(SubTopic)
class SubTopicAdmin(admin.ModelAdmin):

    list_display = ('topic', 'title', 'previous_block')
    list_filter = ('topic', )
