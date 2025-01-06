from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.show, name='home'),
    path('category/<int:id>/', views.cat_view, name='category'),
    path('product/<int:id>/', views.cat_view, name='product'),
    path('addprod/<int:id>/',views.addprod,name="addprod"),
    path('register/', views.register, name='register'),
    path('login_details/', views.login_details, name='login_details'),
    path('logout/', views.user_logout, name='logout'),
    path('ty/', views.tym, name='thanks'),
    path('range/', views.range, name='range'),
    path('addcart/<int:pid>/', views.addcart, name='addcart'),
    path('viewcart/', views.viewCart, name='viewcart'),
    path('remove/<int:cid>',views.remove),
    path('updateqty/<qv>/<cid>', views.updateqty),
    path('checkout', views.checkout, name="checkout"),
    path('customer_det', views.customer_detail, name="cdetail"),
    path('ordered', views.placeorder, name="orderitems"),
    path('success/', views.paymentsuccessful, name="paymentsuccess"),
    path('failed/', views.paymentfailed, name="paymentfailed"),
    path('drf_crud/', views.crud_api.as_view(), name='crudview'),
    path('forgetpassword/', views.forgetpassword, name="forgotpass"),
    path('reset_password/<uidb64>/<token>/', views.reset_password, name="resetpass"),
    path('prd/', views.password_reset_done, name="prd"),
    path('search/', views.search_food, name='search'),
    path('rate_food/<int:food_id>/', views.rate_food, name='rate_food'),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)