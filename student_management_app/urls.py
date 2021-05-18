
from django.urls import path, include
from . import views
from .import HodViews, StaffViews, StudentViews, ApiViews

from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token



urlpatterns = [
    path('', views.loginPage, name="login"),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('doLogin/', views.doLogin, name="doLogin"),
    path('get_user_details/', views.get_user_details, name="get_user_details"),
    path('logout_user/', views.logout_user, name="logout_user"),
    path('admin_home/', HodViews.admin_home, name="admin_home"),
    path('add_staff/', HodViews.add_staff, name="add_staff"),
    path('add_staff_save/', HodViews.add_staff_save, name="add_staff_save"),
    path('manage_staff/', HodViews.manage_staff, name="manage_staff"),
    path('edit_staff/<staff_id>/', HodViews.edit_staff, name="edit_staff"),
    path('edit_staff_save/', HodViews.edit_staff_save, name="edit_staff_save"),
    path('delete_staff/<staff_id>/', HodViews.delete_staff, name="delete_staff"),
    path('add_course/', HodViews.add_course, name="add_course"),
    path('add_course_save/', HodViews.add_course_save, name="add_course_save"),
    path('manage_course/', HodViews.manage_course, name="manage_course"),
    path('edit_course/<course_id>/', HodViews.edit_course, name="edit_course"),
    path('edit_course_save/', HodViews.edit_course_save, name="edit_course_save"),
    path('delete_course/<course_id>/', HodViews.delete_course, name="delete_course"),
    path('manage_session/', HodViews.manage_session, name="manage_session"),
    path('add_session/', HodViews.add_session, name="add_session"),
    path('add_session_save/', HodViews.add_session_save, name="add_session_save"),
    path('edit_session/<session_id>', HodViews.edit_session, name="edit_session"),
    path('edit_session_save/', HodViews.edit_session_save, name="edit_session_save"),
    path('delete_session/<session_id>/', HodViews.delete_session, name="delete_session"),
    path('add_student/', HodViews.add_student, name="add_student"),
    path('add_student_save/', HodViews.add_student_save, name="add_student_save"),
    path('edit_student/<student_id>', HodViews.edit_student, name="edit_student"),
    path('edit_student_save/', HodViews.edit_student_save, name="edit_student_save"),
    path('manage_student/', HodViews.manage_student, name="manage_student"),
    path('delete_student/<student_id>/', HodViews.delete_student, name="delete_student"),
    path('add_subject/', HodViews.add_subject, name="add_subject"),
    path('add_subject_save/', HodViews.add_subject_save, name="add_subject_save"),
    path('manage_subject/', HodViews.manage_subject, name="manage_subject"),
    path('edit_subject/<subject_id>/', HodViews.edit_subject, name="edit_subject"),
    path('edit_subject_save/', HodViews.edit_subject_save, name="edit_subject_save"),
    path('delete_subject/<subject_id>/', HodViews.delete_subject, name="delete_subject"),
    path('check_email_exist/', HodViews.check_email_exist, name="check_email_exist"),
    path('check_username_exist/', HodViews.check_username_exist, name="check_username_exist"),
    path('student_feedback_message/', HodViews.student_feedback_message, name="student_feedback_message"),
    path('student_feedback_message_reply/', HodViews.student_feedback_message_reply, name="student_feedback_message_reply"),
    path('staff_feedback_message/', HodViews.staff_feedback_message, name="staff_feedback_message"),
    path('staff_feedback_message_reply/', HodViews.staff_feedback_message_reply, name="staff_feedback_message_reply"),
    path('student_leave_view/', HodViews.student_leave_view, name="student_leave_view"),
    path('student_leave_approve/<leave_id>/', HodViews.student_leave_approve, name="student_leave_approve"),
    path('student_leave_reject/<leave_id>/', HodViews.student_leave_reject, name="student_leave_reject"),
    path('staff_leave_view/', HodViews.staff_leave_view, name="staff_leave_view"),
    path('staff_leave_approve/<leave_id>/', HodViews.staff_leave_approve, name="staff_leave_approve"),
    path('staff_leave_reject/<leave_id>/', HodViews.staff_leave_reject, name="staff_leave_reject"),
    path('admin_view_attendance/', HodViews.admin_view_attendance, name="admin_view_attendance"),
    path('admin_get_attendance_dates/', HodViews.admin_get_attendance_dates, name="admin_get_attendance_dates"),
    path('admin_get_attendance_student/', HodViews.admin_get_attendance_student, name="admin_get_attendance_student"),
    path('admin_profile/', HodViews.admin_profile, name="admin_profile"),
    path('admin_profile_update/', HodViews.admin_profile_update, name="admin_profile_update"),
     #Notice
    path('noticelist/', HodViews.noticelist, name="noticelist"),
    path('create_notice/', HodViews.CreateNotice, name="create_notice"),
    path('create_notice_save/', HodViews.create_notice_save, name='create_notice_save'),
    path('edit_notice/<str:notice_id>/',HodViews.edit_notice, name="edit_notice"),
    path('delete_notice/<str:notice_id>/', HodViews.delete_notice, name="delete_notice"),
    #Catagory
    path('category/', HodViews.manage_category, name="category"),
    path('add_catagory/',HodViews.add_category, name="add_category"),
    path('edit_category/<str:category_id>/', HodViews.edit_category, name="edit_category"),
    path('delete_category/<str:category_id>/', HodViews.delete_category, name="delete_category"),
    #Events Path
    path('events/', HodViews.events, name="events"),
    path('add_events/', HodViews.add_events, name="add_events"), 
    path('edit_events/<str:event_id>/', HodViews.edit_events, name="edit_events"),
    path('delete_events/<str:event_id>/',HodViews.delete_events, name="delete_events"),
    #Carousal Path
    path('hero_carousal/', HodViews.manage_carousal, name='hero_carousal'),
    path('add_carousal/', HodViews.add_carousal, name='add_carousal'),
    path('edit_carousal/<str:carousal_id>/', HodViews.edit_carousal, name="edit_carousal"),
    path('delete_carousal/<str:carousal_id>/', HodViews.delete_carousal, name='delete_carousal'),
    #Faculty Member
    path('faculty_member/', HodViews.faculty_member, name="faculty_member"),
    path('add_faculty_member', HodViews.add_faculty_member, name="add_faculty_member"),
    path('edit_faculty_member/<str:member_id>/', HodViews.edit_faculty_member, name="edit_faculty_member"),
    path('delete_faculty_member/<str:member_id>/',HodViews.delete_faculty_member, name="delete_faculty_member"),
    
    


    # URLS for Staff
    path('staff_home/', StaffViews.staff_home, name="staff_home"),
    path('staff_take_attendance/', StaffViews.staff_take_attendance, name="staff_take_attendance"),
    path('get_students/', StaffViews.get_students, name="get_students"),
    path('save_attendance_data/', StaffViews.save_attendance_data, name="save_attendance_data"),
    path('staff_update_attendance/', StaffViews.staff_update_attendance, name="staff_update_attendance"),
    path('get_attendance_dates/', StaffViews.get_attendance_dates, name="get_attendance_dates"),
    path('get_attendance_student/', StaffViews.get_attendance_student, name="get_attendance_student"),
    path('update_attendance_data/', StaffViews.update_attendance_data, name="update_attendance_data"),
    path('staff_apply_leave/', StaffViews.staff_apply_leave, name="staff_apply_leave"),
    path('staff_apply_leave_save/', StaffViews.staff_apply_leave_save, name="staff_apply_leave_save"),
    path('staff_feedback/', StaffViews.staff_feedback, name="staff_feedback"),
    path('staff_feedback_save/', StaffViews.staff_feedback_save, name="staff_feedback_save"),
    path('staff_profile/', StaffViews.staff_profile, name="staff_profile"),
    path('staff_profile_update/', StaffViews.staff_profile_update, name="staff_profile_update"),
    path('staff_add_result/', StaffViews.staff_add_result, name="staff_add_result"),
    path('staff_add_result_save/', StaffViews.staff_add_result_save, name="staff_add_result_save"),

    # URSL for Student
    path('student_home/', StudentViews.student_home, name="student_home"),
    path('student_view_attendance/', StudentViews.student_view_attendance, name="student_view_attendance"),
    path('student_view_attendance_post/', StudentViews.student_view_attendance_post, name="student_view_attendance_post"),
    path('student_apply_leave/', StudentViews.student_apply_leave, name="student_apply_leave"),
    path('student_apply_leave_save/', StudentViews.student_apply_leave_save, name="student_apply_leave_save"),
    path('student_feedback/', StudentViews.student_feedback, name="student_feedback"),
    path('student_feedback_save/', StudentViews.student_feedback_save, name="student_feedback_save"),
    path('student_profile/', StudentViews.student_profile, name="student_profile"),
    path('student_profile_update/', StudentViews.student_profile_update, name="student_profile_update"),
    path('student_view_result/', StudentViews.student_view_result, name="student_view_result"),

    #API
    path('api/', ApiViews.apiOverview, name="api_overview"),
    path('api/cource_list/', ApiViews.cource_list, name="cource_list"),
    path('api/cource_list/<str:item_id>/', ApiViews.cource_list_item, name="cource_list_item"),
    path('api/notice_list/', ApiViews.notice_list, name="notice_list"),
    path('api/notice_list/<str:item_id>/', ApiViews.notice_list_item, name="notice_list_item"),
    path('api/event_list/', ApiViews.event_list, name="event_list"),
    path('api/event_list/<str:item_id>/', ApiViews.event_list_item, name="event_list_item"),
    path('api/carousal_list/', ApiViews.carousal_list, name="carousal_list"),
    path('api/carousal_list/<str:item_id>/', ApiViews.carousal_list_item, name="carousal_list_item"),
    path('api/faculty_member/', ApiViews.faculty_member_list, name="faculty_member_list"),
    path('api/faculty_member/<str:item_id>/', ApiViews.faculty_member_list_item, name="faculty_member_list_item"),

    #myPath
    path('jquery/', ApiViews.JqueryPlayground, name = "jquery"),

    #JWT
    path('auth-jwt/', obtain_jwt_token),
    path('auth-jwt-refresh,', refresh_jwt_token),
    path('auth-jwt-verify/', verify_jwt_token),




   

]
