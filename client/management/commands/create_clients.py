from django.core.management.base import BaseCommand, CommandError
from client.models import Client
import random
from random import randint
import re
from validate_docbr import CPF

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('number', nargs='+', type=int)

    def handle(self, *args, **options):
        if len(options['number']) > 1:
            self.stderr.write("O comando requer apenas um argumento")

        for i in range(0, int(options['number'][0])):
            consoante= ['B','C','D','F','G','H','J','K','L','M','N','P','R','S','T','V','X']
            vogal = ['A','E','I','O',]
            letra1 = random.choice(consoante)
            letra2 = random.choice(vogal)
            letra3 = random.choice(consoante)
            letra4 = random.choice(vogal)
            letra5 = random.choice(consoante)
            letra6 = random.choice(vogal)
            nome = letra1 + letra2 + letra3 + letra4 + letra5 + letra6
            lista_sobrenome = ['Souza','Cruz','Alves','Lima','Santana','Altoé','Sossai','Agrizzi','De Angeli','Ferreira','da Silva','Zampirolli','Della','Coletta','Fernandes','Alves','Costalonga','Botteon','Caliman','de Oliveira','Zanette','Salvador','Silva','Zandonadi','Pesca','Falqueto','Tosi','da Costa','de Souza','Gomes','Calmon','Pereira','Sossai','de Almeida','Moreira','de Jesus','Martins','Rodrigues','Balarini','Gonçalves','Pizzol','Vieira','Breda','Bazoni','Corrêa','Filete','Oliveira','Venturim','Almeida','dos Santos','Falchetto','Barbosa','Scaramussa','Partelli','de Barros']
            sobrenome = random.choice(lista_sobrenome)
            n_completo = nome + ' ' + sobrenome
            nomecompleto = n_completo.upper()
            while  True:
                digito = ['0','1','2','3','4','5','7','8','9']
                primeiro_digito = random.choice(digito)
                segundo_digito = random.choice(digito)
                terceiro_digito = random.choice(digito)
                quarto_digito = random.choice(digito)
                quinto_digito = random.choice(digito)
                sexto_digito = random.choice(digito)
                setimo_digito = random.choice(digito)
                oitavo_digito = random.choice(digito)
                nono_digito = random.choice(digito)
                decimo_digito = random.choice(digito)
                decimop_digito = random.choice(digito)
                cpff = primeiro_digito + segundo_digito + terceiro_digito +'.'+ quarto_digito + quinto_digito + sexto_digito + '.' + setimo_digito + oitavo_digito + nono_digito + '-'+ decimo_digito + decimop_digito
                cpf = CPF()

                if cpf.validate(cpff) == False:
                    continue
                else:
                    break
            idade = random.randint(18, 70)



            client = Client(name=nomecompleto, cpf=cpff, age=idade)
            client.save()






            
            
    