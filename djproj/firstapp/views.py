from django.views.generic import ListView, DetailView
from .models import Article
from datetime import datetime


class ArticlesList(ListView):
    model = Article
    template_name = 'articles.html'
    context_object_name = 'articles'
    queryset = Article.objects.order_by('-datetime')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context[
            'value1'] = None
        return context


class ArticleDetail(DetailView):
    model = Article
    template_name = 'article.html'
    context_object_name = 'article'