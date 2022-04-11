from django.urls import path

from .views import ProjectDetailView, ProjectView, QuoteView

urlpatterns = [
    path("", ProjectView.as_view(), name="projects"),
    path("project/<int:pk>/", ProjectDetailView.as_view(), name="detail"),
    path("quotes/", QuoteView.as_view(), name="quotes"),
]
