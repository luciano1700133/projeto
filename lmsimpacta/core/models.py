from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.

class UsuarioManager(BaseUserManager):
    use_in_migrations = True
    def _create_user(self, ra, password, **extra_fields):
        if not ra:
            raise ValueError('RA precisa ser preenchido')
        user = self.model(ra=ra, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_user(self, ra, password=None, **extra_fields):
        return self._create_user(ra, password, **extra_fields)
    def create_superuser(self, ra, password, **extra_fields):
        return self._create_user(ra, password, **extra_fields)



class Usuario(AbstractBaseUser):

    nome = models.CharField(max_length=50)
    ra = models.IntegerField(unique=True)
    password = models.CharField(max_length=150)
    perfil = models.CharField(max_length=1, default='C')
    ativo = models.BooleanField(default=True)

    USERNAME_FIELD = 'ra'
    REQUIRED_FIELDS = ['nome']

    objects = UsuarioManager()

class Aluno(models.Model):
    ra = models.CharField(max_length=10)#size 10
    nome = models.CharField(max_length=100)#size 35
    curso = models.CharField(max_length=100)#size 25
    data_nascimento = models.CharField(max_length=15)#size 15
    email = models.CharField(max_length=100)#size 35
    endereco = models.CharField(max_length=200)#size 35
    cidade = models.CharField(max_length=100)#size 10
    estado = models.CharField(max_length=10)#size 5
    telefone = models.CharField(max_length=15)#size 10
    celular = models.CharField(max_length=15)#size 10

    def __unicode__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('editar_aluno', kwargs={'pk': self.pk})

class Candidato(models.Model):
    nome = models.CharField(max_length=100)
    curso = models.CharField(max_length=100)
    data_nascimento = models.CharField(max_length=15)
    email = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=10)
    telefone = models.CharField(max_length=15)
    celular = models.CharField(max_length=15)


class Colaborador(models.Model):
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    data_nascimento = models.CharField(max_length=15)
    email = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=10)
    telefone = models.CharField(max_length=15)
    celular = models.CharField(max_length=15)




class Curso(models.Model):

    sigla = models.CharField(max_length=5)
    nome = models.CharField(max_length=200)
    tipo = models.CharField(max_length=50, blank=True)
    carga_horaria = models.IntegerField(default=1000)
    ativo = models.BooleanField(default=True)

    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome