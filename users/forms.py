from django.core.validators import FileExtensionValidator
from .models import AudioFiles, VideoFiles
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
        widget=forms.TextInput(attrs={'type': 'text', 'placeholder': 'What will be the name of your audio file?'}),
        label='Name',
        required=True,
        help_text='Name provided will be used as name of the generated audio file, e.g. <b>"my-speech", "project-presentation"</b>'
        )
    description = forms.CharField(
        widget=forms.Textarea(attrs={'type': 'text', 'placeholder': 'Type your text ...'}),
        label='Text',
        required=True,
        help_text='This text that will be use to generate an audio file',
        )
    accent = forms.ChoiceField(
        widget=forms.Select(attrs={'type': 'select'}),
        help_text='Select your preferred accent',
        label='Language accent',
        choices=SELECT_ACCENT,
        )
    file_type = forms.ChoiceField(
        widget=forms.Select(attrs={'type': 'select', 'class': 'mb-2'}), 
        label='File Format',
        choices=SELECT_FILE_TYPE, 
        required=True,
        help_text='In what file format do you want the generated audio to be saved?',
        )
    
    class Meta:
        model = AudioFiles
        fields = ['title', 'description', 'accent', 'file_type']


class UploadAudioFileForm(forms.ModelForm):    
    title = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'text', 'placeholder': 'What will be the name of your audio file?'}),
        label='Name',
        required=False,
        help_text='Enter your name of choice if you wish to rename the audio file.',
        )
    audio = forms.FileField(
        widget=forms.FileInput(attrs={'type': 'file', 'class': 'form-control'}),
        help_text='Upload audio files: <b>.mp3, .ogg or .wav only!</b>',
        required=True,
        validators=[FileExtensionValidator(['mp3', 'ogg', 'wav'])]
    )
    
    class Meta:
        model = AudioFiles
        fields = ['audio', 'title']


class UploadVideoFileForm(forms.ModelForm):
    SELECT_FILE_TYPE = (
        (None, '-- Select file format --'),
        ('.srt', '.srt'),
        ('.txt', '.txt'),
    )
    title = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'text', 'placeholder': 'What will be the name of your video file?'}),
        label='Name',
        required=False,
        help_text='Enter your name of choice if you wish to rename the video file.',
        )
    video = forms.FileField(
        widget=forms.FileInput(attrs={'type': 'file', 'class': 'form-control'}),
        help_text='Upload audio files: <b>m4a, .mp4, .mkv, .mpga, .mpeg or .webm only!</b>',
        required=True,
        validators=[FileExtensionValidator(['m4a', 'mp4', 'mkv', 'mpga', 'mpeg', 'webm'])]
    )
    file_type = forms.ChoiceField(
        widget=forms.Select(attrs={'type': 'select', 'class': 'mb-2'}), 
        label='File Format',
        choices=SELECT_FILE_TYPE, 
        required=True,
        help_text='In what file format do you want the generated file to be saved?',
        )


    class Meta:
        model = VideoFiles
        fields = ['video', 'file_type', 'title']
