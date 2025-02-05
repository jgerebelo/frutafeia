from django.db import models
from googleapiclient import model
from numpy import true_divide
from pandas.core.algorithms import quantile
from core.enum import TIPO_PRODUTO_CHOICES, ESTADO_CHOICES, MEDIDA_CHOICES

# Create your models here.


class FamiliaProduto(models.Model):
    """Family of products. one family can have many products associated. One product only has one Family"""

    nome = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Família de Produto"
        verbose_name_plural = "Famílias de Produtos"

    def __str__(self):
        return str(self.nome)


class Produto(models.Model):
    """Possible products"""

    nome = models.CharField(max_length=255)
    familia = models.ForeignKey("FamiliaProduto", on_delete=models.CASCADE, null=True)
    tipo = models.PositiveSmallIntegerField(
        choices=TIPO_PRODUTO_CHOICES, blank=True, null=True
    )
    quantidade_cesta_pequena = models.FloatField(null=True, blank=True)
    quantidade_cesta_grande = models.FloatField(null=True, blank=True)
    medida = models.PositiveSmallIntegerField(
        choices=MEDIDA_CHOICES, null=True, blank=True
    )

    @property
    def tipo_name(self):
        return dict(TIPO_PRODUTO_CHOICES).get(self.tipo)

    def __str__(self):
        return f"{self.nome} - {self.tipo_name}"


class Produtor(models.Model):
    """Produts providers"""

    nome = models.CharField(max_length=255)
    produtos = models.ManyToManyField("Produto")
    estado = models.PositiveSmallIntegerField(
        choices=ESTADO_CHOICES, null=True, blank=True
    )
    email = models.EmailField(max_length=255, null=True, blank=True)
    morada = models.CharField(max_length=255, null=True, blank=True)
    concelho = models.CharField(max_length=255, null=True, blank=True)
    telefone = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Produtores"

    @property
    def estado_name(self):
        return dict(ESTADO_CHOICES).get(self.estado)

    def __str__(self):
        return self.nome


class Disponibilidade(models.Model):
    """Disponibilidades registadas semanalmente. Atualizado sempre que há iteração com o frontend. Reset no inicio da semana"""

    data = models.DateField()
    produto = models.ForeignKey("Produto", on_delete=models.CASCADE)
    produtor = models.ForeignKey("Produtor", on_delete=models.CASCADE)
    quantidade = models.FloatField(null=True, blank=True)
    medida = models.PositiveSmallIntegerField(
        choices=MEDIDA_CHOICES, null=True, blank=True
    )
    preco = models.FloatField(null=True, blank=True)
    urgente = models.BooleanField()
    on_hold = models.BooleanField(default=True)

    @property
    def medida_name(self):
        return dict(MEDIDA_CHOICES).get(self.medida)

    @property
    def medida_dict(self):
        return {"id": self.medida, "nome": dict(MEDIDA_CHOICES).get(self.medida)}

    def __str__(self):
        return f"{self.data} : {self.produtor} : {self.produto}"


class MapaDeCampo(models.Model):
    """Registo dos produtores e produtos utilizados em cada semana"""

    data = models.DateField()
    produto = models.ForeignKey("Produto", on_delete=models.CASCADE)
    produtor = models.ForeignKey("Produtor", on_delete=models.CASCADE)
    quantidade = models.FloatField(null=True, blank=True)
    medida = models.PositiveSmallIntegerField(
        choices=MEDIDA_CHOICES, blank=True, null=True
    )
    preco = models.FloatField(null=True, blank=True)

    @property
    def medida_name(self):
        return dict(MEDIDA_CHOICES).get(self.medida)

    def __str__(self):
        return f"{self.data} : {self.produtor} : {self.produto}"


class noWorkLastWeek(models.Model):
    value = models.BooleanField(default=False)


class CestasFeitas(models.Model):
    """Quantidade de cestas feitas em cada semana"""

    data = models.DateField()
    cestas_pequenas = models.PositiveIntegerField(null=True, blank=True)
    cestas_grandes = models.PositiveIntegerField(null=True, blank=True)


class ConteudoCesta(models.Model):
    """Informação de cada Produto-Produtor que faz parte de uma cesta"""

    produtor = models.ForeignKey("Produtor", on_delete=models.CASCADE)
    produto = models.ForeignKey("Produto", on_delete=models.CASCADE)
    quantidade_pequena = models.FloatField(null=True, blank=True)
    quantidade_grande = models.FloatField()
    medida = models.PositiveSmallIntegerField(
        choices=MEDIDA_CHOICES, null=True, blank=True
    )
    preco_unitario = models.FloatField()
    produto_extra = models.BooleanField()

    @property
    def medida_name(self):
        return dict(MEDIDA_CHOICES).get(self.medida)


class Cesta(models.Model):
    """cada cesta que foi feita, com o respetivo conteudo, preços e pesos"""

    data = models.DateField()
    conteudo = models.ManyToManyField("ConteudoCesta")
    preco_pequena = models.FloatField()
    peso_pequena = models.FloatField()
    preco_grande = models.FloatField()
    peso_grande = models.FloatField()


class CestaResult(models.Model):
    result = models.BooleanField()
    message = models.TextField()


class Ranking(models.Model):
    """Sugestão de produtor/produtos a contactar para cada semana. Atualizado semanalmente"""

    produto = models.ForeignKey("Produto", on_delete=models.CASCADE)
    produtor = models.ForeignKey("Produtor", on_delete=models.CASCADE)
    pontuacao = models.FloatField()


class Sazonalidade(models.Model):
    """Sazonalidade (de 0 a 1) de produtos"""

    produto = models.ForeignKey("Produto", on_delete=models.CASCADE)
    janeiro = models.FloatField(null=True, blank=True)
    fevereiro = models.FloatField(null=True, blank=True)
    marco = models.FloatField(null=True, blank=True)
    abril = models.FloatField(null=True, blank=True)
    maio = models.FloatField(null=True, blank=True)
    junho = models.FloatField(null=True, blank=True)
    julho = models.FloatField(null=True, blank=True)
    agosto = models.FloatField(null=True, blank=True)
    setembro = models.FloatField(null=True, blank=True)
    outubro = models.FloatField(null=True, blank=True)
    novembro = models.FloatField(null=True, blank=True)
    dezembro = models.FloatField(null=True, blank=True)
