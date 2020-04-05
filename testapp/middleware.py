
class ExecutionFlowMiddleware(object):
    def __init__(self, get_response):
        self.get_response=get_response

    def __call__(self, request):
        #Pre-processing
        print('This line printed at pre processing of request')
        response=self.get_response(request)
        #Post-processing
        print('This line printed at post processing of request')
        return response

from django.http import HttpResponse

class AppMaintananceMiddleware(object):
    def __init__(self, get_response):
        self.get_response=get_response

    def __call__(self, request):
        return HttpResponse('<h1>System under maintanace please try after some time........</h1>')
