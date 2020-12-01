from datetime import timedelta
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.mail import send_mail
import json
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.utils import timezone

from .models import Services_Item, Opportunitie, Training, Training_Registration, \
    Footer, Scholarship_Opportunitie, Program_Opportunitie, Call_Mentor, Subscription, User_Profile, AddToProfile_Scholarship, \
    AddToProfile_Program, Premium_Registration, Simple_Registration, \
    Testimonial, Opportunity_Category_Region, Booking_Date, Booking_Time, Booking_Info, Topic_Suggestions

# Create your views here.
def index(request):
    if request.method == 'GET':
        services = Services_Item.objects.all()
        service1 = services[0]
        service2 = services[1]
        service3 = services[2]
        opportunity = Opportunitie.objects.all()
        scholarships = Scholarship_Opportunitie.objects.all()
        programs = Program_Opportunitie.objects.all()
        cat_region = Opportunity_Category_Region.objects.all()

        testimonial = Testimonial.objects.all()
        footer = Footer.objects.all()
        footer1 = footer[0]

        bachelor = 'Bachelor'
        master = 'Master'
        php = 'PhD'
        fellowship = 'Fellowship'
        training = 'Trainings'
        conference = 'Conferences'
        jobs = 'Jobs'
        internship = 'Internships'
        contest = 'Contests'
        grants = 'Grants'
        volunteering = 'Volunteering'

        b_opp = Scholarship_Opportunitie.objects.filter(category__category=bachelor)
        b_sasi = 0
        for s in b_opp:
            b_sasi = b_sasi + 1

        m_opp = Scholarship_Opportunitie.objects.filter(category__category=master)
        m_sasi = 0
        for s in m_opp:
            m_sasi = m_sasi + 1

        p_opp = Scholarship_Opportunitie.objects.filter(category__category=php)
        p_sasi = 0
        for s in p_opp:
            p_sasi = p_sasi + 1

        f_opp = Scholarship_Opportunitie.objects.filter(category__category=fellowship)
        f_sasi = 0
        for s in f_opp:
            f_sasi = f_sasi + 1

        t_opp = Program_Opportunitie.objects.filter(category__category=training)
        t_sasi = 0
        for s in t_opp:
            t_sasi = t_sasi + 1

        c_opp = Program_Opportunitie.objects.filter(category__category=conference)
        c_sasi = 0
        for s in c_opp:
            c_sasi = c_sasi + 1

        j_opp = Program_Opportunitie.objects.filter(category__category=jobs)
        j_sasi = 0
        for s in j_opp:
            j_sasi = j_sasi + 1

        i_opp = Program_Opportunitie.objects.filter(category__category=internship)
        i_sasi = 0
        for s in i_opp:
            i_sasi = i_sasi + 1

        co_opp = Program_Opportunitie.objects.filter(category__category=contest)
        co_sasi = 0
        for s in co_opp:
            co_sasi = co_sasi + 1

        g_opp = Program_Opportunitie.objects.filter(category__category=grants)
        g_sasi = 0
        for s in g_opp:
            g_sasi = g_sasi + 1

        v_opp = Program_Opportunitie.objects.filter(category__category=volunteering)
        v_sasi = 0
        for s in v_opp:
            v_sasi = v_sasi + 1

        context = {'service1': service1, 'service2': service2, 'service3': service3, 'opportunity': opportunity, 'scholarships': scholarships,
                   'programs': programs, 'testimonial': testimonial, 'cat_region': cat_region, 'footer': footer1,
                   'b_sasi': b_sasi, 'm_sasi': m_sasi, 'p_sasi': p_sasi, 'f_sasi': f_sasi, 't_sasi': t_sasi, 'c_sasi': c_sasi,
                   'j_sasi': j_sasi, 'i_sasi': i_sasi, 'co_sasi': co_sasi, 'g_sasi': g_sasi, 'v_sasi': v_sasi}
        return render(request, 'index.html', context)

def online_trainings(request):
    if request.method == 'GET':
        training = Training.objects.all()
        training1 = training[0]
        training2 = training[1]
        footer = Footer.objects.all()
        footer1 = footer[0]
        scholarships = Scholarship_Opportunitie.objects.all()
        programs = Program_Opportunitie.objects.all()
        context = {
            'training': training, 'footer': footer1, 'scholarships': scholarships,
            'programs': programs, 'training1': training1, 'training2': training2
        }
        return render(request, 'trainings.html', context)

