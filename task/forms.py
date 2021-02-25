from django.forms import ModelForm
from task import models
class TaskForm(ModelForm):
    class Meta:
        # connect with the model
        model = models.Task
        fields='__all__'
