# -*- coding: utf8 -*-

from django import forms

class FormItemData(forms.Form):
	name = forms.CharField(max_length=255)
	date = forms.DateField(
		widget = forms.DateInput(format='%d/%m/%Y'),
		input_formarts=['%d/%m/%y','%d/%m/%Y'])
	hora = forms.TimeField()
	description = forms.CharField()
	)
