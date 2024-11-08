from django.views.generic import TemplateView

# Create your views here.


class IndexPageView(TemplateView):
    template_name = 'baseitem/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['content'] = 'Baks Hi-Tech store'
        return context


class AboutPageView(TemplateView):
    template_name = 'baseitem/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Страница о сайте'
        context['content'] = 'Данный сайт создан потому, что был создан.'
        context['text_on_page'] = 'Куча странного текста, которая будет дополнена'
        return context



# def index(request):
#
#     context = {
#         'title': 'Главная страница',
#         'content': 'Baks Hi-Tech store',
#
#     }
#     return render(request, 'baseitem/index.html', context)


# def about(request):
#
#     context = {
#         'title': 'Страница о сайте',
#         'content': 'Данный сайт создан потому, что был создан.',
#         'text_on_page': 'куча странного текста',
#
#     }
#     return render(request, 'baseitem/about.html', context)
