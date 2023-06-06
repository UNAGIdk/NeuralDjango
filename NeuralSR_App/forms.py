from .models import ProcessingImage
from django.forms import ModelForm, FileInput


class ProcessingImageForm(ModelForm):
    class Meta:
        model = ProcessingImage
        fields = '__all__'

        # widgets = {
        #     'sourceFile': FileInput(attrs={
        #         'id': "uploadInput",
        #         'onchange': "loadFile(event)",
        #         'accept': ".jpg, .png",
        #         'type': "file",
        #         'class': "form-control form-control-lg",
        #         'style': "width: 100%",
        #         'required': 'True',
        #     })
        # }
