from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import CreatePdf
from .serializers import CreatePdfSerializer
# Create your views here.

@api_view(["GET","POST"])
def CreatePdfView(request):
    if request.method == "POST":
        data = request.data
        pdf = data.get("pdf")
        dept = data.get("dept")
        session = data.get("session")
        course_title = data.get("course_title")
        teacher = data.get("teacher")
        contributor = data.get("contributor")

        object = CreatePdf(
            pdf = pdf,
            dept = dept,
            session = session,
            course_title = course_title,
            teacher = teacher,
            contributor = contributor
        )
        object.save()

        serializer = CreatePdfSerializer(object)
        return Response(status=status.HTTP_201_CREATED,data=serializer.data)
    

    elif request.method == "GET":
        objects = CreatePdf.objects.filter(is_approved=True)
        serializer = CreatePdfSerializer(objects,many=True)
        return Response(serializer.data)
    
    return Response({"Status":"Currently in live"})

# http://127.0.0.1:8000/createpdf/

@api_view(["GET"])
def GetPdfView(request):
    dept = request.GET.get("dept")
    session = request.GET.get("session")

    objects = CreatePdf.objects.filter(dept=dept,is_approved=True)
    if objects.count() == 0:
        return Response({"Status":"No data found"})

    serializer = CreatePdfSerializer(objects,many=True)
    return Response(serializer.data)

# http://127.0.0.1:8000/getpdf/?dept=CSE


# search funtions
@api_view(["GET"])
def SearchView(request):
    teacher = request.GET.get("teacher")

    objects = CreatePdf.objects.filter(teacher__contains=teacher,is_approved=True)

    if objects.count() == 0:
        return Response({"Status":"No data found"})
    
    serializer = CreatePdfSerializer(objects,many=True)
    return Response(serializer.data)

# http://127.0.0.1:8000/searchpdf/?teacher=al

{
    "pdf":"pdf",
    "dept":"dept",
    "session":"session",
    "course_title":"course_title",
    "teacher":"teacher",
    "contributor":"contributor"
}
