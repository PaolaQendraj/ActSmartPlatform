from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone

from .models import Index_Header, Services_Content, Services_Item, Mentor_Content, Mentor_Features, Opportunitie,Trainings_Page, \
    Footer, Enroll_Page, Enroll_Content_List, Instagram, Scholarship_Opportunitie, Program_Opportunitie, Call_Mentor,\
    Countrie, Trainings_Registration, Enrolled, Subscription
# Create your views here.
def index(request):
    if request.method == 'GET':
        header = Index_Header.objects.all()
        header1 = header[0]
        services_content = Services_Content.objects.all()
        services_content1 = services_content[0]
        services = Services_Item.objects.all()
        mentor_content = Mentor_Content.objects.all()
        mentor_content1 = mentor_content[0]
        mentor_features = Mentor_Features.objects.all
        opportunity = Opportunitie.objects.all()
        scholarships = Scholarship_Opportunitie.objects.all()
        programs = Program_Opportunitie.objects.all()
        footer = Footer.objects.all()
        footer1 = footer[0]
        context = {'header': header1, 'services_content': services_content1, 'services': services, 'mentor_content':
            mentor_content1, 'mentor_features': mentor_features, 'opportunity': opportunity,
                   'scholarships': scholarships, 'programs': programs, 'footer': footer1}
        return render(request, 'index.html', context)

def scholarships(request):
    if request.method == 'GET':
        today = timezone.now().date()
        bachelor_name = 'Bachelor'
        master_name = 'Master'
        phd_name = 'PHD'
        fellowship_name = 'Fellowship'
        bachelor = Scholarship_Opportunitie.objects.filter(category__category__contains=bachelor_name)
        master = Scholarship_Opportunitie.objects.filter(category__category__contains=master_name)
        phd = Scholarship_Opportunitie.objects.filter(category__category__contains=phd_name)
        fellowship = Scholarship_Opportunitie.objects.filter(category__category__contains=fellowship_name)
        mentor_content = Mentor_Content.objects.all()
        mentor_content1 = mentor_content[0]
        mentor_features = Mentor_Features.objects.all
        footer = Footer.objects.all()
        footer1 = footer[0]
        scholarships = Scholarship_Opportunitie.objects.all()
        programs = Program_Opportunitie.objects.all()
        context = {'bachelor': bachelor, 'master': master, 'phd': phd, 'fellowship': fellowship,'footer': footer1,
            'mentor_content': mentor_content1, 'mentor_features': mentor_features, 'scholarships': scholarships,
                   'programs': programs, 'today': today}
        return render(request, 'scholarships.html', context)

def programs(request):
    if request.method == 'GET':
        today = timezone.now().date()
        training_name = 'Trainings & Conferences'
        training = Program_Opportunitie.objects.filter(category__category__contains=training_name)
        jobs_name = 'Jobs & Internships'
        jobs = Program_Opportunitie.objects.filter(category__category__contains=jobs_name)
        contests_name = 'Contests & Grants'
        contests = Program_Opportunitie.objects.filter(category__category__contains=contests_name)
        volunteering_name = 'Volunteering'
        volunteering = Program_Opportunitie.objects.filter(category__category__contains=volunteering_name)
        mentor_content = Mentor_Content.objects.all()
        mentor_content1 = mentor_content[0]
        mentor_features = Mentor_Features.objects.all
        footer = Footer.objects.all()
        footer1 = footer[0]
        scholarships = Scholarship_Opportunitie.objects.all()
        programs = Program_Opportunitie.objects.all()
        context = {'training': training, 'jobs': jobs, 'contests': contests,'volunteering':volunteering, 'footer': footer1, \
                   'mentor_content':mentor_content1, 'mentor_features': mentor_features,
                   'scholarships': scholarships, 'programs': programs, 'today': today}
        return render(request, 'programs.html', context)

