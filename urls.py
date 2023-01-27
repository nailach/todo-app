from django.urls import path
from .import views
from .views import TaskUpdate, TaskDelete

urlpatterns = [
	path('', views.index, name="index"),
	path("signIn/", views.signIn, name="singIn"),
	path("signup/", views.signup, name="singup"),
	path("login/", views.login, name="login"),
	path("blog/", views.blog, name="blog"),
	path("subject/", views.subject, name="subject"),
	path("ict/", views.ict, name="ict"),
	path("addnote/", views.addnote, name="addnote"),
	path("notes/", views.notes, name="notes"),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update'),

	path('<pk>/Update/', TaskUpdate.as_view, name='NotesUpdate'),
	path('<pk>/delete/', TaskDelete.as_view, name='NotesDelete'),
]
