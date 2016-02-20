# Create your views here.
#from django.shortcuts import render_to_response
#from django.template import RequestContext
#from django.http import HttpResponse
#!/usr/bin/env python
# -*- coding: utf8 -*-
from django.http import HttpResponseRedirect
from django.core.files.uploadedfile import UploadedFile

"""from monografia.map.models import MapData

def index(request):
	if request.method == 'POST':
		form = FormItemData(request.P0ST,request.FILES)
		if form.is_valid():
			dados = form_cleaned_data
			item = MapData(data=dados['data'],
				hora = dados['hora'],
				name = dados['name'],
				description = dados['description'])
			item.save()
			return render_to_response("map/salvo.html",{})
		else:
			form = FormItemData()
	return render_to_response("map/index.html",locals(),context_instance=RequestContext(request))
	#return HttpResponse(u"Hello World")"""

from django.shortcuts import render_to_response
from django.template import RequestContext
from django import forms
from django.forms import ModelForm
from monografia.map.models import MapData
from monografia.map.models import Image

#from django import forms

"""class UploadForm(forms.Form):
    title = forms.CharField(max_length=50)
    file  = forms.FileField()"""

"""class FormMap(ModelForm):
	class Meta:
		model = MapData
		fields = ('name','description',)#, 'data', 'hora', 'descricao', 'participantes')"""

class FormPonto(ModelForm):
	class Meta:
		model = Image

def index(request):
    if request.method == 'POST':
        form = FormPonto(request.POST,request.FILES)
        if form.is_valid():
        	form.save()
	        mostrar = 'Contato enviado!'
	        form = FormPonto()
    else:
        form = FormPonto()
    return render_to_response(
        'ponto/index.html',
        locals(),
        context_instance=RequestContext(request),
        )

"""form = UploadForm(request.POST or None, request.FILES or None)
    if form.is_valid():
		form.save()
		return HttpResponseRedirect('/map/envia')
    return render_to_response('map/index.html', {'form': form}, context_instance=RequestContext(request))"""

def meu_upload(request):
	if request.method == 'POST':
		#log.info('received POST to main multiuploader view')
		if request.FILES == None:
			return HttpResponseBadRequest('Must have files attached!')

 		#getting file data for farther manipulations
        file = request.FILES[u'file']
        wrapped_file = UploadedFile(file)
        filename = wrapped_file.name
        file_size = wrapped_file.file.size
        #log.info ('Got file: "'+str(filename)+'"')

        #writing file manually into model
        #because we don't need form of any type.
        image = Image()
        image.title=filename
        image.image=file
        image.save()
		#return HttpResponseRedirect('/map/')
	return render_to_response('map/index.html', context_instance=RequestContext(request))

def home(request):
    return render_to_response('home.html', context_instance=RequestContext(request))


"""def teste(request):
    if request.method == 'POST':
        form = FormPonto(request.POST,request.FILES)
        if form.is_valid():
        	form.save()
	        mostrar = 'Contato enviado!'
	        form = FormPonto()
    else:
        form = FormPonto()
    return render_to_response(
        'ponto/index.html',
        locals(),
        context_instance=RequestContext(request),
        )"""


	
