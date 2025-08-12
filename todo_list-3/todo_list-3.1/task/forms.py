# task/forms.py
from django import forms

class TaskForm(forms.Form):
    title = forms.CharField(
        max_length=100,
        label="What is to be done?"
    )

    # Use HTML5 datetime-local input instead of text input
    deadline = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={
            'type': 'datetime-local',
            }),
    )
    
    # Use textarea tag instead if text input; custom area size; default value to be displayed
    about = forms.CharField(
        widget=forms.Textarea(attrs={
            'cols':25,
            'rows':2,
            }),
        initial='Short description...',
    )

    # Allow for unchecked submission
    status = forms.BooleanField(required=False)


# ----------------------------------------------------------

# Simple Form without customization

# from django import forms

# class TaskForm(forms.Form):
#     title = forms.CharField(max_length=100)
#     deadline = forms.DateTimeField()
#     about = forms.CharField()
#     status = forms.BooleanField()

