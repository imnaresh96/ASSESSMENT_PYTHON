from django.shortcuts import render, redirect
from .models import *
from django.conf import settings
from django.core.mail import send_mail
from django.db.utils import IntegrityError
import os
from random import randint
# Create your views here.
data={}
def index(request):
    return render(request,'index.html',data)
    
def blank_page(request):
    return render(request,'blank_page.html',data)

# def add_book_page(request):
#     return render(request,'add_book_page.html')

def add_club_page(request):
    return render(request,'add_club_page.html')



def add_data(request):
    return render(request,'add_data.html')

def signin_page(request):
    return render(request,'signin_page.html')

def teacher(request):
    return render(request,'teacher.html')

def student(request):
    student_data(request) #load student data
    return render(request,'student.html', data)


def club_page(request):
    club_data(request) #load club data
    return render(request,'club_page.html', data)
    
def book_page(request):
    book_data(request) #load book data
    return render(request,'book_page.html', data)
    
def teacher(request):
    teacher_data(request) #load teacher data
    return render(request,'teacher.html', data)
    

def signup_page(request):
    return render(request,'signup_page.html')

def new_user(request):
    return render(request,'new_user.html')


def forgot_password(request):
    return render(request,'forgot_password.html')

def add_new_student(request):
    return render (request,'add_new_student.html')

def otp_page(request):
    return render (request,'otp_page.html')

def profile_page_teacher(request):
    return render (request,'profile_page_teacher.html',data)


def profile_page(request):
    print(request.session['email'])
    if 'email' in request.session:
        try:
            try:
                profile_data(request) #load student data
                return render(request,'profile_page.html',data) #student profile page
            except:
                profile_data_2(request) #load teacher data
                return redirect(profile_page_teacher) #teacher profile page
        except Exception as err:
            print("data not availabe ! submit your data admin side & relogin")
    return redirect(new_user)


#signup_functionality
def signup(request):
    print(request.POST)
    password = request.POST['password']
    if password == request.POST['confirm_password']:
        master = Master.objects.create(Email = request.POST['email'],Password = password)
        role=Role.objects.create(Role_Type = request.POST['role_type'])
        common=Common.objects.create(Master = master)
        print('Signup successfully.')
        if role.Role_Type == 'student':
            print('Student')
            Student.objects.create(Common=common)
        else:
            print('teacher')
            Teacher.objects.create(Common=common)
    else:
        print('both password should be same.')
        return redirect(signup_page)

    return redirect(signin_page)

# signin functionality
def signin(request):
    print(request.POST)
    try:
        master = Master.objects.get(Email = request.POST['email'])
        if master.Password == request.POST['password']:
            request.session['email'] = master.Email
            print('login successfully')
            return redirect(profile_page)
            # return redirect(index)

        else:
            print('You entered wrong password.')
            return redirect(signin_page)
    except Master.DoesNotExist as err:
        print(f'{request.POST["email"]} not registered.')
    
    return redirect(signup_page)


# load profile student data
def profile_data(request):
    master = Master.objects.get(Email = request.session['email'])
    user_profile = Common.objects.get(Master = master)
    user_roll=Student.objects.get(Common=user_profile)

    user_profile.first_name = user_profile.Full_Name.split()[0]
    user_profile.last_name = user_profile.Full_Name.split()[1]
    user_roll.roll_number = user_roll.Roll_Number
    user_profile.DateOfBirth = user_profile.DateOfBirth.strftime("%Y-%m-%d")
    user_profile.DateOfJoining = user_profile.DateOfJoining.strftime("%Y-%m-%d")

    data['user_data'] = user_profile
    data['roll_user']=user_roll
    
    return redirect(profile_page)

# load profile teacher data
def profile_data_2(request):
    master = Master.objects.get(Email = request.session['email'])
    user_profile = Common.objects.get(Master = master)
    teacher=Teacher.objects.get(Common=user_profile)

    user_profile.first_name = user_profile.Full_Name.split()[0]
    user_profile.last_name = user_profile.Full_Name.split()[1]
    teacher.compensation=teacher.Compensation

    user_profile.DateOfBirth = user_profile.DateOfBirth.strftime("%Y-%m-%d")
    user_profile.DateOfJoining = user_profile.DateOfJoining.strftime("%Y-%m-%d")

    data['user_data'] = user_profile
    data['teacher_data']=teacher
    
    return redirect(profile_page_teacher)

# student profile update functionality
def profile_update(request):
    print(request.POST)
    master = Master.objects.get(Email = request.session['email'])
    user_profile = Common.objects.get(Master = master)
    user_roll=Student.objects.get(Common=user_profile)
    
    user_profile.Full_Name =' '.join([request.POST['first_name'], request.POST['last_name']])
    user_profile.DateOfBirth = request.POST['dateofbirth']
    user_profile.DateOfJoining = request.POST['dateofjoining']
    user_profile.Address = request.POST['address']
    user_roll.Roll_Number=request.POST['roll_number']
    

    user_profile.save()
    user_roll.save()
    return redirect(profile_page)

