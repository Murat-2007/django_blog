from django import forms
from .models import Blog,Comment
from ckeditor.widgets import CKEditorWidget


banned_email_list=['ahmet@gmail.com', 'deneme@gmail.com', 'murat@gmail.com']

class IletisimForm(forms.Form):
    isim     = forms.CharField(max_length=40, label='İsim', required=True)
    soyisim  = forms.CharField(max_length=40, label='Soyisim', required=True)
    email    = forms.EmailField(max_length=40, label='Email', required=True)
    email2   = forms.EmailField(max_length=40, label='Email Kontrol', required=True)
    icerik   = forms.CharField(max_length=1000, label='İçerik', required=True)
    
    def __init__(self, *args, **kwargs):
        super(IletisimForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs={'class':'form-control'}
        self.fields['icerik'].widget=forms.Textarea(attrs={'class':'form-control'})
    
    def clean_isim(self):
        isim = self.cleaned_data.get('isim')
        print(isim)
        if isim == 'ahmet':
            raise forms.ValidationError('Lutfen Ahmet dışında bir isim giriniz')
        return isim
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email in banned_email_list:
            raise forms.ValidationError('Lütfen banlı email adresleri dışında bir email giriniz')
        return email
        
    def clean(self):
        email  = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if email != email2:
            self.add_error('email2', 'emailler eşleşmedi')
            self.add_error('email', 'emailler eşleşmedi')
            


class BlogForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Blog
        fields = ['title', 'image', 'content', 'yayin_taslak', 'kategoriler']
        
    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs={'class':'form-control'}
        self.fields['content'].widget.attrs['rows']=10
       
    #def clean_content(self):  (illa 250 karakter yazmamak icin yorum satiri yaptim)
        #content = self.cleaned_data.get('content')
        #if len(content) < 250:
            #uzunluk = len(content)
            #msg = 'Lütfen en az 250 karakter giriniz.Girilen karakter sayısı (%s)' % (uzunluk)
            #raise forms.ValidationError(msg)
        #return content
        
class PostSorguForm(forms.Form):
    YAYIN_TASLAK =  (('all', 'HEPSI'),('yayin', 'YAYIN'), ('taslak', 'TASLAK'))
    search = forms.CharField(max_length=500, widget=forms.TextInput(attrs={'placeholder':'Bir Şeyler Arayınız','class':'form-control'}))
    taslak_yayin = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=YAYIN_TASLAK, required=True)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields=['icerik']
            
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {'class': 'form-control'}
            