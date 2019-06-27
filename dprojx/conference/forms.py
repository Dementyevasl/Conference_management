from django import forms
from .models import Article


# class SubmissionForm(forms.Form):
#     title = forms.CharField(max_length=100)
#     abstract = forms.CharField(widget=forms.Textarea)
#     keywords = forms.CharField(widget=forms.Textarea)
#     paper = forms.CharField(widget=forms.Textarea)
#
#     def save(self):
#         article = Article(**self.cleaned_data)
#         article.save()
#         return article

class SubmissionForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('title', 'abstract', 'keywords', 'paper', )
        help_texts = {
            'keywords': 'Type at least 3 keywords that characterize your work, separated by commas',
        }