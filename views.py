from django.views.generic import TemplateView


class AboutView(TemplateView):
    template_name = 'about.html'
    navitem = 'about'


class HomepageView(TemplateView):
    template_name = 'homepage.html'
    navitem = 'home'


class ThanksView(TemplateView):
    template_name = 'thanks.html'
    navitem = 'thanks'
