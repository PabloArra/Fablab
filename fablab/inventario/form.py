from django import forms
from .models import maquina, consumibles, solicitud, clasesmaquinas




class articleform(forms.ModelForm):
    class Meta:
        model = maquina
        fields= ['nombre','clasemaq','description','fecham','estado','condicionn']
        labels= {
            'nombre': 'Nombre del equipo',
            'clasemaq': 'Categoria',
            'description': 'Descripcion',
            'fecham': 'Fecha ultima mantencion',
            'estado': 'Estado',
            'condicionn': 'condicion',
        }
        widgets = {
            'nombre': forms.TextInput(
                attrs= {
                    'class':'form-control',
                    'placeholder':'Ingrese el nombre',
                    'id':'nombre'
                }
            ),
            'description': forms.TextInput(
                attrs= {
                    'class':'form-control',
                    'placeholder':'Ingrese los datos',
                    'id':'description'
                }
            ),
            'fecham': forms.TextInput(
                attrs= {
                    'class':'form-control',
                    'placeholder':'Fecha ult. Mantencion',
                    'id':'fecham'
                }
            ),
    
            

        }

class consumiblesform(forms.ModelForm):
    class Meta:
        model = consumibles
        fields= ['nombre','clas','cantidad']
        labels= {
            'nombre': 'Nombre del Consumible',
            'clas': 'Categoria',
            'cantidad': 'Cantidad',
        }
        widgets = {
            'nombre': forms.TextInput(
                attrs= {
                    'class':'form-control',
                    'placeholder':'Ingrese el nombre',
                    'id':'nombre'
                }
            ),

            'cantidad': forms.TextInput(
                attrs= {
                    'class':'form-control',
                    'placeholder':'Ingrese la Cantidad',
                    'id':'cantidad'
                }
            ),

        }


class solicitudform(forms.ModelForm):
    class Meta:
        model = solicitud
        fields= ['titulo','motivo','descripcion']
        labels= {
            'titulo': 'Nombre de la solicitud',
            'motivo': 'Motivo',
            'descripcion': 'Descripcion',
        }
        widgets = {
            'titulo': forms.TextInput(
                attrs= {
                    'class':'form-control',
                    'placeholder':'Nombre de la solicitud',
                    'id':'titulo'
                }
            ),

            'motivo': forms.TextInput(
                attrs= {
                    'class':'form-control',
                    'placeholder':'Motivo',
                    'id':'motivo'
                }
            ),
            'descripcion': forms.TextInput(
                attrs= {
                    'class':'form-control',
                    'placeholder':'Descripcion',
                    'id':'descripcion'
                }
            ),

        }


class categoriaform(forms.ModelForm):
    class Meta:
        model = clasesmaquinas
        fields= ['nombreclase']
        labels= {
            'nombreclase': 'Nombre de la Categoria'
        }
        widgets = {
            'nombreclase': forms.TextInput(
                attrs= {
                    'class':'form-control',
                    'placeholder':'Ingrese el nombre',
                    'id':'nombreclase'
                }
            ),

        }