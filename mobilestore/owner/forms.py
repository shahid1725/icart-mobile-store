from django import forms
from django.forms import ModelForm
from owner.models import Phone,Order

# class AddmobileForm(forms.Form):
#     MobileName=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     Price=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))
#     Color=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     Quantity=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))
#
#     def clean(self):
#         cleaned_data=super().clean()
#         Price=cleaned_data["Price"]
#         Quantity=cleaned_data["Quantity"]
#
#         if Price<0:
#             msg="Invalid price"
#             self.add_error("Price",msg)
#
#         if Quantity<0:
#             msg="Invalid number"
#             self.add_error("Quantity",msg)


class AddmobileForm(ModelForm):
    class Meta:
        model=Phone
        fields=["Name","Price","Color","Copies","image"]


        widgets={
            "Name":forms.TextInput(attrs={"class":"form-control"}),
            "Color":forms.TextInput(attrs={"class":"form-control"}),
            "Price":forms.NumberInput(attrs={"class":"form-control"}),
            "Copies":forms.NumberInput(attrs={"class":"form-control"})

        }
class OrderUpdateForm(ModelForm):
    class Meta:
        model=Order
        fields=["status","expected_delivery_date"]

        widgets={
            "status":forms.Select(attrs={"class":"form-select"}),
            "expected_delivery_date":forms.DateInput(attrs={"type":"date"})
        }