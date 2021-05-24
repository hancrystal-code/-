from django.shortcuts import render
from .models import Post
from django.utils import timezone
# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    #filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts' : posts})
    #posts 변수(글 정렬)를 템플릿(post_list)에 넘겨주기
