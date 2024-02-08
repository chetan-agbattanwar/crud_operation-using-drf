from rest_framework import serializers
from .models import studentModel

class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model = studentModel
        fields = '__all__'

    def create(self, validated_data):
        return studentModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.roll = validated_data.get('roll',instance.roll)
        instance.name = validated_data.get('name',instance.name)
        instance.marks = validated_data.get('marks',instance.marks)

        instance.save()
        return instance