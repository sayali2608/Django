from django.shortcuts import render, redirect
from users.models import User, AssessmentTest

# Create your views here.


def doctors(request):
    username = request.session["username"]
    # specialist_id = request.POST['specialist_id']
    all_users = User.objects.all()
    all_assessment_test = AssessmentTest.objects.all()
    patientHaveTest = []
    for user in all_users:
        for assessment_test in all_assessment_test:
            if user.username == assessment_test.username and user.specialist_id == username:
                patientHaveTest.append(user)
    return render(request, 'doctors/doctors.html', {'all_users': patientHaveTest, 'username': username})


def testResult(request):
    username = request.POST['username']
    specialistusername = request.POST['specialistusername']
    all_assessment_test = AssessmentTest.objects.get(username=username)
    return render(request, 'doctors/testResult.html', {'all_assessment_test': all_assessment_test, 'specialistusername': specialistusername})


def assign(request):
    specialist = request.GET.get("specialist")
    username = request.GET.get("username")
    year = request.GET.get("year")
    month = request.GET.get("month")
    day = request.GET.get("day")
    hour = request.GET.get("hour")
    min = request.GET.get("min")
    AM_PM = request.GET.get("AM_PM")
    usernameprofile = request.GET.get("usernameprofile")
    if (specialist == "Reject"):
        AssessmentTest.objects.filter(username=username).update(state=-1)
        User.objects.filter(username=username).update(specialist_id="Rejected")
    else:
        AssessmentTest.objects.filter(username=username).update(state=1, appointmentYear=year, appointmentMonth=month,
                                                                appointmentDay=day, appointmentHour=hour, appointmentMin=min, appointmentAmPm=AM_PM)
        User.objects.filter(username=username).update(specialist_id=specialist)
    all_assessment_test = AssessmentTest.objects.get(username=username)
    request.session['username'] = usernameprofile
    return redirect("doctors")
