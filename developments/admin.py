from django.contrib import admin
from developments.models import Development, PictureGallery, BlueprintGallery, Amenities, Status, Type

# Register your models here.


@admin.register(Development)
class DevelopmentAdmin(admin.ModelAdmin):
    pass


@admin.register(PictureGallery)
class PictureGalleryAdmin(admin.ModelAdmin):
    pass


@admin.register(BlueprintGallery)
class BlueprintGalleryAdmin(admin.ModelAdmin):
    pass


@admin.register(Amenities)
class AmenitiesAdmin(admin.ModelAdmin):
    pass


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    pass


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    pass
