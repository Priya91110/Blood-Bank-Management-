from django.shortcuts import render
from app1.models import Donor,Acceptor
from django.urls import reverse
from django.views.generic import UpdateView, CreateView, DeleteView
from app1.forms import RegistrationForm
from django.http import HttpResponseRedirect

# Create your views here.
def Home(request):
    return render(request,'app1/index.html')
def DonorInfo(request):
    doners=Donor.objects.all() #select * from Donor
    return render(request,'app1/donor_info.html',{'doners':doners})
def AcceptorInfo(request):
    acceptors=Acceptor.objects.all()
    return render(request,'app1/acceptor_info.html',{'acceptors':acceptors})
                          # ----------------Donor---------------------------------------------------
# Update view
class CreateDonor(CreateView):
    model = Donor
    fields='__all__'
    def get_success_url(self):
        return reverse("donortab")

class UpdateDonor(UpdateView):
    model=Donor
    fields='__all__'
    def get_success_url(self):
        return reverse("donortab")

class DeleteDonor(DeleteView):
    model = Donor
    def get_success_url(self):
        return reverse("donortab")


            # ----------------Acceptor---------------------------------------------------

class CreateAcceptor(CreateView):
    model=Acceptor
    fields='__all__'
    def get_success_url(self):
        return reverse("acceptortab")

class UpdateAcceptor(UpdateView):
    model=Acceptor
    fields='__all__'
    def get_success_url(self):
        return reverse("acceptortab")

class DeleteAcceptor(DeleteView):
    model=Acceptor
    fields='__all__'
    def get_success_url(self):
        return reverse("acceptortab")


def registartionview(request):
    reg_obj = RegistrationForm()
    if request.method == 'POST':
        data = RegistrationForm(request.POST)
        if data.is_valid():
            mydata = data.save()
            mydata.set_password(mydata.password)
            mydata.save()
            return HttpResponseRedirect("/accounts/login/")
    return render(request, 'registration/signup.html', {'reg_obj':reg_obj})
