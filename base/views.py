import decimal
import logging

from optparse import check_builtin
from socket import IP_MULTICAST_IF
from statistics import variance
from tokenize import group
from typing import ItemsView
from unittest import result
from django.contrib import messages

from django.template import RequestContext

from django.db.models import F
import os
import csv, io
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User
from django.conf import settings
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
#from numpy import delete
from pkg_resources import yield_lines
from base.forms import account_Form,plan_Form,account_FormAll

from base.forms import addMem1,addMem2

from .models import Member, modeOfPayment, planList, vatProvision
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import authenticate, login
from django import template

from .models import User,memTypes,prinMem,relaMem

from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import auth_users, allowed_users
# Create your views here.

from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django.db.models import Sum
from django.shortcuts import render


from django.http import HttpResponse
from datetime import datetime
from .forms import addMemberForms
from .models import productType, company, accountStatus,parentCompany,account


User = get_user_model()




def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = form.cleaned_data.get('group')

            group.user_set.add(user)
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            user.save()
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def signupStaffUser(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = form.cleaned_data.get('group')
            group.user_set.add(user)
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            user.is_staff=True
            user.is_superuser=True
            user.save()
            
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})




def home(request):
        if request.user.is_authenticated:
            acc = account.objects.all()
            prod = productType.objects.all()
            comp = company.objects.all()
            stat = accountStatus.objects.all()
            prntC = parentCompany.objects.all()
            
            mop = modeOfPayment.objects.all()
            vp = vatProvision.objects.all()
 

            context = { 'acc':acc,
           }
            
            return render(request, 'base/Home.html', context)
        else:
            return render (request, 'landing.html')
    



def AccountDashboard(request):
     if request.user.is_authenticated:
       
        acc = account.objects.filter()
        context = {'acc': acc}
        return render(request, 'base/accountDashboard.html',context)
     else:
        return render (request, 'landing.html')

def AccountMember(request):
     if request.user.is_authenticated:
       
        acc = Member.objects.filter()
        
        context = {'acc': acc}
        return render(request, 'base/memberDashboard.html',context)
     else:
        return render (request, 'landing.html')




def updatePlanType(request,pk):
    status = account.objects.get(id=pk)
    form = plan_Form(instance=status)
    pln = planList.objects.all()
    acc = account.objects.all()
    if request.method == 'POST':
       calc = account.objects.filter(id=pk).update(
       planTypewithDescription1 = request.POST.get('planTypewithDescription1'),
       planTypewithDescription2 = request.POST.get('planTypewithDescription2'),
       planTypewithDescription3 = request.POST.get('planTypewithDescription3'),
       planTypewithDescription4 = request.POST.get('planTypewithDescription4'),
       planTypewithDescription5 = request.POST.get('planTypewithDescription5'),
       )
       return redirect('Accounts')
    context ={'form': form, 'acc':acc, 'pln':pln}
    return render(request, 'base/accountHMForms/updatePlan.html', context)




