from django.forms import ModelForm
from .models import Client
from localflavor.br.forms import BRCPFField


class ClientForm(ModelForm):
    """
    Formulário para gestão dos dados do cliente.
    Usado em CreateView e UpdateView.
    """
    class Meta:
        model = Client
        fields = ['name', 'cpf', 'age']
        labels = {
            'cpf':'CPF',
        }

    cpf = BRCPFField(label=u'CPF')
    
    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            print(field_name)
            if field_name == 'cpf':
                field.widget.attrs['data-mask'] = "000.000.000-00"
                field.widget.attrs['placeholder'] = 'XXX.XXX.XXX-XX'
                field.widget.attrs['class'] = 'mask'
