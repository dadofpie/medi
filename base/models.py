
from asyncio.windows_events import NULL
from cProfile import label
from unicodedata import decimal
from unittest.util import _MAX_LENGTH
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Sum
from datetime import date
from django.core.exceptions import ValidationError
from django.utils.functional import cached_property
from django.forms import CharField
from django.forms import ModelForm
from django.forms import widgets









#---------------- Foreign Keys --------------------------
class productType (models.Model):
    productName = models.CharField(max_length=200, null = False)

    def __str__(self):
        return str(self.productName)

class company(models.Model):
    companyName = models.CharField(max_length=200, null = False)
    companyLocationNumAndStreet = models.CharField(max_length=200, null = False)
    companyLocationBarangayAndDistrict = models.CharField(max_length=200, null = True)
    companyCityAndProvince = models.CharField(max_length=200, null = True)
    companyZipCode = models.CharField(max_length=200, null = True)

    def __str__(self):
        return str(self.companyName)

class accountStatus(models.Model):
    accStatus = models.CharField(max_length=200,null = True)

    def __str__(self):
        return str(self.accStatus)

class parentCompany(models.Model):
    prntCompany = models.CharField(max_length=200, null = True)
    prntLocationNumAndStreet = models.CharField(max_length=200, null = False)
    prntLocationBarangayAndDistrict = models.CharField(max_length=200, null = True)
    prntCityAndProvince = models.CharField(max_length=200, null = True)
    prntZipCode = models.CharField(max_length=200, null = True)

    def __str__(self):
        return str(self.prntCompany)

class planList(models.Model):
    planTypewDescName =  models.CharField(max_length=200, null = True)
        
    def __str__(self):
        return str(self.planTypewDescName)



class modeOfPayment (models.Model):
    mop = models.CharField(max_length=200, null = True) 

    def __str__ (self):
        return str (self.mop)

class vatProvision (models.Model):
    vp = models.CharField(max_length=200, null = True)

    def __str__ (self):
        return str (self.vp)


#--------------------Key Details--------------------------------------------
class account(models.Model):
    accNumber = models.CharField(max_length=200, null = True)
    productName = models.CharField(max_length=200, null = True)
    companyName = models.CharField(max_length=200, null = True)
    accStatus = models.CharField(max_length=200, null = True)
    prntCompany = models.CharField(max_length=200, null = True)
    rollUp = models.CharField(max_length=200, null = True)
    TIN = models.CharField(max_length=200, null = True)
    NatureOfBusiness = models.CharField(max_length=200, null = True)
    AMF = models.CharField (max_length= 200, null = True )

#----------------- Signatories --------------------------------------------
    Signatory1 = models.CharField (max_length= 200, null = True )
    Signatory1Designation = models.CharField (max_length= 200, null = True )
    Signatory2 = models.CharField (max_length= 200, null = True )
    Signatory2Designation = models.CharField (max_length= 200, null = True )
    Signatory3 = models.CharField (max_length= 200, null = True )
    Signatory3Designation =models.CharField (max_length= 200, null = True )

      #--------------------Account Address --------------------------
                
    accNumberStreet = models.CharField(max_length=200, null = True)
    accBrgy = models.CharField(max_length=200, null = True)
    accCityProvReg = models.CharField(max_length=200, null = True)
    accZipCode = models.CharField(max_length=200, null = True)

#------------------ Contact Details ---------------------------------
    ContactPerson1 = models.CharField (max_length= 200, null = True )
    ContactPerson1Designation = models.CharField (max_length= 200, null = True )
    ContactPerson1Phone = models.CharField (max_length=200, null = True )
    ContactPerson1Email = models.EmailField (max_length=200, null = True)
    ContactPerson2 = models.CharField (max_length= 200, null = True )
    ContactPerson2Designation = models.CharField (max_length= 200, null = True )
    ContactPerson2Phone = models.CharField (max_length=200, null = True )
    ContactPerson2Email = models.EmailField (max_length=200, null = True)
    FaxNumber1 = models.CharField (max_length= 200, null = True )
    FaxNumber2 = models.CharField (max_length= 200, null = True )
#------------------ -PlanTypeChoices-----------------------------------------
    planTypewithDescription1 = models.CharField(max_length=200, null = True)
    planTypewithDescription2 = models.CharField(max_length=200, null = True)
    planTypewithDescription3 = models.CharField(max_length=200, null = True)
    planTypewithDescription4 = models.CharField(max_length=200, null = True)
    planTypewithDescription5 = models.CharField(max_length=200, null = True)
    planMembershipFee1 = models.DecimalField(max_digits=60,decimal_places=2,null = True)
    planMembershipFee2 = models.DecimalField(max_digits=60,decimal_places=2,null = True)
    planMembershipFee3 = models.DecimalField(max_digits=60,decimal_places=2,null = True)
    planMembershipFee4 = models.DecimalField(max_digits=60,decimal_places=2,null = True)
    planMembershipFee5 = models.DecimalField(max_digits=60,decimal_places=2,null = True)

    remarks = models.CharField(max_length=200, null = True)


#----------------------ActionDates-------------------------------------------
    PlanTypeBenefitsSummaryReceiveDates = models.CharField (max_length= 200, null = True )
    ConformeDate = models.CharField (max_length= 200, null = True )
    OriginalEffectiveDate = models.CharField (max_length= 200, null = True )
    EffectiveDate = models.CharField (max_length= 200, null = True )
    ExpiryDate = models.CharField (max_length= 200, null = True )
    SuspensionDate = models.CharField (max_length= 200, null = True )
    ReactivationDate = models.CharField (max_length= 200, null = True )
    TerminationExtensionDate = models.CharField (max_length= 200, null = True )

