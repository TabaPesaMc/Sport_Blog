from django import forms
from .models import Post, Category,Comment

# choice = [('sports','sports'),('coding','coding'),('entertainment','entertainment'),]
choice = Category.objects.all().values_list('name', 'name')

choice_list = []

for item in choice:
    choice_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('tittle', 'tittle_tag', 'author', 'Category', 'body','snippet','header_image')
        widgets = {
            'tittle': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your tittle here'}),
            'tittle_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your tittle tag here'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'elder', 'type': 'hidden'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'Category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),

        }


class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('tittle', 'tittle_tag', 'body','snippet','header_image')
        widgets = {
            'tittle': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your tittle here'}),
            'tittle_tag': forms.TextInput(attrs={'class': 'form-control'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),

        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name here'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),

        }
