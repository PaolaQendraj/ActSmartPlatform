from django.db import models

# Create your models here.
class Index_Header(models.Model):
    line_one = models.CharField(max_length=50)
    line_two = models.CharField(max_length=150)
    line_three = models.CharField(max_length=100)
    images = models.ImageField(upload_to='media', null=True, blank=True)

    def __str__(self):
        return 'Content'

class Services_Content(models.Model):
    line_one = models.CharField(max_length=50)
    line_two = models.CharField(max_length=300)
    line_three = models.CharField(max_length=100)

    def __str__(self):
        return 'Content'

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

class Mentor_Content(models.Model):
    line_one = models.CharField(max_length=100)
    line_two = models.CharField(max_length=50)
    line_three = models.CharField(max_length=300)

    def __str__(self):
        return 'Content'

class Mentor_Features(models.Model):
    feature = models.CharField(max_length=100)

    def __str__(self):
        return self.feature

class Trainings_Page(models.Model):
    name = models.CharField(max_length=100)
    desctiption = models.CharField(max_length=500)
    images = models.ImageField(upload_to='media')
    deadline = models.DateField()

    def __str__(self):
        return self.name

class Enroll_Page(models.Model):
    line_one = models.CharField(max_length=60)
    line_two = models.CharField(max_length=100)
    line_three = models.CharField(max_length=100)
    line_four = models.CharField(max_length=100)
    line_five = models.CharField(max_length=100)
    images = models.ImageField(upload_to='media')
    line_six = models.CharField(max_length=250)
    line_seven = models.CharField(max_length=250, default='', blank=True, null=True)
    line_eight = models.CharField(max_length=250, default='', blank=True, null=True)
    instagram_account = models.CharField(max_length=20)
    instagram_link = models.CharField(max_length=50, default='')

    def __str__(self):
        return 'Content'


class Enroll_Content_List(models.Model):
    item = models.CharField(max_length=120)

    def __str__(self):
        return self.item

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
    category_two = models.ForeignKey(Opportunitie, on_delete=models.CASCADE, null=True, blank=True)
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

class Footer(models.Model):
    line_one = models.CharField(max_length=100)
    line_two = models.CharField(max_length=100)
    link_facebook = models.CharField(max_length=70)
    link_instagram = models.CharField(max_length=70)
    link_linkedin = models.CharField(max_length=70)
    link_pinterest = models.CharField(max_length=70)
    link_gmail = models.CharField(max_length=70)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    email = models.CharField(max_length=40)
    copyright_text = models.CharField(max_length=50)
    copyright_link = models.CharField(max_length=30)

    def __str__(self):
        return 'Footer'


class Call_Mentor(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50)
    opportunity_name = models.CharField(max_length=50)
    opportunity_selected = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name


class Countrie(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Trainings_Registration(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50)
    gender = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    training = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Enrolled(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=20, default='')
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    payment = models.CharField(max_length=20)

    def __str__(self):
        return self.name + ' ' + self.surname


class Subscription(models.Model):
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.email