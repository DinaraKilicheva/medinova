from django.urls import path

from .views import HomeView, AboutView, ServicesListView, PricesListView, BlogsListView, TeamsListView, TestimonialView, \
    AppointmentView, SearchView, ContactView, DetailView

urlpatterns = [
    path('about/', AboutView.as_view(), name="about"),
    path('index/', HomeView.as_view(), name="index"),
    path('sevice/', ServicesListView.as_view(), name="service"),
    path('price/', PricesListView.as_view(), name="price"),
    path('blog/', BlogsListView.as_view(), name="blog"),
    path('detail/<int:pk>', DetailView.as_view(), name="detail"),
    path('team/', TeamsListView.as_view(), name="team"),
    path('testimonial/', TestimonialView.as_view(), name="testimonial"),
    path('appointment/', AppointmentView.as_view(), name="appointment"),
    path('search/', SearchView.as_view(), name="search"),
    path('contact/', ContactView.as_view(), name="contact"),
    path('', HomeView.as_view(), name="index"),
]
