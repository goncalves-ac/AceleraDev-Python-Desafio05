from django.contrib import admin

# Register your models here.
from api.models import Agent, Event, Group, GroupUser, User

class AgentModelEvent(admin.ModelAdmin):
    list_display = ('id', 'name', 'status', 'env', 'version', 'address')


class UserModelEvent(admin.ModelAdmin):
    list_display = ('id', 'name', 'last_login', 'email', 'password')


class EventModelEvent(admin.ModelAdmin):
    list_display = ('id', 'level', 'data', 'arquivado', 'date', 'agent_id', 'user_id')


class GroupModelEvent(admin.ModelAdmin):
    list_display = ('id', 'name')


class GroupUserModelEvent(admin.ModelAdmin):
    list_display = ('id', 'group_id', 'user_id')


admin.site.register(Agent, AgentModelEvent)
admin.site.register(User, UserModelEvent)
admin.site.register(Event, EventModelEvent)
admin.site.register(Group, GroupModelEvent)
admin.site.register(GroupUser, GroupUserModelEvent)