def suggestions(request):
    if request.method == 'POST':
        suggestions = request.POST
        topic = suggestions['topic']
        InsertSuggestions = Topic_Suggestions(topic=topic)
        InsertSuggestions.save()
        subject = 'Act Smart - Training Suggestions'
        full_message = 'You have a new topic suggestions for Act Smart Trainings: \n' + topic
        send_mail(subject,
                  full_message,
                  settings.EMAIL_HOST_USER,
                  ['paolaqendraj@gmail.com'],
                  fail_silently=False)
        return HttpResponseRedirect('/trainings/')

def training_register(request):
    if request.method == 'GET':
        training_id = request.GET['id']
        training = Training.objects.get(id=training_id)
        context = {'training': training}
        return render(request, 'training_register.html', context)

def training_form(request):
    if request.method == 'POST':
        from django.core.validators import validate_email
        from django.core.exceptions import ValidationError
        register = request.POST
        name = register['fullname']
        email = register['email']
        phone = register['phone']
        training_id = register['t-id']
        training = Training.objects.get(id=training_id)
        try:
            validate_email(email)
            InsertRegistration = Training_Registration(name=name, email=email, phone=phone, training=training)
            InsertRegistration.save()
            subject = 'Training Registration - Act Smart'
            full_message = 'This email was sent from: ' + name + ' ' +'\nEmail: ' + email + '\nPhone Nr: ' \
                            + phone + '\nRegistered in: ' + training.name
            send_mail(subject,
                      full_message,
                      settings.EMAIL_HOST_USER,
                      ['paolaqendraj@gmail.com'],
                      fail_silently=False)

            subject2 = 'Act Smart Online Trainings'
            full_message2 = 'Dear ' + name + ',\n' + 'Thank you for registering in "' + training.name + '" Online Training.' +\
                            '\nWe are very excited for the journey you will take toward your success.' + \
                            '\nWe will be in contact with you very soon!' + '\n\n All the best!' + \
                            '\n\nAct Smart EU \nProject Office \nRr. Myslym Shyri, 56/2 1st floor, \nP.O.BOX 1001 Tirana, Albania \nT:+355 69 40 2222 8 \ninfo@actsmarts.eu www.actsmarts.eu'

            send_mail(subject2,
                      full_message2,
                      settings.EMAIL_HOST_USER,
                      [email],
                      fail_silently=False)
            return HttpResponseRedirect('/training_success/')
        except ValidationError:
            email_error = "Your email is incorrect"
            training = Training.objects.get(id=training_id)
            context = {'email_error': email_error, 'training': training}
            return render(request, 'training_register.html', context)

def training_success(request):
    if request.method == 'GET':
        return render(request, 'booking_success.html')

def template_scholarship(request):
    template_id = request.GET['id']
    scholarship = Scholarship_Opportunitie.objects.get(id=template_id)
    eligible = scholarship.eligibility.split("*")
    tags = scholarship.tags
    cat = tags.split("*")
    founded = scholarship.founded_features
    features = founded.split("*")
    training = Training.objects.all()
    footer = Footer.objects.all()
    footer1 = footer[0]
    scholarships = Scholarship_Opportunitie.objects.all()
    programs = Program_Opportunitie.objects.all()
    trainings = Training.objects.all()
    context = {'scholarship': scholarship, 'training': training, 'cat': cat, 'features': features,'footer': footer1,
    'scholarships': scholarships, 'programs': programs, 'trainings': trainings, 'eligible': eligible}
    return render(request, 'template_scholarships.html', context)


