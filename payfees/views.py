from django.shortcuts import render
from . models import PayfeeModel

# Create your views here.
def PayfeeView(request):
	pay = PayfeeModel.objects.all()
	return render(request,'home.html', {'pay':pay})