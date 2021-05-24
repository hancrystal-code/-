from django import forms
from .models import Post

class PostForm(forms.ModelForm): #폼, ModelForm이라는 걸 장고에게 알려주기. 장고가 마법을 부릴거임!!
    class Meta:
        model = Post #어떤 모델이 쓰여야하는지 장고에게 알려주기
        fields = ('title', 'text',)