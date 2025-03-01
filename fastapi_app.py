from fastapi import FastAPI
import os
import django
from django.contrib.auth.models import User

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mbbs_backend.settings')
django.setup()


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to MBBS Coaching API"}

@app.get("/users/")
def list_users():
    return [{"id": user.id, "username": user.username} for user in User.objects.all()]
