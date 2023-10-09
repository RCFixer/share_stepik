from django import forms
from django_select2 import forms as s2forms
from .models import Course, SharePage, SpecializationPage


class SharePageWidget(s2forms.ModelSelect2MultipleWidget):
    search_fields = [
        "title__icontains",
    ]


class SharePageForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].widget.attrs['class'] = 'form-control'

    class Meta:
        model = SharePage
        fields = ('title', 'courses')
        widgets = {
            "courses": SharePageWidget(attrs={"class": "form-select"}),
        }
        labels = {
            'title': ('Название подборки'),
            'courses': ('Список курсов'),
        }


class SpecializationForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].widget.attrs['class'] = 'form-control'

    class Meta:
        model = SpecializationPage
        fields = ('title',)
        labels = {
            'title': ('Название специализации'),
        }
