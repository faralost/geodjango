from rest_framework import serializers
from rest_framework.generics import get_object_or_404

from geoapp.models import Plot, Culture, Season, Farmer


class FarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer
        exclude = ['user', ]


class CultureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Culture
        fields = '__all__'


class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = '__all__'


class PlotSerializer(serializers.ModelSerializer):
    farmer = FarmerSerializer(read_only=True)
    culture = CultureSerializer()
    season = SeasonSerializer(read_only=True)

    def update(self, instance, validated_data):
        print(validated_data)
        if 'culture' in validated_data:
            culture_title = validated_data.pop('culture')['title']
            culture_instance = get_object_or_404(Culture, title=culture_title)
            instance.culture = culture_instance
            instance.save()
        return super().update(instance, validated_data)

    class Meta:
        model = Plot
        fields = ['id', 'contour', 'farmer', 'culture', 'season']
        read_only_fields = ['contour', ]
