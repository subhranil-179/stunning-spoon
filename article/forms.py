from django import forms
from article.models import Comment


class CommentForm(forms.ModelForm):
    author = forms.CharField(
            label="",
            widget=forms.TextInput(attrs={"placeholder": "Your Name"}),
            required=True
    )
    text = forms.CharField(
            label="",
            widget=forms.TextInput(attrs={"placeholder": "Comment your thoughts"}),
            required=True
    )

    class Meta:
        model = Comment
        fields = ['author', 'text']
