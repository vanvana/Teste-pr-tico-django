from msilib.schema import Feature
from django.urls import path

from client.views import CreateClient, DeleteClient, Features, ListClient, UpdateClient, delete_client, Features

urlpatterns = [
    path('novo', CreateClient.as_view(), name = 'create-client'),
    path('listar', ListClient.as_view(), name = 'list-client'),
    path('editar/<int:pk>', UpdateClient.as_view(), name = 'update-client'),
    path('apagar/<int:pk>', DeleteClient.as_view(), name = 'delete-client'),
    path('recursos', Features, name='features-by'),
]