def trainings(request):
    if request.method == 'GET':
        training = Trainings_Page.objects.all()
        training1 = training[0]
        training2 = training[1]
        mentor_content = Mentor_Content.objects.all()
        mentor_content1 = mentor_content[0]
        mentor_features = Mentor_Features.objects.all
        footer = Footer.objects.all()
        footer1 = footer[0]
        scholarships = Scholarship_Opportunitie.objects.all()
        programs = Program_Opportunitie.objects.all()
        context = {
            'training1': training1, 'training2': training2, 'mentor_content': mentor_content1, 'mentor_features': \
            mentor_features, 'footer': footer1, 'scholarships': scholarships, 'programs': programs,
        }
        return render(request, 'trainings.html', context)

def enroll(request):
    if request.method == 'GET':
        content = Enroll_Page.objects.all()
        content1 = content[0]
        content_list = Enroll_Content_List.objects.all()
        instagram = Instagram.objects.all()
        countries = Countrie.objects.all()
        mentor_content = Mentor_Content.objects.all()
        mentor_content1 = mentor_content[0]
        mentor_features = Mentor_Features.objects.all
        footer = Footer.objects.all()
        footer1 = footer[0]
        scholarships = Scholarship_Opportunitie.objects.all()
        programs = Program_Opportunitie.objects.all()
        context = {
            'content': content1, 'content_list': content_list, 'instagram': instagram, 'footer': footer1,
            'mentor_content': mentor_content1, 'mentor_features': mentor_features, 'scholarships': scholarships,
            'programs': programs, 'countries':countries}
        return render(request, 'enrollme.html', context)
    else:
        from django.core.validators import validate_email
        from django.core.exceptions import ValidationError
        enroll = request.POST
        name = enroll['name']
        surname = enroll['surname']
        email = enroll['email']
        phone = enroll['phone']
        address = enroll['address']
        city = enroll['city']
        country = enroll['country']
        payment = enroll['payment']
        try:
            validate_email(email)
            InsertEnroll = Enrolled(name=name, surname=surname, email=email, phone=phone, address=address,
                                        city=city, country=country, payment=payment)
            InsertEnroll.save()
            subject = 'Enroll Form'
            full_message = 'This email was sent from: ' + name + ' ' + surname +'\nEmail: ' + email + '\nPhone Nr: ' \
                           + phone + '\nAddress: ' + address + '\nCity: ' + city + '\nCountry: ' + country + \
                           '\nPayment:' + payment
            send_mail(subject,
                      full_message,
                      settings.EMAIL_HOST_USER,
                      ['paolaqendraj@gmail.com'],
                      fail_silently=False)
            if payment == 'PayPal':
                return HttpResponseRedirect('https://www.paypal.com/')
            else:
                return HttpResponseRedirect('/')
        except ValidationError:
            email_error = "Your email is incorrect"
            header = Index_Header.objects.all()
            header1 = header[0]
            services_content = Services_Content.objects.all()
            services_content1 = services_content[0]
            services = Services_Item.objects.all()
            opportunity = Opportunitie.objects.all()
            scholarships = Scholarship_Opportunitie.objects.all()
            programs = Program_Opportunitie.objects.all()
            mentor_content = Mentor_Content.objects.all()
            mentor_content1 = mentor_content[0]
            mentor_features = Mentor_Features.objects.all
            footer = Footer.objects.all()
            footer1 = footer[0]
            context = {
                'header': header1, 'services_content': services_content1, 'services': services, 'mentor_content':
            mentor_content1, 'mentor_features': mentor_features, 'opportunity': opportunity,
                   'scholarships': scholarships, 'programs': programs, 'footer': footer1, 'email_error':email_error
            }
            return render(request, 'index.html', context)






