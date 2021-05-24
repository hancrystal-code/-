from django.urls import path
from . import views #어플리케이션에서 사용할 모든 view 임포트

urlpatterns = [
    path('', views.post_list, name='post_list'),
    #post_list라는 view가 루트 URL에 할당
    #누군가 웹사이트에 'http://127.0.0.1:8000/' 주소로 들어왔을 때 
    #장고에게 views.post_list를 보여주라고 말해주는 패턴이다.
    #전체 URL 경로에서 접두어(prefix)에 포함되는 도메인 이름(i.e. http://127.0.0.1:8000/)을 무시하고 받아들임
    #마지막 부분인 name='post_list'는 URL에 이름을 붙인 것으로 뷰를 식별
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    # post/기본키/ 경로로 접근 시, post_detail 뷰 보여주기
    
]