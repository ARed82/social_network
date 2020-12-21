from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView, View

from accounts.forms import SignUpForm
from .clearbit import Clearbit


class SignUpView(View):
    def get(self, request):
        form = SignUpForm()

        response = Clearbit('andreyredkin82@gmail.com').enrichment_api()
        args = {'form': form}
        return render(request, 'signup_form.html', args)

    def post(self, request):
        return HttpResponse('Accounts result: post')


