from django.db import models



class clasesmaquinas(models.Model):
    nombreclase=models.CharField(max_length=80,verbose_name="Nombre")

    class Meta:
        verbose_name="Clases de maquina"
        verbose_name_plural="Clases de maquinas"

    def __str__(self):
        return self.nombreclase
    
class estados(models.Model):
    estado=models.CharField(max_length=80,verbose_name="Nombre")

    class Meta:
        verbose_name="estado"
        verbose_name_plural="estados"

    def __str__(self):
        return self.estado
    
class condiciones(models.Model):
    condicion=models.CharField(max_length=80,verbose_name="Nombre")

    class Meta:
        verbose_name="condicion"
        verbose_name_plural="condiciones"

    def __str__(self):
        return self.condicion
    
    

class maquina(models.Model):

    nombre=models.CharField(max_length=80,verbose_name="Nombre")
    clasemaq=models.ForeignKey(clasesmaquinas,null=True,on_delete=models.SET_NULL)
    description=models.TextField(verbose_name="Descripcion")
    fecham=models.DateField(verbose_name="Ultima mantencion")
    estado=models.ForeignKey(estados, null=True,on_delete=models.SET_NULL)
    condicionn=models.ForeignKey(condiciones, null=True,on_delete=models.SET_NULL)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name="Inventario maquina"
        verbose_name_plural="Inventario maquinas"

    def __str__(self):
        return self.nombre

class consumibles(models.Model):
    nombre=models.CharField(max_length=80,verbose_name="Nombre")
    clas=models.ForeignKey(clasesmaquinas,null=True,on_delete=models.SET_NULL)
    cantidad=models.PositiveBigIntegerField(verbose_name="Cantidad")

    class Meta:
        verbose_name="Inventario consumible"
        verbose_name_plural="Inventario consumibles"

    def __str__(self):
        return self.nombre

class solicitud(models.Model):
    titulo=models.CharField(max_length=80,verbose_name="Nombre")
    motivo=models.CharField(max_length=80,verbose_name="Motivo")
    descripcion=models.TextField(verbose_name="descripcion")

    class Meta:
        verbose_name="Solicitud"
        verbose_name_plural="Solicitudes"

    def __str__(self):
        return self.titulo
