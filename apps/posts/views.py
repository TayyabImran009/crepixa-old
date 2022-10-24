from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from django.db import models
from django.db.models import OuterRef, Subquery
from django.http import Http404
from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils.translation import gettext_lazy as _
from django.core.paginator import Paginator

from common.models import BlogPage
from core.functions import Array
from .models import Post, Category, Section


class PostsView(TemplateView):
    template_name = 'posts/posts.html'

    def get_posts(self, request):
        qs = Post.pobs.all()
        limit = request.GET.get('limit', 12)
        page = request.GET.get('page', 1)

        try:
            limit = int(limit)
            page = int(page)
        except (ValueError, TypeError, AttributeError):
            limit = 12
            page = 1

        q = request.GET.get('q')
        c = request.GET.get('c')

        if q:
            vector = SearchVector(Post.title_lang(), weight='A')
            vector += SearchVector(Post.author_full_name_lang(), weight='B')
            vector += SearchVector('text_sections', weight='C')
            query = SearchQuery(q)
            sub = Subquery(
                Section.pobs
                .filter(section_type=Section.TEXT, post=OuterRef('pk'))
                .values(Section.section_text_lang()),
            )
            qs = (
                qs.annotate(text_sections=models.Func(
                    Array(sub), models.Value(' ', output_field=models.TextField()), function='array_to_string'),
                )
                .annotate(rank=SearchRank(vector, query))
                .filter(rank__gte=0.1)
                .order_by('rank', 'ordering_number', '-posted_at')
            )

        if c:
            qs = qs.filter(categories=c)

        if not q:
            qs = qs.order_by('ordering_number', '-posted_at')

        paginator = Paginator(qs, limit)
        return paginator.get_page(page)

    def get_context_data(self, **kwargs):
        context = super(PostsView, self).get_context_data(**kwargs)

        context['page_title'] = _('Blog')
        context['meta_description'] = _('''meta description''')

        context['blog_page'] = BlogPage.objects.first()
        context['page_obj'] = self.get_posts(self.request)
        context['categories'] = Category.pobs.all()
        return context

    def get(self, request, *args, **kwargs):
        is_ajax = request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
        if is_ajax:
            return render(request, 'posts/includes/posts.html', context=dict(page_obj=self.get_posts(request)))

        return super(PostsView, self).get(request, *args, **kwargs)


class PostView(TemplateView):
    template_name = 'posts/post.html'

    def get_context_data(self, **kwargs):
        context = super(PostView, self).get_context_data(**kwargs)

        post = Post.pobs.filter(url_slug=kwargs.get('slug')).prefetch_related('categories').first()
        if not post:
            raise Http404

        context['page_title'] = post.title
        context['meta_description'] = _('''meta description''')

        context['post'] = post
        context['Section'] = Section
        context['sections'] = Section.pobs.filter(post=post.id).all()
        context['posts'] = Post.pobs.exclude(id=post.id).prefetch_related('categories')[:6]
        return context
