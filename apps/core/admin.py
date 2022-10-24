from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import reverse


class ConceptAdmin(admin.ModelAdmin):
    def changelist_view(self, request, extra_context=None):
        obj = self.model.objects.first()

        if obj is not None:
            return HttpResponseRedirect(
                reverse(f"admin:{self.model._meta.app_label}_{self.model._meta.model_name}_change", args=(obj.id,))
            )
        return super(ConceptAdmin, self).changelist_view(request=request, extra_context=extra_context)

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
