from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(
        "Título",
        max_length=200
    )
    description = models.TextField(
        "Descrição",
        null=True,
        blank=True
    )
    complete = models.BooleanField(
        "Concluída",
        default=False
    )
    created = models.DateTimeField(
        "Criado em",
        auto_now_add=True
    )

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['complete', '-created']