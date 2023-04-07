from .models import Audios
from django import forms


class GenerateAudioFileForm(forms.ModelForm):
    SELECT_ACCENT = (
        ('co.uk', '-- Select one option --'),
        ('com.au', 'English (Australia)'),
        ('ca', 'English (Canada)'),
        ('co.in', 'English (India)'),
        ('ie', 'English (Ireland)'),
        ('com.uk', 'English (UK)'),
        ('us', 'English (US)'),
    )
    SELECT_FILE_TYPE = (
        (None, '-- Select audio format --'),
        ('.mp3', '.mp3'),
        ('.ogg', '.ogg'),
        ('.wav', '.wav')
    )

    title = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'text', 'placeholder': 'Enter name of your choice ...'}),
        label='Audio name',
        help_text='Name provided will be used to name the generated audio file, e.g. <b>"my-speech", "project-presentation"</b>'
        )
    description = forms.CharField(
        widget=forms.Textarea(attrs={'type': 'text', 'class': 'mt-2', 'placeholder': 'Type your text ...'}),
        label='Text',
        help_text='This text that will be use to generate an audio file',
        )
    accent = forms.ChoiceField(
        widget=forms.Select(attrs={'type': 'select', 'class': 'mt-2'}),
        help_text='Select your preferred accent',
        choices=SELECT_ACCENT,
        )
    file_type = forms.ChoiceField(widget=forms.Select(attrs={'type': 'select', 'class': 'mt-2 mb-2'}), choices=SELECT_FILE_TYPE)
    
    class Meta:
        model = Audios
        fields = '__all__'

