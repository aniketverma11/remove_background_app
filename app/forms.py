from django import forms
from .models import Image, Result

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image',)
        
class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ('image',)

    def get_image(self, obj):
        return obj.image