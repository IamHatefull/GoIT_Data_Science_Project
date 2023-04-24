from django.urls import path

from fileuploader.views import IndexView, AboutView, AddModelView, upload_file

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('add_model/', AddModelView.as_view(), name='add_model'),
    path('about/', AboutView.as_view(), name='about'),
]

