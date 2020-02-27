from django.urls import path
from affiliate.views import HomeView


urlpatterns = [
    path('', HomeView.as_view())
]