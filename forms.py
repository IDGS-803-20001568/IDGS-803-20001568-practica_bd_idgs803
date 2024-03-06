from wtforms import Form
from wtforms import StringField,SelectField,RadioField,EmailField,IntegerField
from wtforms import validators


class EmpleadosForm(Form):
    id = IntegerField('id')
    nombre= StringField('nombre',[
        validators.DataRequired(message='el campo es requerido'),
        validators.length(min=4,max=10,message='ingresa nombre valido')
    ])
    correo= EmailField('correo',[
        validators.Email(message='Ingresa un correo valido'),
    ])
    telefono= StringField('telefono',[
        validators.DataRequired(message='el campo es requerido'),
        validators.length(min=4,max=10,message='Ingresa un telefono valido')
    ])
    direccion= StringField('direccion',[
        validators.DataRequired(message='el campo es requerido'),
        validators.length(min=4,max=10,message='Ingresa una direccion valida')
    ])
    sueldo= StringField('sueldo',[
        validators.DataRequired(message='el campo es requerido'),
        validators.length(min=4,max=10,message='Ingresa una sueldo valida')
    ])





class PizzeriaForm(Form):
    nombre_completo = StringField('Nombre Completo', [
        validators.DataRequired(message='El campo es requerido'),
        validators.Length(min=4, max=50, message='Ingresa un nombre válido')
    ])
    direccion = StringField('Dirección', [
        validators.DataRequired(message='El campo es requerido'),
        validators.Length(min=4, max=100, message='Ingresa una dirección válida')
    ])
    telefono = StringField('Teléfono', [
        validators.DataRequired(message='El campo es requerido'),
        validators.Length(min=7, max=15, message='Ingresa un teléfono válido')
    ])
    fecha_compra = StringField('Fecha de compra (dd-mm-yyyy)', [
        validators.DataRequired(message='El campo es requerido'),
        validators.Regexp(r'^\d{2}-\d{2}-\d{4}$', message='Ingresa una fecha válida en formato dd-mm-yyyy')
    ])
    
    num_pizzas = IntegerField('Número de Pizzas', [
        validators.DataRequired(message='El campo es requerido'),
        validators.NumberRange(min=1, message='Ingresa al menos una pizza')
    ])
    
    tamaPizza = RadioField('Tamaño de la Pizza', 
       choices=[
            ('Chica', 'Chica - $40'),
            ('Mediana', 'Mediana - $80'),
            ('Grande', 'Grande - $120')
            ], 
        validators=[validators.InputRequired(message='Selecciona un tamaño de pizza')])
    
    ingredientesPizza = RadioField('Ingredientes de la Pizza', 
       choices=[
            ('Jamon', 'Jamón - $10'),
            ('Piña', 'Piña - $10'),
            ('Champiñones', 'Champiñones - $20')
            ], 
        validators=[validators.InputRequired(message='Selecciona al menos un ingrediente')])



