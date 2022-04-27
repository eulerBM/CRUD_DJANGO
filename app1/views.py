from django.shortcuts import render
from app1.forms import ClienteForm

# Create your views here.

def base(request):
    if request.method == "GET":
        form = ClienteForm
        context = {
            'form': form
        }
        return render(request, 'tasks/base.html', context=context)

    else:
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save()
            form1 = ClienteForm()
        
        
        context = {
            'form': form
        }
        return render(request, 'tasks/base.html', context=context)


