from django.db import models


class Tema(models.Model):

    COR = (
        ('Vermelho', 'Vermelho'),
        ('Verde', 'Verde'),
        ('Azul', 'Azul'),
        ('Amarelo', 'Amarelo'),
        ('Magenta', 'Magenta'),
        ('Ciano', 'Ciano'),
        ('Branco', 'Branco'),
        ('Preto', 'Preto'),
    )

    nome = models.CharField(max_length=30)
    valorAluguel = models.DecimalField(max_digits=6, decimal_places=2)
    corDestaque = models.CharField(max_length=20, choices=COR)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
