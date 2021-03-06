from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib import messages
from django.http import HttpResponse, Http404

from poeditor.models import *
from poeditor import forms, utils

from translationtools.settings import MEDIA_ROOT

import json

import sys    # sys.setdefaultencoding is cancelled by site.py
reload(sys)    # to re-enable sys.setdefaultencoding()
sys.setdefaultencoding('utf-8')

def index(request):
    """
        Home Page. Upload PO files.
    """
    if request.method == 'POST' :
        form = forms.PoForm(request.POST, request.FILES)
        if form.is_valid() :
            p = form.save()
            reader = utils.convert_po(p.po.path, MEDIA_ROOT)
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


def list(request):
    """
        Get list of PO files
    """
    files = PoFile.objects.all()
    return render_to_response('poeditor/list.html', {
                'files' : files,
    }, context_instance=RequestContext(request))


def details(request, pofile_id):
    """
        Get details/Messages of a PO file
    """
    po_messages = PoMessages.objects.filter(po_file__pk = pofile_id)
    return render_to_response('poeditor/details.html', {
                'po_messages' : po_messages,
    }, context_instance=RequestContext(request))

def update(request):
    """
        Used by AJAX function. Updates messages in DB.
    """
    if request.method == 'POST' :
        data = json.loads(request.raw_post_data)
        po_file_id = None
        for message in data['messages']:
            po_message = get_object_or_404(PoMessages, pk = message['pk'])
            po_message.location = message['location']
            po_message.source = message['source']
            po_message.target = message['target']
            po_message.save()
            po_file_id = po_message.po_file.pk
        #Update po file too
        if update_po(po_file_id):
            return HttpResponse("Data Updated Successfully!")
    else:
        return HttpResponse("ERROR")

def update_po(pofile_id):
    """
        Update PO file when db messages get updated
    """
    messages = PoMessages.objects.filter(po_file__pk = pofile_id)
    if not messages.exists():
        print pofile_id
        raise Http404
    data = []
    tmp = ['location', 'source', 'target']
    data.append(tmp)
    for message in messages:
        tmp = []
        tmp.append(message.location)
        tmp.append(message.source)
        tmp.append(message.target)
        data.append(tmp)
    path = messages[0].po_file.po.path
    if utils.update_po_file(data, path, MEDIA_ROOT):
        return True
    else:
        return False
