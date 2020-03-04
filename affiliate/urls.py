from django.urls import path
from affiliate.views import HomeView, ContactView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contact-us/', ContactView.as_view(), name='contact-us'),   
]