# Create your views here.

from django.contrib import messages
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404

from braces.views import LoginRequiredMixin
from fancy_formsets.views import FormsetsView
from rest_framework import viewsets
from .serializers import DatasetSerializer


from .models import Dataset, Tag
from resources.models import Resource

from .forms import DatasetForm, ResourceFormSet

class DatasetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializer

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
    slug_field = 'unique_identifer'
    
class TagDetailView(DetailView):
    model = Tag    

class DatasetCreateView(LoginRequiredMixin, DatasetActionMixin, CreateView):
    model = Dataset
    action = "created"
    form_class = DatasetForm
    
    def form_valid(self):
        # override the ModelFormMixin definition so you don't save twice
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, formset):
        return self.render_to_response(self.get_context_data(form=form, formset=formset))

    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        formset = ResourceFormSet(queryset=Resource.objects.none())
        return self.render_to_response(self.get_context_data(form=form, formset=formset))

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        formset = ResourceFormSet(request.POST)
        form_valid = form.is_valid()
        formset_valid = formset.is_valid()
        if form_valid and formset_valid:
            self.object = form.save()
            resources = formset.save(commit=False)
            for resource in resources:
                resource.dataset = self.object
                resource.save()
            formset.save_m2m()
            return self.form_valid()
        else:
            return self.form_invalid(form, formset)
    
    def get_success_url(self):
        return reverse_lazy("dataset_detail", kwargs={'slug': self.object.unique_identifer})

class DatasetUpdateView(LoginRequiredMixin, DatasetActionMixin, UpdateView):
    model = Dataset
    action = "updated"
    form_class = DatasetForm
    slug_field = 'unique_identifer'
    
    def get_success_url(self):
        return reverse_lazy("dataset_detail", kwargs={'slug': self.object.unique_identifer})
    
class DatasetDeleteView(LoginRequiredMixin, DatasetActionMixin, DeleteView):
    model = Dataset
    action = "deleted"
    slug_field = 'unique_identifer'
    def get_success_url(self):
        return reverse_lazy("dataset_list")

class DataJsonView(ListView):
    model = Dataset
    template_name = "datasets/data.json"
    def render_to_response(self, context, **response_kwargs):
        response_kwargs['content_type'] = 'application/json'
        return super(ListView, self).render_to_response(context, **response_kwargs)