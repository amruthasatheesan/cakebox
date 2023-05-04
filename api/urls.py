from django.urls import path
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import ObtainAuthToken

router=DefaultRouter()
router.register("register",views.UsersView,basename="users")
router.register("cakes",views.CakesView,basename="cake")
router.register("carts",views.CartListView,basename="cart")
router.register("orders",views.OrderListView,basename="order")
router.register("reviews",views.ReviewListView,basename="reviews")
urlpatterns=[
    path("token/",ObtainAuthToken.as_view()),
]+router.urls