from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, SubjectListCreateView, SubjectRetrieveUpdateDestroyView, ExamCategoryListCreateView, ExamCategoryRetrieveUpdateDestroyView, ExamListCreateView, ExamRetrieveUpdateDestroyView

router = DefaultRouter()
router.register(r'students', StudentViewSet, basename='student')

urlpatterns = [
    path('', include(router.urls)),
    path('subjects/', SubjectListCreateView.as_view(), name='subject-list-create'),
    path('subjects/<uuid:id>/', SubjectRetrieveUpdateDestroyView.as_view(), name='subject-detail'),
    path('exam_category/', ExamCategoryListCreateView.as_view(), name='exam_category-list-create'),
    path('exam_category/<uuid:id>/', ExamCategoryRetrieveUpdateDestroyView.as_view(), name='exam-category-detail'),
    path('exam/', ExamListCreateView.as_view(), name='exam-list-create'),
    path('exam/<uuid:id>/', ExamRetrieveUpdateDestroyView.as_view(), name='exam-detail'),
]