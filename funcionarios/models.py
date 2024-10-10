from django.db import models

estado = (
            ("AC", "Acre"),
            ("AL", "Alagoas"),
            ("AP", "Amapá"),
            ("AM", "Amazonas"),
            ("BA", "Bahia"),
            ("CE", "Ceará"),
            ("DF", "Distrito Federal"),
            ("ES", "Espírito Santo"),
            ("GO", "Goiás"),
            ("MA", "Maranhão"),
            ("MT", "Mato Grosso"),
            ("MS", "Mato Grosso do Sul"),
            ("MG", "Minas Gerais"),
            ("PA", "Pará"),
            ("PB", "Paraíba"),
            ("PR", "Paraná"),
            ("PE", "Pernambuco"),
            ("PI", "Piauí"),
            ("RJ", "Rio de Janeiro"),
            ("RN", "Rio Grande do Norte"),
            ("RS", "Rio Grande do Sul"),
            ("RO", "Rondônia"),
            ("RR", "Roraima"),
            ("SC", "Santa Catarina"),
            ("SP", "São Paulo"),
            ("SE", "Sergipe"),
            ("TO", "Tocantins")
)

class Funcionarios(models.Model):
    nome = models.CharField(max_length=150, null=True)
    data_nascimento = models.DateField(null=True)
    cpf = models.CharField(max_length=14, unique=True, null=True)
    numero = models.CharField(max_length=150, null=True)
    estado = models.CharField(max_length=100, choices=estado,null=True)
    logradouro = models.CharField(max_length=200, null=True)
    cep = models.CharField(max_length=150, null=True)
