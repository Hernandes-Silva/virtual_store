from products.models import Department

def template_base(request):
    base_departments = Department.objects.all()
    return {'base_departments': base_departments}