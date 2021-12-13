from django.shortcuts import render,redirect
from user import forms
from django.contrib.auth import authenticate,login,logout
from owner.models import Phone,Cart,Order
from django.views.generic import TemplateView,ListView,UpdateView,DetailView,DeleteView,CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.decorators import method_decorator
from owner.decorators import signin_required
from django.db.models import Sum
# Create your views here.

@method_decorator(signin_required,name="dispatch")
class UserHomeView(TemplateView):
    def get(self, request, *args, **kwargs):
        mobile = Phone.objects.all()
        context = {"mobile": mobile}
        return render(request, "basenew.html", context)


class SignUpView(TemplateView):
    def get(self, request, *args, **kwargs):
        form = forms.UserRegistrationForm()
        context = {}
        context["form"] = form
        return render(request, "registertemp.html", context)
    def post(self,request):
        form = forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            print("user registration success")
            return redirect("signin")

        else:
            context = {}
            context["form"] = form
            return render(request, "registertemp.html", context)

class SignInView(TemplateView):
    def get(self, request, *args, **kwargs):
        form = forms.LoginForm()
        context = {"form": form}
        return render(request, "logintempnew.html", context)
    def post(self,request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)

            if (user):
                login(request, user)
                return redirect("userhome")

            else:
                return render(request, "logintempnew.html", {"form": form})

@method_decorator(signin_required,name="dispatch")
class AddToCart(TemplateView):
    model=Cart
    def get(self, request, *args, **kwargs):

        id=kwargs["id"]
        mobile=Phone.objects.get(id=id)
        cart=Cart.objects.create(item=mobile,user=request.user)
        cart.save()
        messages.success(request,"item added success")
        return redirect("userhome")

@method_decorator(signin_required,name="dispatch")
class ViewCart(TemplateView):
    model=Cart
    template_name = "mycart.html"
    def get(self, request, *args, **kwargs):
        context={}
        items=Cart.objects.filter(user=request.user,status="incart")
        context["items"]=items

        total=Cart.objects.filter(user=request.user,status="incart").aggregate(Sum("item__Price"))
        context["total"]=total["item__Price__sum"]

        return render(request,self.template_name,context)

@method_decorator(signin_required,name="dispatch")
class RemoveItemCart(TemplateView):
    model=Cart

    def get(self, request, *args, **kwargs):
        id=kwargs["id"]
        cart=self.model.objects.get(id=id)
        cart.status="cancelled"
        cart.save()
        messages.success(request,"item removed success")
        return redirect("userhome")

@method_decorator(signin_required,name="dispatch")
class OrderCreationView(TemplateView):
    model=Order
    form_class=forms.OrderForm
    template_name = "ordercreation.html"
    context={}

    def get(self, request, *args, **kwargs):
        form=self.form_class()
        self.context["form"]=form
        return render(request,self.template_name,self.context)




    def post(self,request,*args,**kwargs):
        cart_id=kwargs["id"]
        cart_item=Cart.objects.get(id=cart_id)

        form=self.form_class(request.POST)
        if form.is_valid():
            address=form.cleaned_data["address"]
            user=request.user.username
            item=cart_item.item

            order=self.model.objects.create(
                address=address,
                user=user,
                item=item
            )

            order.save()

            cart_item.status="orderplaced"
            cart_item.save()
            messages.success(request,"your order has been placed")

            return redirect("userhome")

@method_decorator(signin_required,name="dispatch")
class ViewMyOrder(ListView):
    model=Order
    template_name = "myorder.html"
    context_object_name = "order"












# def user_home(request):
#     mobile=Phone.objects.all()
#     context={"mobile":mobile}
#     return render(request,"home.html",context)
#
# def signup(request):
#     form=forms.UserRegistrationForm()
#     context={}
#     context["form"]=form
#
#     if request.method=="POST":
#         form=forms.UserRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             print("user registration success")
#             return redirect("signin")
#
#         else:
#             context={}
#             context["form"]=form
#             return render(request,"user_register.html",context)
#
#     return render(request,"user_register.html",context)
#
# def signin(request):
#     form=forms.LoginForm()
#     context={"form":form}
#
#     if request.method=="POST":
#         form=forms.LoginForm(request.POST)
#         if form.is_valid():
#             username=form.cleaned_data["username"]
#             password=form.cleaned_data["password"]
#             user=authenticate(request,username=username,password=password)
#
#             if(user):
#                 login(request,user)
#                 return redirect("userhome")
#
#             else:
#                 return render(request,"login.html",{"form":form})
#
#
#
#     return render(request,"login.html",context)
@signin_required
def signout(request):
    logout(request)
    return redirect("signin")
