from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractBaseUser,BaseUserManager


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

ALUNO = 'A'
PROFESSOR = 'P'
COORDENADOR = 'C'
PERFIS = (
     (ALUNO,'Aluno'),
     (PROFESSOR,'Professor'),
     (COORDENADOR,'Coordenador')
)
class Usuario(AbstractBaseUser):
    ra= models.IntegerField('RA', unique=True)
    nome = models.CharField('Nome', max_length=100, blank=True)
    email = models.EmailField('E-Mail', unique=True)
    ativo = models.BooleanField('Ativo', default=True)
    perfil = models.CharField('Perfil', max_length=1, choices=PERFIS)

    USERNAME_FIELD = 'ra'
    REQUIRED_FIELDS = ['nome']

    objects = UsuarioManager()
    
    @property
    def is_staff(self):
        return self.perfil == 'C'

    def has_perm(self, perm, obj=None):
        return True
    def has_module_perms(self, app_label):
        return True

    def get_short_name(self):
        return self.nome
    def get_full_name(self):
        return self.nome
    def __str__(self):
        return self. nome








class Curso(models.Model):

    sigla = models.CharField(max_length=5)
    nome = models.CharField(max_length=200)
    tipo = models.CharField(max_length=50, blank=True)
    carga_horaria = models.IntegerField(default=1000)
    ativo = models.BooleanField(default=True)

    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome

class Aluno(models.Model):
    ra_aluno = models.CharField(max_length=10)
    nome_aluno = models.CharField(max_length=100)
    email_aluno = models.CharField(max_length=50)
    celular_aluno = models.CharField(max_length=15)
    sigla_curso = models.CharField(max_length=5)

class Coordenador(models.Model):
    nome_coordenador = models.CharField(max_length=50)
    email_coordenador = models.CharField(max_length=50)
    celular_coordenador = models.CharField(max_length=15)

class Cursturma(models.Model):
    sigla_curso = models.CharField(max_length=5)
    nome_disciplina = models.CharField(max_length=240)
    ano_disciplina = models.CharField(max_length=5)
    semestre_disciplina = models.CharField(max_length=5)
    id_turma = models.CharField(max_length=5)

class Disciplina(models.Model):
    nome_disciplina = models.CharField(max_length=240)
    carga_horaria_disciplina = models.CharField(max_length=100)
    teoria_disciplina = models.CharField(max_length=100)
    pratica_disciplina = models.CharField(max_length=100)
    ementa_disciplina = models.CharField(max_length=50)
    competencias_disciplina = models.CharField(max_length=50)
    habilidades_disciplina = models.CharField(max_length=50)
    conteudo_disciplina = models.CharField(max_length=50)
    bibliografia_disciplina = models.CharField(max_length=50)
    bibliografia_complementar_disciplina = models.CharField(max_length=50)

class Disciplinofertada(models.Model):
    nome_disciplina = models.CharField(max_length=240)
    ano_disciplina = models.CharField(max_length=5)
    semestre_disciplina = models.CharField(max_length=5)

class Grade(models.Model):
    sigla_curso = models.CharField(max_length=5)
    ano_grade = models.CharField(max_length=4)
    semestre_grade = models.CharField(max_length=1)

class Matricula(models.Model):
    ra_aluno = models.CharField(max_length=5)
    nome_disciplina = models.CharField(max_length=240)
    ano_disciplina = models.CharField(max_length=5)
    semestre_disciplina = models.CharField(max_length=5)
    id_turma = models.CharField(max_length=5)

class Periodo(models.Model):
    sigla_curso = models.CharField(max_length=5)
    ano_grade = models.CharField(max_length=5)
    semestre_grade = models.CharField(max_length=5)
    numero_periodo = models.CharField(max_length=5)

class Perioddisciplina(models.Model):
    sigla_curso = models.CharField(max_length=5)
    ano_grade = models.CharField(max_length=5)
    semestre_grade = models.CharField(max_length=5)
    numero_periodo = models.CharField(max_length=5)
    nome_disciplina = models.CharField(max_length=240)

class Professor(models.Model):
    ra_professor = models.CharField(max_length=10)
    apelido_professor = models.CharField(max_length=30)
    nome_professor = models.CharField(max_length=120)
    email_professor = models.CharField(max_length=80)
    celular_professor = models.CharField(max_length=11)

class Resposta(models.Model):
    nome_disciplina = models.CharField(max_length=240)
    ano_disciplina = models.CharField(max_length=5)
    semestre_disciplina = models.CharField(max_length=5)
    id_turma = models.CharField(max_length=5)
    numero_questao = models.CharField(max_length=5)
    ra_aluno = models.CharField(max_length=5)
    dataavaliacao_resposta = models.CharField(max_length=15)
    nota_resposta = models.CharField(max_length=5)
    avaliacao_resposta = models.CharField(max_length=100)
    descricao_resposta = models.CharField(max_length=100)
    datadeenvio_resposta = models.CharField(max_length=15)

class Questao(models.Model):
    nome_disciplina = models.CharField(max_length=10)
    ano_disciplina = models.CharField(max_length=5)
    semestre_disciplina = models.CharField(max_length=5)
    id_turma = models.CharField(max_length=5)
    numero_questao = models.CharField(max_length=5)
    datalimiteentrega_questao = models.CharField(max_length=15)
    descricao_questao = models.CharField(max_length=100)
    data_questao = models.CharField(max_length=15)

class Turma(models.Model):
    nome_disciplina = models.CharField(max_length=240)
    ano_disciplina = models.CharField(max_length=5)
    semestre_disciplina = models.CharField(max_length=5)
    turno_turma = models.CharField(max_length=15)
    ra_professor = models.CharField(max_length=11)

class Arquivresposta(models.Model):
    nome_disciplina = models.CharField(max_length=240)
    ano_disciplina = models.CharField(max_length=5)
    semestre_disciplina = models.CharField(max_length=5)
    id_turma = models.CharField(max_length=5)
    numero_questao = models.CharField(max_length=5)
    ra_aluno = models.CharField(max_length=5)
    aquivo_resposta = models.CharField(max_length=500)

class Arquivquestao(models.Model):
    nome_disciplina = models.CharField(max_length=240)
    ano_disciplina = models.CharField(max_length=5)
    semestre_disciplina = models.CharField(max_length=5)
    id_turma = models.CharField(max_length=5)
    numero_questao = models.CharField(max_length=5)
    arquivo_questao = models.CharField(max_length=5)


