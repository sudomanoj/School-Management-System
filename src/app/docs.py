from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from . import serializers

LISTSTUDENTS = swagger_auto_schema(
    tags=['student'],
    operation_summary='List all students.',
    operation_description='This endpoint retrieves all students of the site.',
    operation_id='list_students',
    request_body=None,
    responses={200: serializers.StudentReadSerializer(many=True), 400: "Invalid data"}
)

student_example = {
    "user": {
        "username": "manoj",
        "password": "manoj123",
        "first_name": "Manoj",
        "last_name": "Paudel",
        "email": "contact@manoj.com"
    },
    "roll_no": "46",
    "stu_class": 10,
    "section": "A"
}

CREATESTUDENT = swagger_auto_schema(
    tags=['student'],
    operation_summary='Create a student.',
    operation_description='This endpoint a student.',
    operation_id='create',
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'user': openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'username': openapi.Schema(type=openapi.TYPE_STRING),
                    'password': openapi.Schema(type=openapi.TYPE_STRING),
                    'first_name': openapi.Schema(type=openapi.TYPE_STRING),
                    'last_name': openapi.Schema(type=openapi.TYPE_STRING),
                    'email': openapi.Schema(type=openapi.TYPE_STRING),
                },
            ),
            'roll_no': openapi.Schema(type=openapi.TYPE_STRING),
            'stu_class': openapi.Schema(type=openapi.TYPE_INTEGER),
            'section': openapi.Schema(type=openapi.TYPE_STRING),
        },
        example=student_example
    ),
    responses={201: "Student created successfully", 400: "Invalid data"}
)


USERLOGIN = swagger_auto_schema(
    tags=['login'],
    operation_summary='Login a student.',
    operation_description='This endpoint logs in a student.',
    operation_id='login_student',
    request_body=serializers.UserLoginSerializer,
    responses={200: "Login successful", 400: "Invalid credentials"}
)

UPDATESTUDENT = swagger_auto_schema(
    tags=['student'],
    operation_summary='Update the student.',
    operation_description='This endpoint updates a student by id.',
    operation_id='update_student',
    request_body=serializers.StudentWriteSerializer,
    responses={204: "Student updated successfully", 400: "Invalid data"}
)

STUDENTRETRIEVE = swagger_auto_schema(
    tags=['student'],
    operation_summary='Retrieve a student.',
    operation_description='This endpoint retrieves a student by id.',
    operation_id='retrieve_student',
    request_body=None,
    responses={200: serializers.StudentReadSerializer, 400: "Invalid data"}
)

DELETESTUDENT = swagger_auto_schema(
    tags=['student'],
    operation_summary='Delete a student.',
    operation_description="This endpoint deletes a student by student's id.",
    operation_id='delete_student',
    request_body=None,
    responses={204: "Student deleted successfully", 400: "Invalid data"}
)


### Subject Docs ###

LISTSUBJECTS = swagger_auto_schema(
        tags=['subject'],
        operation_summary='List all subjects.',
        operation_description='This endpoint retrieves all subjects of the site.',
        operation_id='list_subjects',
        responses={200: serializers.SubjectSerializer(many=True), 400: "Invalid data"}
    )

UPDATESUBJECT = swagger_auto_schema(
        tags=['subject'],
        operation_summary='Update a subject.',
        operation_description='This endpoint updates a subject according to provided id.',
        operation_id='update_subject',
        responses={204: "Subject updated successfully", 400: "Invalid data"}
    )

subject_example = {
  "name": "Science",
  "code": "Sc-001",
  "description": "Science is so important."
}

CREATESUBJECT = swagger_auto_schema(
        tags=['subject'],
        operation_summary='Create a new subject.',
        operation_description='This endpoint creates a new subject.',
        operation_id='create_subject',
        request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'name': openapi.Schema(type=openapi.TYPE_STRING),
            'code': openapi.Schema(type=openapi.TYPE_STRING),
            'description': openapi.Schema(type=openapi.TYPE_STRING)
        },
        example=subject_example
    ),
        responses={201: serializers.SubjectSerializer, 400: "Invalid data"}
    )


DELETESUBJECT = swagger_auto_schema(
    tags=['subject'],
    operation_summary='Delete a subject.',
    operation_description="This endpoint deletes a subject by subject's id.",
    operation_id='delete_subject',
    request_body=None,
    responses={204: "Subject deleted successfully", 400: "Invalid data"}
)