def template_programs(request):
    template_id = request.GET['id']
    program = Program_Opportunitie.objects.get(id=template_id)
    eligible = program.eligibility.split("*")
    training = Training.objects.all()
    tags = program.tags
    cat = tags.split("*")
    founded = program.founded_features
    features = founded.split("*")
    footer = Footer.objects.all()
    footer1 = footer[0]
    scholarships = Scholarship_Opportunitie.objects.all()
    programs = Program_Opportunitie.objects.all()
    trainings = Training.objects.all()
    context = {'program': program, 'training': training, 'footer': footer1, 'cat': cat, 'features': features,
               'scholarships': scholarships, 'programs': programs, 'trainings': trainings, 'eligible':eligible}
    return render(request, 'template_programs.html', context)


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
            subject = 'Act Smart - Subscriptions'
            full_message = 'You have a new subscription:\nEmail:  ' + email
            send_mail(subject,
                      full_message,
                      settings.EMAIL_HOST_USER,
                      ['paolaqendraj@gmail.com'], #ndrysho emailin
                      fail_silently=False)

            subject2 = 'Welcome to Act Smart'
            full_message2 = 'Thank you for subscribing to our newsletter! \nYou will hear from us very soon! \n\nWishing you good luck and welcome to AS Network!' + '\n\nAct Smart EU \nProject Office \nRr. Myslym Shyri, 56/2 1st floor, \nP.O.BOX 1001 Tirana, Albania \nT:+355 69 40 2222 8 \ninfo@actsmarts.eu www.actsmarts.eu'

            send_mail(subject2,
                      full_message2,
                      settings.EMAIL_HOST_USER,
                      [email],
                      fail_silently=False)
            return HttpResponseRedirect('/')
        except ValidationError:
            email_error = "Your email is incorrect"
            services = Services_Item.objects.all()
            service1 = services[0]
            service2 = services[1]
            service3 = services[2]
            opportunity = Opportunitie.objects.all()
            scholarships = Scholarship_Opportunitie.objects.all()
            programs = Program_Opportunitie.objects.all()
            footer = Footer.objects.all()
            footer1 = footer[0]
            context = {'service1': service1, 'service2': service2, 'service3': service3,  'opportunity': opportunity,
                'scholarships': scholarships, 'programs': programs, 'footer': footer1, 'email_error': email_error
            }
            return render(request, 'index.html', context)



def template_opp(request, kategori):
    if request.method == 'GET':
        today = timezone.now().date()
        scholarship = Scholarship_Opportunitie.objects.filter(category__category__contains=kategori)
        program = Program_Opportunitie.objects.filter(category__category__contains=kategori)
        footer = Footer.objects.all()
        footer1 = footer[0]
        scholarships = Scholarship_Opportunitie.objects.all()
        programs = Program_Opportunitie.objects.all()
        trainings = Training.objects.all()
        context = {'scholarship': scholarship, 'program': program, 'kategori': kategori, 'footer': footer1,  'scholarships': scholarships, 'programs': programs,
                   'trainings': trainings, 'today': today}
        if kategori == 'Bachelor' or kategori == 'Master' or kategori == 'PhD' or kategori == 'Fellowship':
            return render(request, 'template_opp_scholarships.html', context)
        elif kategori == 'Trainings' or kategori == 'Conferences' or kategori == 'Jobs' or kategori == 'Internships' or kategori == 'Contests' or kategori == 'Grants' or kategori == 'Volunteering':
            return render(request, 'template_opp_programs.html', context)


def someOpportunities(request):
    if request.method == 'GET':
        opportunite = request.GET['id']
        if opportunite == 'PhD':
            today = timezone.now().date()
            phd_name = 'PhD'
            phd = Scholarship_Opportunitie.objects.filter(category__category__contains=phd_name)
            footer = Footer.objects.all()
            footer1 = footer[0]
            scholarships = Scholarship_Opportunitie.objects.all()
            programs = Program_Opportunitie.objects.all()
            context = {
                'scholarship': phd, 'footer': footer1, 'scholarships': scholarships,
                'programs': programs, 'today': today, 'opportunite': opportunite
            }
            return render(request, 'scholarships.html', context)
        if opportunite == 'Master':
            today = timezone.now().date()
            master_name = 'Master'
            master = Scholarship_Opportunitie.objects.filter(category__category__contains=master_name)
            footer = Footer.objects.all()
            footer1 = footer[0]
            scholarships = Scholarship_Opportunitie.objects.all()
            programs = Program_Opportunitie.objects.all()
            context = {
                'scholarship': master, 'footer': footer1, 'scholarships': scholarships,
                'programs': programs, 'today': today, 'opportunite': opportunite
            }
            return render(request, 'scholarships.html', context)
        if opportunite == 'Bachelor':
            today = timezone.now().date()
            bachelor_name = 'Bachelor'
            bachelor = Scholarship_Opportunitie.objects.filter(category__category__contains=bachelor_name)
            footer = Footer.objects.all()
            footer1 = footer[0]
            scholarships = Scholarship_Opportunitie.objects.all()
            programs = Program_Opportunitie.objects.all()
            context = {
                'scholarship': bachelor, 'footer': footer1, 'scholarships': scholarships,
                'programs': programs, 'today': today, 'opportunite': opportunite
            }
            return render(request, 'scholarships.html', context)
        if opportunite == 'Fellowship':
            today = timezone.now().date()
            fellowship_name = 'Fellowship'
            fellowship = Scholarship_Opportunitie.objects.filter(category__category__contains=fellowship_name)
            footer = Footer.objects.all()
            footer1 = footer[0]
            scholarships = Scholarship_Opportunitie.objects.all()
            programs = Program_Opportunitie.objects.all()
            context = {
                'scholarship': fellowship, 'footer': footer1, 'scholarships': scholarships,
                'programs': programs, 'today': today, 'opportunite': opportunite
            }
            return render(request, 'scholarships.html', context)


