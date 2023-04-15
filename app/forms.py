from django import forms

class AgregarTarea(forms.Form):
    # Definir los datos de la clase (inputs del formulario)
    # Si no se especifica lo contrario, todos los inputs seran required=TRUE por defecto
    tarea = forms.CharField()
