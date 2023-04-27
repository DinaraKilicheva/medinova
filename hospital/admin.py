from django.contrib import admin

from .models import Service, Department, Doctor, Price, FeedBack, SocialLink, \
    DoctorContact, Speciality, Appointment, Blog, Comment, BlogCategory, User


class DoctorAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "photo", "speciality", "department"]


class PriceAdmin(admin.ModelAdmin):
    list_display = ["title", "annual_price", "photo"]


admin.site.register(Service)
admin.site.register(Department)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Price, PriceAdmin)
admin.site.register(FeedBack)
admin.site.register(SocialLink)
admin.site.register(DoctorContact)
admin.site.register(Speciality)
admin.site.register(Appointment)
admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(BlogCategory)
admin.site.register(User)
