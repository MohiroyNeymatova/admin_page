from django.urls import path, include


urlpatterns = [
    path('backoffice/', include('main.backoffice.urls'))
]