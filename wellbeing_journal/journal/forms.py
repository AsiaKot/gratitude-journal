from django import forms
from .models import Daily


class CreateJournalingPost(forms.ModelForm):

    class Meta:
        model = Daily
        fields = ['thoughts']
        labels = {'thoughts': ''}
        widgets = {'thoughts': forms.Textarea(attrs={'placeholder': 'Write something here...'})}

        def form_valid(self, form):
            form.instance.author = self.request.user
            return super().form_valid(form)


class AddDailyPic(forms.ModelForm):

    class Meta:
        model = Daily
        fields = ['daily_pic']
        labels = {'daily_pic': ''}

        def form_valid(self, form):
            form.instance.author = self.request.user
            return super().form_valid(form)


class CreateGratefulPost(forms.Form):
    grateful_for1 = forms.CharField(label="1: ",
                                    max_length=500,
                                    widget=forms.TextInput(attrs={"placeholder": "I'm grateful for..."}))
    grateful_for2 = forms.CharField(label="2: ",
                                    max_length=500,
                                    widget=forms.TextInput(attrs={"placeholder": "I'm grateful for..."}))
    grateful_for3 = forms.CharField(label="3: ",
                                    max_length=500,
                                    widget=forms.TextInput(attrs={"placeholder": "I'm grateful for..."}))

