# from dataclasses import field, fields
# from email.policy import default
# from pyexpat import model
# # from tkinter import Widget
# from turtle import width
# from urllib import request
# from PIL import Image
# from django.core.files.uploadedfile import SimpleUploadedFile
from cProfile import label
from dataclasses import field, fields
from pyexpat import model
from random import choices
from django.forms import widgets
from django import forms
# from tickets import models
from tickets.models import Ariza, Firma, ImageKesif, KesifPTSMalzeme, Paylasim, Comment,Kesif,KesifOlayMalzeme,Image,KesifCCTVMalzeme
# from ckeditor.fields import RichTextField
# from django.db import models
from django.core.mail import send_mail
from django import forms
from django.conf import settings
# from django.core.mail import EmailMessage
# from phonenumber_field.modelfields import PhoneNumberField


# class ProductCreateForm(forms.Form):
#     göndericiAdi= forms.CharField(label='Your name',max_length=100)
#     gönderiKonu= forms.CharField()
#     gönderiAciklama= forms.Textarea()
#     gönderiFoto= forms.ImageField(label='foto name')
#     gönderiDurumu= forms.BooleanField(required=False)
#     yazılımUrunumu= forms.BooleanField(required=False)
#     cameUrunumu= forms.BooleanField(required=False)
#     sssmi= forms.BooleanField(required=False)


class ArizaGönder(forms.ModelForm):

    class Meta:
        model = Ariza
        fields = "__all__"
        exclude = [
            'slug',
            'CozumVarMı',
            'Arsivmi',
            'firma_bilgi',
        ]

        widgets = {
            "firma_bilgi": widgets.Select(attrs={"class": "form-control"}),
            "gelenKonu": widgets.TextInput(attrs={"class": "form-control", "placeholder": "Kamera Görüntüsü Gelmiyor"}),
            "gelenMail": widgets.EmailInput(attrs={"class": "form-control", "placeholder": "mert.tekin@aksiyonteknoloji.com"}),
            "gelenAdSoyad": widgets.TextInput(attrs={"class": "form-control", "placeholder": "Mert TEKİN"}),
            "gelenTelefon": widgets.TextInput(attrs={"class": "form-control", "placeholder": "05302489999", 'maxlength': '11', }),
            "gelenAciklama": widgets.Textarea(attrs={"class": "form-control", "placeholder": "Açıklama..."}),

        }

        labels = {
            "gelenAdSoyad": "Ad Soyad",
            "gelenKonu": "Konu",
            "gelenMail": "Email Adresi Giriniz",
            "gelenTelefon": "İrtibat Telefonu",
            "gelenAciklama": "Açıklama",
            "firma_bilgi": "Firma Seç",
        }

    def __init__(self, *args, **kwargs):
        super(ArizaGönder, self).__init__(*args, **kwargs)
        self.fields['firma_bilgi'].required = False

    def __init__(self, *args, **kwargs):
        super(ArizaGönder, self).__init__(*args, **kwargs)
        self.fields['gelenAciklama'].required = True

    def get_info(self):
        """
        Method that returns formatted information
        :return: subject, msg
        """
        # Cleaned dataaa

        cl_data = super().clean()

        gelenAdSoyad = cl_data.get('gelenAdSoyad')
        gelenMail = cl_data.get('gelenMail')
        gelenKonu = cl_data.get('gelenKonu')
        print(gelenKonu)

        msg = f' Ad Soyad: {gelenAdSoyad}\n Mail: {gelenMail} \n Konu: '
        msg += f'"{gelenKonu}"\n\n Mesaj:'
        msg += cl_data.get('gelenAciklama')

        return gelenKonu, msg

    def bizeMail(self):

        gelenKonu, msg = self.get_info()
        print(gelenKonu)
        send_mail(
            gelenKonu,
            message=msg,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.RECIPIENT_ADDRESS],
            fail_silently=True,
        )

    def get_inf(self):
        """
        Method that returns formatted information
        :return: subject, msg
        """
        # Cleaned data

        cl_data = super().clean()

        gelenAdSoyad = cl_data.get('gelenAdSoyad')
        gelenMail = cl_data.get('gelenMail')
        gelenKonu = cl_data.get('gelenKonu')
        print(gelenKonu)

        msg2 = f'Merhaba {gelenAdSoyad},\n\n'
        msg2 += f'Aksiyon Teknoloji ariza bilgidirim formunuz alınmıştır.\n\n'
        msg2 += f'Sizelere en kısa sürede dönüş yapacağız \n\n'
        msg2 += f'Saygılarımızla'

        return msg2, gelenMail

    def karsiMail(self):

        msg2, gelenMail,  = self.get_inf()
        subject = "Aksiyon Teknoloji Teknik"
        send_mail(
            subject,
            message=msg2,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[gelenMail],
            fail_silently=True,
        )

