from django.urls import path
from .views import *

urlpatterns=[
    path('',index,name='index'),
    path('signin_page/',signin_page, name='signin_page'),
    path('signup_page/',signup_page, name='signup_page'),
    path('forgot_password/',forgot_password, name='forgot_password'),
    path('profile_page_teacher/',profile_page_teacher,name='profile_page_teacher'),
    path('profile_page/',profile_page,name='profile_page'),
    path('student/',student,name='student'),
    path('add_club_page/',add_club_page,name='add_club_page'),
    path('add_book/',add_book,name='add_book'),
    path('add_club/',add_club,name='add_club'),
    path('add_data/',add_data,name='add_data'),
    path('blank_page/',blank_page,name='blank_page'),
    path('book_page/',book_page,name='book_page'),
    path('delete_account/',delete_account,name='delete_account'),
    path('profile_data/',profile_data,name='profile_data'),
    path('profile_data_load/',profile_data_load,name='profile_data_load'),
    path('profile_data_2/',profile_data_2,name='profile_data_2'),
    path('profile_update/',profile_update,name='profile_update'),
    path('profile_update_teacher/',profile_update_teacher,name='profile_update_teacher'),
    path('add_new_student/',add_new_student,name='add_new_student'),
    path('password_reset/',password_reset,name='password_reset'),
    path('signup/',signup,name='signup'),
    path('otp_page/',otp_page,name='otp_page'),
    path('forgot_password_page/',forgot_password_page,name='forgot_password_page'),
    path('otp_creation/',otp_creation,name='otp_creation'),
    path('logout/',logout,name='logout'),
    path('otp_send/',otp_send,name='otp_send'),
    path('teacher_data/',teacher_data,name='teacher_data'),
    path('teacher/',teacher,name='teacher'),
    path('signin/',signin,name='signin'),
    path('student_data/',student_data,name='student_data'),
    path('club_page/',club_page,name='club_page'),
    path('club_delete/',club_delete,name='club_delete'),
    path('club_count/',club_count,name='club_count'),
]