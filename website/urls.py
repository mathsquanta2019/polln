from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "website"

urlpatterns = [
    path("", views.index, name="index"),
    path("guide", views.guide, name="guide"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("signup", views.signup, name="signup"),
    path("delete_account", views.delete_account, name="delete_account"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)