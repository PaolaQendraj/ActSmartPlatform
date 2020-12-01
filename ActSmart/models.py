from datetime import timedelta

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.utils.datetime_safe import datetime

class Services_Item(models.Model):
    name = models.CharField(max_length=20)
    icon = models.CharField(max_length=100)
    link = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Opportunitie(models.Model):
    name = models.CharField(max_length=50)
    link = models.CharField(max_length=40, default='')

    def __str__(self):
        return self.name

class Training(models.Model):
    name = models.CharField(max_length=100)
    hours = models.CharField(max_length=30, default='')
    price = models.FloatField(null=True, blank=True)
    language = models.CharField(max_length=30, default='')
    description = models.TextField(default='')
    images = models.ImageField(upload_to='media')
    small_image = models.ImageField(upload_to='media', null=True)
    YES = 'Y'
    NO = 'N'
    TYPE_CHOICES = [
        (YES, 'Yes'),
        (NO, 'No'),
    ]
    available = models.CharField(
        max_length=2,
        choices=TYPE_CHOICES,
        default=NO
    )
    deadline = models.DateField()

    def __str__(self):
        return self.name

class Topic_Suggestions(models.Model):
    topic = models.TextField()

    def __str__(self):
        return self.topic

class Training_Registration(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=20, default='')
    training = models.ForeignKey(Training, on_delete=models.CASCADE, null=True, blank=True)
    date_register = models.DateField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name + self.training.name

class Instagram(models.Model):
    image = models.ImageField(upload_to='media')
    link = models.CharField(max_length=60)

    def __str__(self):
        return 'Image'

class Opportunities_Category(models.Model):
    category = models.CharField(max_length=40)

    def __str__(self):
        return self.category

class Scholarship_Opportunitie(models.Model):
    title = models.CharField(max_length=170)
    category = models.ForeignKey(Opportunities_Category, on_delete=models.CASCADE, null=True, blank=True)
    image_big = models.ImageField(upload_to='media')
    image_small = models.ImageField(upload_to='media', null=True)
    deadline = models.DateField()
    location = models.CharField(max_length=50)
    objectives = models.CharField(max_length=500)
    description = models.TextField()
    small_description = models.CharField(max_length=500, default='')
    YES = 'Y'
    NO = 'N'
    TYPE_CHOICES = [
        (YES, 'Yes'),
        (NO, 'No'),
    ]
    founded = models.CharField(
        max_length=2,
        choices=TYPE_CHOICES,
        default=NO
    )
    founded_features = models.TextField(default='',null=True, blank=True)
    eligibility = models.TextField()
    tags = models.TextField(default='')
    official_link = models.CharField(max_length=200, default='', null=True, blank=True)

    def __str__(self):
        return self.title

class Program_Opportunitie(models.Model):
    title = models.CharField(max_length=170)
    category = models.ForeignKey(Opportunities_Category, on_delete=models.CASCADE, null=True, blank=True)
    image_big = models.ImageField(upload_to='media')
    image_small = models.ImageField(upload_to='media', null=True)
    deadline = models.DateField()
    location = models.CharField(max_length=50)
    objectives = models.CharField(max_length=500)
    description = models.TextField()
    small_description = models.CharField(max_length=500, default='')
    YES = 'Y'
    NO = 'N'
    TYPE_CHOICES = [
        (YES, 'Yes'),
        (NO, 'No'),
    ]
    founded = models.CharField(
        max_length=2,
        choices=TYPE_CHOICES,
        default=NO
    )
    founded_features = models.TextField(default='',null=True, blank=True)
    eligibility = models.TextField()
    tags = models.TextField(default='')
    official_link = models.CharField(max_length=200, default='', null=True, blank=True)

    def __str__(self):
        return self.title

class Opportunity_Category_Region(models.Model):
    category = models.ForeignKey(Opportunitie, on_delete=models.CASCADE, null=True, blank=True)
    region = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.category.name +  ' - ' + self.region


class Footer(models.Model):
    line_one = models.CharField(max_length=100)
    line_two = models.CharField(max_length=100)
    link_facebook = models.CharField(max_length=70)
    link_instagram = models.CharField(max_length=70)
    link_linkedin = models.CharField(max_length=70)
    link_pinterest = models.CharField(max_length=70)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    email = models.CharField(max_length=40)
    copyright_text = models.CharField(max_length=50)
    copyright_link = models.CharField(max_length=30)

    def __str__(self):
        return 'Footer'


class Call_Mentor(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, default='')
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50)
    date_register = models.DateField(default=datetime.now, blank=True)
    opportunity_category = models.CharField(max_length=50, default='')
    opportunity_name = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username + ' ' + self.opportunity_name


class Subscription(models.Model):
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.email


class User_Profile(models.Model):
    full_name = models.CharField(max_length=100, default='')
    email = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=100,default='')
    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'
    TYPE_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
    ]
    gender = models.CharField(
        max_length=3,
        choices=TYPE_CHOICES,
        default=OTHER
    )
    country = models.CharField(max_length=50, default='')
    city = models.CharField(max_length=50, default='')
    address = models.CharField(max_length=100, default='')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, default='')
    premium_account = models.CharField(max_length=20, default='N')

    def __str__(self):
        return self.full_name

class Premium_Registration(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField(null=True, blank=True)
    features = models.TextField(default='')

    def __str__(self):
        return self.title

class Simple_Registration(models.Model):
    title = models.CharField(max_length=50)
    features = models.TextField()

    def __str__(self):
        return self.title

class AddToProfile_Scholarship(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, default='')
    scholarships = models.ForeignKey(Scholarship_Opportunitie, on_delete=models.DO_NOTHING, default='')

class AddToProfile_Program(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, default='')
    programs = models.ForeignKey(Program_Opportunitie, on_delete=models.DO_NOTHING, default='')


class Testimonial(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=100)
    description = models.TextField(default='')
    image = models.ImageField(upload_to='media')

    def __str__(self):
        return self.name + ' ' + self.surname

class Booking_Date(models.Model):
    date = models.CharField(max_length=100)

    def __str__(self):
        return self.date


class Booking_Time(models.Model):
    date = models.ForeignKey(Booking_Date, on_delete=models.CASCADE, null=True, blank=True)
    time = models.CharField(max_length=100)
    YES = 'Y'
    NO = 'N'
    TYPE_CHOICES = [
        (YES, 'Yes'),
        (NO, 'No'),
    ]
    available = models.CharField(
        max_length=2,
        choices=TYPE_CHOICES,
        default=YES
    )

    def __str__(self):
        return self.date.date + ' ' + self.time

class Booking_Info(models.Model):
    fullname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    time = models.CharField(max_length=50)

    def __str__(self):
        return self.fullname + ', ' + self.date + ', ' + self.time

class Zoom_Link(models.Model):
    meeting = models.CharField(max_length=50)
    date = models.DateTimeField()
    link = models.TextField(default='')

    def __str__(self):
        return self.meeting
