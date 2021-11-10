from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from crud_app.forms import student_form
from crud_app.models import Student_profile

# Create your views here.
def index(request):
    student_list = Student_profile.objects.order_by('first_name')
    dict={'student_list': student_list}
    return render(request, 'crud_app/index.html', context=dict)

def student_forms(request):
    forms = student_form()
    if request.method == 'POST':
        forms = student_form(request.POST)
        if forms.is_valid():
            forms.save()
            return HttpResponseRedirect(reverse('crud_app:index'))
    dict={'forms': forms}
    return render(request, 'crud_app/forms.html', context=dict)

def student_info(request, id):
    info = Student_profile.objects.get(pk=id)
    dict = {'info': info}
    return render(request, 'crud_app/student_info.html', context=dict)

def update(request, id):
    current_form = Student_profile.objects.get(pk=id)
    form = student_form(instance=current_form)
    if request.method == 'POST':
        form = student_form(request.POST, instance=current_form)
        if form.is_valid():
            form.save()
           # return index(request)
            return HttpResponseRedirect(reverse('crud_app:index'))
    diction = {'form': form}
    return render(request, 'crud_app/update.html', context=diction)



def student_delete(request, id):
    student = Student_profile.objects.get(pk=id).delete()
    diction = {}
    return render(request, 'crud_app/student_delete.html ', context=diction)
