from django.urls import path
from django.http import JsonResponse
from . import views


def api_home(request):
    return JsonResponse({
        "message": "Welcome to HH API",
        "endpoints": [
            "/api/companies/",
            "/api/companies/<id>/",
            "/api/companies/<id>/vacancies/",
            "/api/vacancies/",
            "/api/vacancies/<id>/",
            "/api/vacancies/top_ten/"
        ]
    })


urlpatterns = [
    path("", api_home, name="api-home"),
    path("companies/", views.company_list, name="company-list"),
    path("companies/<int:id>/", views.company_detail, name="company-detail"),
    path("companies/<int:id>/vacancies/", views.company_vacancies, name="company-vacancies"),
    path("vacancies/", views.vacancy_list, name="vacancy-list"),
    path("vacancies/<int:id>/", views.vacancy_detail, name="vacancy-detail"),
    path("vacancies/top_ten/", views.top_ten_vacancies, name="top-ten-vacancies"),
]