def somePrograms(request):
    if request.method == 'GET':
        opportunite = request.GET['id']
        if opportunite == 'Trainings':
            today = timezone.now().date()
            training_name = 'Trainings'
            training = Program_Opportunitie.objects.filter(category__category__contains=training_name)
            footer = Footer.objects.all()
            footer1 = footer[0]
            scholarships = Scholarship_Opportunitie.objects.all()
            programs = Program_Opportunitie.objects.all()
            context = {'program': training, 'footer': footer1,
                       'scholarships': scholarships, 'programs': programs, 'today': today, 'opportunite': opportunite}
            return render(request, 'programs.html', context)
        elif opportunite == 'Conferences':
            today = timezone.now().date()
            conference_name = 'Conferences'
            conference = Program_Opportunitie.objects.filter(category__category__contains=conference_name)
            footer = Footer.objects.all()
            footer1 = footer[0]
            scholarships = Scholarship_Opportunitie.objects.all()
            programs = Program_Opportunitie.objects.all()
            context = {'program': conference, 'footer': footer1,
                       'scholarships': scholarships, 'programs': programs, 'today': today, 'opportunite': opportunite}
            return render(request, 'programs.html', context)
        elif opportunite == 'Jobs':
            today = timezone.now().date()
            jobs_name = 'Jobs'
            jobs = Program_Opportunitie.objects.filter(category__category__contains=jobs_name)
            footer = Footer.objects.all()
            footer1 = footer[0]
            scholarships = Scholarship_Opportunitie.objects.all()
            programs = Program_Opportunitie.objects.all()
            context = {'program': jobs, 'footer': footer1,
                       'scholarships': scholarships, 'programs': programs, 'today': today, 'opportunite': opportunite}
            return render(request, 'programs.html', context)
        elif opportunite == 'Internships':
            today = timezone.now().date()
            internship_name = 'Internships'
            internship = Program_Opportunitie.objects.filter(category__category__contains=internship_name)
            footer = Footer.objects.all()
            footer1 = footer[0]
            scholarships = Scholarship_Opportunitie.objects.all()
            programs = Program_Opportunitie.objects.all()
            context = {'program': internship, 'footer': footer1,
                       'scholarships': scholarships, 'programs': programs, 'today': today, 'opportunite': opportunite}
            return render(request, 'programs.html', context)
        elif opportunite == 'Contests':
            today = timezone.now().date()
            contests_name = 'Contests'
            contests = Program_Opportunitie.objects.filter(category__category__contains=contests_name)
            footer = Footer.objects.all()
            footer1 = footer[0]
            scholarships = Scholarship_Opportunitie.objects.all()
            programs = Program_Opportunitie.objects.all()
            context = {'program': contests, 'footer': footer1,
                       'scholarships': scholarships, 'programs': programs, 'today': today, 'opportunite': opportunite}
            return render(request, 'programs.html', context)
        elif opportunite == 'Grants':
            today = timezone.now().date()
            grants_name = 'Grants'
            grants = Program_Opportunitie.objects.filter(category__category__contains=grants_name)
            footer = Footer.objects.all()
            footer1 = footer[0]
            scholarships = Scholarship_Opportunitie.objects.all()
            programs = Program_Opportunitie.objects.all()
            context = {'program': grants, 'footer': footer1,
                       'scholarships': scholarships, 'programs': programs, 'today': today, 'opportunite': opportunite}
            return render(request, 'programs.html', context)
        elif opportunite == 'Volunteering':
            today = timezone.now().date()
            volunteering_name = 'Volunteering'
            volunteering = Program_Opportunitie.objects.filter(category__category__contains=volunteering_name)
            footer = Footer.objects.all()
            footer1 = footer[0]
            scholarships = Scholarship_Opportunitie.objects.all()
            programs = Program_Opportunitie.objects.all()
            context = {'program': volunteering, 'footer': footer1,
                       'scholarships': scholarships, 'programs': programs, 'today': today,'opportunite': opportunite}
            return render(request, 'programs.html', context)


