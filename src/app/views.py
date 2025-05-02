from rest_framework import viewsets
from .models import Student, Subject, ExamCategory, Exam
from .serializers import StudentReadSerializer, StudentWriteSerializer, UserLoginSerializer, SubjectSerializer, ExamCategorySerializer, ExamWriteSerializer, ExamReadSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from .permissions import IsStaff, IsStaffOrOwner
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from . import docs
from drf_yasg.utils import swagger_auto_schema

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.select_related(
        'user'
    )
    
    def get_permissions(self):
        if self.action in ['create', 'login']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsStaffOrOwner]
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return StudentWriteSerializer
        return StudentReadSerializer
    
    @docs.LISTSTUDENTS
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @docs.CREATESTUDENT
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @docs.STUDENTRETRIEVE
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @action(detail=False, methods=['post'])
    @docs.USERLOGIN
    def login(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
    
    @docs.swagger_auto_schema(auto_schema=None)
    def update(self, request, *args, **kwargs):
        """Handles complete store update"""
        raise MethodNotAllowed("Put method is not allowed.")
    
    @docs.UPDATESTUDENT
    def partial_update(self, request, *args, **kwargs):
        """Handles complete store update"""
        response = super().update(request, *args, **kwargs)
        return Response(response.data, status=status.HTTP_204_NO_CONTENT)
    
    @docs.DELETESTUDENT
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)



### Subject Section ###
class SubjectListCreateView(ListCreateAPIView):
    """
    View to list all subjects or create a new subject
    """
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [IsAuthenticated]
    
    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAdminUser()]
        return [IsAuthenticated()]
    
    @docs.LISTSUBJECTS
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @docs.CREATESUBJECT
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class SubjectRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update or delete a subject
    """
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'
    
    def get_permissions(self):
        if self.request.method in ['PATCH', 'DELETE']:
            return [IsAdminUser()]
        return [IsAuthenticated()]
    
    @docs.SUBJECTRETRIEVE
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    @docs.UPDATESUBJECT
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)
    
    @docs.DELETESUBJECT
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
    
    @docs.swagger_auto_schema(auto_schema=None)
    def put(self, request, *args, **kwargs):
        """Handles complete store update"""
        raise MethodNotAllowed("Put method is not allowed.")
    
    
### Exam Category Section ###
class ExamCategoryListCreateView(ListCreateAPIView):
    """
    View to list all categories or create a new category
    """
    queryset = ExamCategory.objects.filter(is_active=True)
    serializer_class = ExamCategorySerializer
    permission_classes = [IsAuthenticated]
    
    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAdminUser()]
        return [IsAuthenticated()]
    
    @docs.LISTEXAMCATEGORIES
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @docs.CREATEEXAMCATEGORY
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    
    
class ExamCategoryRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update or delete a subject
    """
    queryset = ExamCategory.objects.filter(is_active=True)
    serializer_class = ExamCategorySerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'
    
    def get_permissions(self):
        if self.request.method in ['PATCH', 'DELETE']:
            return [IsAdminUser()]
        return [IsAuthenticated()]
    
    @docs.EXAMCATEGORYRETRIEVE
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    @docs.UPDATEEXAMCATEGORY
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)
    
    @docs.DELETEEXAMCATEGORY
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
    
    @docs.swagger_auto_schema(auto_schema=None)
    def put(self, request, *args, **kwargs):
        """Handles complete store update"""
        raise MethodNotAllowed("Put method is not allowed.")
    
    

### Exam Section ###
class ExamListCreateView(ListCreateAPIView):
    """
    View to list all categories or create a new 
    """
    queryset = Exam.objects.all()
    permission_classes = [IsAuthenticated]
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ExamReadSerializer
        return ExamWriteSerializer
    
    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAdminUser()]
        return [IsAuthenticated()]
    
    @docs.LISTEXAMS
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @docs.CREATEEXAM
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    
class ExamRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update or delete a subject
    """
    queryset = Exam.objects.all()
    serializer_class = ExamWriteSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'
    
    def get_permissions(self):
        if self.request.method in ['PATCH', 'DELETE']:
            return [IsAdminUser()]
        return [IsAuthenticated()]
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ExamReadSerializer
        return ExamWriteSerializer
    
    @docs.EXAMRETRIEVE
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    @docs.UPDATEEXAM
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)
    
    @docs.DELETEEXAM
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
    
    @docs.swagger_auto_schema(auto_schema=None)
    def put(self, request, *args, **kwargs):
        """Handles complete store update"""
        raise MethodNotAllowed("Put method is not allowed.")