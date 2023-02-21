from django import forms

class CreateUserForm(forms.Form):
    first_name = forms.CharField(label="Nombre", max_length=255)
    last_name = forms.CharField(label="Apellido", max_length=255)
    age = forms.IntegerField(label="Edad")

class LookupUserForm(forms.Form):
    first_name = forms.CharField(label="Nombre", max_length=255, required=False)
    last_name = forms.CharField(label="Apellido", max_length=255, required=False)
    age = forms.IntegerField(label="Edad", required=False)

class CreateWarehouseForm(forms.Form):
    alias = forms.CharField(label="Alias", max_length=255)
    location = forms.CharField(label="Ubicación", max_length=255)
    capacity_in_m3 = forms.IntegerField(label="Capacidad en M3")
    cooling_system = forms.BooleanField(label="Sistema de Refrigeración", required=False)

class LookupWarehouseForm(forms.Form):
    alias = forms.CharField(label="Alias", max_length=255, required=False)
    location = forms.CharField(label="Ubicación", max_length=255, required=False)
    capacity_in_m3 = forms.IntegerField(label="Capacidad en M3", required=False)
    cooling_system = forms.BooleanField(label="Sistema de Refrigeración", required=False)

class CreateProductForm(forms.Form):
    name = forms.CharField(label="Nombre", max_length=255)
    category = forms.CharField(label="Categoría", max_length=255)
    price = forms.DecimalField(label="Precio", max_digits=10, decimal_places=2)

class LookupProductForm(forms.Form):
    name = forms.CharField(label="Nombre", max_length=255, required=False)
    category = forms.CharField(label="Categoría", max_length=255, required=False)
    price = forms.DecimalField(label="Precio", max_digits=10, decimal_places=2, required=False)