def register(request):
    if request.method == 'POST':
        from django.core.validators import validate_email
        from django.core.exceptions import ValidationError
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        c_password = request.POST['c_password']
        phone = request.POST['phone']
        gender = request.POST['gender']
        country = request.POST['country']
        city = request.POST['city']
        address = request.POST['address']
        try:
            validate_email(email)
            if User.objects.filter(email=email).exists():
                return HttpResponseRedirect('/register/')
            else:
                if password == c_password:
                    user = User.objects.create_user(username, email, password)
                    user.username = username
                    user.save()
                    InsertUser = User_Profile(full_name=username, email=email, phone_number=phone, gender=gender, country=country,
                                              city=city, address=address, user=user)
                    InsertUser.save()
                    return HttpResponseRedirect('/login/')
                else:
                    pass_error = "Passwords don't match!"
                    context = {'pass_error': pass_error}
                    return render(request, 'register.html', context)
        except ValidationError:
            email_error = "This email is incorrect!"
            context = {'email_error': email_error}
            return render(request, 'register.html', context)
    elif request.method == 'GET':
        return render(request, 'register.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/user_profile/')
            else:
                not_active = "Përdoruesi nuk është aktiv"
                context = {'not_active': not_active}
                return render(request, 'login.html', context)
        else:
            not_exists = "Përdoruesi nuk ekziston"
            context = {'not_exists': not_exists}
            return render(request, 'login.html', context)
    elif request.method == 'GET':
        footer = Footer.objects.all()
        footer1 = footer[0]
        context = {'footer': footer1}
        return render(request, 'login.html', context)


def user_profile(request):
    if request.method == 'GET':
        profile = User_Profile.objects.filter(user=request.user)
        scholarships = AddToProfile_Scholarship.objects.filter(user=request.user)
        programs = AddToProfile_Program.objects.filter(user=request.user)
        footer = Footer.objects.all()
        footer1 = footer[0]
        p_registration = Premium_Registration.objects.all()
        p_features = p_registration[0].features.split("*")
        s_registrations = Simple_Registration.objects.all()
        s_features = s_registrations[0].features.split("*")
        footer = Footer.objects.all()
        footer1 = footer[0]
        context = {
            'p_features': p_features, 's_features': s_features,
            'profile': profile, 'scholarships': scholarships, 'programs': programs, 'footer': footer1
        }
        return render(request, 'user_profile.html', context)

