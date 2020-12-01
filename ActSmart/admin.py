from django.contrib import admin
from .models import Services_Item, Opportunitie, \
    Footer, Training, Training_Registration, Instagram, Scholarship_Opportunitie, \
    Program_Opportunitie, Opportunities_Category, Call_Mentor, \
    Subscription, User_Profile, AddToProfile_Scholarship, AddToProfile_Program, \
    Testimonial, Opportunity_Category_Region, Booking_Date, Booking_Time, Booking_Info, Topic_Suggestions, Premium_Registration, Simple_Registration

# Register your models here.
admin.site.register(Services_Item)
admin.site.register(Opportunitie)
admin.site.register(Training)
admin.site.register(Training_Registration)
admin.site.register(Instagram)
admin.site.register(Scholarship_Opportunitie)
admin.site.register(Program_Opportunitie)
admin.site.register(Opportunities_Category)
admin.site.register(Opportunity_Category_Region)
admin.site.register(Call_Mentor)
admin.site.register(Subscription)
admin.site.register(Footer)
admin.site.register(User_Profile)
admin.site.register(AddToProfile_Scholarship)
admin.site.register(AddToProfile_Program)
admin.site.register(Testimonial)
admin.site.register(Booking_Date)
admin.site.register(Booking_Time)
admin.site.register(Booking_Info)
admin.site.register(Topic_Suggestions)
admin.site.register(Premium_Registration)
admin.site.register(Simple_Registration)

