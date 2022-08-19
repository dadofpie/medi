from dataclasses import fields
from django import forms
from django.forms import ModelForm
from django.forms import Form, ModelForm, DateField, widgets
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, ModelChoiceField
from .models import Member

from crispy_forms.helper import FormHelper
from django.contrib.auth.models import Group
from .models import productType, company, accountStatus,parentCompany,modeOfPayment,vatProvision,account

from django.forms import modelformset_factory



class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30)
    first_name = forms.CharField(max_length=30, required=False, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Required.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    group = forms.ModelChoiceField(queryset=Group.objects.all(),empty_label='No group')

    class Meta:
        model = User
        fields = ('username','email', 'first_name','last_name','password1','password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['group'] = ModelChoiceField(
            queryset=Group.objects.all(),
            empty_label='No group'
        )




class addMemberForms(ModelForm):
    """Auto generated form to create Server models."""
    
    class Meta:
        model = Member
        fields = '__all__'


class account_Form(ModelForm):

    class Meta:
        model = account
        exclude= ['planTypewithDescription1','planMembershipFee','remarks']
        

class plan_Form(ModelForm):
    class Meta:
        model = account
        fields = '__all__'

class account_FormAll(ModelForm):
      class Meta:
        model = account
        fields = '__all__'
        

class addMem1 (ModelForm):
    class Meta:
        model = Member
        fields = '__all__'
        exclude = ['BirthDate','Height','Weight','CStat','gen','philHealth','employeeNum','posAndocu','MemberAddressNumberAndStreet','MemberAddressBarangayAndDistrict','MemberCityProvinceRegion','MemberCityZipCode','MemberContactNumber','Mop','remarksMem']


class addMem2 (ModelForm):
    class Meta:
        model = Member
        fields = ('BirthDate','Height','Weight','CStat','gen','philHealth','employeeNum','posAndocu','MemberAddressNumberAndStreet','MemberAddressBarangayAndDistrict','MemberCityProvinceRegion','MemberCityZipCode','MemberContactNumber','Mop','remarksMem')

class parentCompany(ModelForm):
    class Meta:
        model = vatProvision
        fields = '__all__'

class company(ModelForm):
    class Meta:
        model = vatProvision
        fields = '__all__'

