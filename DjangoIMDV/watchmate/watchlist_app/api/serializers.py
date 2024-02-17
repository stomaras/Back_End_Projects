from rest_framework import serializers
from watchlist_app.models import Movie

    
class MovieSerializer(serializers.ModelSerializer):
    
    # Serializer Method Field
    len_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Movie
        fields = "__all__"
    
    def get_len_name(self, obj):
        length = len(obj.name)
        return length  
    
    # field level validation
    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError('Name is too short!')
        else:
            return value
        
    # object level validation
    def validate(self,data):
        if data['name'] == data['description']:
            raise serializers.ValidationError('Title and Description cannot be the same!')
        else:
            return data