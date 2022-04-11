from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Profile, Project, Quote


class ProjectView(ListView):

    template_name = "index.html"
    model = Project
    context_object_name = "projects"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ProjectView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context["profile"] = Profile.objects.all()
        return context


class ProjectDetailView(DetailView):

    model = Project
    template_name = "project.html"


class QuoteView(ListView):

    template_name = "quotes.html"
    model = Quote
    context_object_name = "quotes"