SUBJECTRETRIEVE = swagger_auto_schema(
    tags=['subject'],
    operation_summary='Retrieve a subject.',
    operation_description='This endpoint retrieves a subject by id.',
    operation_id='retrieve_subject',
    request_body=None,
    responses={200: serializers.SubjectSerializer, 400: "Invalid data"}
)


LISTEXAMCATEGORIES = swagger_auto_schema(
    tags=['exam_category'],
    operation_summary='List all exam categories.',
    operation_description='This endpoint retrieves all exam categories of the site.',
    operation_id='list_exam_categories',
    responses={200: serializers.ExamCategorySerializer(many=True), 400: "Invalid data"}
)

exam_category_example = {
    'name' : 'Oral Test',
    'is_active' : True,
    'description' : 'Oral Test'
}

CREATEEXAMCATEGORY = swagger_auto_schema(
        tags=['exam_category'],
        operation_summary='Create a new exam_category.',
        operation_description='This endpoint creates a new exam category.',
        operation_id='create_exam_category',
        request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'name': openapi.Schema(type=openapi.TYPE_STRING),
            'is_active': openapi.Schema(type=openapi.TYPE_BOOLEAN),
            'description': openapi.Schema(type=openapi.TYPE_STRING)
        },
        example=exam_category_example
    ),
        responses={201: serializers.ExamCategorySerializer, 400: "Invalid data"}
    )


EXAMCATEGORYRETRIEVE = swagger_auto_schema(
    tags=['exam_category'],
    operation_summary='Retrieve a exam category.',
    operation_description='This endpoint retrieves a exam category by id.',
    operation_id='retrieve_exam_category',
    request_body=None,
    responses={200: serializers.ExamCategorySerializer, 400: "Invalid data"}
)

UPDATEEXAMCATEGORY = swagger_auto_schema(
    tags=['exam_category'],
    operation_summary='Update a exam_category.',
    operation_description='This endpoint updates a exam category according to provided id.',
    operation_id='update_exam_category',
    responses={204: "Exam Category updated successfully", 400: "Invalid data"}
)


DELETEEXAMCATEGORY = swagger_auto_schema(
    tags=['exam_category'],
    operation_summary='Delete a exam_category.',
    operation_description="This endpoint deletes a exam category by category's id.",
    operation_id='delete_exam_category',
    request_body=None,
    responses={204: "Exam Category deleted successfully", 400: "Invalid data"}
)


LISTEXAMS = swagger_auto_schema(
    tags=['exam'],
    operation_summary='List all exams.',
    operation_description='This endpoint retrieves all exams of the site.',
    operation_id='list_exams',
    responses={200: serializers.ExamReadSerializer(many=True), 400: "Invalid data"}
)

exam_example = {
    "name": "Mid-Term 2024",
    "year": "2024",
    "student": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "category": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "marks": "48.50"
}


CREATEEXAM = swagger_auto_schema(
    tags=['exam'],
    operation_summary='Create a new exam.',
    operation_description='This endpoint creates a new exam category.',
    operation_id='create_exam',
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'name': openapi.Schema(type=openapi.TYPE_STRING, description="Name of the exam"),
            'year': openapi.Schema(type=openapi.TYPE_STRING, description="Examination year"),
            'student': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_UUID, description="UUID of the student"),
            'category': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_UUID, description="UUID of the exam category"),
            'marks': openapi.Schema(type=openapi.TYPE_STRING, description="Marks obtained")
        },
        example=exam_example
    ),
    responses={201: serializers.ExamCategorySerializer, 400: "Invalid data"}
)


EXAMRETRIEVE = swagger_auto_schema(
    tags=['exam'],
    operation_summary='Retrieve an exam.',
    operation_description='This endpoint retrieves an exam by id.',
    operation_id='retrieve_exam',
    request_body=None,
    responses={200: serializers.ExamReadSerializer, 400: "Invalid data"}
)

UPDATEEXAM = swagger_auto_schema(
    tags=['exam'],
    operation_summary='Update an exam.',
    operation_description='This endpoint updates an exam according to provided id.',
    operation_id='update_exam',
    responses={204: "Exam updated successfully", 400: "Invalid data"}
)


DELETEEXAM = swagger_auto_schema(
    tags=['exam'],
    operation_summary='Delete an exam.',
    operation_description="This endpoint deletes an exam by exam's id.",
    operation_id='delete_exam',
    request_body=None,
    responses={204: "Exam deleted successfully", 400: "Invalid data"}
)