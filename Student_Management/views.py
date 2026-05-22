from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Student
import json


@csrf_exempt
def user_login(request):
    if request.method == "POST":
        data = json.loads(request.body)

        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            return JsonResponse({
                "status": "error",
                "message": "Username and password required"
            }, status=400)

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            return JsonResponse({
                "status": "success",
                "message": "Login successful"
            })

        return JsonResponse({
            "status": "error",
            "message": "Invalid credentials"
        }, status=401)

    return JsonResponse({
        "status": "error",
        "message": "Only POST method allowed"
    }, status=405)


@login_required
@csrf_exempt
def user_logout(request):
    if request.method == "POST":
        logout(request)

        return JsonResponse({
            "status": "success",
            "message": "Logged out successfully"
        })

    return JsonResponse({
        "status": "error",
        "message": "Only POST method allowed"
    }, status=405)


def student_show(request):
    students = Student.objects.all()

    data = []

    for student in students:
        data.append({
            "id": student.id,
            "name": student.name,
            "age": student.age,
            "course": student.course,
            "created_at": student.created_at,
        })

    return JsonResponse({
        "status": "success",
        "message": "Students retrieved successfully",
        "data": data
    })


def student_get(request, id):
    try:
        student = Student.objects.get(id=id)

        data = {
            "id": student.id,
            "name": student.name,
            "age": student.age,
            "course": student.course,
            "created_at": student.created_at,
        }

        return JsonResponse({
            "status": "success",
            "data": data
        })

    except Student.DoesNotExist:
        return JsonResponse({
            "status": "error",
            "message": "Student not found"
        }, status=404)


@csrf_exempt
@login_required
def student_create(request):
    if request.method == "POST":
        data = json.loads(request.body)

        student = Student.objects.create(
            name=data["name"],
            age=data["age"],
            course=data["course"],
        )

        return JsonResponse({
            "status": "success",
            "message": "Student created",
            "data": {
                "id": student.id,
                "name": student.name,
                "age": student.age,
                "course": student.course,
            }
        })

    return JsonResponse({
        "status": "error",
        "message": "Only POST method allowed"
    }, status=405)


@csrf_exempt
@login_required
def student_update(request, id):
    if request.method == "PUT":
        try:
            student = Student.objects.get(id=id)
            data = json.loads(request.body)

            student.name = data.get("name", student.name)
            student.age = data.get("age", student.age)
            student.course = data.get("course", student.course)
            student.save()

            return JsonResponse({
                "status": "success",
                "message": "Student updated"
            })

        except Student.DoesNotExist:
            return JsonResponse({
                "status": "error",
                "message": "Student not found"
            }, status=404)

    return JsonResponse({
        "status": "error",
        "message": "Only PUT method allowed"
    }, status=405)


@csrf_exempt
@login_required
def student_delete(request, id):
    if request.method == "DELETE":
        try:
            student = Student.objects.get(id=id)
            student.delete()

            return JsonResponse({
                "status": "success",
                "message": "Student deleted"
            })

        except Student.DoesNotExist:
            return JsonResponse({
                "status": "error",
                "message": "Student not found"
            }, status=404)

    return JsonResponse({
        "status": "error",
        "message": "Only DELETE method allowed"
    }, status=405)