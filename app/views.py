from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from .forms import ReportForm
from django.core import serializers
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# for rest rest_framework
from rest_framework import viewsets
from .serializers import ReportSerializer
from .models import Entrys
# Create your views here.


class ReportviewSet(viewsets.ModelViewSet):
    """
    ModelViewSet is a special view that Django Rest Framework provides. 
    It will handle GET and POST for Heroes without us having to do any more work.
    """
    queryset = Entrys.objects.all()
    serializer_class = ReportSerializer


def thanks(request):
    return render(request, 'thanks.html')


def get_data(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ReportForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            name = form['Name'].value()
            # print(name)
            form.save()
            messages.success(
                request, "Hi {}, message was sent Successfully,Thank you".format(name))
            return HttpResponseRedirect('thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ReportForm()
        # print(form)

    return render(request, 'form.html', {'form': form})
