# from django import forms
# from . import Quiz


# class QuizForm(forms.ModelForm):
#     class Meta:
#         model = Quiz
#         fields = [
#             "content",
#             "choices",
#         ]

#     choices = forms.ModelChoiceField(
#         widget=forms.RadioSelect, queryset=Quiz.objects.all()
#     )
# # 