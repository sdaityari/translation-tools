from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

def index(request):
    """
    Home Page
    """
    return render_to_response('poeditor/index.html', {
      'message' : 'Hello',
      }, context_instance=RequestContext(request))
