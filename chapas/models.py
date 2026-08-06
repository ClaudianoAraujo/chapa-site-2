from django.db import models


class Chapa(models.Model):
    ESTADO_CHOICES = [
        ('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'),
        ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'),
        ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'),
        ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'),
        ('TO', 'Tocantins'),
    ]

    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20, help_text="Com DDD, ex: 11999998888")
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2, choices=ESTADO_CHOICES)
    verificado = models.BooleanField(default=False)
    contador_contatos = models.PositiveIntegerField(default=0)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        ordering = ['-data_cadastro']
        verbose_name = 'Chapa'
        verbose_name_plural = 'Chapas'

    def __str__(self):
        return f"{self.nome} - {self.cidade}/{self.estado}"

    def link_whatsapp(self):
        numero = ''.join(filter(str.isdigit, self.telefone))
        return f"https://wa.me/55{numero}"
