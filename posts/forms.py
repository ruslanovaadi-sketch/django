# app/forms.py
from django import forms,Charfield,Form,ModelForm,Integerfield,Imagefield
from .models import Category,Post,Tag,

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']




class TestForm(Form):
        title = CharField(max_length=255, required=False)
        content = CharField(required=False)
        rate = IntegerField(min_value=1, max_value=10, required=False)
        category = IntegerField(required=False)
        image = ImageField(required=False)   
        

class PostForm(forms.ModelForm):
    
    tags = forms.CharField(
        required=False,
        help_text='Введите теги через запятую'
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

    def save(self, commit=True):
        post = super().save(commit=False)

        if commit:
            post.save()

        tags_str = self.cleaned_data.get('tags', '')
        tags_list = [tag.strip() for tag in tags_str.split(',') if tag.strip()]

        for tag_name in tags_list:
            tag, created = Tag.objects.get_or_create(name=tag_name)
            post.tags.add(tag)

        return post             