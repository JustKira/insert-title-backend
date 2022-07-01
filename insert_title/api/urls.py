from django.urls import path
from .views import PostingGetAllView, PostingGetView, PostingDeleteView, PostingAddView, PostingUpdateView, MyTokenObtainPairView, RegisterView, getRoutes
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('postings/', PostingGetAllView.as_view()),
    path('postings/<int:pk>', PostingGetView.as_view()),
    path('postings/delete/<int:pk>', PostingDeleteView.as_view()),
    path('postings/create/', PostingAddView.as_view()),
    path('postings/update/<int:pk>', PostingUpdateView.as_view()),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('', getRoutes)
]