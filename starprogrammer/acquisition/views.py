from django.views.generic.base import TemplateView


class LandingView(TemplateView):
    template_name = 'acquisition/landing.html'