def addAccount(request):
    if request.user.is_authenticated:
        acc = account.objects.all()
        prod = productType.objects.all()
        comp = company.objects.all()
        stat = accountStatus.objects.all()
        prntC = parentCompany.objects.all()
        mop = modeOfPayment.objects.all()
        vp = vatProvision.objects.all()
        if request.method =="POST": 
            accn = account.objects.create(
                accNumber = request.POST.get('accNumber'),
                productName = request.POST.get('productName'),
                companyName = request.POST.get('companyName'),
                accStatus = request.POST.get('accStatus'),
                prntCompany = request.POST.get('prntCompany'), 
                rollUp = request.POST.get('rollUp'),
                TIN = request.POST.get('TIN'),
                NatureOfBusiness = request.POST.get('NatureOfBusiness'),
                AMF = request.POST.get('NatureOfBusiness'),
                #----------------- Signatories --------------------------------------------
                Signatory1 = request.POST.get('Signatory1'),
                Signatory1Designation = request.POST.get('Signatory1Designation'),
                Signatory2 = request.POST.get('Signatory2'),
                Signatory2Designation = request.POST.get('Signatory2Designation'),
                Signatory3 = request.POST.get('Signatory3'),
                Signatory3Designation = request.POST.get('Signatory3Designation'),

                #--------------------Account Address --------------------------
                accNumberStreet = request.POST.get('accNumberStreet'),
                accBrgy = request.POST.get('accBrgy'),
                accCityProvReg = request.POST.get('accCityProvReg'),
                accZipCode = request.POST.get('accZipCode'),
                
                #------------------ Contact Details ---------------------------------
                ContactPerson1 = request.POST.get('ContactPerson1'),
                ContactPerson1Designation = request.POST.get('ContactPerson1Designation'),
                ContactPerson1Phone = request.POST.get('ContactPerson1Phone'),
                ContactPerson1Email = request.POST.get('ContactPerson1Email'),
                ContactPerson2 = request.POST.get('ContactPerson2'),
                ContactPerson2Designation = request.POST.get('ContactPerson2Designation'),
                ContactPerson2Phone = request.POST.get('ContactPerson2Phone'),
                ContactPerson2Email = request.POST.get('ContactPerson2Email'),
                FaxNumber1 = request.POST.get('FaxNumber1'),
                FaxNumber2 = request.POST.get('FaxNumber2'),
            #-------------------PlanTypeChoices-----------------------------------------
                planTypewithDescription1 = request.POST.get('planTypewithDescription1'),
                planTypewithDescription2= request.POST.get('planTypewithDescription2'),
                planTypewithDescription3 = request.POST.get('planTypewithDescription3'),
                planTypewithDescription4 = request.POST.get('planTypewithDescription4'),
                planTypewithDescription5 = request.POST.get('planTypewithDescription5'),
                planMembershipFee1 = request.POST.get('planMembershipFee1'),
                remarks = request.POST.get('remarks'),
           
            #----------------------ActionDates-------------------------------------------
                PlanTypeBenefitsSummaryReceiveDates = request.POST.get('PlanTypeBenefitsSummaryReceiveDates'),
                ConformeDate = request.POST.get('ConformeDate'),
                OriginalEffectiveDate = request.POST.get('OriginalEffectiveDate'),
                EffectiveDate = request.POST.get('EffectiveDate'),
                ExpiryDate = request.POST.get('ExpiryDate'),
                SuspensionDate = request.POST.get('SuspensionDate'),
                ReactivationDate = request.POST.get('ReactivationDate'),
                TerminationExtensionDate = request.POST.get('TerminationExtensionDate'),

            #---------------------- Billing ----------------------------------------------
                ModeofPayment = request.POST.get('ModeofPayment'),
                proRatingFee = request.POST.get('proRatingFee'),
                VatProvision = request.POST.get('vatProvision'),
                philHealth = request.POST.get('philHealth'),
                payeeName = request.POST.get('payeeName'),
                NumberStreet = request.POST.get('NumberStreet'),
                BarangayDistrict = request.POST.get('BarangayDistrict'),
                CityProvinceRegion  = request.POST.get('CityProvinceRegion'),
                ZipCode = request.POST.get('ZipCode'),
                BillingAddressee = request.POST.get('BillingAddressee'),
                BillingAddresseeDesignation = request.POST.get('BillingAddresseeDesignation'),


            #------------------------ Other Information -----------------------------------

                initialNumberofEmployees = request.POST.get('initialNumberofEmployees'),
                initialNumberofImmediateDependents = request.POST.get('initialNumberofImmediateDependents'),
                initialNumberofExtendedDependents = request.POST.get('initialNumberofExtendedDependents'),
                foreignEmployees = request.POST.get('foreignEmployees'),
                nationalitiesPositionsofExpatriates = request.POST.get('nationalitiesPositionsofExpatriates'),
                companyNameonCard = request.POST.get('companyNameonCard'),
                remarksInfo = request.POST.get('remarksInfo'),


            )


            return redirect('Accounts')
        context = { 'acc':acc,'prod':prod, 'comp':comp, 'stat':stat, 'prntC':prntC, 'mop':mop,'vp':vp}
        return render(request, 'base/accountHMForms/account_form.html', context)
    else:
        return render (request, 'landing.html')


def viewAllAcc(request,pk):
    status = account.objects.get(id=pk)
    form = account_FormAll(instance=status)
    
    if request.method == 'POST':
        invcard = account_FormAll(request.POST, instance=status)
        if  invcard.is_valid():
            invcard.save()
            return redirect('Accounts')

    context ={'form': form}
    return render(request, 'base/accountHMForms/account_form.html', context)





