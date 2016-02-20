# -*- coding: utf8 -*-

from django.db import models

# SIGNALS
from django.db.models import signals
from utils.signals_comuns import slug_pre_save
from datetime import datetime
from django.db import models
from django.core.urlresolvers import reverse

class Imagem(models.Model):
    """Cada instancia desta classe contem uma imagem da galeria, com seu
    respectivo thumbnail (miniatura) e imagem em tamanho natural.
    Varias imagens podem conter dentro de um Album"""

    class Meta:
        ordering = ('ponto','titulo',)

    ponto = models.ForeignKey('MapData')
    titulo = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True, unique=True)
    descricao = models.TextField(blank=True)
    original = models.ImageField(
        null=True,
        blank=True,
        upload_to='galeria/original',
        )
    thumbnail = models.ImageField(
        null=True,
        blank=True,
        upload_to='galeria/thumbnail',
        )
    publicacao = models.DateTimeField(default=datetime.now(), blank=True)

    def __unicode__(self):
        return self.titulo


class MapData(models.Model):
	class Meta:
		verbose_name = 'Marcação'
		verbose_name_plural = 'Marcações'
	titulo = models.CharField(('Nome'),
			max_length=255,
			help_text=('Entries in future dates are only published on '
                    'correct date.'))
	description = models.TextField(('Descrição'))
	date = models.DateTimeField(('Data de criação'),auto_now_add=True)
	slug = models.SlugField(max_length=100, blank=True, unique=True)

	TYPES_CHOICES = (
		    (u'1',u'Em verificação'),
		    (u'2','Aprovado'),
	)
	moderator = models.CharField(('Status'),max_length=1,choices=TYPES_CHOICES)
	inlines = [
        Imagem,
    ]

	def __unicode__(self):
		return self.titulo
		# + " " + self.moderator

signals.pre_save.connect(slug_pre_save, sender=MapData)
signals.pre_save.connect(slug_pre_save, sender=Imagem)

class Image(models.Model):
    title = models.CharField(max_length=60, blank=True, null=True)
    image = models.FileField(upload_to="images/")
    
    def __unicode__(self):
        return self.image.name
