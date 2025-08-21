from django import forms
from task.models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task

        # Rendering the fields
        fields = '__all__'      # or, ['title', 'deadline', 'about', 'status']

        # Not rendering the fileds
        # exclude = ['status']    # If status was not needed

        # Label Customization
        labels = {
            'title':'What is to be done?',
        }

        # Customized rendering of field in HTML
        widgets = {
            'title':forms.TextInput(attrs={
                'placeholder':'Enter task title',
            }),
            'deadline':forms.DateTimeInput(attrs={
                'type': 'datetime-local',
            }),
            'about':forms.Textarea(attrs={
                'cols':25,
                'rows':2,
                'placeholder':'About...',
            }),
            'user':forms.HiddenInput(),
        }

        # Hint for the fields
        help_texts = {
            'about':'Provide a detailed info of task'
        }

        # Message, if form input validation fails in server side (if bypassed from client side)
        error_messages = {
            'title':{
                'max_length':'Title is too long.',
            },
        }


# ----------------------------------------------------------

# Simple ModelForm without customization

# from django import forms
# from task.models import Task

# class TaskForm(forms.ModelForm):
#     class Meta:
#         model = Task
#         fields = '__all__'

