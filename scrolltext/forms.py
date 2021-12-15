from django import forms
from .models import MarqueeModel


class MarqueeEditForm(forms.ModelForm):
	class Meta:
		model = MarqueeModel
		fields = ("scroll_text",)
		
		widgets = {
			"scroll_text":forms.Textarea(attrs={"class":'form-control'}),
			}

