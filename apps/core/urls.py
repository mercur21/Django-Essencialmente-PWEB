from django.urls import path, include
from apps.core.views import index, avaliacoes

urlpatterns = [
    path("", index, name='index'),
    path("avaliacoes/", avaliacoes, name='avaliacoes'),
]