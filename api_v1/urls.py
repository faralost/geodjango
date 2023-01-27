from django.urls import path

from api_v1.views import PlotsListView, CulturesListView, PlotDetailView

app_name = "api_v1"

urlpatterns = [
    path('plots/', PlotsListView.as_view()),
    path('plots/<int:pk>/', PlotDetailView.as_view()),
    path('cultures/', CulturesListView.as_view()),
]
