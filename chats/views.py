from django.http import HttpResponse
from django.views.generic.edit import FormView


class ChatView(FormView):
    def get(self, request):
        return HttpResponse('Chats result')

    def post(self, request):
        return HttpResponse('Chats result: post')