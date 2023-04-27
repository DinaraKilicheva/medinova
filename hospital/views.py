from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, TemplateView, DetailView, CreateView

from hospital.forms import AppointmentForm
from hospital.models import SocialLink, Price, Doctor, Service, Department, FeedBack, Blog, Comment, BlogCategory, \
    Appointment


class BaseView(DetailView):
    queryset = SocialLink.objects.all()
    template_name = "base.html"
    context_object_name = "links"


class HomeView(ListView):
    queryset = Doctor.objects.all()
    template_name = 'index.html'
    context_object_name = 'doctors'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = 'home'
        context['links'] = SocialLink.objects.all()
        context['services'] = Service.objects.all()
        context['doctors'] = Doctor.objects.all()
        context['departments'] = Department.objects.all()
        context['prices'] = Price.objects.all()
        context['feedbacks'] = FeedBack.objects.all()
        context['blogs'] = Blog.objects.all()
        return context


class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = 'about'
        context['teams'] = Doctor.objects.all()
        context['links'] = SocialLink.objects.all()
        return context


class ServicesListView(ListView):
    template_name = 'service.html'
    queryset = Service.objects.all()
    context_object_name = 'services'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = 'service'
        context['links'] = SocialLink.objects.all()
        context['departments'] = Department.objects.all()
        context['doctors'] = Doctor.objects.all()
        context['feedbacks'] = FeedBack.objects.all()
        return context


class PricesListView(ListView):
    queryset = Price.objects.all()
    template_name = 'price.html'
    context_object_name = 'prices'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = 'price'
        context['departments'] = Department.objects.all()
        context['doctors'] = Doctor.objects.all()
        context['feedbacks'] = FeedBack.objects.all()
        context['links'] = SocialLink.objects.all()
        return context


class BlogsListView(ListView):
    queryset = Blog.objects.all()
    template_name = 'blog.html'
    context_object_name = 'blogs'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = 'blog'
        context['departments'] = Department.objects.all()
        context['doctors'] = Doctor.objects.all()
        context['feedbacks'] = FeedBack.objects.all()
        context['links'] = SocialLink.objects.all()
        return context


class DetailView(DetailView):
    template_name = 'detail.html'
    queryset = Blog.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        blog_id = self.kwargs.get(self.pk_url_kwarg)
        context['menu'] = 'detail'
        context['blogs'] = Blog.objects.all()
        context['blog'] = Blog.objects.filter(id=blog_id).first()
        context['comments'] = Comment.objects.all()
        context['blogcategories'] = BlogCategory.objects.all()
        context['links'] = SocialLink.objects.all()
        return context


class TeamsListView(ListView):
    template_name = 'team.html'
    queryset = Doctor.objects.all()
    context_object_name = 'teams'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = 'team'
        context['links'] = SocialLink.objects.all()
        return context


class TestimonialView(ListView):
    template_name = 'testimonial.html'
    queryset = FeedBack.objects.all()
    context_object_name = 'testimonials'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = 'testimonial'
        context['links'] = SocialLink.objects.all()
        return context


class AppointmentView(CreateView):
    model = Appointment
    form_class = AppointmentForm
    template_name = 'appointment.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = 'appointment'
        context['departments'] = Department.objects.all()
        context['doctors'] = Doctor.objects.all()
        context['links'] = SocialLink.objects.all()
        return context

    def get_success_url(self):
        return reverse('index')
    #
    # def get(self, request, *args, **kwargs):
    #     return render(request, self.template_name)
    #
    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST or None)
    #     print(form)
    #     print(form.is_valid())
    #
    #     if form.is_valid():
    #         Appointment.objects.create(
    #             department_id=form.department_id,
    #             doctor_id=form.doctor_id,
    #             name=form.patient_name,
    #             email=form.patient_email,
    #             appointment_time=form.appointment_date
    #         ).save()
    #     return HttpResponseRedirect('/index/')


class SearchView(ListView):
    template_name = 'search.html'
    queryset = Doctor.objects.all()
    context_object_name = 'results'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = 'search'
        context['links'] = SocialLink.objects.all()
        context['departments'] = Department.objects.all()
        return context

    def post(self, request):
        search_query = request.POST.get("search")
        expression = (
                Q(first_name__icontains=search_query) |
                Q(last_name__icontains=search_query)
        )
        queryset = Doctor.objects.filter(expression)
        return render(request, "search.html", {"results": queryset})


class ContactView(TemplateView):
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = 'contact'
        context['links'] = SocialLink.objects.all()
        return context
