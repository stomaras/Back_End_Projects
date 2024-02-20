from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform, Review

class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = "__all__"

    
class WatchListSerializer(serializers.ModelSerializer):
    # read only means on the post i am not going to add review
    # but in the get request i will receive this readonly field also
    reviews = ReviewSerializer(many=True, read_only=True)
    # Serializer Method Field
    class Meta:
        model = WatchList
        fields = "__all__"
    
class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True)
    
    
    class Meta:
        model = StreamPlatform
        fields = "__all__"