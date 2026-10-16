from rest_framework import serializers
from .models import Service, Contact, Project, BlogPost


class ServiceSerializer(serializers.ModelSerializer):
    feature_list = serializers.ReadOnlyField()

    class Meta:
        model = Service
        fields = [
            'id', 'title', 'short_desc', 'full_desc',
            'icon', 'features', 'feature_list', 'order',
        ]


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = [
            'id', 'name', 'email', 'phone', 'company',
            'service', 'budget', 'message', 'created_at',
        ]
        read_only_fields = ['id', 'created_at']

    def validate_name(self, value):
        if len(value.strip()) < 2:
            raise serializers.ValidationError("Name must be at least 2 characters.")
        return value.strip()

    def validate_message(self, value):
        if len(value.strip()) < 10:
            raise serializers.ValidationError("Message must be at least 10 characters.")
        return value.strip()


class ProjectSerializer(serializers.ModelSerializer):
    tag_list = serializers.ReadOnlyField()
    image_final = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = [
            'id', 'title', 'client', 'category', 'year', 'description',
            'tags', 'tag_list', 'image', 'image_url', 'image_final',
            'is_featured', 'order',
        ]

    def get_image_final(self, obj):
        if obj.image:
            request = self.context.get('request')
            return request.build_absolute_uri(obj.image.url) if request else obj.image.url
        return obj.image_url


class BlogPostSerializer(serializers.ModelSerializer):
    image_final = serializers.SerializerMethodField()

    class Meta:
        model = BlogPost
        fields = [
            'id', 'title', 'slug', 'category', 'author',
            'excerpt', 'content', 'read_time',
            'image', 'image_url', 'image_final',
            'is_featured', 'created_at',
        ]

    def get_image_final(self, obj):
        if obj.image:
            request = self.context.get('request')
            return request.build_absolute_uri(obj.image.url) if request else obj.image.url
        return obj.image_url