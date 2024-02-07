from django.contrib import admin

# Register your models here.
from feedback.models import Feedback


class FeedbackList(admin.ModelAdmin):
	list_display = ['name', 'email', 'message']
	class Meta:
		Model = Feedback

admin.site.register(Feedback, FeedbackList)
