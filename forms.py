from wtforms import Form
from wtforms import StringField,SelectField,RadioField,EmailField,IntegerField,DateField,BooleanField
from wtforms import validators
from wtforms.validators import DataRequired


class UsersForm(Form):
    nombre=StringField('nombre',[
        validators.DataRequired(message='el campo es requerido'),
        validators.length(min=4, max=10, message='ingrese nombre valido')
    ])
    apaterno=StringField('apaterno',[
        validators.DataRequired(message='el campo es requerido'),
        validators.length(min=4, max=10, message='ingrese apellido valido')
    ])
    amaterno=StringField('amaterno',[
        validators.DataRequired(message='el campo es requerido'),
        validators.length(min=4, max=10, message='ingrese apellido valido')
    ])

    edad=IntegerField('edad',[        
        validators.number_range(min=1, max=20,message='ingrese edad valida')
    ])
    correo=StringField('correo',[
        validators.DataRequired(message='el campo es requerido'),
    ])


class EmpleadosForm(Form):
    id=IntegerField('id')
    nombre=StringField('nombre',[
        validators.DataRequired(message='el campo es requerido'),
        validators.length(min=4, max=10, message='ingrese nombre valido')
    ])
    correo=StringField('correo',[
        validators.DataRequired(message='ingresar un correo valido'),
    ])
    telefono=StringField('telefono')
    direccion=StringField('direccion')
    sueldo=StringField('sueldo')
    

class PizzeriaForm(Form):
    id = IntegerField('id')
    nombre= StringField('Nombre',[
        validators.DataRequired(message='el campo es requerido')
    ])
    direccion= StringField('Direccion',[
        validators.DataRequired(message='el campo es requerido')
    ])
    telefono= StringField('Telefono',[
        validators.DataRequired(message='el campo es requerido')
    ])
    fecha = DateField('Fecha', validators=[DataRequired()], format='%Y-%m-%d')

    numPizzas = IntegerField('Cantidad Pizzas', [
        validators.DataRequired(message='El campo es requerido'),
        validators.NumberRange(min=1, message='El número de pizzas no puede ser negativo')
    ])    
    tamaPizza = RadioField('Tamaño', 
       choices=[
            ('40','Chica $40.00'),
            ('80','Mediana $80.00'),
            ('120','Grande $120.00')
            ])

    ingteJamon = BooleanField('Jamon $10', default=False)
    ingtePiña = BooleanField('Piña $10', default=False)
    ingteChampiñones = BooleanField('Champiñones $10',default=False)
    
    
    numVenta = StringField('numVenta')
    estatus= StringField('Estatus')
    subtotal= StringField('Subtotal')
    total= StringField('Total')


class ConsultaPedidosForm(Form):
    fecha_seleccionada = DateField(format='%Y-%m-%d')

    dias_semana = SelectField('Día de la semana', choices=[('', 'Seleccione un día'), (0, 'Lunes'), (1, 'Martes'), (2, 'Miércoles'), (3, 'Jueves'), (4, 'Viernes'), (5, 'Sábado'), (6, 'Domingo')])

    meses = SelectField('Mes', choices=[('', 'Seleccione un mes'), (1, 'Enero'), (2, 'Febrero'), (3, 'Marzo'), (4, 'Abril'), (5, 'Mayo'), (6, 'Junio'), (7, 'Julio'), (8, 'Agosto'), (9, 'Septiembre'), (10, 'Octubre'), (11, 'Noviembre'), (12, 'Diciembre')])

    anios = SelectField('Año', choices=[('', 'Seleccione un año'), (2020, '2020'), (2021, '2021'), (2022, '2022'), (2023, '2023'), (2024, '2024')])