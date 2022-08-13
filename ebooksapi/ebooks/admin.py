from django.contrib import admin


from ebooks.models import Ebook, Review
# Register your models here.


class ReviewAdmin(admin.ModelAdmin):

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


admin.site.register(Ebook)
admin.site.register(Review, ReviewAdmin)
