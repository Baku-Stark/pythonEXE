from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Task(models.Model):

    STATUS = (
        ('doing', 'Doing'),
        ('done', 'Done')
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    done = models.CharField(
        max_length=5, choices=STATUS
    )

    # [ID DO USUÁRIO]
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    # [CRIAR]
    created_at = models.DateTimeField(auto_now_add=True)
    # [ATUALIZAR]
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        # Retornar título da tarefa
        return self.title