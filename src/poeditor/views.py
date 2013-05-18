from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib import messages
from django.http import Http404

from poeditor.models import *
from poeditor import forms, utils

from translationtools.settings import MEDIA_ROOT

def index(request):
    """
        Home Page. Upload PO files.
    """
    if request.method == 'POST' :
        form = forms.PoForm(request.POST, request.FILES)
        if form.is_valid() :
            p = form.save()
            reader = utils.convert_po(p.po.path, p.pk, MEDIA_ROOT)
            if not reader:
                raise Http404
            flag = 1
            for row in reader:
                if flag == 1:
                    flag = 2
                    continue
                po_message = PoMessages()
                po_message.po_file = p
                po_message.location = row[0]
                po_message.source = row[1]
                po_message.target = row[2]
                po_message.save()
            messages.success(request, "PoFile added successfully")
        else:
            messages.error(request, form.errors, extra_tags='form_error')
    form = forms.PoForm()
    return render_to_response('poeditor/index.html', {
                'form' : form,
    }, context_instance=RequestContext(request))

