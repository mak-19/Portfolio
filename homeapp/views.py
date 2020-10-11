from django.shortcuts import render
from django.http import HttpResponse
from .models import Intro, Resume, MySkill, MyProject

# intro = [
#     {
#         'name':"Hi I'm Mayank",
#         'title':'I am looking for a job as Python/Django Developer.'
#     }
# ]

# aboutme = [
#     {
#         'f1':'I am Mayank Sharma. I am innovative, hard working and capable of collaborating with team. I am looking for an opportunity as Python/Django Developer.',
#         'f2':'I am B.Tech 2019 batch passout from KIET Group of Institutions, Ghaziabad Uttar Pradesh in Electronics and Communication Engineering. My B.Tech overall aggregate is 72.23%.',
#         'f3':'I belong to Unnao Uttar Pradesh. I have done my 12th from Sun De Sun Public Inter College and my 12th class percentage is 83.8%. I have done my 10th from C S A Inter College and my 10th class percentage is 77.5%.'
#     }
# ]




# Create your views here.
def home(request):
    context = {
        # 'intro':intro,
        'intro':Intro.objects.all(),
        'aboutme':Resume.objects.all(),
        'myskills':MySkill.objects.all(),
        'myprojects':MyProject.objects.all()
    }
    return render(request,'homeapp/home.html', context)
    