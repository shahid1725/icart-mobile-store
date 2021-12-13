from django.urls import path
from owner import views

urlpatterns=[
    path("add/",views.AddMobileView.as_view(),name="addmobile"),
    path("list",views.ListMobileView.as_view(),name="listphone"),
    path("remove/<int:id>",views.DeleteMobileView.as_view(),name="removephone"),
    path("edit/<int:id>",views.MobileUpdateView.as_view(),name="editphone"),
    path("view/<int:id>",views.ViewMobileView.as_view(),name="mobileview"),
    path("user/orders",views.UserOrdersView.as_view(),name="userorder"),
    path("order/update/<int:id>",views.OrderUpdateView.as_view(),name="orderupdate"),
    path("findphone",views.PhoneFilterView.as_view(),name="phonesearch"),
    path("findorder",views.OrderFilterView.as_view(),name="ordersearch")

]
