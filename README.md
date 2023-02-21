# Configuración del proyecto
1. Crear un nuevo ambiente virtual `python3 -m venv venv`
1. Correr `pip install -r requirements.txt`
1. Ir a la carpeta `tercera_pre_entrega` donde se encuentra el archivo `manage.py`
1. Correr los siguientes comandos:
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

# Plataforma
## Header
El header cuenta con un menú para acceder a las distintas clases creadas:
* Usuarios
* Productos
* Depósitos

## Navegación
El proyecto empezará vacío, en cada sección de Listado se mostrará un mensaje.
Una vez que se cree tanto un Usuario, como un Producto o un Depósito, podrán ser listados y buscados

## Validación de Creación
La validación se da utilizando Django Forms y permite garantizar que los campos contengan los datos necesarios.

## Búsquedas
Las búsquedas se realizan utilizando un filtro múltiple, lo que permite que se pueda buscar a todos (dejando completamente vacío el formulario), como filtrar por varias cualidades.
A su vez, los filtros de texto, se basan en que contengan la cadena de caracteres, lo que posibilita la búsqueda con palabras parciales. Tampoco se necesita respetar las mayúsculas y minúsculas.

## Detalle
Para acceder al detalle se pueden listar todos los Usuarios, Productos o Depósitos, y cada uno tendrá un link para ir a un detalle.
