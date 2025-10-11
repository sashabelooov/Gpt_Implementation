from django.contrib import admin
from .models import Chat, Message
from .models import CustomUser  


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'username', 'phone', 'is_staff', 'created_at')
    list_filter = ('is_staff', 'is_superuser', 'created_at')
    search_fields = ('email', 'username', 'phone')
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('Asosiy maʼlumotlar', {
            'fields': ('email', 'username', 'first_name', 'last_name', 'phone', 'profile_image')
        }),
        ('Huquqlar', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('Tizim maʼlumotlari', {
            'fields': ('last_login', 'created_at', 'updated_at')
        }),
    )


class MessageInline(admin.TabularInline):
    model = Message
    extra = 0
    readonly_fields = ('created_at',)
    ordering = ('created_at',)


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'created_at', 'updated_at')
    list_filter = ('created_at',)
    search_fields = ('title', 'user__email')
    inlines = [MessageInline]
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'chat', 'sender', 'short_content', 'created_at')
    list_filter = ('sender', 'created_at')
    search_fields = ('content',)
    readonly_fields = ('created_at',)

    def short_content(self, obj):
        return (obj.content[:50] + '...') if len(obj.content) > 50 else obj.content
    short_content.short_description = "Xabar"
