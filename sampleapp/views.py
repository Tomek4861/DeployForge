from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from . import forms


# Create your views here.


class HomeAPIView(APIView):
    def get(self, request):
        return Response(dict(message="Hello world"))

    def put(self, request):
        return Response(dict(message="PUT request received"))

    def post(self, request):
        return Response(dict(message="POST request received"))


@api_view(['DELETE'])
def user_delete(request):
    return Response(dict(message="Received DELETE request at /user"))


def home(request):
    return render(request, 'index.html')


def portfolio_page(request):
    return render(request, 'portfolio.html')


def contact_page(request):
    if request.method == 'POST':
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]
            print(f"New contact message from {name} ({email}): {message}")

    form = forms.ContactForm()
    return render(request, 'contact.html', {'form': form})
