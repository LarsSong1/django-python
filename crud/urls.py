from django.urls import path
from .views import HomePageView

app_name="crud"


urlpatterns = [
    path("", HomePageView.as_view(), name="home")
]
