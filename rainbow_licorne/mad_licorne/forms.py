from django.forms import ModelForm
from mad_licorne.models import Comment

class CommentForm(ModelForm):
	class Meta:
		model = Comment
		fields = ['name','content']