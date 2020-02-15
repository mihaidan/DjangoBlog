from django import forms
from .models import Post


# Form for creating and editing a post.
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'description']
        
        # Styling the forms so that they look better.
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'})
        }