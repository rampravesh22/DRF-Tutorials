from rest_framework.views import APIView
from rest_framework.response import Response
from core.serailizers import StudentSerializer
from core.models import Student
# Create your views here.


class StudentView(APIView):
    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "data added sucessfully"})
        return Response(serializer.errors)

    def get(self, request, id=None, format=None):
        if id is None:
            students = Student.objects.all()
            serializer = StudentSerializer(students, many=True)
            print(Response(serializer.data))
            return Response(serializer.data)
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def delete(self, request, id, format=None):
        student = Student.objects.get(id=id)
        student.delete()
        return Response({"msg": "student is deleted"})

    def put(self, request, id, format=None):
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "data updated successfully"})
        return Response(serializer.errors)

    def patch(self, request, id, format=None):
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(
            student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "partial data updated successfully"})
        return Response(serializer.errors)
# v2022.9.30
