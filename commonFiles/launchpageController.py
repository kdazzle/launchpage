from django.template import Context, loader, RequestContext, Template
from django.views.generic import RedirectView
from django.http import HttpResponse
from django.conf import settings

class LaunchpageController():

    def __init__(self):
        import logging
        self.logger = logging.getLogger(__name__)
        logging.basicConfig()

    def loadPage(self, request, context, template):
        t = loader.get_template(template)
        c = RequestContext(request, {
            })

        if context:
            c.update(context)
        return HttpResponse(t.render(c))
