from django import forms
from fileuploader.models import NeuralModel


class UploadFile(forms.Form):
    choose_file = forms.ImageField(widget=forms.FileInput(attrs={'class': 'upload_file'}))
    model = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'model_choice'}), queryset=NeuralModel.objects.all(), initial=0)


class NNModelForm(forms.Form):
    modelfile = forms.FileField(
        label='Select a file',
    )
#class UploadModel(forms.Form):
#   choose_model = 