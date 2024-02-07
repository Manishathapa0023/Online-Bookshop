# feedback/views.py
from django.shortcuts import render, redirect
from .forms import FeedbackForm

def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("feedback:thank_you_feedback")
    else:
        form = FeedbackForm()
    return render(request, 'feedback/feedback.html', {'form': form})

def thank_you_feedback(request):
    return render(request, 'feedback/thank_you_feedback.html')
