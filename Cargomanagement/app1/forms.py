from django import forms
from app1.models import Branch
from app1.models import User
from app1.models import Customermanager
from app1.models import Book
from app1.models import Login

class Loginform(forms.ModelForm):
    class Meta:
        model = Login
        fields = "__all__"

class Branchform(forms.ModelForm):
    class Meta:
        model = Branch
        fields = "__all__"

class Userform(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"

class Customermanagerform(forms.ModelForm):
    class Meta:
        model = Customermanager
        fields = "__all__"

class BookingForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
    
