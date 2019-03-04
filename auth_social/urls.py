from django.urls import path, re_path
import auth_social.views as auth_social

app_name = 'auth_social'

urlpatterns = [
    re_path(r'^$', auth_social.index, name='index'),

]
