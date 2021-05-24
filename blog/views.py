from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect
# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    #filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts' : posts})
    #posts 변수(글 정렬)를 템플릿(post_list)에 넘겨주기
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
def post_new(request):
    #글쓰고 POST 기능 구현
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)#pk=post.pk를 사용해서 뷰에게 값을 넘겨주기
    else:
        form = PostForm()
    form = PostForm() #Post 폼을 추가하기 위함
    return render(request, 'blog/post_edit.html', {'form': form})

'''<단순히 글쓰기 기능 구현>
def post_new(request):
    form = PostForm() #Post 폼을 추가하기 위함
    return render(request, 'blog/post_edit.html', {'form': form})def post_new(request):
    form = PostForm() #Post 폼을 추가하기 위함
    return render(request, 'blog/post_edit.html', {'form': form})'''

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST,instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})