def template_opp_scholarships(request, category):
    if request.method == 'GET':
        today = timezone.now().date()
        scholarship = Scholarship_Opportunitie.objects.filter(category__category__contains=category)
        mentor_content = Mentor_Content.objects.all()
        mentor_content1 = mentor_content[0]
        mentor_features = Mentor_Features.objects.all
        footer = Footer.objects.all()
        footer1 = footer[0]
        scholarships = Scholarship_Opportunitie.objects.all()
        programs = Program_Opportunitie.objects.all()
        trainings = Trainings_Page.objects.all()
        countries = Countrie.objects.all()
        context = {'scholarship': scholarship, 'category': category, 'footer': footer1, 'mentor_content':
            mentor_content1, 'mentor_features': mentor_features, 'scholarships': scholarships, 'programs': programs,
                   'trainings': trainings, 'countries': countries, 'today': today}
        return render(request, 'template_opp.html', context)

def template_opp_programs(request, category):
    if request.method == 'GET':
        today = timezone.now().date()
        program = Program_Opportunitie.objects.filter(category__category__contains=category)
        mentor_content = Mentor_Content.objects.all()
        mentor_content1 = mentor_content[0]
        mentor_features = Mentor_Features.objects.all
        footer = Footer.objects.all()
        footer1 = footer[0]
        scholarships = Scholarship_Opportunitie.objects.all()
        programs = Program_Opportunitie.objects.all()
        trainings = Trainings_Page.objects.all()
        countries = Countrie.objects.all()
        context = {'program': program, 'category': category, 'footer': footer1, 'mentor_content':
            mentor_content1, 'mentor_features': mentor_features, 'scholarships': scholarships, 'programs': programs,
                   'trainings': trainings, 'countries': countries, 'today': today}
        return render(request, 'template_opp_programs.html', context)

def template_scholarship(request):
    template_id = request.GET['id']
    scholarship = Scholarship_Opportunitie.objects.get(id=template_id)
    tags = scholarship.tags
    cat = tags.split(",")
    founded = scholarship.founded_features
    features = founded.split(",")
    training = Trainings_Page.objects.all()
    mentor_content = Mentor_Content.objects.all()
    mentor_content1 = mentor_content[0]
    mentor_features = Mentor_Features.objects.all
    footer = Footer.objects.all()
    footer1 = footer[0]
    scholarships = Scholarship_Opportunitie.objects.all()
    programs = Program_Opportunitie.objects.all()
    trainings = Trainings_Page.objects.all()
    countries = Countrie.objects.all()
    context = {'scholarship': scholarship, 'training': training, 'cat': cat, 'features': features,'footer': footer1,'mentor_content':mentor_content1,
    'mentor_features':mentor_features, 'scholarships': scholarships, 'programs': programs, 'trainings': trainings, 'countries': countries}
    return render(request, 'template_scholarships.html', context)

def template_programs(request):
    template_id = request.GET['id']
    program = Program_Opportunitie.objects.get(id=template_id)
    training = Trainings_Page.objects.all()
    tags = program.tags
    cat = tags.split(",")
    founded = program.founded_features
    features = founded.split(",")
    mentor_content = Mentor_Content.objects.all()
    mentor_content1 = mentor_content[0]
    mentor_features = Mentor_Features.objects.all
    footer = Footer.objects.all()
    footer1 = footer[0]
    scholarships = Scholarship_Opportunitie.objects.all()
    programs = Program_Opportunitie.objects.all()
    trainings = Trainings_Page.objects.all()
    countries = Countrie.objects.all()
    context = {'program': program, 'training': training, 'footer': footer1, 'cat': cat, 'features': features,'mentor_content': mentor_content1,
               'mentor_features': mentor_features, 'scholarships': scholarships, 'programs': programs, 'trainings': trainings, 'countries': countries}
    return render(request, 'template_programs.html', context)


