from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
# . represents current directory

urlpatterns = [
    path("", views.indexpage, name="home"),
    path("contactus", views.contactpage, name="contactus"),
    path("login", views.loginpage, name="login"),
    path("registration", views.registration, name="registration"),
    path("userhome", views.userhome, name="userhome"),
    path("userlogout", views.userlogout, name="userlogout"),
    path("fl",views.fl,name="fl"),
    path("checkuserlogin", views.checkuserlogin, name="checkuserlogin"),
    path("deleteuser/<int:uid>", views.deleteuser, name="deleteuser"),
    path("deleteowner/<int:uid>", views.deleteowner, name="deleteowner"),
    path('empchangepwd', views.empchangepwd, name="empchangepwd"),
    path('empupdatepwd', views.empupdatepwd, name="empupdatepwd"),
    path("addproduct", views.addproduct, name="addproduct"),
    path("owner", views.owner, name="owner"),
    path("viewcars", views.viewaproducts, name="viewcars"),
    path("viewaproducts", views.viewaproducts, name="viewaproducts"),
    path("deleteproduct/<int:uid>",views.deleteproduct,name="deleteproduct"),
    path("adminpanel", views.adminpage, name="adminpanel"),
    path("sassion", views.session, name="session"),
    path("rent",views.rentpage,name="rent"),
    path("paysucc",views.paysucc,name="paysucc"),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)