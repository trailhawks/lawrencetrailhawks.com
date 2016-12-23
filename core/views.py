from django.views.generic import TemplateView


class AboutView(TemplateView):
    template_name = 'about.html'
    navitem = 'about'


class HomepageView(TemplateView):
    template_name = 'homepage.html'
    navitem = 'home'

    def get_context_data(self, **kwargs):
        context = super(HomepageView, self).get_context_data(**kwargs)
        context['use_bootstrap'] = True if self.request.GET.get('bootstrap') else False
        return context


class HumansView(TemplateView):
    content_type = 'text/plain'
    template_name = 'humans.txt'


class StyleGuideView(TemplateView):
    template_name = 'styleguide.html'
    navitem = 'styleguide'


class ThanksView(TemplateView):
    template_name = 'thanks.html'
    navitem = 'thanks'
