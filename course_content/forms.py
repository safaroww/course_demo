from django import forms
from .models import Tag, Course, Lesson
from dataclasses import field
from distutils.command.clean import clean
from django.core.exceptions import ValidationError


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        
        title = cleaned_data.get('title')
        if title:
            if Tag.objects.filter(title__iexact=title).exists():
                raise ValidationError('Belə bir tag mövcuddur')



class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        widgets = {
            'rank': forms.NumberInput(attrs={'max': 5, 'min': 1, 'value': 1}),
            'description': forms.Textarea(attrs={'placeholder': 'Açıqlama Girin '})
        }



class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        exclude = ['view_count'] 
        