def call_mentor_scholarship(request):
    if request.method == 'POST':
        from django.core.validators import validate_email
        from django.core.exceptions import ValidationError
        mentor = request.POST
        user_profile = User_Profile.objects.get(user=request.user)
        email = user_profile.email
        phone = user_profile.phone_number
        date = timezone.now().date()
        opportunity_name = mentor['opp']
        scholarship = Scholarship_Opportunitie.objects.get(title=opportunity_name)
        opportunity_category = scholarship.category
        try:
            validate_email(email)
            InsertMentor = Call_Mentor(user=request.user, email=email, phone=phone, date_register=date,opportunity_category=opportunity_category, opportunity_name=opportunity_name)
            InsertMentor.save()
            subject1 = 'Call for Act Smart Mentor'
            full_message1 = user_profile.full_name + ' is looking for a mentor. \nEmail: ' + email + '\nPhone Nr: ' + phone + \
                           '\nOpportunity Category: ' + opportunity_category.category + '\nOpportunity Selected: ' + opportunity_name
            send_mail(subject1,
                      full_message1,
                      settings.EMAIL_HOST_USER,
                      ['paolaqendraj@gmail.com'],
                      fail_silently=False)

            subject2 = 'Act Smart Mentorship'
            full_message2 = 'Dear ' + user_profile.full_name + ',\n' + 'Thank you for signing up for a mentor in our ' \
                             'platform.' + '\nWe are very excited for the journey you will take toward your success.' + '\nWe will ' \
                            'be in contact with you very soon!' + '\n\n All the best! \n Act Smart Team'

            send_mail(subject2,
                      full_message2,
                      settings.EMAIL_HOST_USER,
                      [email],
                      fail_silently=False)
            return HttpResponseRedirect('/call_mentor_success/')
        except ValidationError:
            email_error = "Your email is incorrect"
            services = Services_Item.objects.all()
            service1 = services[0]
            service2 = services[1]
            service3 = services[2]
            opportunity = Opportunitie.objects.all()
            scholarships = Scholarship_Opportunitie.objects.all()
            programs = Program_Opportunitie.objects.all()
            footer = Footer.objects.all()
            footer1 = footer[0]
            context = {'service1': service1, 'service2': service2, 'service3': service3, 'opportunity': opportunity,
                   'scholarships': scholarships, 'programs': programs, 'footer': footer1, 'email_error':email_error
            }
            return render(request, 'index.html', context)

def call_mentor_program(request):
    if request.method == 'POST':
        from django.core.validators import validate_email
        from django.core.exceptions import ValidationError
        mentor = request.POST
        user_profile = User_Profile.objects.get(user=request.user)
        email = user_profile.email
        phone = user_profile.phone_number
        date = timezone.now().date()
        opportunity_name = mentor['opp']
        program = Program_Opportunitie.objects.get(title=opportunity_name)
        opportunity_category = program.category
        try:
            validate_email(email)
            InsertMentor = Call_Mentor(user=request.user, email=email, phone=phone, date_register=date, opportunity_category=opportunity_category, opportunity_name=opportunity_name)
            InsertMentor.save()
            subject1 = 'Call for Act Smart Mentor'
            full_message1 = user_profile.full_name + ' is looking for a mentor. \nEmail: ' + email + '\nPhone Nr: ' + phone + \
                           '\nOpportunity Category: ' + opportunity_category.category + '\nOpportunity Selected: ' + opportunity_name
            send_mail(subject1,
                      full_message1,
                      settings.EMAIL_HOST_USER,
                      ['paolaqendraj@gmail.com'],
                      fail_silently=False)

            subject2 = 'Act Smart Mentorship'
            full_message2 = 'Dear ' + user_profile.full_name + ',\n' + 'Thank you for signing up for a mentor in our ' \
                             'platform.' + '\nWe are very excited for the journey you will take toward your success.' + '\nWe will ' \
                            'be in contact with you very soon!' + '\n\n All the best! \n Act Smart Team'

            send_mail(subject2,
                      full_message2,
                      settings.EMAIL_HOST_USER,
                      [email],
                      fail_silently=False)
            return HttpResponseRedirect('/call_mentor_success/')
        except ValidationError:
            email_error = "Your email is incorrect"
            services = Services_Item.objects.all()
            service1 = services[0]
            service2 = services[1]
            service3 = services[2]
            opportunity = Opportunitie.objects.all()
            scholarships = Scholarship_Opportunitie.objects.all()
            programs = Program_Opportunitie.objects.all()
            footer = Footer.objects.all()
            footer1 = footer[0]
            context = {'service1': service1, 'service2': service2, 'service3': service3, 'opportunity': opportunity,
                   'scholarships': scholarships, 'programs': programs, 'footer': footer1, 'email_error': email_error
            }
            return render(request, 'index.html', context)


def call_mentor_success(request):
    if request.method == 'GET':
        user_profile = User_Profile.objects.get(user=request.user)
        context = {'user_profile': user_profile}
        return render(request, 'call_mentor_success.html', context)

def add_s(request):
    if request.method == 'GET':
        scholarship_id = request.GET['id']
        profile_s = AddToProfile_Scholarship(user=request.user, scholarships=Scholarship_Opportunitie.objects.get(id=scholarship_id))
        profile_s.save()
        return HttpResponseRedirect('/user_profile/')

