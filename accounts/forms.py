from django import forms
from django.db import transaction
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
# from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordResetForm

from course.models import Program
# from .models import User, Student, LEVEL
from .models import *

class SuperuserCreationForm(UserCreationForm):
    username = forms.CharField(
        max_length=30, widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control', }),
        label="Username", )

    first_name = forms.CharField(
        max_length=30, widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control', }),
        label="First Name", )

    last_name = forms.CharField(
        max_length=30, widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control', }),
        label="Last Name", )

    address = forms.CharField(
        max_length=30, widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control', }),
        label="Address", )

    phone = forms.CharField(
        max_length=30, widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control', }),
        label="Mobile No.", )

    email = forms.CharField(
        max_length=30, widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control', }),
        label="Email", )

    password1 = forms.CharField(
        max_length=30, widget=forms.TextInput(attrs={'type': 'password', 'class': 'form-control', }),
        label="Password", )

    password2 = forms.CharField(
        max_length=30, widget=forms.TextInput(attrs={'type': 'password', 'class': 'form-control', }),
        label="Password Confirmation", )

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic()
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_staff = True
        user.is_superuser=True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.phone = self.cleaned_data.get('phone')
        user.address = self.cleaned_data.get('address')
        user.email = self.cleaned_data.get('email')
        if commit:
            user.save()
        return user

class StaffAddForm(UserCreationForm):
    username = forms.CharField(
        max_length=30, widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control', }),
        label="Username", )

    first_name = forms.CharField(
        max_length=30, widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control', }),
        label="First Name", )

    last_name = forms.CharField(
        max_length=30, widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control', }),
        label="Last Name", )

    address = forms.CharField(
        max_length=30, widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control', }),
        label="Address", )

    phone = forms.CharField(
        max_length=10, widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control', }),
        label="Mobile No.", )

    email = forms.CharField(
        max_length=30, widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control', }),
        label="Email", )

    password1 = forms.CharField(
        max_length=30, widget=forms.TextInput(attrs={'type': 'password', 'class': 'form-control', }),
        label="Password", )

    password2 = forms.CharField(
        max_length=30, widget=forms.TextInput(attrs={'type': 'password', 'class': 'form-control', }),
        label="Password Confirmation", )

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic()
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_lecturer = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.phone = self.cleaned_data.get('phone')
        user.address = self.cleaned_data.get('address')
        user.email = self.cleaned_data.get('email')
        if commit:
            user.save()
        return user


class StudentAddForm(UserCreationForm):
    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'id': 'username_id'
            }
        ),
        label="Usuario",
    )
    address = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
            }
        ),
        label="Direccion*",
    )

    phone = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
            }
        ),
        label="Numero de telefono",
    )

    first_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
            }
        ),
        label="Nombres*",
    )

    last_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
            }
        ),
        label="Apellido*",
    )

    level = forms.CharField(
        widget=forms.Select(
            choices=LEVEL,
            attrs={
                'class': 'browser-default custom-select form-control',
            }
        ),
    )

    department = forms.ModelChoiceField(
        queryset=Program.objects.all(),
        widget=forms.Select(attrs={'class': 'browser-default custom-select form-control'}),
        label="Departamentos*",
    )

    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'type': 'email',
                'class': 'form-control',
            }
        ),
        label="Correo*",
    )

    password1 = forms.CharField(
        max_length=30, widget=forms.TextInput(attrs={'type': 'password', 'class': 'form-control', }),
        label="Contraseña*", )

    password2 = forms.CharField(
        max_length=30, widget=forms.TextInput(attrs={'type': 'password', 'class': 'form-control', }),
        label="Confirmar contraseña*", )

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic()
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.address = self.cleaned_data.get('address')
        user.phone = self.cleaned_data.get('phone')
        user.email = self.cleaned_data.get('email')
        user.save()
        student = Student.objects.create(
            student=user,
            level=self.cleaned_data.get('level'),
            department=self.cleaned_data.get('department')
        )
        student.save()
        return user


class ProfileUpdateForm(UserChangeForm):
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'type': 'email', 'class': 'form-control', }),
        label="Email*", )

    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control', }),
        label="Primer nombre*", )

    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control', }),
        label="Apellido*", )

    phone = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control', }),
        label="Numero de telefono*", )

    address = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control', }),
        label="Direccion / Ciudad*", )

    class Meta:
        model = User
        fields = ['email', 'phone', 'address', 'picture', 'first_name', 'last_name']


class EmailValidationOnForgotPassword(PasswordResetForm):
    def clean_email(self):
        email = self.cleaned_data['email']
        if not User.objects.filter(email__iexact=email, is_active=True).exists():
            msg = "There is no user registered with the specified E-mail address. "
            self.add_error('email', msg)
            return email


class ParentAddForm(UserCreationForm):
    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
            }
        ),
        label="Nombre de usuario*",
    )
    address = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
            }
        ),
        label="Correo*",
    )

    phone = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
            }
        ),
        label="Numero telefono*",
    )

    first_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
            }
        ),
        label="Primer nombre*",
    )

    last_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
            }
        ),
        label="Apellido*",
    )

    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'type': 'email',
                'class': 'form-control',
            }
        ),
        label="Correo*",
    )

    student = forms.ModelChoiceField(
        queryset=Student.objects.all(),
        widget=forms.Select(attrs={'class': 'browser-default custom-select form-control'}),
        label="Estudiante",
    )

    relation_ship = forms.CharField(
        widget=forms.Select(
            choices=RELATION_SHIP,
            attrs={'class': 'browser-default custom-select form-control',}
        ),
    )

    password1 = forms.CharField(
        max_length=30, widget=forms.TextInput(attrs={'type': 'password', 'class': 'form-control', }),
        label="Contraseña*", )

    password2 = forms.CharField(
        max_length=30, widget=forms.TextInput(attrs={'type': 'password', 'class': 'form-control', }),
        label="Confirmar contraseña*", )

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic()
    def save(self):
        user = super().save(commit=False)
        user.is_parent = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.address = self.cleaned_data.get('address')
        user.phone = self.cleaned_data.get('phone')
        user.email = self.cleaned_data.get('email')
        user.save()
        parent = Parent.objects.create(
            user=user,
            student=self.cleaned_data.get('student'),
            relation_ship=self.cleaned_data.get('relation_ship')
        )
        parent.save()
        return user