def call_mentor(request):
    if request.method == 'POST':
        from django.core.validators import validate_email
        from django.core.exceptions import ValidationError
        mentor = request.POST
        full_name = mentor['name']
        email = mentor['email']
        phone = mentor['phone']
        opportunity_name = mentor['opportunity']
        opportunity_selected = mentor['available']
        try:
            validate_email(email)
            InsertMentor = Call_Mentor(full_name=full_name, email=email, phone=phone, opportunity_name=opportunity_name, opportunity_selected=opportunity_selected)
            InsertMentor.save()
            subject = 'Call A Mentor Form'
            full_message = 'This email was sent from: ' + full_name + '\nEmail: ' + email + '\nPhone Nr: ' + phone + \
                           '\nOpportunity Category: ' + opportunity_name + '\nOpportunity Selected: ' + opportunity_selected
            send_mail(subject,
                      full_message,
                      settings.EMAIL_HOST_USER,
                      ['info@actsmartprogram.com'],
                      fail_silently=False)
            return HttpResponseRedirect('/')
        except ValidationError:
            email_error = "Your email is incorrect"
            header = Index_Header.objects.all()
            header1 = header[0]
            services_content = Services_Content.objects.all()
            services_content1 = services_content[0]
            services = Services_Item.objects.all()
            opportunity = Opportunitie.objects.all()
            scholarships = Scholarship_Opportunitie.objects.all()
            programs = Program_Opportunitie.objects.all()
            mentor_content = Mentor_Content.objects.all()
            mentor_content1 = mentor_content[0]
            mentor_features = Mentor_Features.objects.all
            footer = Footer.objects.all()
            footer1 = footer[0]
            context = {
                'header': header1, 'services_content': services_content1, 'services': services, 'mentor_content':
            mentor_content1, 'mentor_features': mentor_features, 'opportunity': opportunity,
                   'scholarships': scholarships, 'programs': programs, 'footer': footer1, 'email_error':email_error
            }
            return render(request, 'index.html', context)

def register(request):
    if request.method == 'POST':
        from django.core.validators import validate_email
        from django.core.exceptions import ValidationError
        register = request.POST
        name = register['name']
        email = register['email']
        phone = register['phone']
        gender = register['gender']
        country = register['country']
        training = register['training']
        try:
            validate_email(email)
            InsertRegistration = Trainings_Registration(name=name, email=email, phone=phone, gender=gender,
                                                        country=country, training=training)
            InsertRegistration.save()
            subject = 'Registration Form'
            full_message = 'This email was sent from: ' + name + '\nEmail: ' + email + '\nPhone Nr: ' + phone + \
                           '\nGender: ' + gender + '\nCountry: ' + country + '\nTraining:' + training
            send_mail(subject,
                      full_message,
                      settings.EMAIL_HOST_USER,
                      ['paolaqendraj@gmail.com'],
                      fail_silently=False)
            return HttpResponseRedirect('/')
        except ValidationError:
            email_error = "Your email is incorrect"
            header = Index_Header.objects.all()
            header1 = header[0]
            services_content = Services_Content.objects.all()
            services_content1 = services_content[0]
            services = Services_Item.objects.all()
            opportunity = Opportunitie.objects.all()
            scholarships = Scholarship_Opportunitie.objects.all()
            programs = Program_Opportunitie.objects.all()
            mentor_content = Mentor_Content.objects.all()
            mentor_content1 = mentor_content[0]
            mentor_features = Mentor_Features.objects.all
            footer = Footer.objects.all()
            footer1 = footer[0]
            context = {
                'header': header1, 'services_content': services_content1, 'services': services, 'mentor_content':
            mentor_content1, 'mentor_features': mentor_features, 'opportunity': opportunity,
                   'scholarships': scholarships, 'programs': programs, 'footer': footer1, 'email_error':email_error
            }
            return render(request, 'index.html', context)

