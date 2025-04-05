from . import views
from django.urls import path

urlpatterns = [
    path("createpdf/",views.CreatePdfView,name="create-pdf"),
    path("getpdf/",views.GetPdfView,name="get-pdf"),
    path("searchpdf/",views.SearchView,name="search-pdf"),
]
