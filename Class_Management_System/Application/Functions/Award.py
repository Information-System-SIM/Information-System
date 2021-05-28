import os
from urllib.parse import quote

from django.http import FileResponse, StreamingHttpResponse, HttpResponseRedirect
from django.shortcuts import render

from Application import models
from Application.Functions.function import get_image_path
from Class_Management_System.settings import BASE_DIR
import tkinter.messagebox as ms

def award_upload_page(request):
    return render(request, "award_upload.html", locals())