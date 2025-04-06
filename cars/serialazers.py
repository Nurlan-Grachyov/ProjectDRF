from rest_framework import serializers

from cars.models import Cars, Moto, Milage
from cars.services import current
from cars.validators import TitleValidator


class MilageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Milage
        fields = "__all__"


class CarSerializer(serializers.ModelSerializer):
    last_milage = serializers.IntegerField(source='milage.all.first.milage', read_only=True)
    milage = MilageSerializer(many=True, read_only=True)
    rub_price = serializers.SerializerMethodField()

    class Meta:
        model = Cars
        fields = '__all__'

    def get_rub_price(self, obj):
        return current(obj.price)


class MotoSerializer(serializers.ModelSerializer):
    last_milage = serializers.SerializerMethodField()

    class Meta:
        model = Moto
        fields = '__all__'

    def get_last_milage(self, obj):
        if obj.milage.all().first():
            return obj.milage.all().first().milage
        return 0


class MotoMilageSerializer(serializers.ModelSerializer):
    moto = MotoSerializer()

    class Meta:
        model = Milage
        fields = ('milage', 'year', 'moto',)


class MotoCreateSerializer(serializers.ModelSerializer):
    milage = MilageSerializer(many=True)

    class Meta:
        model = Moto
        fields = '__all__'
        validators = [TitleValidator(field="title"),
                      serializers.UniqueTogetherValidator(fields=["title", "description"], queryset=Moto.objects.all())]

    def create(self, validated_data):
        milage = validated_data.pop('milage')

        moto_item = Moto.objects.create(**validated_data)

        for m in milage:
            Milage.objects.create(**m, moto=moto_item)
        return moto_item
