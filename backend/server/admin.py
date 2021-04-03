from django.contrib import admin

from .models import  Module, Topic, SubTopic, Materials


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):

    list_display = ('title', 'importance', 'next_block')


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):

    list_display = ('module', 'title', 'next_block')
    list_filter = ('module', )


@admin.register(SubTopic)
class SubTopicAdmin(admin.ModelAdmin):

    list_display = ('topic', 'title', 'next_block')
    list_filter = ('topic', )


@admin.register(Materials)
class MaterialsAdmin(admin.ModelAdmin):

    list_display = ('item', )