#---------------------- Billing ----------------------------------------------
    ModeofPayment = models.CharField (max_length= 200, null = True )
    proRatingFee = models.CharField (max_length= 200,null = True)
    VatProvision = models.CharField (max_length= 200, null = True )
    philHealth = models.CharField (max_length= 200,null = True)
    payeeName = models.CharField (max_length= 200, null = True)
    NumberStreet = models.CharField (max_length=200, null = True)
    BarangayDistrict = models.CharField(max_length= 200,default=" ")
    CityProvinceRegion  = models.CharField(max_length = 200, default = " ")
    ZipCode = models.CharField(max_length = 200, null = True)
    BillingAddressee = models.CharField(max_length = 200, default = " ")
    BillingAddresseeDesignation = models.CharField(max_length = 200, null = True)


#------------------------ Other Information -----------------------------------

    initialNumberofEmployees = models.BigIntegerField(null = True, default= 0)
    initialNumberofImmediateDependents = models.BigIntegerField(null = True, default= 0)
    initialNumberofExtendedDependents = models.BigIntegerField(null = True, default=0)
    foreignEmployees = models.CharField (max_length= 200,null = True, default=0)
    nationalitiesPositionsofExpatriates = models.CharField(max_length = 200, null = True)
    companyNameonCard = models.CharField(max_length = 200, null = True)
    remarksInfo = models.CharField(max_length = 200, null = True)

    
 

    
    def __str__(self):
        return self.accNumber

    def date_diff(self):
            datetime_object = datetime.strptime(self.ExpiryDate, "%Y-%m-%d").date()
            return (datetime_object - date.today()).days


class memTypes (models.Model):
    memTypeName = models.CharField(max_length=200, null = True)

    def __str__(self):
        return self.memTypeName

class prinMem (models.Model):
    relationship = models.CharField(max_length=200, null = True)

    def __str__(self):
        return self.relationship

class relaMem (models.Model):
    rel = models.CharField(max_length=200, null = True)

    def __str__(self):
        return self.rel

class memParti (models.Model):
    memParti = models.CharField(max_length=200, null = True)

    def __str__(self):
        return self.memParti

class CivilStatus (models.Model):
    civilStat = models.CharField(max_length=200,null =True)
    def __str__(self):
        return self.civilStat


class Gender (models.Model):
    gender = models.CharField(max_length=200,null =True)
    def __str__(self):
        return self.gender

class Member(models.Model):
    accNumberMem = models.ForeignKey(account,verbose_name=u"Account Number",on_delete=models.SET_NULL,null = True)
    comName = models.ForeignKey(company,on_delete=models.SET_NULL,verbose_name=u"Company Name", null = True)
    hmoCardNumber = models.BigIntegerField(verbose_name=u"HMO Card Number",null = True)
    lastName = models.CharField(max_length=200,verbose_name=u"Last Name", null = True)
    firstName = models.CharField(max_length=200,verbose_name=u"First Name", null = True)
    middleName = models.CharField(max_length=200, null = True)
    memStatus = models.ForeignKey(accountStatus,on_delete=models.SET_NULL,verbose_name=u"Member Status",null = True)
    memType = models.ForeignKey(memTypes,on_delete=models.SET_NULL,null = True,verbose_name=u"Member Type",)
    attachPrinMember = models.ForeignKey('self',verbose_name=u"Attached Principle Member",on_delete=models.SET_NULL,null = True)
    relationshipPrinMember = models.ForeignKey(relaMem,verbose_name=u"Relationship to Principle Member",on_delete=models.SET_NULL,null = True)
    memberParticipation = models.ForeignKey(memParti,verbose_name=u"Member Participation",on_delete=models.SET_NULL,null = True)
    planType = models.ForeignKey(planList,verbose_name=u"Plan Type",on_delete=models.SET_NULL,null = True)
    OriginalEffectiveDate = models.CharField (max_length= 200, null = True )
    EffectiveDate = models.DateField(null = True)
    ExpiryDate = models.DateField(null = True)
    SuspensionDate = models.DateField(null = True)
    ReactivationDate = models.DateField(null = True)
    TerminationExtensionDate = models.CharField (max_length= 200, null = True )

    BirthDate = models.CharField (max_length= 200, null = True )
    Height = models.CharField(max_length=200, null = True)
    Weight = models.CharField(max_length= 200, null = True)
    CStat = models.ForeignKey(CivilStatus,on_delete=models.SET_NULL,null = True)
    gen = models.ForeignKey(Gender,on_delete=models.SET_NULL,null = True)
    philHealth = models.BooleanField (null = True)
    employeeNum = models.CharField(max_length= 200, null = True)
    posAndocu = models.CharField(max_length= 200, null = True)
    MemberAddressNumberAndStreet = models.CharField(max_length= 200, null = True)
    MemberAddressBarangayAndDistrict = models.CharField(max_length= 200, null = True)
    MemberCityProvinceRegion = models.CharField(max_length= 200, null = True)
    MemberCityZipCode = models.CharField(max_length= 200, null = True)
    MemberContactNumber = models.CharField(max_length= 200, null = True)
    Mop = models.ForeignKey(modeOfPayment,on_delete=models.SET_NULL,null = True)
    remarksMem = models.CharField(max_length= 200, null = True)


    def __str__(self):
        return self.accNumberMem

