from django.db import models
# from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager










# class CustomAccountManager(BaseUserManager):

#     def create_superuser(self, Nombre_usuario, Nombre, Apellido_pat, Numero_celular, Email, password, **other_fields):

#         other_fields.setdefault('is_staff', True)
#         other_fields.setdefault('is_superuser', True)
#         other_fields.setdefault('is_active', True)

#         if other_fields.get('is_staff') is not True:
#             raise ValueError('Superuser debe ser seleccionado si is_staff=True')
#         if other_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser debe ser seleccionado si is_superuser=True')
        
#         return self.create_user(self, Nombre_usuario, Nombre, Apellido_pat, Numero_celular, Email, password, **other_fields)

#     def create_user(self, Nombre_usuario, Nombre, Apellido_pat, Numero_celular, Email, password, **other_fields):

#         Email = self.normalize_email(Email)
#         user = self.model(Nombre_usuario=Nombre_usuario, Nombre=Nombre, Apellido_pat=Apellido_pat, Numero_celular=Numero_celular, Email=Email, **other_fields)
#         user.set_password(password)
#         user.save()
#         return user




# class NewUser(AbstractUser, PermissionsMixin):

#     Nombre_usuario = models.CharField(max_length=50, unique=True)
#     Nombre = models.CharField(max_length=30, blank=True)
#     Apellido_pat = models.CharField(max_length=30, blank=True)
#     Numero_celular = models.IntegerField(max_length=15, blank=True)
#     Email = models.EmailField(unique=True)
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=False)

#     objects = CustomAccountManager()

#     USERNAME_FIELD = 'Nombre_usuario'
#     REQUIRED_FIELDS = ['Email','Apellido_pat']

#     def __str__(self):
#         return self.Nombre_usuario