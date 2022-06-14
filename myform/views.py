from django.shortcuts import render, redirect
from myform.forms import SubscribeForm
from myform.models import Subscribe

#  ----------Create CONTACT FORM ---------
def form_page(request):
    if request.method=='POST':
        form =SubscribeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form =SubscribeForm()
    return render(request, 'form_page.html', {'form':form})