from django import forms
from .models import Display_Photo

class PhotosEditForm(forms.ModelForm):
	class Meta:
		model = Display_Photo
		fields = ("photo1","photo1_Description","photo2","photo2_Description",
			"photo3","photo3_Description","photo4","photo4_Description",
			"photo5","photo5_Description")
		
		widgets = {
			"photo1_Description":forms.TextInput(attrs={"class":'form-control'}),
			"photo1":forms.FileInput(),
			"photo2_Description":forms.TextInput(attrs={"class":'form-control'}),
			"photo2":forms.FileInput(),
			"photo3_Description":forms.TextInput(attrs={"class":'form-control'}),
			"photo3":forms.FileInput(),
			"photo4_Description":forms.TextInput(attrs={"class":'form-control'}),
			"photo4":forms.FileInput(),
			"photo5_Description":forms.TextInput(attrs={"class":'form-control'}),
			"photo5":forms.FileInput(),
			}
