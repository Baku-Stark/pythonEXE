from django.db import models

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

    # [CRIAR]
    created_at = models.DateTimeField(auto_now_add=True)
    # [ATUALIZAR]
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        # Retornar título da tarefa
        return self.title