# pylint: disable=missing-class-docstring, missing-module-docstring
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from courses.forms import SearchForm
from .models import Category, Course, Exam


class CourseListView(ListView):
    model = Course
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hierarchical_categories'] = Category.get_hierarchical_categories()
        context['search_form'] = SearchForm()
        return context

    def get_queryset(self):
        category = self.request.GET.get('category')
        search_query = self.request.GET.get('query')
        if category:
            try:
                category_obj = Category.objects.get(name=category)
                return Category.get_category_courses(category_obj).order_by('-created_at')
            except Category.DoesNotExist:
                return self.model.objects.none()

        if search_query:
            return Course.search_courses(search_query).order_by('-created_at')
        return self.model.objects.all().order_by('-created_at')


class CourseDetailView(DetailView):
    model = Course
    slug_field = 'name'
    slug_url_kwarg = 'name'

class ExamListView(ListView):
    model = Exam
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hierarchical_categories'] = Category.get_hierarchical_categories()
        context['search_form'] = SearchForm()
        return context

    def get_queryset(self):
        category = self.request.GET.get('category')
        search_query = self.request.GET.get('query')
        if category:
            try:
                category_obj = Category.objects.get(name=category)
                return Category.get_category_exams(category_obj).order_by('-created_at')
            except Category.DoesNotExist:
                return self.model.objects.none()

        if search_query:
            return self.model.search_exams(search_query).order_by('-created_at')
        return self.model.objects.all().order_by('-created_at')


class ExamDetailView(DetailView):
    model = Exam
    slug_field = 'name'
    slug_url_kwarg = 'name'
