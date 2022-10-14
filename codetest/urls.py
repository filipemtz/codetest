from django.urls import include, path

from . import views

urlpatterns = [
    # user management
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup', views.signup_form, name="signup"),

    # main pages
    path('', views.index, name='index'),

    # courses management
    path('courses/', views.CourseListView.as_view(), name="courses"),
    path('course/<int:pk>', views.CourseDetailView.as_view(), name="course-detail"),
    path('course/create/', views.CourseCreate.as_view(), name="course-create"),
    path('course/<int:pk>/update/',
         views.CourseUpdate.as_view(), name='course-update'),
    path('course/<int:pk>/delete/',
         views.CourseDelete.as_view(), name='course-delete'),

    # section management
    path('course/<int:course_id>/section/create/',
         views.SectionCreate.as_view(), name="section-create"),
    path('section/<int:pk>/update/',
         views.SectionUpdate.as_view(), name='section-update'),
    path('section/<int:pk>/delete/',
         views.SectionDelete.as_view(), name='section-delete'),

    # question management
    path('section/<int:section_id>/question/create/',
         views.QuestionCreate.as_view(), name="question-create"),
    path('question/<int:pk>/update/',
         views.QuestionUpdate.as_view(), name='question-update'),
    path('question/<int:pk>/delete/',
         views.QuestionDelete.as_view(), name='question-delete'),

    # course enrollment
    path('course/<int:course_id>/enroll/<uuid:enroll_password>',
         views.enroll_course, name="enroll-course"),
    path('course/<int:course_id>/unenroll/',
         views.unenroll_course, name='unenroll-course'),

    # submission
    path('question/<int:pk>',
         views.QuestionDetailView.as_view(), name="question-detail"),
    path('question/<int:question_id>/submission',
         views.perform_question_submission, name="question-submission"),
]