def addPlan(request):
    if request.user.is_authenticated:
        form = account_Form()
        
        acc = account.objects.all()
        prod = productType.objects.all()
        comp = company.objects.all()
        stat = accountStatus.objects.all()
        prntC = parentCompany.objects.all()
        
        mop = modeOfPayment.objects.all()
        vp = vatProvision.objects.all()
        if request.method =="POST":
            accn = account .objects.create(
               

               
            )
            
            return redirect('account')
        context = {'form': form, 'acc':acc,'prod':prod, 'comp':comp, 'stat':stat, 'prntC':prntC, 'ptwd':ptwd, 'mop':mop,'vp':vp}
        return render(request, 'base/accountHMForms/account_form.html', context)
    else:
        return render (request, 'landing.html')

#-------------------------Update Status -----------------------------------------------

def addMember(request):
    if request.user.is_authenticated:
        form = addMem1()
        mem = Member.objects.all()
        acc = account.objects.all()
        prod = productType.objects.all()
        comp = company.objects.all()
        stat = accountStatus.objects.all()
        prntC = parentCompany.objects.all()
        memtype = memTypes.objects.all()
        prinmem = prinMem.objects.all()
        rela = relaMem.objects.all()

        if request.method =="POST":
            accn = Member.objects.create(
                
                #--------------------Account Address --------------------------
                accNumberMem = request.POST.get('accNumberMem'),
                comName = request.POST.get('comName'),
                hmoCardNumber = request.POST.get('hmoCardNumber'),
                lastName = request.POST.get('lastName'),
                firstName= request.POST.get('firstName'),
                middleName= request.POST.get('middleName'),
                memStatus= request.POST.get('memStatus'),
                memType= request.POST.get('memType'),
                attachPrinMember= request.POST.get('attachPrinMember'),
                relationshipPrinMember= request.POST.get('relationshipPrinMember'),
                memberParticipation= request.POST.get('memberParticipation'),
                planType= request.POST.get('planType'),
                OriginalEffectiveDate= request.POST.get('OriginalEffectiveDate'),
                EffectiveDate= request.POST.get('EffectiveDate'),
                ExpiryDate= request.POST.get('ExpiryDate'),
                SuspensionDate= request.POST.get('SuspensionDate'),
                ReactivationDate= request.POST.get('ReactivationDate'),
                TerminationExtensionDate= request.POST.get('TerminationExtensionDate'),

                BirthDate= request.POST.get('BirthDate'),
                Height= request.POST.get('Height'),
                Weight= request.POST.get('Weight'),
                CStat= request.POST.get('CStat'),
                gen= request.POST.get('gen'),
                philHealth= request.POST.get('philHealth'),
                employeeNum= request.POST.get('employeeNum'),
                posAndocu= request.POST.get('posAndocu'),
                MemberAddressNumberAndStreet= request.POST.get('MemberAddressNumberAndStreet'),
                MemberAddressBarangayAndDistrict= request.POST.get('MemberAddressBarangayAndDistrict'),
                MemberCityProvinceRegion= request.POST.get('MemberCityProvinceRegion'),
                MemberCityZipCode= request.POST.get('MemberCityZipCode'),
                MemberContactNumber= request.POST.get('MemberContactNumber'),
                Mop= request.POST.get('Mop'),
                remarksMem= request.POST.get('remarksMem'),
                remarksInfo = request.POST.get('remarksInfo'),

            

               
            )



            return redirect('AccountMember')
        context = {'form': form, 'acc':acc, 'mem':mem, 'comp':comp, 'memtype':memtype,'prinmem':prinmem,'rela':rela,}
        return render(request, 'base/memberHMForms/member_form.html', context)
    else:
        return render (request, 'landing.html')



def create_Member(request):
    if request.user.is_authenticated:
        form = addMemberForms()
        if request.method =="POST":
            raw = addMemberForms(request.POST)
            if  raw.is_valid():
                raw.save()
                return redirect('adminPanel')
        context = {'form': form}
        return render(request, 'base/memberHMForms/membergenerate.html', context)
    else:
        return render (request, 'home.html')


