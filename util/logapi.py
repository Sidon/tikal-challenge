from core.models import Processo, Logdb
from datetime import date

class Log_api:

    def _build_post(self, _data):
        data = '{ "numero_processo": '+_data['numero_processo']
        data += ', "dados_anterior": '+_data['dados_anterior']
        data += ', "dados_atual": '+_data['dados_atual']
        data += ', "data_edit": '+str(date.today())
        data += ', "user_id": '+str(_data['user_id'])
        data += '}'

        #  Utilizando curls
        curl = 'curl -d '+data+'-H "Content-Type: application/json" -u user:password -X POST https://url/da/api/'
        #  Utiliando requests (http for Humans :-)
        req = 'requests.post("https://url/api", data='+data
        #  strpost = 'Utilizando request [http for human :-)]:\n'+r
        #  strpost += '\nUtilizando curl:'+curl
        return {'curl': curl, 'request': req}

    def update_api(self, data ):
        post = self._build_post(data)
        Logdb.objects.create(post_req=post['request'], post_curl=post['curl'])

