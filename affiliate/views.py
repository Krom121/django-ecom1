from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView 
from .forms import ContactForm, SubscribeForm
from blog.models import Post

'''

Class based views where used for the landing page and conact page.
Form view was use to serve the forms conact and subscriber. This allows for
my code to be cleaner, reusable and maintainable.
Template view is used to serve the index.html file.

'''

class HomeView(FormView,TemplateView):
    form_class = SubscribeForm
    template_name = 'home/index.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.save()
        return super(HomeView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        # bring in the featured blogs from the post model
        featured = Post.published.filter(featured=True)[0:3]
        context = super().get_context_data(**kwargs)
        # Change the block title for each page when nessecery
        context['title'] = 'Welcome'
        # Context for the featured blogs
        context['featured'] = featured
        return context


class ContactView(FormView):
    form_class = ContactForm
    template_name = 'layout/forms/contact.html'
    success_url = reverse_lazy('home')
    # Saving the new contacts details
    def form_valid(self, form):
        form.save()
        return super(ContactView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Change the block title for each page when nessecery
        context['title'] = 'Contact Us'
        return context