# profile update teacher functionality
def profile_update_teacher(request):
    print(request.POST)
    master = Master.objects.get(Email = request.session['email'])
    user_profile = Common.objects.get(Master = master)
    teacher=Teacher.objects.get(Common=user_profile)

    user_profile.Full_Name =' '.join([request.POST['first_name'], request.POST['last_name']])
    user_profile.DateOfBirth = request.POST['dateofbirth']
    user_profile.DateOfJoining = request.POST['dateofjoining']
    user_profile.Address = request.POST['address']
    teacher.Compensation=request.POST['compensation']
    

    user_profile.save()
    teacher.save()
    return redirect(profile_page)

# Password reset
def password_reset(request):
    print(request.POST)
    master = Master.objects.get(Email = request.session['email'])
    if master.Password == request.POST['current_password']:
        if request.POST['new_password'] == request.POST['confirm_password']:
            master.Password = request.POST['new_password']
            print('Password change successfully')
            master.save()
            return redirect(signin_page)
        else:
            print('both password should be same.')
            return redirect(profile_page)
    else:
        print('Current password does not matched.')
    return redirect(profile_page)


# logout functionality
def logout(request):
    if 'email' in request.session:
        del request.session['email']
        return redirect(signin_page)
    else:
        return redirect(signin_page)

# forgot password
def forgot_password_page(request):
    print(request.POST)
    try:
        master = Master.objects.get(Email = request.POST['email'])
        request.session['email'] = master.Email
        if master.Email == request.POST['email']:
            print('OTP Sent Successfully')
            otp_creation(request)
            return redirect(otp_page)
        else:
            print("Email Not Register")
            return redirect(signup_page)
    except :
        print("invalid Email")
        return redirect(signin_page)
# OTP Creation
def otp_creation(request):
    otp_number = randint(1000, 9999)
    print("OTP is: ", otp_number)
    request.session['otp'] = otp_number
    return otp_number

# #otp send
def otp_send(request):
    if request.session['otp'] == int(request.POST['otp']):
        print('otp match')
        master = Master.objects.get(Email = request.session['email'])
        if request.POST['new_password'] == request.POST['confirm_password']:
            master.Password = request.POST['new_password']
            print('password change successfully')
            master.save()
        else:   
            print('both password should be same.')
            return redirect(forgot_password)
    else:
        print('Wrong OTP')
        return redirect(forgot_password)
    return redirect(signin_page)
    
#student data
def student_data(request):
    print(request.POST)
    student = Student.objects.all()
    # print(student)
    data['student'] = student
    # return redirect(student)

#teacher data
def teacher_data(request):
    print(request.POST)
    teacher = Teacher.objects.all()
    # print(student)
    data['teacher'] = teacher
    # return redirect(student)

#club data
def club_data(request):
    # print(request.POST)
    club = Club.objects.all()
    data['club'] = club

#book data
def book_data(request):
    # print(request.POST)
    book = Book.objects.all()
    data['book'] = book
    

def profile_data_load(request):
    print(request.POST)
    password = request.POST['password']
    if password == request.POST['confirm_password']:
        master = Master.objects.create(Email = request.POST['email'],Password = password)
        common=Common.objects.create(Master=master)
        user_roll=Student.objects.create(Common=common)
        common.Full_Name =' '.join([request.POST['first_name'], request.POST['last_name']])
        common.DateOfBirth = request.POST['dateofbirth']
        common.DateOfJoining = request.POST['dateofjoining']
        common.Address = request.POST['address']
        user_roll.Roll_Number=request.POST['roll_number']

        master.save()
        common.save()
        user_roll.save()
        return redirect(signin_page)
    else:
        print('Both Password Should Be Same')
        return redirect(add_new_student)


# Add Book's    
def add_book(request):
    print(request.POST)
    
    Book.objects.create(
        Book_Name=request.POST['book_name'],
        Author_Name=request.POST['author_name'],
        Price=request.POST['price'],
        Time_Period=request.POST['time_period']
        )
    # book.save()
    print('successfully')
    return redirect(profile_page_teacher)

# Add club's    
def add_club(request):
    print(request.POST)
    
    Club.objects.create(
        Club_Name=request.POST['club_name'],
        Open_Time=request.POST['open_time'],
        Close_Time=request.POST['close_time'],
        Head_Of_Club=request.POST['head_of_club'],
        Contact=request.POST['contact']
        )

    print('successfully')
    return redirect(profile_page_teacher)
    

# Profile Page Update Logic
def new_user_update(request):
    print(request.POST)
    master = Master.objects.get(Email = request.session['email'])
    common= Common.objects.get(Master = master)

    common.Full_Name = ' '.join([request.POST['first_name'], request.POST['last_name']])
    common.DateOfBirth = request.POST['dateofbirth']
    common.DateOfJoining = request.POST['dateofjoining']
    common.Address = request.POST['address']

    common.save()
    return redirect(signin_page)




def club_delete(request,club_name):
    print(request.POST)
    club=Club.objects.get(Club_Name=club_name)
    club.delete()
    return redirect(club_page)


def delete_account(request):
    print(request.POST)
    master=Master.objects.get(Email = request.session['email'])
    master.delete()
    return redirect(signin_page)

#club count
def club_count(request):
    club = Club.objects.all()
    club_num=0
    for m in club:
        club_num+=1
        print(m)
    club_num

