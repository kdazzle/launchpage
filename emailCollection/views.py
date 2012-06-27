from django.views.generic import RedirectView
from django.template import Context, loader, RequestContext, Template
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_protect
from django.conf import settings
from django.core.urlresolvers import reverse

from emailCollection.models import EmailRequest
from emailCollection.models import EmailRequestForm
from commonFiles.launchpageController import LaunchpageController

@csrf_protect
def displayHomepage(request):
    view = EmailRequestController()
    return view.enterHomeView(request)

def displayThankYou(request):
    view = EmailRequestController()
    return view.displayThankYou(request)

class EmailRequestController(LaunchpageController):
    errorMessage = None

    def enterHomeView(self, request):
        if request.method=='POST':
            form = EmailRequestForm(request.POST)

            try:
                if form.is_valid():
                    emailRequest = form.save()
                    return redirect('thankYou')
            except:
                self.errorMessage = """We're very sorry, but there has been an error
                    processing the form. Please try again."""

        else:
            form = EmailRequestForm()

        t = 'emailCollection/home.html'
        c = RequestContext(request, {
                     'form': form,
                     'action': "",
                     'errorMessage': self.errorMessage,
                     })
        return self.loadPage(request, c, t)

    def displayThankYou(self, request):
        t = 'emailCollection/thankYou.html'
        c = RequestContext(request, {})
        return self.loadPage(request, c, t)