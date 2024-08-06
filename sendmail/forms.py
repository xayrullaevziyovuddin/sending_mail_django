from django import forms


class EmailFORM(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput
    )
    email = forms.EmailField(
        widget=forms.EmailInput
    )

    comments = forms.CharField(
        widget=forms.Textarea
    )
