from django.conf.urls import url,include

app_name = "accounts"

from .views import login_page,password_reset    , RegisterView, guest_register_view,logout_user

urlpatterns = [
    # /service/ homepage with no extra information

    url(r'^login_user/$', login_page , name='login_user'),
    url(r'^logout/$', logout_user , name='logout_user'),
#    path(        'change-password/',   auth_views.PasswordChangeView.as_view(template_name='accounts/change-password.html'), ),

    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^subscribe_us/$', guest_register_view, name='guest_register'),

]