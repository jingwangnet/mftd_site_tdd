from django.contrib import admin
from .models import Quote

# Register your models here.


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "company",
        "submitted",
        "quotedate",
        "quoteprice",
    )
    list_filter = ("submitted", "quotedate")
    date_hierarchy = "submitted"
    ordering = ("-submitted",)
    readonly_fields = ("submitted",)
    fieldsets = (
        (None, {"fields": ("name", "email", "description")}),
        (
            "Contact Information",
            {
                "classes": ("collapse",),
                "fields": ("position", "company", "address", "phone", "web"),
            },
        ),
        (
            "Job information",
            {
                "classes": ("collapse",),
                "fields": ("sitestatus", "priority", "jobfile", "submitted"),
            },
        ),
        (
            "Quote Admin",
            {
                "classes": ("collapse",),
                "fields": ("quotedate", "quoteprice", "username"),
            },
        ),
    )
