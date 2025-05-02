from rest_framework import serializers
from .models import Student, Subject, ExamCategory, Exam, User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email']
        extra_kwargs = {'password': {'write_only': True}}


class StudentWriteSerializer(serializers.ModelSerializer):
    user = UserCreateSerializer()
    
    class Meta:
        model = Student
        fields = ['user', 'roll_no', 'stu_class', 'section']
    
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        
        # Create student profile
        student = Student.objects.create(
            user=user,
            roll_no=validated_data.get('roll_no'),
            stu_class=validated_data.get('stu_class'),
            section=validated_data.get('section')
        )
        return student

class StudentReadSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Student
        fields = ['id', 'user_name', 'roll_no', 'stu_class', 'section']
        extra_kwargs = {'roll_no': {'read_only': True}}
        
        
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        user = authenticate(
            username=attrs.get('username'),
            password=attrs.get('password')
        )
        if not user:
            raise serializers.ValidationError("Invalid credentials")
        
        refresh = RefreshToken.for_user(user)

        return {
            "message": "User Logged In successfully!",
            "access": str(refresh.access_token),
            "refresh": str(refresh),
        }
        
        
        
class SubjectSerializer(serializers.ModelSerializer):
    """
    Serializer for Subject model
    """
    class Meta:
        model = Subject
        fields = ['id', 'name', 'code', 'description']
        read_only_fields = ['id']
        
    
        
class ExamCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamCategory
        fields = ['id', 'name', 'is_active', 'description']
        read_only_fields = ['id']
        
        
class ExamWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = [
            'name', 'year', 'student', 'category', 'marks'
        ]
        
    def validate(self, attrs):
        marks = attrs.get('marks')
        if marks > 50:
            raise serializers.ValidationError(
                f"Maximum marks for the student is 50."
            )
        return attrs
        
        
class ExamReadSerializer(serializers.ModelSerializer):
    student = StudentReadSerializer(read_only=True)
    category = ExamCategorySerializer(read_only=True)

    class Meta:
        model = Exam
        fields = [
            'id', 'name', 'year', 'student', 'category', 'marks'
        ]