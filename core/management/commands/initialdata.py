from django.core.management.base import BaseCommand
from  core.models import Processo


procs = []

procs.append('''
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. 
Sed nisi. Nulla quis sem at nibh elementum imperdiet. Duis sagittis ipsum. Praesent mauris. Fusce nec tellus sed augue 
semper porta. Mauris massa. Vestibulum lacinia arcu eget nulla. Class aptent taciti sociosqu ad litora torquent per 
conubia nostra, per inceptos himenaeos. Curabitur sodales ligula in libero.''')

procs.append(''' Sed dignissim lacinia nunc. Curabitur tortor. Pellentesque nibh. Aenean quam. In scelerisque sem at 
dolor. Maecenas mattis. Sed convallis tristique sem. Proin ut ligula vel nunc egestas porttitor. Morbi lectus risus, 
iaculis vel, suscipit quis, luctus non, massa. Fusce ac turpis quis ligula lacinia aliquet. Mauris ipsum. Nulla metus 
metus, ullamcorper vel, tincidunt sed, euismod in, nibh. Quisque volutpat condimentum velit. ''')


procs.append('''Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Nam nec ante. 
Sed lacinia, urna non tincidunt mattis, tortor neque adipiscing diam, a cursus ipsum ante quis turpis. Nulla facilisi. 
Ut fringilla. Suspendisse potenti. Nunc feugiat mi a tellus consequat imperdiet. Vestibulum sapien. Proin quam. Etiam 
ultrices. Suspendisse in justo eu magna luctus suscipit. Sed lectus.''')

procs.append('''Integer euismod lacus luctus magna. Quisque cursus, metus vitae pharetra auctor, sem massa mattis sem, 
at interdum magna augue eget diam. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia 
Curae; Morbi lacinia molestie dui. Praesent blandit dolor. Sed non quam. In vel mi sit amet augue congue elementum. 
Morbi in ipsum sit amet pede facilisis laoreet. Donec lacus nunc, viverra nec, blandit vel, egestas et, augue. 
Vestibulum tincidunt malesuada tellus. Ut ultrices ultrices enim. Curabitur sit amet mauris. Morbi in dui quis est 
pulvinar ullamcorper. Nulla facilisi.''')


procs.append('''Integer lacinia sollicitudin massa. Cras metus. Sed aliquet risus a tortor. Integer id quam. Morbi mi. 
Quisque nisl felis, venenatis tristique, dignissim in, ultrices sit amet, augue. Proin sodales libero eget ante. Nulla 
quam. Aenean laoreet. Vestibulum nisi lectus, commodo ac, facilisis ac, ultricies eu, pede. Ut orci risus, accumsan 
porttitor, cursus quis, aliquet eget, justo.''')

# Gerando 20 numeros consecutivos de 20 digitos
data = []
for n in range(5):
    zeros = '0' * 20
    last = str(n+1)
    num_proc = zeros[:len(last)*-1]+last
    # dado_proc = 'Esse é o texto padrão de testes para o processo cujo número termina com ' + last
    data.append({'num': num_proc, 'dados': procs[n]})


class Command(BaseCommand):
    help = 'Create initial data'

    def handle(self, *args, **options):

        Processo.objects.all().delete()

        for processo in data:
            Processo.objects.create(numero_processo=processo['num'], dados_processo=processo['dados'])
