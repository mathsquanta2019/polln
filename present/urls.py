from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = "present"

urlpatterns = [
    path("<str:prj>", views.index, name="index"),
    path("live_vote_count/<int:id>", views.live_vote_count, name="live_vote_count"),
    path("deliver_answers/<int:id>", views.deliver_answers, name="deliver_answers"),
]

# Serve media files during development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
