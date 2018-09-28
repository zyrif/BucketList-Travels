from django.shortcuts import render, HttpResponse, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .models import Destination, Lodging, Room
from .forms import SearchForm, FilterForm

# Create your views here.


def index(request):
    if request.method == 'POST':
        # TO-DO: implement this with django forms to sanitize input data
        # search_string = request.POST.get('search')
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


class SearchView(ListView):
    model = Lodging
    template_name = 'home/search.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # add extra context here
        if 'place' in self.request.session:
            place = Destination.objects.get(name=self.request.session['place'])
            context['place_name'] = place.name
            context['place_description'] = place.description
            context['filter_form'] = FilterForm()

        return context
