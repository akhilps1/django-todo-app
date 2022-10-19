from django import forms
from .models import Todos

class TodoForm(forms.ModelForm):
    class Meta:
        model =Todos
        fields = ['task', 'priority', 'date', 'completed']
        widgets = {
            'task': forms.Textarea(attrs={'class': 'form-control border-dark border-opacity-50 my-1 text-dark'}),
            'priority': forms.NumberInput(attrs={'class': 'form-control border-dark border-opacity-50 my-1 text-dark'}),
            'date': forms.DateInput(attrs={'class': 'form-control border-dark border-opacity-50 my-1 text-dark'}),
            
        }

