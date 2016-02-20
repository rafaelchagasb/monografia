try:
    import Image
except ImportError:
    from PIL import Image

from django.contrib import admin
from django import forms
from map.models import MapData,Imagem

class ImagemInline(admin.StackedInline):
    model = Imagem

class AdminMap(admin.ModelAdmin):
	list_display = ("titulo", "date","moderator")
   	#list_filter = ("is_defunct",)
	ordering = ("date",)
	search_fields = ("titulo", "description")
	list_per_page = 2
	inlines = [
			ImagemInline,
		]

class FormImagem(forms.ModelForm):
    class Meta:
        model = Imagem

class AdminImagem(admin.ModelAdmin):
    list_display = ('ponto','titulo',)
    list_filter = ('ponto',)
    search_fields = ('titulo','descricao',)
    form = FormImagem

    def save_model(self, request, obj, form, change):
        """Metodo declarado para criar miniatura da imagem depois de salvar"""
        super(AdminImagem, self).save_model(request, obj, form, change)

        if 'original' in form.changed_data:
            extensao = obj.original.name.split('.')[-1]
            obj.thumbnail = 'galeria/thumbnail/%s.%s'%(
               obj.id, extensao)

            miniatura = Image.open(obj.original.path)
            miniatura.thumbnail((100,100), Image.ANTIALIAS)
            miniatura.save(obj.thumbnail.path,extensao)

            obj.save()
		
admin.site.register(MapData,AdminMap)
admin.site.register(Imagem, AdminImagem)
