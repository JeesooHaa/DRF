from rest_framework import serializers
from .models import Music, Artist, Comment

class MusicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Music
        fields = ('id', 'title', 'artist_id', )


class ArtistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artist
        fields = ('id', 'name', )


# ArtistSerializer 만드는 방식으로 만들어도됨
class ArtistDetailSerializer(ArtistSerializer):
    # artist_id 가 중복되...
    musics = MusicSerializer(many=True)
    musics_count = serializers.IntegerField(source='musics.count')

    class Meta(ArtistSerializer.Meta):
        fields = ArtistSerializer.Meta.fields + ('musics', 'musics_count', )


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'content', 'music_id', )
