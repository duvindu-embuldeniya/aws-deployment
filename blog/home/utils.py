from . models import Blog, Tag
from django.db.models import Q



def search_blog(request):
    query_value = request.GET.get('query') if request.GET.get('query') else ''

    tags = Tag.objects.filter(
        Q(name__icontains = query_value)
    )

    blogs = Blog.objects.distinct().filter(
        Q(author__username__icontains = query_value) |
        Q(title__icontains = query_value) |
        Q(tag__in = tags)
    )

    return blogs, query_value