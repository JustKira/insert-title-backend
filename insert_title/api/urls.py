from django.urls import path
from .views import PostingGetAllView, PostingGetView, PostingDeleteView, PostingAddView, PostingUpdateView

urlpatterns = [
    path('postings/', PostingGetAllView.as_view()),
    path('postings/<int:pk>', PostingGetView.as_view()),
    path('postings/delete/<int:pk>', PostingDeleteView.as_view()),
    path('postings/create/', PostingAddView.as_view()),
    path('postings/update/<int:pk>', PostingUpdateView.as_view()),
]