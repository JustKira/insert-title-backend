from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    ## Postings
    path('postings/', views.PostingGetAllView.as_view(), name='posting_getAll'),
    path('postings/<int:pk>', views.PostingGetView.as_view(), name='posting_getID'),
    path('postings/delete/<int:pk>', views.PostingDeleteView.as_view(), name='posting_delete'),
    path('postings/create/', views.PostingAddView.as_view(), name='posting_create'),
    path('postings/update/<int:pk>', views.PostingUpdateView.as_view(), name='posting_update'),

    ## User
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterView.as_view(), name='auth_register'),
    path('students/update/<int:pk>', views.StudentUserUpdateView.as_view(), name='student_update'),
    path('recruiters/update/<int:pk>', views.RecruiterUserUpdateView.as_view(), name='recruiter_update'),
    path('users/userType/update/<int:pk>', views.UpdateUserTypeView.as_view(), name='userType_update'),
    path('students/delete/<int:pk>', views.DeleteStudentView.as_view(), name='students_delete'),
    path('recruiters/delete/<int:pk>', views.DeleteRecruiterView.as_view(), name='recruiter_delete'),

    ## CV Template
    path('cv_builder/', views.CVTemplateGetAllView.as_view(), name='cv_getAll'),
    path('cv_builder/create/', views.CVTemplateAddView.as_view(), name='cv_create'),
    path('cv_builder/render/<int:cv_template_id>', csrf_exempt(views.RenderCVView.as_view()), name='cv_render'),

    ## Road Map

    path('road_map/create/',views.NodeAddView.as_view(),name='road_map_create'),
    path('road_map/',views.NodeAllView.as_view(),name='road_map_all'),
    path('road_map/<int:pk>',views.NodeGetView.as_view(),name='road_map_one'),
    path('road_map/delete/<int:pk>',views.NodeDeleteView.as_view(),name='road_map_delete'),

    ## questions
    path('question/create/',views.QuestionAddView.as_view(),name='question_create'),
    path('question/<int:pk>',views.QuestionGetView.as_view(),name='question_get_one'),
    path('question/',views.QuestionAllView.as_view(),name='question_get_all'),
    path('question/delete/<int:pk>',views.DeleteQuestionView.as_view(),name='question_get_delete'),

    ## Testing endpoints
    path('users/', views.UserView.as_view(), name='users_getAll'),
    path('', views.getRoutes)
]