# Create your views here.

from django.contrib import messages
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from braces.views import LoginRequiredMixin

from .models import Dataset

#from .forms import DatasetForm

class DatasetActionMixin(object):
    
    @property
    def action(self):
        msg = "{0} is mission action.".format(self.__class__)
        raise NotImplementedError(msg)
        
    def form_valid(self, form):
        msg = "Dataset {0}!".format(self.action)
        messages.info(self.request, msg)
        return super(DatasetActionMixin, self).form_valid(form)
        
class DatasetListView(ListView):
    model = Dataset
    
class DatasetDetailView(DetailView):
    model = Dataset
    slug_field = 'unique_identifier'    
    
class DatasetCreateView(LoginRequiredMixin, DatasetActionMixin, CreateView):
    model = Dataset
    action = "created"
    #form_class = DatasetForm
    def get_success_url(self):
        return reverse_lazy("dataset_detail", kwargs={'slug': self.object.unique_identifier})
    
class DatasetUpdateView(LoginRequiredMixin, DatasetActionMixin, UpdateView):
    model = Dataset
    action = "updated"
    #form_class = DatasetForm
    slug_field = 'unique_identifier'
    def get_success_url(self):
        return reverse_lazy("dataset_detail", kwargs={'slug': self.object.unique_identifier})
    
class DatasetDeleteView(LoginRequiredMixin, DatasetActionMixin, DeleteView):
    model = Dataset
    action = "deleted"
    slug_field = 'unique_identifier'
    def get_success_url(self):
        return reverse_lazy("dataset_list")