from django.db import models


class Curso(models.Model):
    DEFAULT_PK=1
    nome = models.CharField(max_length=100)
    carga_horaria = models.IntegerField()
    ementa = models.TextField()
    valor = models.DecimalField(max_digits=8, decimal_places=2,default=0)

    class Meta:
        verbose_name_plural = 'Cursos'
        verbose_name = 'Curso'

    def __str__(self):
        return self.nome


class Professor(models.Model):
    DEFAULT_PK = 1
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=10)
    valor_hora_aula = models.DecimalField(max_digits=8, decimal_places=2,default=0)

    class Meta:
        verbose_name_plural = 'Professores'
        verbose_name = 'Professor'

    def __str__(self):
        return self.nome


class Turma(models.Model):
    curso = models.ForeignKey(Curso,default=Curso.DEFAULT_PK, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor,default=Professor.DEFAULT_PK,on_delete=models.CASCADE)
    data_inicio = models.DateField()
    data_termino = models.DateField()
    hora_inicio = models.TimeField()
    hora_termino = models.TimeField()

    class Meta:
        verbose_name_plural = 'Turmas'
        verbose_name = 'Turma'

    def __str__(self):
        return str(self.data_inicio) + ', professor ' + str(self.professor)


