from django.contrib import admin
from .models import User, AssessmentTest, Profile
from django.db.models.signals import post_delete
from django.dispatch import receiver
# Register your models here.

# admin.site.register(Profile)
admin.site.register(User)
admin.site.register(AssessmentTest)

@receiver(post_delete, sender=User)
def signal_function_name(sender, instance, using, **kwargs):
    if(instance.category == 'doctor' or instance.category == 'councelor'):
        specialistUsername = instance.username
        all_users = User.objects.filter(category='patient')
        all_assessment_test = AssessmentTest.objects.all()

        for user in all_users:
            for assessment_test in all_assessment_test:
                if user.username == assessment_test.username:
                    if assessment_test.state == 1 and user.specialist_id == specialistUsername:
                        AssessmentTest.objects.filter(username=user.username).update(
                        state=0, appointmentYear='', appointmentMonth='', appointmentDay='', appointmentHour='', appointmentMin='', appointmentAmPm='')
                        User.objects.filter(username=user.username).update(specialist_id='unassigned')
                        #delete assesment when patient delete
    elif(instance.category == 'patient'):
        patientUsername = instance.username
        all_assessment_test = AssessmentTest.objects.all()
        for assessment_test in all_assessment_test:
            if patientUsername == assessment_test.username:
                AssessmentTest.objects.filter(username=patientUsername).delete()

