from django.shortcuts import render
from .models import AboutMe, Experience, Education
from django.views.generic import TemplateView
# Create your views here.
def home(request):
    return render(request, 'home.html')

class AboutView(TemplateView):
    template_name = 'about_me.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about_me'] = AboutMe.objects.select_related('user').first()
        context['experience'] = Experience.objects.filter(about_me=context['about_me'])
        context['education'] = Education.objects.filter(about_me=context['about_me'])
        return context


class CredentialsView(TemplateView):
    template_name = 'credentials.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        about_me = AboutMe.objects.select_related('user').first()

        context['about_me'] = about_me
        context['experience'] = Experience.objects.filter(about_me=about_me) if about_me else []
        context['experience'] = Experience.objects.filter(about_me=about_me) if about_me else [] 
        context['social_media'] = about_me.social_media if about_me else {}
        context['skills'] = about_me.skills.all() if about_me else []
        return context











