from django.views import View
from django.views.generic.base import TemplateView
from django.http.response import HttpResponse
from django.shortcuts import render


line_of_cars = {"change_oil": {"time": 2, "queue": []}, "inflate_tires": {"time": 5, "queue": []},
                "diagnostic": {"time": 30, "queue": []}, "next": ""}
client_id = 1


class WelcomeView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('<h2>Welcome to the Hypercar Service!</h2>')


class MenuView(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'tickets/menu.html', context=None)


class NextView(View):
    def get(self, request, *args, **kwargs):
        next_car = line_of_cars['next'] if line_of_cars['next'] else "Nobody"
        if next_car != "Nobody":
            nexto = f"Next ticket #{line_of_cars['next']}"
        else:
            nexto = "Waiting for the next client"
        return render(request, 'tickets/next.html', context={'next_client': nexto})


class ProcessView(View):
    # if request.method == "POST":

    def post(self, request, *args, **kwargs):
        if len(line_of_cars['change_oil']['queue']) > 0:
            nxt = line_of_cars['change_oil']['queue'].pop(0)
        elif len(line_of_cars['inflate_tires']['queue']) > 0:
            nxt = line_of_cars['inflate_tires']['queue'].pop(0)
        elif len(line_of_cars['diagnostic']['queue']) > 0:
            nxt = line_of_cars['diagnostic']['queue'].pop(0)
        else:
            nxt = ""
        line_of_cars['next'] = nxt
        return render(request, 'tickets/process.html', context={'line_of_cars': line_of_cars})

    def get(self, request, *args, **kwargs):

        return render(request, 'tickets/process.html', context={'line_of_cars': line_of_cars})


class TickView(View):

    def get(self, request, *args, **kwargs):
        client = dict()
        global client_id
        client['id'] = client_id
        client_id += 1

        if 'oil' in request.path:
            client['service'] = "change_oil"
            wait_time = len(line_of_cars["change_oil"]["queue"]) * line_of_cars["change_oil"]["time"]
        elif 'tires' in request.path:
            client['service'] = "inflate_tires"
            wait_time = len(line_of_cars["inflate_tires"]["queue"]) * line_of_cars["inflate_tires"]["time"] + len(line_of_cars["change_oil"]["queue"]) * line_of_cars["change_oil"]["time"]

        else:
            client['service'] = "diagnostic"
            wait_time = len(line_of_cars["diagnostic"]["queue"]) * line_of_cars["diagnostic"]["time"] + len(line_of_cars["inflate_tires"]["queue"]) * line_of_cars["inflate_tires"]["time"] + len(line_of_cars["change_oil"]["queue"]) * line_of_cars["change_oil"]["time"]
        if wait_time < 0:
            wait_time = 0
        client['wait'] = wait_time
        line_of_cars[client['service']]["queue"].append(client["id"])
        # print(line_of_cars)

        return render(request, 'tickets/ticket_page.html', context={'client': client, 'line_of_cars': line_of_cars})


class TicketView(TemplateView):
    template_name = 'tickets/ticket_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # n_chapter = kwargs['n_chapter']
        context['ticket_number'] = kwargs['ticket_number']
        # if kwargs['ticket_type'] ==
        # context['wait_time'] = timer
        return context

