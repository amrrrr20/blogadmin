from django.http import HttpResponse
from django.template import loader
from blogam.models import Blog


def blog(request):
        posts = Blog.objects.all().order_by('-date')
        template = loader.get_template('blog.html')
        context={
                'posts':posts,
        }
        return HttpResponse(template.render(context,request))