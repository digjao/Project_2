from auctions.models import Listing
from django import forms

class Newlist(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'description', 'initialBid', 'image', 'category',]