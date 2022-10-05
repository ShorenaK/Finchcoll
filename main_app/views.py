from multiprocessing import context
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect
from django.views import View
from django.views.generic.base import TemplateView
from .models import Finchcoll, Location, Season
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
# Create your views here.
class Home(TemplateView):
    template_name = "home.html"
# Here we will be creating a class called Home and extending it from the View class
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["seasons"] = Season.objects.all()
        return context


class About(TemplateView):
    template_name = "about.html"



class FinchcollList(TemplateView):
    template_name = "finchcoll_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        # If a query exists we will filter by name 
        if name != None:
            # .filter is the sql WHERE statement and name__icontains is doing a search for any name that contains the query param
            context["finchcolls"] = Finchcoll.objects.filter(name__icontains=name)
            context["header"] = f"Searching for {name}"
        else:
            context["finchcolls"] = Finchcoll.objects.all()
            context["header"] = "The Best Birds"
        return context
        
class FinchcollCreate(CreateView):
    model = Finchcoll
    fields = ['name', 'image', 'bio', 'verified_artist']
    template_name = "finchcoll_create.html"
    def get_success_url(self):
        return reverse('finchcoll_detail', kwargs={'pk': self.object.pk})
        
class FinchcollDetail(DetailView):
    model = Finchcoll
    template_name = "finchcoll_detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["seasons"] = Season.objects.all()
        return context

class FinchcollUpdate(UpdateView):
      model = Finchcoll
      fields = ['name', 'image', 'bio', 'verified_artist']
      template_name = "finchcoll_update.html"
      def get_success_url(self):
          return reverse('finchcoll_detail', kwargs={'pk': self.object.pk})


class FinchcollDelete(DeleteView):
    model = Finchcoll
    template_name = "finchcoll_delete_confirmation.html"
    success_url = "/finchcolls/"     

class LocationCreate(View):

    def post(self, request, pk):
        location_name = request.POST.get("location_name")
        finchcoll = Finchcoll.objects.get(pk=pk)
        Location.objects.create(location_name=location_name, finchcall=finchcoll)
        return redirect('finchcoll_detail', pk=pk)


class  SeasonLocationAssoc(View):

    def get(self, request, pk, location_pk):
        # get the query param from the url
        assoc = request.GET.get("assoc")
        if assoc == "remove":
            # get the playlist by the id and
            # remove from the join table the given song_id
            Season.objects.get(pk=pk).seasons.remove(location_pk)
        if assoc == "add":
            # get the playlist by the id and
            # add to the join table the given song_id
            Season.objects.get(pk=pk).seasons.add(location_pk)
        return redirect('home')





       