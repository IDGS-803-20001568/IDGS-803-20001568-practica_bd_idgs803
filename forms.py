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


from wtforms import DateField

class PizzeriaForm(Form):
    id = IntegerField('id')
    nombre = StringField('nombre', [
        validators.DataRequired(message='el campo es requerido')
    ])
    direccion = StringField('direccion', [
        validators.DataRequired(message='el campo es requerido')
    ])
    telefono = StringField('telefono', [
        validators.DataRequired(message='el campo es requerido')
    ])
    numPizzas = IntegerField('Número Pizzas', [
        validators.DataRequired(message='el campo es requerido')
    ])

    tamaPizza = RadioField('Tamaño Pizza', 
       choices=[
            ('40','Chica $40'),
            ('80','Mediana $80'),
            ('120','Grande $120')
            ])
    ingredientesPizza = RadioField('Ingredientes Pizza', 
       choices=[
            ('10','Jamon $10'),
            ('10','Piña $10'),
            ('10','Champiñones $120')
            ])

    fecha_compra = DateField('Fecha de Compra', format='%Y-%m-%d')