def add_p(request):
    if request.method == 'GET':
        program_id = request.GET['id']
        profile_p = AddToProfile_Program(user=request.user, programs=Program_Opportunitie.objects.get(id=program_id))
        profile_p.save()
        return HttpResponseRedirect('/user_profile/')


def search_opportunities(request):
    if request.method == 'POST':
        today = timezone.now().date()
        opportunitie = request.POST['opportunity']
        region = request.POST['region']
        s_opp = Scholarship_Opportunitie.objects.filter(category__category__contains=opportunitie)
        s_filter = s_opp.filter(location=region)
        p_opp = Program_Opportunitie.objects.filter(category__category__contains=opportunitie)
        p_filter = p_opp.filter(location=region)
        trainings = Training.objects.all()
        footer = Footer.objects.all()
        footer1 = footer[0]
        var_region = []
        for s in s_opp:
            var_region.append(s.location)
        var_region = list(dict.fromkeys(var_region))
        print(var_region)
        if region == 'any':
            return HttpResponseRedirect('/' + opportunitie + '/')
        context = {'scholarships': s_filter, 'opportunitie': opportunitie, 'region': region, 'today': today,
                   'programs': p_filter, 'var_region': var_region, 'trainings': trainings,'footer': footer1}
        return render(request, 'template_select.html', context)

def booking(request):
    if request.method == 'GET':
        date = Booking_Date.objects.all()
        time = Booking_Time.objects.all()
        count = 0
        for d in date:
            count = 0
            for t in time:
                if t.date.date == d.date:
                    count = count+1
            print(count)
            if count == 0:
                d.delete()
        context = {'date': date, 'time': time}
        return render(request, 'booking.html', context)

def booking_sent(request):
    if request.method == 'POST':
        from django.core.validators import validate_email
        from django.core.exceptions import ValidationError
        booking = request.POST
        fullname = booking['fullname']
        email = booking['email']
        phone = booking['phone']
        date = booking['date']
        time = booking['time']
        try:
            validate_email(email)
            InsertBooking = Booking_Info(fullname=fullname, email=email, phone=phone, date=date, time=time)
            InsertBooking.save()

            time_available = Booking_Time.objects.filter(date__date=date,time__contains=time)
            time_available.delete()

            dates = Booking_Date.objects.all()
            times = Booking_Time.objects.all()
            count = 0
            for d in dates:
                count = 0
                for t in times:
                    if t.date.date == d.date:
                        count = count + 1
                print(count)
                if count == 0:
                    d.delete()

            subject1 = 'Act Smart - Booking'
            full_message1 = fullname + ' ' + 'just booked an online meeting!\n' + 'Full name: ' + fullname + '\nEmail: ' + email + '\nPhone: ' + phone + '\nDate: ' + date + '\nTime: ' + time
            send_mail(subject1,
                      full_message1,
                      settings.EMAIL_HOST_USER,
                      ['qendraj.p@gssolutions.al'],
                      fail_silently=False)

            subject2 = 'Act Smart - Online Meeting'
            full_message2 = 'Dear ' + fullname + ',\n' + 'Thank you for booking your place for the free online meeting with one of our mentors!\nIn 15 minutes you will learn about worldwide opportunities that will change your life.' +\
                            '\n\nFind the Zoom link below for the online meeting that you can access it on ' + date + ', at ' + time +'.\n(link)' + '\n\nWishing you good luck and welcome to AS Network!' + '\n\nAct Smart EU \nProject Office \nRr. Myslym Shyri, 56/2 1st floor, \nP.O.BOX 1001 Tirana, Albania \nT:+355 69 40 2222 8 \ninfo@actsmarts.eu www.actsmarts.eu'
            send_mail(subject2,
                      full_message2,
                      settings.EMAIL_HOST_USER,
                      [email],
                      fail_silently=False)
            return HttpResponseRedirect('/booking_success/')
        except ValidationError:
            email_error = "Your email is incorrect"
            date = Booking_Date.objects.all()
            time = Booking_Time.objects.all()
            context = {'date': date, 'time': time, 'email_error': email_error}
            return render(request, 'booking.html', context)

def booking_success(request):
    if request.method == 'GET':
        return render(request,'booking_success.html')