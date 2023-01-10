from email.policy import default
from random import choices
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE)
    # image = models.ImageField(default='profilepic.jpg',
    #                         upload_to='profile_pictures')
    street = models.CharField(max_length=200, null=True)
    #city = models.CharField(max_length=50, null=True)
    #province = models.CharField(max_length=50, null=True)
    #country = models.CharField(max_length=50, null=True)
    zipcode = models.CharField(max_length=10, null=True)
    #birthdate = models.DateField(null=True, blank=True)
    #phone = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.user.username


class User(models.Model):

    def __str__(self):
        return self.username

    COLOR_CHOICES = (
        ('counselor', 'Counselor'),
        ('doctor', 'Doctor'),
        ('patient', 'Patient'),
    )
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, null=True)
    specialist_id = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    password = models.CharField(max_length=50, null=True)
    password1 = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=400, null=True)
    city = models.CharField(max_length=100, null=True)
    province = models.CharField(max_length=100, null=True)
    zipcode = models.CharField(max_length=10, null=True)
    country = models.CharField(max_length=100, null=True)
    birthdate = models.DateField(null=True, blank=True)
    phone = models.IntegerField(null=True)
    category = models.CharField(
        max_length=50, choices=COLOR_CHOICES, default='patient')


class AssessmentTest(models.Model):

    def _str_(self):
        return self.username

    ANSWER_CHOICES = (
        ('Not at all', 'Not at all'),
        ('Several Days', 'Several Days'),
        ('More than half the Days', 'More than half the Days'),
        ('Nearly everydays', 'Nearly everydays')
    )

    DAY = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
        ('13', '13'),
        ('14', '14'),
        ('15', '15'),
        ('16', '16'),
        ('17', '17'),
        ('18', '18'),
        ('19', '19'),
        ('20', '20'),
        ('21', '21'),
        ('22', '22'),
        ('23', '23'),
        ('24', '24'),
        ('25', '25'),
        ('26', '26'),
        ('27', '27'),
        ('28', '28'),
        ('29', '29'),
        ('30', '30'),
        ('31', '31'),
    )

    MONTH = (
        ('Jan', 'Jan'),
        ('Feb', 'Feb'),
        ('Mar', 'Mar'),
        ('Apr', 'Apr'),
        ('May', 'May'),
        ('June', 'June'),
        ('July', 'July'),
        ('Aug', 'Aug'),
        ('Sep', 'Sep'),
        ('Oct', 'Oct'),
        ('Nov', 'Nov'),
        ('Dec', 'Dec'),
    )

    YEAR = (
        ('2022', '2022'),
        ('2023', '2023'),
        ('2024', '2024'),
        ('2025', '2025'),
    )

    HOUR = (
        ('00', '00'),
        ('01', '01'),
        ('02', '02'),
        ('03', '03'),
        ('04', '04'),
        ('05', '05'),
        ('06', '06'),
        ('07', '07'),
        ('08', '08'),
        ('09', '09'),
        ('10', '10'),
        ('11', '11'),
    )

    MIN = (
        ('00', '00'),
        ('15', '15'),
        ('30', '30'),
        ('45', '45'),
    )

    AM_PM = (
        ('AM', 'AM'),
        ('PM', 'PM'),
    )

    # user_id = models.IntegerField(null=True)
    username = models.CharField(max_length=200)
    answer_1 = models.CharField(
        max_length=200, choices=ANSWER_CHOICES, default='Not at all')
    answer_2 = models.CharField(
        max_length=200, choices=ANSWER_CHOICES, default='Not at all')
    answer_3 = models.CharField(
        max_length=200, choices=ANSWER_CHOICES, default='Not at all')
    answer_4 = models.CharField(
        max_length=200, choices=ANSWER_CHOICES, default='Not at all')
    answer_5 = models.CharField(
        max_length=200, choices=ANSWER_CHOICES, default='Not at all')
    answer_6 = models.CharField(
        max_length=200, choices=ANSWER_CHOICES, default='Not at all')
    answer_7 = models.CharField(
        max_length=200, choices=ANSWER_CHOICES, default='Not at all')
    answer_8 = models.CharField(
        max_length=200, choices=ANSWER_CHOICES, default='Not at all')
    answer_9 = models.CharField(
        max_length=200, choices=ANSWER_CHOICES, default='Not at all')
    state = models.IntegerField(default=0)
    appointmentDay = models.CharField(max_length=2, null=True)
    appointmentMonth = models.CharField(max_length=4, null=True)
    appointmentYear = models.CharField(max_length=4, null=True)
    appointmentHour = models.CharField(max_length=2, null=True)
    appointmentMin = models.CharField(max_length=2, null=True)
    appointmentAmPm = models.CharField(max_length=2, null=True)
