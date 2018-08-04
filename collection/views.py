from django.views import generic
from .models import Category
from .forms import FeedbackForm
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'collection/index.html'
    context_object_name = 'all_categories'

    def get_queryset(self):
        return Category.objects.all()


class DetailView(generic.DeleteView):
    model = Category
    template_name = 'collection/detail.html'


def feedback_form(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, 'collection/thanx.html')

    else:
        form = FeedbackForm()
    return render(request, 'collection/feedback_form.html', {'form': form})

