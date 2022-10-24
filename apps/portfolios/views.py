from django.core.paginator import Paginator
from django.db.models import Q
from django.http import Http404
from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils.translation import gettext_lazy as _

from common.models import PortfolioPage
from .models import Portfolio, Category, SubCategory, Tag, PortfolioFile


class PortfoliosView(TemplateView):
    template_name = 'portfolios/portfolios.html'

    def get_portfolios(self, request):
        qs = Portfolio.pobs.all()
        limit = request.GET.get('limit', 6)
        page = request.GET.get('page', 1)

        try:
            limit = int(limit)
            page = int(page)
        except (ValueError, TypeError, AttributeError):
            limit = 12
            page = 1

        categories = request.GET.getlist('c')
        sub_categories = request.GET.getlist('sc')
        tags = request.GET.getlist('t')

        if categories:
            filters = Q()
            for c in categories:
                if c.isnumeric():
                    filters |= Q(categories__id=c)
            qs = qs.filter(filters)

        if sub_categories:
            filters = Q()
            for sc in sub_categories:
                if sc.isnumeric():
                    filters |= Q(sub_categories__id=sc)
            qs = qs.filter(filters)

        if tags:
            filters = Q()
            for t in tags:
                if t.isnumeric():
                    filters |= Q(tags__id=t)
            qs = qs.filter(filters)

        paginator = Paginator(qs.distinct().order_by('ordering_number', '-project_date'), limit)
        return paginator.get_page(page)

    def get_context_data(self, **kwargs):
        context = super(PortfoliosView, self).get_context_data(**kwargs)

        context['page_title'] = _('Blog')
        context['meta_description'] = _('''meta description''')

        context['page_obj'] = self.get_portfolios(self.request)

        categories = Category.pobs.all()
        selected_categories = {int(c) for c in self.request.GET.getlist('c') if c.isnumeric()}
        self.set_selected(categories, selected_categories)

        sub_categories = SubCategory.pobs.all()
        selected_sub_categories = {int(sc) for sc in self.request.GET.getlist('sc') if sc.isnumeric()}
        self.set_selected(sub_categories, selected_sub_categories)

        tags = Tag.pobs.all()
        selected_tags = {int(t) for t in self.request.GET.getlist('t') if t.isnumeric()}
        self.set_selected(tags, selected_tags)

        context['categories'] = categories
        context['sub_categories'] = sub_categories
        context['tags'] = tags
        context['portfolio_page'] = PortfolioPage.objects.first()
        return context

    @staticmethod
    def set_selected(items, selected_items):
        for item in items:
            item.selected = False
            if item.pk in selected_items:
                item.selected = True

    def get(self, request, *args, **kwargs):
        is_ajax = request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
        if is_ajax:
            return render(
                request,
                'portfolios/includes/portfolios.html',
                context=dict(page_obj=self.get_portfolios(request)),
            )

        return super(PortfoliosView, self).get(request, *args, **kwargs)


class PortfolioView(TemplateView):
    template_name = 'portfolios/portfolio.html'

    def get_context_data(self, **kwargs):
        context = super(PortfolioView, self).get_context_data(**kwargs)

        portfolio = Portfolio.pobs.filter(url_slug=kwargs.get('slug')).first()
        if not portfolio:
            raise Http404

        context['page_title'] = portfolio.title
        context['meta_description'] = _('''meta description''')

        context['portfolio'] = portfolio
        context['categories'] = portfolio.categories.all()
        context['sub_categories'] = portfolio.sub_categories.all()
        context['tags'] = portfolio.tags.all()
        context['portfolio_files'] = PortfolioFile.pobs.filter(portfolio=portfolio)
        context['portfolio_page'] = PortfolioPage.objects.first()
        return context