########################## MAil ###################


class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Paylasim
        fields = "__all__"
        error_messages = {

            "gönderiKonu": {
                "required": "Konu Giriniz",
            },
            "gönderiAciklama": {
                "required": "Açıklama Giriniz",
            },
            "gönderiFoto": {
                "required": "Açıklama Giriniz",
            },

        }
        labels = {
            "göndericiAdi": "Gönderici Adı",
            "gönderiKonu": "Konu",
            "gönderiFoto": "Görsel Ekleyiniz",
            "gönderiDurumu": "Paylaşımınız yayınlansın mı ?",
            "yazılımUrunumu": "Yazılım sayfası altında mı yayınlansın ?",
            "cameUrunumu": "Came sayfası altında mı yayınlansın ?",
            "sssmi": "S.S.S. sayfası altında mı yayınlansın ?",
            "category": "Hangi kategori altında yayınlansın ?",
            "gönderiAciklama": "Bir açıklama Giriniz",
        }
        widgets = {
            "göndericiAdi": widgets.TextInput(attrs={"class": "form-control"}),
            "gönderiKonu": widgets.TextInput(attrs={"class": "form-control"}),
            "gönderiFoto": widgets.FileInput(attrs={"class": "form-control"}),
            "gönderiDurumu": widgets.NullBooleanSelect(attrs={"class": "form-control"}),
            "yazılımUrunumu": widgets.NullBooleanSelect(attrs={"class": "form-control"}),
            "cameUrunumu": widgets.NullBooleanSelect(attrs={"class": "form-control"}),
            "sssmi": widgets.NullBooleanSelect(attrs={"class": "form-control"}),
            "category": widgets.Select(attrs={"class": "form-control"}),
            "gönderiAciklama": widgets.Textarea(attrs={
                'class': 'form-control django-ckeditor-widget ckeditor',
                'id': 'form-control',
                'spellcheck': 'False'}),

        }

    def __init__(self, *args, **kwargs):
        super(ProductCreateForm, self).__init__(*args, **kwargs)
        self.fields['category'].required = True

    def __init__(self, *args, **kwargs):
        super(ProductCreateForm, self).__init__(*args, **kwargs)
        self.fields['göndericiAdi'].required = True

    def __init__(self, *args, **kwargs):
        super(ProductCreateForm, self).__init__(*args, **kwargs)
        self.fields['gönderiKonu'].required = True


class ArizaCevapForm(forms.ModelForm):
    class Meta:
        model = Ariza
        fields = ['CozumVarMı']


class ArizaArsiv(forms.ModelForm):
    class Meta:
        model = Ariza
        fields = ['Arsivmi']
        Arsivmi = True


class FirmaGönder(forms.ModelForm):
    class Meta:
        model = Firma
        fields = ['FirmaName']

        labels = {
            "FirmaName": "Firma Adı Giriniz",
        }
        widgets = {
            "FirmaName": widgets.TextInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
        }

    def __init__(self, *args, **kwargs):
        super(FirmaGönder, self).__init__(*args, **kwargs)
        self.fields['FirmaName'].required = False


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('yorum',)
        labels = {
            "yorum": "Uygulanan çözümü ayrıntılı yazmayı unutmayınız",
        }
        widgets = {
            "yorum": widgets.Textarea(attrs={"class": "form-control", "placeholder": "test"}),
        }

