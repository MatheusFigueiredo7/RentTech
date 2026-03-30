from django.db import models

class Equipamento(models.Model):
    STATUS_CHOICES = [
        ("DISPONIVEL", "Disponível"),
        ("ALUGADO", "Alugado"),
        ("MANUTENCAO", "Em Manutenção"),
        ("INDISPONIVEL", "Indisponível")
    ]

    nome = models.CharField("Nome",max_length=255)
    especificacoes = models.TextField("Especificações")

    status = models.CharField(
        max_length=20, 
        choices=STATUS_CHOICES, 
        default="DISPONIVEL"
    )
    
    valor_diaria = models.DecimalField("Valor da Diária",max_digits=10, decimal_places=2)
    data_aquisicao = models.DateField("Data de Aquisição")
    
    def __str__(self):
        return self.nome