from django import forms
from django.core.exceptions import ValidationError

from .models import NewsLink, Tag

class NewsLinkForm(forms.ModelForm):
    class Meta:
        model = NewsLink
        fields = '__all__'

class SlugCleanMixin:
    def clean_slug(self):
        new_slug = (self.cleaned_data['slug'].lower())
        if new_slug == 'create':
            raise ValidationError('Slug may not be "created".')
        return new_slug
    
class StartupForm(SlugCleanMixin, forms.ModelForm):
    class Meta:
        model = Startup
        fields = '__all__'
        
class TagForm(SlugCleanMixin, forms.ModelForm):
    def clean_name(self):
        return self.cleaned_data['name'].lower()
    
    class Meta:
        model = Tag
        exclude = tuple()