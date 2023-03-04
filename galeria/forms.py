from django.forms import ModelForm
from django import forms
from .models import Userr




class PerfilForm(ModelForm):
    class Meta:
        model = Userr
        fields = ['avatar','pasion','biografia']

   

class MyUserCreationForm(forms.Form):
   username = forms.CharField(label='Nombre',required=True)
   password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput(), strip=False)
   password2 = forms.CharField(label='Confirmar Contraseña',widget=forms.PasswordInput(), strip=False)

   username.widget.attrs.update({'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white'})
   password1.widget.attrs.update({'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white'})
   password2.widget.attrs.update({'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white'})