class KesifForm(forms.ModelForm):
    class Meta:
        model = Kesif
        fields = [
            "kesifYapilanYerAdi",
            "kesifYapanKisi",
            "kesifSenaryosu",
            "kesifPTSVarMi",
            "kesifOlayVarMi",
            "kesifCctvVarMi",
            ]
        exclude = [
            "kesifPTSKameraSayisi",
            "kesifOnaylandiMi",
            "kesifArsivMi",
            "kesifPTSDirekSayisi",
            "kesifPTSSwitchSayisi",
            "kesifPTSBigisayarConfigi",
        ]
        labels={
            "kesifYapilanYerAdi":"Keşif yapılan yerin adını:",
            "kesifYapanKisi":"Keşif yapan kişi-kişiler:",
            "kesifSenaryosu":"Keşif Senaryosunu giriniz",
            "kesifPTSVarMi":"PTS var mı?",
            "kesifOlayVarMi":"OAS var mı ?",
            "kesifCctvVarMi":"CC-TV var mı ?",

        }
        widgets={
            "kesifYapilanYerAdi":widgets.TextInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifYapanKisi":widgets.TextInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifSenaryosu":widgets.Textarea(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifPTSVarMi":widgets.NullBooleanSelect(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifOlayVarMi":widgets.NullBooleanSelect(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifCctvVarMi":widgets.NullBooleanSelect(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),

        }


class KesifPTSMalzemeForm(forms.ModelForm):

    class Meta:
        model = KesifPTSMalzeme
        fields = "__all__"
        exclude = [
            'kesifPTSyeradi'
        ]
        # labels={
        #     "kesifKameraSayisi":"Kaç kamera kullanılacak ???",
        #     "kesifDirekSayisi":"Kaç direk kullanılacak ?",
        #     "kesifDirekUzunlugu":"Direk uzunluğu kaç metre ?",
        #     "kesifAdaptorSayisi":"Kaç adaptör kullanılacak ?",
        # }

        widgets={
            "kesifPTSKameraSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri",'required': False}),
            "kesifPTSKameraBoatSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifPTSKameraAdaptorSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifPTSExtraKameraAdaptorSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifPTSKameraTipi":widgets.Select(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifPTSExtraKameraSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifPTSExtraKameraTipi":widgets.Select(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifPTSDirekSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifPTSDirekUzunlugu":widgets.TextInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifPTSFlanshSayisi":widgets.Select(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifPTSDirekAçıklama":widgets.Textarea(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifPTSAdaptorSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifPTSSwitchPortSayisi":widgets.Select(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifPTSSwitchSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifPTSSwitchPoeMi":widgets.NullBooleanSelect(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifPTSBilgisayarConfigi":widgets.TextInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifPTSBilgisayarSayısı":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifPTSIoKartSayısı":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifPTSIoKartTipi":widgets.Select(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifPTSIoKartModulSayısı":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifPTSIoKartAdaptorSayısı":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifPTSPanoTipi":widgets.Select(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifPTSPanoOlcusu":widgets.TextInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifPTSPanoSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifPTSCAT6kablometre":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifPTSEnerjikablometre":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifPTSEnerjikabloTipi":widgets.Select(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifPTSDT8kablometre":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifPTSSpiralÇapı":widgets.TextInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifPTSSpiralMetre":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifPTSFiberVarMi":widgets.NullBooleanSelect(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifPTSFiberMetre":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifPTSPatchPanelTipi":widgets.TextInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifPTSPatchPanelSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifPTSBariyerModeli":widgets.Select(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifPTSBariyerSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifPTSBariyerKolBoyu":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),

            "kesifPTSMantarBariyerAciklama":widgets.Textarea(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            

            "kesifPTSLoopDedektorSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifPTSLoopTrafoSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifPTSLoopKabloCesidi":widgets.Select(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifPTSLoopKabloMetresi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),


            "kesifPTSLedEkranModeli":widgets.TextInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifPTSLedEkranSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            
            "kesifPTSFiberMetre":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifPTSFiberKabloModeli":widgets.Select(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),

            "kesifPTSPatchPanelSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifPTSPatchPanelTipi":widgets.Select(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            
            "kesifPTSPatchPanelEkKasetSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifPTSPatchCordSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifPTSPatchCordTipi":widgets.Select(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),

            "kesifPTSFiberAdaptorSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifPTSFiberAdaptorTipi":widgets.Select(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),

            "kesifPTSCibikModuleSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),


        }
class KesifOlayMalzemeForm(forms.ModelForm):
    class Meta:
        model = KesifOlayMalzeme
        fields = "__all__"
        exclude = [
            'kesifOlayyeradi'
        ]
        widgets={         
            "kesifOlayKameraSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri",'required': False}),
            "kesifOlayKameraBoatSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifOlayKameraAdaptorSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifOlayExtraKameraAdaptorSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifOlayKameraTipi":widgets.Select(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifOlayExtraKameraSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifOlayExtraKameraTipi":widgets.Select(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifOlayDirekSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifOlayDirekUzunlugu":widgets.TextInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifOlayFlanshSayisi":widgets.Select(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifOlayDirekAçıklama":widgets.Textarea(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifOlayAdaptorSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifOlaySwitchPortSayisi":widgets.Select(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifOlaySwitchSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifOlaySwitchPoeMi":widgets.NullBooleanSelect(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifOlayBilgisayarConfigi":widgets.TextInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifOlayBilgisayarSayısı":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifOlayIoKartSayısı":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifOlayIoKartTipi":widgets.Select(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifOlayIoKartModulSayısı":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifOlayIoKartAdaptorSayısı":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifOlayPanoTipi":widgets.Select(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifOlayPanoOlcusu":widgets.TextInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifOlayPanoSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifOlayCAT6kablometre":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifOlayEnerjikablometre":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifOlayEnerjikabloTipi":widgets.Select(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifOlayDT8kablometre":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifOlaySpiralÇapı":widgets.TextInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifOlaySpiralMetre":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifOlayFiberVarMi":widgets.NullBooleanSelect(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifOlayFiberMetre":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifOlayPatchPanelTipi":widgets.TextInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifOlayPatchPanelSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifOlayBariyerModeli":widgets.Select(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifOlayBariyerSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifOlayBariyerKolBoyu":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifOlayMantarBariyerAciklama":widgets.Textarea(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}), 
            "kesifOlayLoopDedektorSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifOlayLoopTrafoSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifOlayLoopKabloCesidi":widgets.Select(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifOlayLoopKabloMetresi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifOlayLedEkranModeli":widgets.TextInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifOlayLedEkranSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),            
            "kesifOlayFiberMetre":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifOlayFiberKabloModeli":widgets.Select(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifOlayPatchPanelSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifOlayPatchPanelTipi":widgets.Select(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),           
            "kesifOlayPatchPanelEkKasetSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifOlayPatchCordSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifOlayPatchCordTipi":widgets.Select(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifOlayFiberAdaptorSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifOlayFiberAdaptorTipi":widgets.Select(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifOlayCibikModuleSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
  
        }
class KesifCCTVMalzemeForm(forms.ModelForm):
    class Meta:
        model = KesifCCTVMalzeme
        fields = "__all__"
        exclude = [
            'kesifCCTVyeradi'
        ]
        widgets={         
            "kesifCCTVKameraSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri",'required': False}),
            "kesifCCTVKameraBoatSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifCCTVKameraAdaptorSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifCCTVExtraKameraAdaptorSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifCCTVKameraTipi":widgets.TextInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifCCTVExtraKameraSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifCCTVExtraKameraTipi":widgets.Select(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifCCTVDirekSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifCCTVDirekUzunlugu":widgets.TextInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifCCTVFlanshSayisi":widgets.Select(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifCCTVDirekAçıklama":widgets.Textarea(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifCCTVAdaptorSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifCCTVSwitchPortSayisi":widgets.Select(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifCCTVSwitchSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifCCTVSwitchPoeMi":widgets.NullBooleanSelect(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifCCTVBilgisayarConfigi":widgets.TextInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifCCTVBilgisayarSayısı":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifCCTVIoKartSayısı":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifCCTVIoKartTipi":widgets.Select(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifCCTVIoKartModulSayısı":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifCCTVIoKartAdaptorSayısı":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifCCTVPanoTipi":widgets.Select(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifCCTVPanoOlcusu":widgets.TextInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifCCTVPanoSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifCCTVCCTVkablometre":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifCCTVCCTVkabloTipi":widgets.Select(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifCCTVEnerjikablometre":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifCCTVEnerjikabloTipi":widgets.Select(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifCCTVDT8kablometre":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifCCTVSpiralÇapı":widgets.TextInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifCCTVSpiralMetre":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            
            "kesifCCTVKayitCihaziSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifCCTVKayitCihaziModeli":widgets.Select(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifCCTVKayitCihaziHDDTeraByte":widgets.TextInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),

        }

class ImageForm(forms.ModelForm):
    class Meta:
        model = ImageKesif
        fields=('kesifImage',)
        labels ={
            "kesifImage":"Keşifte Çekilen Fotoğrafları Ekleyiniz."
        }
        widgets={
            "imageLabel":"Fotoğraları Ekleyiniz",
            "kesifImage":widgets.FileInput(attrs={"multiple":True, "class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
        }