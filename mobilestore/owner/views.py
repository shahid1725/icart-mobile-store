from django.shortcuts import render,redirect
from owner.forms import AddmobileForm,OrderUpdateForm
from owner.models import Phone,Order
from django.views.generic import TemplateView,ListView,UpdateView,DetailView,DeleteView,CreateView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from owner.decorators import signin_required,admin_permission_required
from .filters import PhoneFilter,OrderFilter

# Create your views here.

# @method_decorator(admin_permission_required,name="dispatch")
class AddMobileView(CreateView):
    model = Phone
    template_name = "add_mobile.html"
    form_class = AddmobileForm
    success_url = reverse_lazy("listphone")


# def Addmobile(request):
#     if request.method=="GET":
#         form=AddmobileForm
#
#         context={}
#         context["form"]=form
#
#         return render(request,"add_mobile.html",context)
#
#     if request.method=="POST":
#         form=AddmobileForm(request.POST,request.FILES)
#         if form.is_valid():
#
#             form.save()

            # print(form.cleaned_data)
            # name=form.cleaned_data["MobileName"]
            # price=form.cleaned_data["Price"]
            # color=form.cleaned_data["Color"]
            # Copies=form.cleaned_data["Quantity"]
            #
            # mobile=Phone.objects.create(Name=name,Color=color,Price=price,Copies=Copies)
            # mobile.save()
        #     print("Phone saved")
        #     return redirect("listphone")
        #
        # else:
        #     return render(request,"add_mobile.html",{'form':form})
        #

# def list_phone(request):
#     mobile=Phone.objects.all()
#     context={}
#     context["mobile"]=mobile
#
#     return render(request,"phone_list.html",context)

# @method_decorator(signin_required,name="dispatch")
class ListMobileView(ListView):
    model=Phone
    template_name = "phone_list.html"
    context_object_name = "mobile"


# def remove_phone(request,id):
#     mobile=Phone.objects.get(id=id)
#     mobile.delete()
#
#     return redirect("listphone")

# @method_decorator(admin_permission_required,name="dispatch")
class DeleteMobileView(DeleteView):
    model = Phone
    template_name = "deletemobile.html"
    success_url = reverse_lazy("listphone")
    pk_url_kwarg = "id"

# @method_decorator(admin_permission_required,name="dispatch")
class MobileUpdateView(UpdateView):
    model=Phone
    template_name = "edit_phone.html"
    success_url = reverse_lazy("listphone")
    pk_url_kwarg = "id"
    form_class = AddmobileForm

# def change_phone(request,id):
#     mobile=Phone.objects.get(id=id)
#     if request.method=="GET":
#         form=AddmobileForm(initial={
#             "MobileName":mobile.Name,
#             "Color":mobile.Color,
#             "Price":mobile.Price,
#             "Quantity":mobile.Copies
#
#         })
#
#         context={}
#         context["form"]=form
#
#         return render(request,"edit_phone.html",context)
#
#
#     if request.method=="POST":
#         form=AddmobileForm(request.POST)
#         if form.is_valid():
#
#             mobile.Name=form.cleaned_data["MobileName"]
#             mobile.Color=form.cleaned_data["Color"]
#             mobile.Price=form.cleaned_data["Price"]
#             mobile.Copies=form.cleaned_data["Quantity"]
#
#             mobile.save()
#             return redirect("listphone")


# def mobileview(request,id):
#     mobile=Phone.objects.get(id=id)
#     context={}
#     context["mobile"]=mobile
#
#     return render(request,"mobileview.html",context)

# @method_decorator(admin_permission_required,name="dispatch")
class ViewMobileView(DetailView):
    model=Phone
    template_name = "mobileview.html"
    pk_url_kwarg = "id"
    context_object_name = "mobile"

# @method_decorator(admin_permission_required,name="dispatch")
class UserOrdersView(ListView):
    model=Order
    template_name = "userorder.html"
    context_object_name = "orders"

    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)

        neworders=self.model.objects.filter(status="order_placed")
        context["neworders"]=neworders

        delivered_orders=self.model.objects.filter(status="delivered")
        context["deliveredorders"]=delivered_orders

        context["neworders_count"]=neworders.count()
        context["delivered_count"]=delivered_orders.count()

        return context

class OrderUpdateView(UpdateView):
    model = Order
    template_name = "orderupdate.html"
    form_class = OrderUpdateForm
    pk_url_kwarg = "id"

class PhoneFilterView(TemplateView):
    template_name = "phonesearch.html"

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        f= PhoneFilter(self.request.GET,queryset=Phone.objects.all())
        context["filter"]=f

        return context

class OrderFilterView(TemplateView):
    template_name = "ordersearch.html"

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        f=OrderFilter(self.request.GET,queryset=Order.objects.all())
        context["filter"]=f

        return context


