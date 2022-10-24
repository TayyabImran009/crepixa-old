from django.contrib.postgres.search import SearchRank, SearchQuery, SearchVector
from django.db import models
from django.db.models import functions
from django.db.models import Q, OuterRef, Subquery
from django.http import Http404
from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils.translation import gettext_lazy as _
from django.core.paginator import Paginator

from common.models import StorePage
from core.functions import Array
from .models import Store, Category, SubCategory, Tag, StoreFeature


class StoresView(TemplateView):
    template_name = 'stores/stores.html'

    def get_stores(self, request):
        qs = Store.pobs.all()
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
        q = request.GET.get('q')

        if q:
            vector = SearchVector(Store.title_lang(), weight='A')
            vector += SearchVector(Store.subtitle_lang(), weight='B')
            vector += SearchVector(Store.description_lang(), weight='C')
            vector += SearchVector('store_features', weight='C')
            query = SearchQuery(q)
            sub = Subquery(
                StoreFeature.objects
                .filter(store=OuterRef('pk'))
                .annotate(store_features=functions.Cast(StoreFeature.feature_text_lang(), output_field=models.TextField()))
                .values('store_features'),
            )
            qs = (
                qs.annotate(store_features=models.Func(
                    Array(sub), models.Value(' ', output_field=models.TextField()), function='array_to_string'),
                )
                .annotate(rank=SearchRank(vector, query))
                .filter(rank__gte=0.1)
                .order_by('rank', 'ordering_number', '-project_date')
            )

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

        if not q:
            qs = qs.order_by('ordering_number', '-project_date')

        paginator = Paginator(qs.distinct(), limit)
        return paginator.get_page(page)

    def get_context_data(self, **kwargs):
        context = super(StoresView, self).get_context_data(**kwargs)

        context['page_title'] = _('Stores')
        context['meta_description'] = _('''meta description''')

        context['page_obj'] = self.get_stores(self.request)

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
        context['store_page'] = StorePage.objects.first()
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
                'stores/includes/stores.html',
                context=dict(page_obj=self.get_stores(request)),
            )

        return super(StoresView, self).get(request, *args, **kwargs)


class StoreView(TemplateView):
    template_name = 'stores/store.html'

    def get_context_data(self, **kwargs):
        context = super(StoreView, self).get_context_data(**kwargs)

        store = Store.pobs.filter(url_slug=kwargs.get('slug')).first()
        if not store:
            raise Http404

        context['page_title'] = store.title
        context['meta_description'] = _('''meta description''')

        context['store'] = store
        context['similar_stores'] = Store.pobs.exclude(id=store.id)[:6]
        context['categories'] = store.categories.all()
        context['sub_categories'] = store.sub_categories.all()
        context['tags'] = store.tags.all()
        context['store_features'] = StoreFeature.objects.filter(store=store)
        context['store_page'] = StorePage.objects.first()
        return context
