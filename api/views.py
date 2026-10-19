from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import Service, Contact, Project, BlogPost
from .serializers import (
    ServiceSerializer, ContactSerializer,
    ProjectSerializer, BlogPostSerializer,
)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_root(request):
    return Response({
        'message': 'SKILL CORE SOLUTION — API v1',
        'endpoints': {
            'services': '/api/services/',
            'contact': '/api/contact/',
            'projects': '/api/projects/',
            'blog': '/api/blog/',
        },
    })


# ============ SERVICES ============
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def service_list(request):
    services = Service.objects.filter(is_active=True)
    serializer = ServiceSerializer(services, many=True)
    return Response(serializer.data)


# ============ CONTACT ============
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def contact_create(request):
    serializer = ContactSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {
                'success': True,
                'message': 'Thank you! We received your message and will reply within 24 hours.',
            },
            status=status.HTTP_201_CREATED,
        )
    return Response(
        {'success': False, 'errors': serializer.errors},
        status=status.HTTP_400_BAD_REQUEST,
    )


# ============ PROJECTS ============
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def project_list(request):
    category = request.query_params.get('category')
    projects = Project.objects.filter(is_active=True)
    if category and category != 'All':
        projects = projects.filter(category=category)

    serializer = ProjectSerializer(
        projects, many=True, context={'request': request}
    )
    return Response(serializer.data)


# ============ BLOG ============
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def blog_list(request):
    category = request.query_params.get('category')
    posts = BlogPost.objects.filter(is_published=True)
    if category and category != 'All':
        posts = posts.filter(category=category)

    serializer = BlogPostSerializer(
        posts, many=True, context={'request': request}
    )
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def blog_detail(request, pk):
    try:
        post = BlogPost.objects.get(pk=pk, is_published=True)
    except BlogPost.DoesNotExist:
        return Response(
            {'success': False, 'message': 'Post not found.'},
            status=status.HTTP_404_NOT_FOUND,
        )
    serializer = BlogPostSerializer(post, context={'request': request})
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def blog_categories(request):
    categories = BlogPost.objects.filter(is_published=True).values_list('category', flat=True).distinct()
    return Response({'categories': list(categories)})
    