from django.core.management.base import BaseCommand
from  core.models import Processo
from django.contrib.auth.models import User
from django.db.models import Q


procs = []
procs.append('Amet porttitor eget dolor morbi. Magna fringilla urna porttitor rhoncus. In vitae turpis massa sed elementum.')
procs.append('Et malesuada fames ac turpis egestas. Cursus risus at ultrices mi tempus imperdiet.')
procs.append('Tincidunt arcu non sodales neque sodales ut etiam sit amet. Viverra nibh cras pulvinar mattis.')
procs.append('Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.')
procs.append('Sed lacinia, urna non tincidunt mattis, tortor neque adipiscing diam, a cursus ipsum ante quis turpis.')
procs.append('Suspendisse potenti. Nunc feugiat mi a tellus consequat imperdiet. Vestibulum sapien. Proin quam.')
procs.append('Integer euismod lacus luctus magna. Quisque cursus, metus vitae pharetra auctor, sem massa mattis.')
procs.append('Et netus et malesuada fames ac turpis egestas. In vitae turpis massa sed elementum tempus.')
procs.append('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
procs.append('Morbi tristique senectus et netus et malesuada. Feugiat in fermentum posuere urna nec tincidunt praesent semper. Cursus euismod quis.')
procs.append('Magna sit amet purus gravida quis blandit turpis cursus in. At imperdiet dui accumsan sit amet nulla facilisi. Sit amet est placerat.')

# Gerando 20 numeros consecutivos de 20 digitos
data = []
for n in range(len(procs)):
    zeros = '0' * 20
    last = str(n+1)
    num_proc = zeros[:len(last)*-1]+last
    # dado_proc = 'Esse é o texto padrão de testes para o processo cujo número termina com ' + last
    data.append({'num': num_proc, 'dados': procs[n]})


class Command(BaseCommand):
    help = 'Create initial data'

    def handle(self, *args, **options):
        if User.objects.filter(Q(username='admin') & Q(is_superuser=1)):
            Processo.objects.all().delete()
            for processo in data:
                Processo.objects.create(user_id='1', numero_processo=processo['num'], dados_processo=processo['dados'])
        else:
            print ('Inclua um usuário superuser com o nome admin')
            return
