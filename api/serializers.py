from rest_framework import serializers
from core.models import Disponibilidade, Produtor, Produto, Ranking


class ProdutoSerializer(serializers.ModelSerializer):
    """Serializer for produto objects"""
   
    class Meta:
        model = Produto
        fields = "__all__"

class ProdutoNameSerializer(serializers.ModelSerializer):
    """Serializer for produto objects"""
   
    class Meta:
        model = Produto
        fields = ('nome',)


class ProdutorSerializer(serializers.ModelSerializer):
    """Serializer for produtor objects"""
    produtos = ProdutoSerializer(many=True, read_only=True)
    class Meta:
        model = Produtor
        fields = "__all__"

class DisponibilidadeSerializer(serializers.ModelSerializer):
    """Serializer for disponibilidade objects"""

    produto = serializers.SlugRelatedField(
        queryset=Produto.objects.all(), read_only=False, slug_field="nome"
    )

    produtor = serializers.SlugRelatedField(
        queryset=Produtor.objects.all(), read_only=False, slug_field="nome"
    )

    class Meta:
        model = Disponibilidade
        fields ="__all__"



class RankingSerializer(serializers.ModelSerializer):
    """Serializer for disponibilidade objects"""

    produto = serializers.SlugRelatedField(
        queryset=Produto.objects.all(), read_only=False, slug_field="nome"
    )

    produtor = serializers.SlugRelatedField(
        queryset=Produtor.objects.all(), read_only=False, slug_field="nome"
    )

    class Meta:
        model = Ranking
        fields ="__all__"
