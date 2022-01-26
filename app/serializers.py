from unicodedata import category
from rest_framework import serializers
from .models import Blog,Comment,Like,Category,Contact



# Like


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'

class LikeCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['value','user']

#  comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields='__all__'
        

class CommentCreateAPIView(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields='__all__'

# category

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model=Category
        fields='__all__'
        

# blog

class BlogSerializer(serializers.ModelSerializer):
    comments=CommentSerializer(read_only=True,many=True)
    categories=CategorySerializer(read_only=True,many=True)

    class Meta:
        model=Blog
        fields='__all__'

        
class BlogCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Blog
        fields='__all__'




# tag

# class TagSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Tag
#         fields='__all__'


# contact

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'