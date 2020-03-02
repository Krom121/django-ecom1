from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView 
from .forms import ContactForm, SubscribeForm
from blog.models import Post

class HomeView(FormView,TemplateView):
    form_class = ContactForm
    template_name = 'home/index.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.save()
        return super(HomeView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        featured = Post.published.filter(featured=True)[0:3]
        context = super().get_context_data(**kwargs)
        context['title'] = 'Welcome'
        context['featured'] = featured
        return context


class ContactView(FormView):
    form_class = ContactForm
    template_name = 'form/contact.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.save()
        return super(ContactView, self).form_valid(form)