from django.urls import path
from user import views

urlpatterns=[
    path('home',views.UserHomeView.as_view(),name="userhome"),
    path('signup',views.SignUpView.as_view(),name="signup"),
    path('signin',views.SignInView.as_view(),name="signin"),
    path('signout',views.signout,name="signout"),
    path('books/addcart/<int:id>',views.AddToCart.as_view(),name="addcart"),
    path('mycart',views.ViewCart.as_view(),name="viewmycart"),
    path('removecart/<int:id>',views.RemoveItemCart.as_view(),name="removecart"),
    path('buycart/<int:id>',views.OrderCreationView.as_view(),name="orderitem"),
    path('myorder',views.ViewMyOrder.as_view(),name="myorder"),

]