def subscriptions(request):
    if request.method == 'POST':
        from django.core.validators import validate_email
        from django.core.exceptions import ValidationError
        subscribe = request.POST
        email = subscribe['email']
        try:
            validate_email(email)
            InsertSubcription = Subscription(email=email)
            InsertSubcription.save()
            subject = 'Subscription Form'
            full_message = 'Email:  ' + email
            send_mail(subject,
                      full_message,
                      settings.EMAIL_HOST_USER,
                      ['paolaqendraj@gmail.com'],
                      fail_silently=False)
            return HttpResponseRedirect('/')
        except ValidationError:
            email_error = "Your email is incorrect"
            header = Index_Header.objects.all()
            header1 = header[0]
            services_content = Services_Content.objects.all()
            services_content1 = services_content[0]
            services = Services_Item.objects.all()
            opportunity = Opportunitie.objects.all()
            scholarships = Scholarship_Opportunitie.objects.all()
            programs = Program_Opportunitie.objects.all()
            mentor_content = Mentor_Content.objects.all()
            mentor_content1 = mentor_content[0]
            mentor_features = Mentor_Features.objects.all
            footer = Footer.objects.all()
            footer1 = footer[0]
            context = {
                'header': header1, 'services_content': services_content1, 'services': services, 'mentor_content':
                    mentor_content1, 'mentor_features': mentor_features, 'opportunity': opportunity,
                'scholarships': scholarships, 'programs': programs, 'footer': footer1, 'email_error': email_error
            }
            return render(request, 'index.html', context)


def search(request):
    if request.method == 'POST':
        search = request.POST
        tag = search['tag']
        if tag == 'Scholarship' or tag == 'scholarship' or tag == 'Scholarships' or tag == 'scholarships':
            return HttpResponseRedirect('/scholarships/')
        elif tag == 'Program' or tag == 'Programs' or tag == 'program' or tag == 'programs':
            return HttpResponseRedirect('/programs/')
        elif tag == 'Bachelor' or tag == 'bachelor' or tag == 'BACHELOR':
            return HttpResponseRedirect('/Bachelor/')
        elif tag == 'Master' or tag == 'master' or tag == 'MASTER':
            return HttpResponseRedirect('/Master/')
        elif tag == 'PHD' or tag == 'phd' or tag == 'Phd':
            return HttpResponseRedirect('/PHD/')
        elif tag == 'Fellowship' or tag == 'FELLOWSHIP' or tag == 'Fellowships' or tag == 'fellowships':
            return HttpResponseRedirect('/Fellowship/')
        elif tag == 'Trainings' or tag == 'Training' or tag == 'trainings' or tag == 'training' or tag == 'TRAININGS' or tag == 'TRAINING':
            return HttpResponseRedirect('/Trainings%20&%20Conferences/')
        elif tag == 'Conference' or tag == 'Conferences' or tag == 'conference' or tag == 'conferences' or tag == \
                'CONFERENCES' or tag == 'CONFERENCE':
            return HttpResponseRedirect('/Trainings%20&%20Conferences/')
        elif tag == 'Jobs' or tag == 'Job' or tag == 'job' or tag == 'jobs' or tag == \
                'JOB' or tag == 'JOBS':
            return HttpResponseRedirect('/Jobs%20&%20Internships/')
        elif tag == 'Internships' or tag == 'Internship' or tag == 'internships' or tag == 'internship' or tag == \
                'INTERNSHIPS' or tag == 'INTERNSHIP':
            return HttpResponseRedirect('/Jobs%20&%20Internships/')
        elif tag == 'Contests' or tag == 'Contest' or tag == 'contests' or tag == 'contest' or tag == \
                'CONTESTS' or tag == 'CONTEST':
            return HttpResponseRedirect('/Contests%20&%20Grants/')
        elif tag == 'Grants' or tag == 'Grant' or tag == 'grants' or tag == 'grant' or tag == \
                'GRANTS' or tag == 'GRANT':
            return HttpResponseRedirect('/Contests%20&%20Grants/')
        elif tag == 'Grants' or tag == 'Grant' or tag == 'grants' or tag == 'grant' or tag == \
                'GRANTS' or tag == 'GRANT':
            return HttpResponseRedirect('/Contests%20&%20Grants/')
        elif tag == 'Volunteering' or tag == 'volunteering' or tag == 'Volunteer' or tag == 'volunteers' or tag == \
                'VOLUNTEERS' or tag == 'VOLUNTEER':
            return HttpResponseRedirect('/Volunteering/')