from rest_framework import serializers
from watchlist_app.models import Movie

# Three types of validation

# 1. Field Level Validation validate_field
# 2. Object Validation
# 3. Validators

def name_length(value):
    if len(value) < 2:
        raise serializers.ValidationError('Name is too short!')

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(validators=[name_length])
    description = serializers.CharField()
    active = serializers.BooleanField()
    
    def create(self, validated_data):
        return Movie.objects.create(**validated_data)
    
    # instance carries the old values 
    # validated_data carries the new values 
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance
    
    # field level validation
    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError('Name is too short!')
    #     else:
    #         return value
        
    # object level validation
    def validate(self,data):
        if data['name'] == data['description']:
            raise serializers.ValidationError('Title and Description cannot be the same!')
        else:
            return data