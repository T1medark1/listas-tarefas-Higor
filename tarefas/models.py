from django.db import models

class Tarefa(models.Model):
        PRIORIDADES = [
            ('baixa' , 'Baixa'),
            ('media' , 'Média'),
            ('alta' , 'Alta'),   
        ]

        titulo = models.CharField(max_length=120)
        descricao = models.TextField()
        prioridade = models.CharField(max_length=5,choices=PRIORIDADES)
        concluida = models.BooleanField(default=False)
        criada_em = models.DateTimeField(auto_now_add=True)











