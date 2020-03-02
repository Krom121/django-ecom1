from django.forms import ModelForm
from .models import Subscriber, NewContact

#### SUBCRIBER FORM #######

class SubscribeForm(ModelForm):

    class Meta:
        model = Subscriber
        fields = ('name','email')

##### CONTACT FORM #######

class ContactForm(ModelForm):

    class Meta:
        model = NewContact
        fields = ('first_name','last_name','email','tell_us_more')