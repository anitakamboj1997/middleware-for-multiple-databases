from django.conf import settings


class SetLanguage:
    def __init__(self, get_response):
        self.get_response = get_response
       
    def __call__(self, request):
     
        print('-=-=-=-=-=-=-=-=-')
        print('settings.DATABASENAME middleware : ',settings.DATABASENAME)

        settings.DATABASENAME = 'database_1'
        print('settings.DATABASENAME middleware : ',settings.DATABASENAME)
        response = self.get_response(request)
        return response
