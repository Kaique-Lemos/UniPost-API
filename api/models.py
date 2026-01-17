from django.db import models
from django.db.models import Max

class Aluno(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    nome = models.CharField(max_length=100)
    curso = models.CharField(max_length=100)
    matricula = models.CharField(max_length=20)

    def save(self, *args, **kwargs):
        if not self.id:
            max_id = Aluno.objects.aggregate(Max('id'))['id__max'] or 0
            self.id = max_id + 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome
