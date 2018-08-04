from django.contrib import admin
from .models import Category, dresses, Feedback


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'message')
    list_filter = ('username', 'email', 'message')
    search_fields = ('username', 'email', 'message')

    class Meta:
        model = Feedback

        
admin.site.register(Category)
admin.site.register(dresses)
admin.site.register(Feedback)
