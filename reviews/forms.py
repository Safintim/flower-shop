from django import forms

from reviews.models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('name', 'phone', 'city', 'social_link', 'text', 'image')
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4, 'cols': 15}),
        }
