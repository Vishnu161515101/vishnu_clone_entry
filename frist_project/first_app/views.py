from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
# from .models import Member
from django.template import loader
# Create your views here.
from django.db.models import Q # to Use the Q object to combine the queries for username and email.
import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
def vishnu(request):
    return HttpResponse('hello vishnu')


def vishnu12a(request):
    if request.method == 'POST':
        fname=request.POST.get('fname')
        Password=request.POST.get('Password')
        Email=request.POST.get('Email')
        flag=request.POST.get('flag')
        
        try:
            custom_password_validator(Password)
 
        # user=
        # fname1=fname,'-',Password,'-',Email
        # if fname1 != '' :
            # return HttpResponse(fname1)
            if fname == '' and Password != '' and Email != '':
                template = loader.get_template('entry_page_frist.html')
                context = {
                                'mymembers1': 'pelase entere the First name',
                                fname: fname,
                            
                            }
                return HttpResponse(template.render(context, request))
        
            elif fname == '' and Password == '' and Email != '':
                template = loader.get_template('entry_page_frist.html')
                context = {
                                'fname':fname,
                                'Email':Email,
                                'mymembers1': 'pelase entere the First name',
                                'mymembers3': 'pelase entere the Password',
                            
                            }
                return HttpResponse(template.render(context, request))
                    
            elif fname == '' and Password != '' and Email == '':
                template = loader.get_template('entry_page_frist.html')
                context = {
                                'Password':Password,
                                'mymembers1': 'pelase entere the First name',
                                'mymembers3': 'pelase entere the Email',
                            
                            }
                return HttpResponse(template.render(context, request))
            

            elif Password == '' and fname != '' and Email != '':
                template = loader.get_template('entry_page_frist.html')
                context = {
                                'Password':Password,
                                'mymembers2': 'pelase entere the Password',
                            }
                return HttpResponse(template.render(context, request))
            
            elif Password == '' and fname == '' and Email != '':
                template = loader.get_template('entry_page_frist.html')
                context = {
                    'Email':Email,
                                'mymembers2': 'pelase entere the Password',
                                'mymembers1': 'pelase entere the First name',
                            }
                return HttpResponse(template.render(context, request))
            
                    
            elif Password == '' and fname != '' and Email == '':
                template = loader.get_template('entry_page_frist.html')
                context = {
                    'fname': fname,
                                'mymembers2': 'pelase entere the Password',
                                'mymembers3': 'pelase entere the Email',
                            }
                return HttpResponse(template.render(context, request))
            

            elif Email == '' and Password != '' and fname != '':
                template = loader.get_template('entry_page_frist.html')
                context = {
                    'Password':Password,
                    'fname':fname,
                                'mymembers3': 'pelase entere the Email',
                                
                            }
                return HttpResponse(template.render(context, request))
            
            elif Email == '' and Password == '' and fname != '':
                template = loader.get_template('entry_page_frist.html')
                context = {
                            'fname': fname,
                                'mymembers3': 'pelase entere the Email',
                            'mymembers2': 'pelase entere the Password',
                            }
                return HttpResponse(template.render(context, request))
                    
            elif Email == '' and Password != '' and fname == '':
                template = loader.get_template('entry_page_frist.html')
                context = {
                    'Password':Password,
                                'mymembers3': 'pelase entere the Email',
                                'mymembers1': 'pelase entere the First name',
                            }
                return HttpResponse(template.render(context, request))
            
            elif Email == '' and Password == '' and fname == '':
                template = loader.get_template('entry_page_frist.html')
                context = {
                                'mymembers3': 'pelase entere the Email',
                                'mymembers1': 'pelase entere the First name',
                                'mymembers2': 'pelase entere the Password',
                            }
                return HttpResponse(template.render(context, request))
            
            else:
                if not User.objects.filter(Q(username=fname) | Q(email=Email)).exists():
                        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
                        if not re.match(email_regex, Email):
                            template = loader.get_template('entry_page_frist.html')
                            context = {
                                    'mymembers3': 'Invalid email format',
                                    'fname': fname,
                                    'Email': Email,
                                    'Password': Password,
                            }
                            return HttpResponse(template.render(context, request))
                        else:
                            validate(Password)
                            
                            User.objects.create_superuser(username=fname, email=Email, password=Password)
                            template = loader.get_template('entry_page_frist.html')
                            context = {
                                    'mymembers4': 'Superuser  created successfully.',
                                } 
                            return HttpResponse(template.render(context, request))
                    # print(f'Superuser {fname} created successfully.')
                else:
                    if User.objects.filter(username=fname).exists():
                        template = loader.get_template('entry_page_frist.html')
                        context = {
                                    'fname': fname,
                                    'Email': Email,
                                    'Password': Password,
                                    'mymembers4': 'Super user name  already exists Please change user name.',
                                }
                        return HttpResponse(template.render(context, request))
                    elif User.objects.filter(email=Email).exists():
                        template = loader.get_template('entry_page_frist.html')
                        context = {
                                    'fname': fname,
                                    'Email': Email,
                                    'Password': Password,
                                    'mymembers4': 'Email already exists Please change user Email.',
                                }
                        return HttpResponse(template.render(context, request))
                    else:
                        template = loader.get_template('entry_page_frist.html')
                        context = {
                                    'mymembers4': 'Superuser already exists.',
                                }
                        return HttpResponse(template.render(context, request))
        except  ValidationError as e:
            template = loader.get_template('entry_page_frist.html')
            context = {'mymembers4': ' '.join(e.messages)}
            return HttpResponse(template.render(context, request)) 
    
    return render(request,'entry_page_frist.html')

def contact(request):
    # return HttpResponse('hello vishnu')
     return render(request,'login_content.html')


def validate():
    return HttpResponse('test from password')



def custom_password_validator(password):
    # Custom password criteria
    if len(password) < 8:
        raise ValidationError("Password must be at least 8 characters long.")
    if len(password) > 15:
        raise ValidationError("This password must contain at most 15 characters.")
    if not re.search(r'[A-Z]', password):
        raise ValidationError("Password must contain at least one uppercase letter.")
    if not re.search(r'[a-z]', password):
        raise ValidationError("Password must contain at least one lowercase letter.")
    if not re.search(r'[0-9]', password):
        raise ValidationError("Password must contain at least one digit.")
    if not re.search(r'[\W_]', password):  # \W matches any non-word character (special characters)
        raise ValidationError("Password must contain at least one special character.")

def create_superuser_view(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            # Custom password validation
            custom_password_validator(password)
            
            # Django's built-in password validation
            # validate_password(password)

            if User.objects.filter(username=fname).exists():
                template = loader.get_template('password_validation.html')
                context = {'mymembers4': 'Superuser already exists.'}
                return HttpResponse(template.render(context, request))
            elif User.objects.filter(email=email).exists():
                template = loader.get_template('password_validation.html')
                context = {'mymembers4': 'Superuser already exists.'}
                return HttpResponse(template.render(context, request))
            
            # Create superuser if validation passes
            User.objects.create_superuser(username=fname, email=email, password=password)
            template = loader.get_template('password_validation.html')
            context = {'mymembers4': 'Superuser created successfully.'}
            return HttpResponse(template.render(context, request))

        except ValidationError as e:
            template = loader.get_template('password_validation.html')
            context = {'mymembers4': ' '.join(e.messages)}
            return HttpResponse(template.render(context, request))

    template = loader.get_template('password_validation.html')
    return HttpResponse(template.render({}, request))