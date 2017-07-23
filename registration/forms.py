from django import forms
from . import models





class register(forms.ModelForm):
  
  class Meta:
      model = models.Participant
      fields = [  'email',
                  'name',
                  'college',
                  'phone_number',
                  'event',
                  
              ]
      widgets = {
          # 'email':forms.EmailInput(attrs = { 
          #           'class': "email",
          #           # 'type': "text",
          #           'placeholder': "ENTER YOUR E-MAIL HERE",
          #           'autocomplete':"off",
          #                              }),
          # 'name': forms.TextInput(attrs = { 
          #           'class': "name",
          #           # 'type': "text",
          #           'placeholder': "ENTER YOUR NAME HERE",
          #           'autocomplete': "off",
          #                              }),
          # 'college':forms.TextInput(attrs = { 
          #           'class': "college",
          #           # 'type': "text",
          #           'placeholder': "ENTER YOUR COLLEGE NAME HERE",
          #           'autocomplete': "off",
          #                              }),
          # 'phone_number': forms.TextInput(attrs = { 
          #           'class': "number",
          #           # 'type': "text",
          #           'placeholder': "ENTER YOUR PHONE NUMBER HERE",
          #           'autocomplete': "off",
          #                              }),
          # 'event': forms.TextInput(attrs = { 
          #           'class': "events",
          #           # 'type': "text",
          #           'placeholder': "EVENTS YOU WISH TO JOIN",
          #           'autocomplete': "off",
          #                              }),
          
          'email':forms.EmailInput(attrs = { 
                    'class': "textbox1",
                    # 'type': "text",
                    'placeholder': "Enter Your Email",
                    'autocomplete':"off",
                                       }),
          'name': forms.TextInput(attrs = { 
                    'class': "textbox",
                    # 'type': "text",
                    'placeholder': "Enter Your Name",
                    'autocomplete': "off",
                                       }),
          'college':forms.TextInput(attrs = { 
                    'class': "textbox",
                    # 'type': "text",
                    'placeholder': "Enter Your College name",
                    'autocomplete': "off",
                                       }),
          'phone_number': forms.TextInput(attrs = { 
                    'class': "number",
                    # 'type': "textbox",
                    'placeholder': "Enter Your Contact No.",
                    'autocomplete': "off",
                                       }),
          'event': forms.TextInput(attrs = { 
                    'class': "textbox",
                    # 'type': "text",
                    'placeholder': "Event You Want To Register For",
                    'autocomplete': "off",
                                       }),
          
                                       
      }