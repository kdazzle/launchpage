from django.views.generic import RedirectView
from django.template import Context, loader, RequestContext, Template
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.conf import settings
from django.core.urlresolvers import reverse

from emailCollection.models import EmailRequest
from emailCollection.models import EmailRequestForm
from commonFiles.launchPageController import LaunchPageController

@csrf_protect
def displayHomepage(request):
    view = EmailRequestController()
    return view.enterHomeView(request)

class EmailRequestController(LaunchpageController):
    def enterHomeView(self, request):
        if request.method=='POST':
            form = EmailRequestForm(request.POST)
            if form.is_valid():
                # record that the user has gained access to this record
                # allow the user to proceed
                return RedirectView('')
        else:
            form = EmailRequestForm()

        t = 'emailCollection/home.html'
        c = RequestContext(request, {
                     'form': form,
                     'action': ""
                     })
        return self.loadPage(request, c, t)
