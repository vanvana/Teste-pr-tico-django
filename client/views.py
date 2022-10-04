from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import UpdateView, CreateView, ListView, DeleteView
from client.forms import ClientForm
from client.models import Client


class CreateClient(CreateView):
    """
    Screen to create a customer
    """
    model = Client
    template_name = 'client/create_client.html'
    success_url = reverse_lazy('list-client')
    form_class = ClientForm


class UpdateClient(UpdateView):
    """
    Screen to edit a customer's data
    """
    model = Client
    template_name = 'client/update_client.html'
    success_url = reverse_lazy('list-client')
    form_class = ClientForm


class ListClient(ListView):
    """
    Screen to list a client's data
    """
    model = Client
    template_name = 'client/list_client.html'
    
    def get_queryset(self):
        queryset = super(ListClient, self).get_queryset()
        queryset = Client.objects.all()
        
        name = self.request.GET.get('name')
        cpf = self.request.GET.get('cpf')
        age = self.request.GET.get('age')

        if name:
            queryset = queryset.filter(name__icontains=name)
        
        if cpf:
            queryset = queryset.filter(cpf__icontains=cpf)
        
        if age:
            queryset = queryset.filter(age=age)
        
        return queryset


def delete_client(request, pk):
    client = get_object_or_404(Client, pk=pk)
    client.delete()
    return redirect('list-client')


class DeleteClient(DeleteView):
    model = Client
    template_name = 'client/delete_client.html'
    success_url = reverse_lazy('list-client')

def Features(request):
    return render(request, 'client/features.html')








"""
for i in range(100):
    ga_item,created = GapAnalysisItem.objects.get_or_create(gap_analysis=ga,text='Questão - {}'.format(i),order=i)
"""