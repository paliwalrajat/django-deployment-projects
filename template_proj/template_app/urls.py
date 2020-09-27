from django.urls import path
from template_app import views

# TEMPLATE TAGGING

# VARIABLE
app_name = 'template_app'
# THIS 'app_name' WHICH IS 'template_app' IN THIS IS USED FOR 'href' TAG IN 'RELATED_URL_TEMP.HTML'

urlpatterns = [
    path('relative/',views.relative,name='relative'),
    path('other/',views.other,name='other'),
]
