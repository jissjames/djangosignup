from django.conf.urls import url
from django.contrib import admin

#imprt the views of the app and apply an alias
from signupapp import views as signupapp_views

urlpatterns = [
    #The make the signupform as the index
    url(r'^$', signupapp_views.signupform),
    #map the signupform url again, because the view actually renders result.html as well
    url(r'^signup/', signupapp_views.signupform),
    url(r'^admin/', admin.site.urls),
]
