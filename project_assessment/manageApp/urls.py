from django.urls import path
from .views import *

urlpatterns=[
    path('',index,name='index'),
    path('signin_page/',signin_page, name='signin_page'),
    path('signup_page/',signup_page, name='signup_page'),
    path('forgot_password_page/',forgot_password_page,name='forgot_password_page'),
    path('blank_page/',blank_page,name='blank_page'),
    path('otp_page/',otp_page,name='otp_page'),

    path('signin/',signin,name='signin'),
    path('signup/',signup,name='signup'),
    path('forgot_password/',forgot_password, name='forgot_password'),
    path('password_reset/',password_reset,name='password_reset'),
    path('add_data/',add_data,name='add_data'),

    path('otp_creation/',otp_creation,name='otp_creation'),
    path('logout/',logout,name='logout'),
    path('otp_send/',otp_send,name='otp_send'),

    path('delete_account/',delete_account,name='delete_account'),
    path('profile_data_2/',profile_data_2,name='profile_data_2'),
    path('profile_update_teacher/',profile_update_teacher,name='profile_update_teacher'),
    path('teacher_data/',teacher_data,name='teacher_data'),
    path('teacher/',teacher,name='teacher'),
    path('profile_page_teacher/',profile_page_teacher,name='profile_page_teacher'),

    path('profile_page/',profile_page,name='profile_page'),
    path('profile_data/',profile_data,name='profile_data'),
    path('profile_update/',profile_update,name='profile_update'),
    path('student/',student,name='student'),
    path('student_data/',student_data,name='student_data'),

    path('book_page/',book_page,name='book_page'),
    path('add_book/',add_book,name='add_book'),
    path('book_delete/<str:book_name>',book_delete,name='book_delete'),
    #club
    path('add_club/',add_club,name='add_club'),
    path('club_page/',club_page,name='club_page'),
    path('club_delete/<str:club_name>',club_delete,name='club_delete'),
    path('club_count/',club_count,name='club_count'),
]