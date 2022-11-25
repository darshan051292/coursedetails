from django.shortcuts import render
from .models import CourseDetails


def class_review_view(request):

    courses = CourseDetails.objects.all()
    context = {'courses': courses}
    return render(request, 'coursereview.html', context)







