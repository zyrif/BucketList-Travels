from django.shortcuts import render, reverse, render_to_response
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import FormView
from .models import Destination, Lodging, Room, Booking
from .forms import SearchForm, FilterForm
import math

# Create your views here.


def index(request):
    if request.method == 'POST':

        search_form = SearchForm(request.POST)

        if search_form.is_valid():
            search_string = search_form.cleaned_data['search']
            try:
                place = Destination.objects.get(name__icontains=search_string)
            except Destination.DoesNotExist:
                error_desc = "Destination does not exist."
                error_desc += "Are you sure you entered the correct spelling?"
                error_desc += "If you think this is a mistake,"
                error_desc += " please submit a bug report."
                search_form.add_error(
                    'search', error_desc)
                return render(request, 'home/index.html',
                              {'form': search_form})
            if place:
                request.session['place'] = place.name
                return HttpResponseRedirect(reverse('searchpage'))

        return render(request, 'home/index.html', {'form': search_form})
    else:
        return render(request, 'home/index.html', {'form': SearchForm()})


@login_required
def profileView(request):
    return HttpResponse('Profile page will be here')


@login_required
def ProcessBooking(request):
    pass

# class SearchView(TemplateView):
#     # model = Lodging
#     template_name = 'home/search.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         # add extra context here
#         if 'place' in self.request.session:
#             place = Destination.objects.get(name=self.request.session['place']) # noqa: E501
#             context['place_name'] = place.name
#             context['place_description'] = place.description
#             context['filter_form'] = FilterForm()

#         return context

#     def post(self, request, *args, **kwargs):
#         context = self.get_context_data(**kwargs)
#         filter_form = FilterForm(request.POST)
#         if filter_form.is_valid():
#             return HttpResponseRedirect(reverse('selectionpage'))

#         return super(TemplateView, self).render_to_response(context)


# add custom decorator to access the page.
# If place name is not set in session, redirect to home page.
# IF SESSION VARIABLE NAMES ARE CHANGED, UPDATE DECORATORS ACCORDINGLY!
class SearchView(FormView):
    form_class = FilterForm
    template_name = 'home/search.html'
    success_url = '/selection'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # add extra context here
        if 'place' in self.request.session:
            place = Destination.objects.get(name=self.request.session['place'])
            context['place_name'] = place.name
            context['place_description'] = place.description
            context['place_background'] = place.background
            context['filter_form'] = FilterForm()

        return context

    def form_valid(self, form):
        self.request.session['start_date'] = str(
            form.cleaned_data['start_date'])
        self.request.session['end_date'] = str(form.cleaned_data['end_date'])
        self.request.session['people'] = str(form.cleaned_data['capacity'])
        self.request.session['stay_days'] = str(
            form.cleaned_data['end_date'].day - form.cleaned_data['start_date'].day)
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


# add custom decorator to access the page.
# If filter details are not set in session, redirect to search page.
# IF SESSION VARIABLE NAMES ARE CHANGED, UPDATE DECORATORS ACCORDINGLY!
class SelectionView(ListView):
    model = Room
    template_name = 'home/selection.html'
    context_object_name = 'rooms'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

    def post(self, request, *args, **kwargs):
        room_id = request.POST.get('room_id')
        request.session['room_id'] = room_id
        return HttpResponseRedirect(reverse('bookingpage'))
        # return HttpResponse(
        # 'Booking page will be here. Room ID: {}'.format(room_id))


class BookingView(LoginRequiredMixin, TemplateView):
    template_name = 'home/booking.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['user'] = self.request.user
        context['no_of_people'] = self.request.session.get('people')

        room_obj = Room.objects.get(
            id=int(self.request.session.get('room_id')))

        context['room'] = room_obj

        room_price = room_obj.price
        room_required = (math.ceil(int(self.request.session.get('people')
                                       ) / int(room_obj.capacity)))

        room_cost = (int(room_price) * int(room_required) *
                     int(self.request.session.get('stay_days')))

        context['stay_days'] = self.request.session.get('stay_days')
        context['room_price'] = room_price
        context['room_required'] = room_required
        context['room_cost'] = room_cost

        context['start_date'] = self.request.session.get('start_date')
        context['end_date'] = self.request.session.get('end_date')

        # context['session_keys'] = [key for key in self.request.session.keys()]
        # context['session_data'] = [self.request.session[key]
        #                            for key in self.request.session.keys()]
        return context
