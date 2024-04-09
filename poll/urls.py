from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = "poll"

urlpatterns = [
    path("<str:prj>", views.index, name="index"),
    path("check_if_poll_open/check", views.check_if_poll_open, name="check_if_poll_open"),
    path("get_answers/answer", views.get_answers, name="get_answers"),
    path("check_poll_password/password", views.check_poll_password, name="check_poll_password"),
]

# Serve media files during development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
