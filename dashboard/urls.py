from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = "dashboard"

urlpatterns = [
    path("", views.index, name="index"),
    path("add_project", views.add_project, name="add_project"),
    path("project/<int:id>", views.project, name="project"),
    path("edit_project/<int:id>", views.edit_project, name="edit_project"),
    path("delete_project/<int:id>", views.delete_project, name="delete_project"),
    path("add_question", views.add_question, name="add_question"),
    path("question_order", views.question_order, name="question_order"),
    path("edit_question/<int:id>", views.edit_question, name="edit_question"),
    path("delete_question/<int:id>", views.delete_question, name="delete_question"),
    path("open_poll/<int:id>", views.open_poll, name="open_poll"),
    path("close_poll/<int:id>", views.close_poll, name="close_poll"),
    path("project_answers/<int:id>", views.project_answers, name="project_answers"),
]

# Serve media files during development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
