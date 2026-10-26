from .models import UserMovie
from django import forms

# The form that the user fills out on the added movie page
class UserMovieForm(forms.ModelForm):
    class Meta:
        model = UserMovie
        fields = ["rating", "watched_date", "opinion", "favourite_quotes", "favourite_scene_url"]
        widgets = {
            "watched_date": forms.DateInput(attrs={"type": "date"}, format="%Y-%m-%d"),
            "opinion": forms.Textarea(attrs={"rows": 5, "placeholder": "What did you think?"}),
            "favourite_quotes": forms.Textarea(attrs={"rows": 4, "placeholder": "One quote per line..."}),
            "favourite_scene_url": forms.URLInput(attrs={"placeholder": "https://example.com/scene.jpg"}),
        }