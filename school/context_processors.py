from departments.models import DepartmentsModel
from scrolltext.models import MarqueeModel
from payfees.models import PayfeeModel

def get_departments(request):
    return {'departments': DepartmentsModel.objects.all(), }

def marquee(request):
    return {'marquee': MarqueeModel.objects.all(), }

def payfee(request):
    return {'pay': PayfeeModel.objects.all(), }