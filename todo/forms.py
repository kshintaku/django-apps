from django import forms


class TaskForm(forms.Form):
    task_title = forms.CharField(
        label="task_title",
        max_length=200,
        widget=forms.TextInput(attrs={"placeholder": "Add new item"}),
    )
