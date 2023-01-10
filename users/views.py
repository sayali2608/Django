from .forms import RegisterSpecialist, RegisterUser, SaveQuestions, UserLogin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from users.models import User, AssessmentTest


def register(request):
    form = RegisterUser(request.POST or None)

    if form.is_valid():
        form.save()
        messages.success(request, 'Registration Successful.')
        return redirect('login')
    else:
        return render(request, "users/register.html", {'form': form})


@login_required
def profilepage(request):
 #   if request.method == 'POST':
 #       form = ProfileForm(request.POST)
 #       if form.is_valid():
 #           form.save()
 #   else:
 #       form = ProfileForm()
    return render(request, 'users/profile.html')


def home(request):
    return render(request, 'users/home.html')


def register_specialist(request):
    form = RegisterSpecialist(request.POST or None)

    if form.is_valid():
        form.save()
        messages.success(request, 'Registration Successful.')
        return redirect('login')
    else:
        return render(request, "users/register_specialist.html", {'form': form})


def save_questions(request):
    username = request.session["username"]
    form = SaveQuestions(request.POST or None)
    all_users = AssessmentTest.objects.all()
    for user in all_users:
        if user.username == username:
            # send message that you do in before
            messageTxt = ""
            item = AssessmentTest.objects.get(username=username)
            userFound = User.objects.get(username=username)
            if item.state == 1:
                if item.appointmentDay is None:
                    messageTxt = "you are assiged to doctor" + userFound.specialist_id + \
                        ". Doctor will further assess your test."
                else:
                    appointmentDate = item.appointmentDay + "-" + \
                        item.appointmentMonth + "-" + item.appointmentYear
                    appointmentTime = item.appointmentHour + ":" + \
                        item.appointmentMin + " " + item.appointmentAmPm
                    messageTxt = "you are assiged to " + userFound.specialist_id + \
                        ". Your appointment time is on " + appointmentDate + " at " + appointmentTime
            elif item.state == 0:
                messageTxt = "You have taken the test. Please wait for results"
            else:
                messageTxt = "you do not require further appointment. You are rejected"
            return render(request, "users/userHomePage.html", {'username': username, 'messageTxt': messageTxt, 'state': item.state})
        else:
            messageTxt = "You have taken the test. Please wait for results"
            if form.is_valid():
                form.save()
                return render(request, "users/userHomePage.html", {'username': username, 'messageTxt': messageTxt, 'state': 0})
    if len(all_users) <= 0:
        if form.is_valid():
            form.save()

    return render(request, "users/base.html", {'form': form, 'username': username})


def loginPage(request):

    form = UserLogin(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        all_users = User.objects.all()
        for user in all_users:
            if (username == user.username) & (password == user.password):
                if user.category == "patient":
                    user_id = user.user_id
                    form = SaveQuestions(request.POST or None)
                    request.session['username'] = username
                    return redirect('test')
                if user.category == "doctor":
                    request.session['username'] = username
                    return redirect("doctors")
                if user.category == "counselor":
                    request.session['username'] = username
                    return redirect("counselors")
        return render(request, "users/password.html", {'form': form})

    else:
        return render(request, "users/password.html", {'form': form})
