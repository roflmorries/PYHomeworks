from django import forms

from task.models import Comment, Rating, Member


class CommentForm(forms.Form):
	user_name = forms.CharField(max_length=255)
	text = forms.CharField(max_length=2000)
	choices = forms.ChoiceField(
		choices=[
			('issues', 'Issues'),
			('comment', 'Comment')
		]
	)


class CommentModelForm(forms.ModelForm):
	class Meta:
		model = Comment  # Название модели
		fields = '__all__'  # ['user_name', 'text']  # Список полей


class RatingModelForm(forms.ModelForm):
	class Meta:
		model = Rating
		fields = '__all__'
		labels = {
			'point': 'Rate',
			'user_name': 'Your name'
		}


class MemberModelForm(forms.ModelForm):
	class Meta:
		model = Member
		fields = '__all__'
		labels = {
			'email': 'Your mail',
			'name': 'Your name',
			'phome': 'Your phone'
		}