from django import forms


class StudentFile(forms.Form):
    file = forms.FileField()  # for creating file input


class StudentForm(forms.Form):
    Firstname = forms.CharField(
        label="Enter Your Firstname:",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'enter firstname here...',
                'id' : 'fname'
            }
        )
    )
    Middlename = forms.CharField(
        label="Enter Your Middlename:",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'enter middlename here...'
            }
        )
    )
    Lastname = forms.CharField(
        label="Enter Your Lastname:",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'enter lastname here...'
            }
        )
    )
    SSC_marks = forms.IntegerField(
        label="Enter Xth Marks:",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'enter marks here...'
            }
        )
    )
    Diploma_marks = forms.IntegerField(
        label="Enter Diploma Marks:",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'enter marks here...'
            }
        )
    )
    BE_marks = forms.IntegerField(
        label="Enter BE Marks:",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'enter marks here...'
            }
        )
    )
    Email = forms.EmailField(
        label="Enter Your Email-id:",
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'enter email-id here...'
            }
        )
    )
    contact = forms.IntegerField(
        label="Enter Your Contact Number:",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'enter contact here...'
            }
        )
    )
