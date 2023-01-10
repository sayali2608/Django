from users.models import User



def get_number_users(request):
    patients = User.objects.filter(category='patient').count()
    doctors = User.objects.filter(category='doctor').count()
    counselors = User.objects.filter(category='counselor').count()

    return {
        'patients': patients,
        'doctors': doctors,
        'counselors': counselors,
    }
