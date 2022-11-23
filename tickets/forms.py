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
            "kesifYapilanYerAdi":"Keşif Yapılan Yerin Adını Yazınız:",
            "kesifYapanKisi":"Keşif Yapan Kişi-Kişileri Yazınız:",
            "kesifSenaryosu":"Keşif Senaryosunu Yazınız",
            "kesifPTSVarMi":"PTS var mı?",
            "kesifOlayVarMi":"OAS var mı ?",
            "kesifCctvVarMi":"CC-TV var mı ?",

        }
        widgets={
            "kesifYapilanYerAdi":widgets.TextInput(attrs={"class": "form-control", "placeholder": "Keşif Yapılan Yer. Örn; Cadde54"}),
            "kesifYapanKisi":widgets.TextInput(attrs={"class": "form-control", "placeholder": "İsminizi Giriniz. "}),
            "kesifSenaryosu":widgets.Textarea(attrs={"class": "form-control", "placeholder": "Keşif Senaryosunu Yazınız. "}),
            "kesifPTSVarMi":widgets.NullBooleanSelect(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifOlayVarMi":widgets.NullBooleanSelect(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifCctvVarMi":widgets.NullBooleanSelect(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),

        }
        error_messages={
            "kesifYapilanYerAdi":{
                "required":"Kesif yapılan yer ismi girilmesi zorunludur.",
            }
        }

        help_texts = {
            'kesifYapilanYerAdi': 'Group to which this message belongs to',
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
        labels = {
            "kesifPTSKameraSayisi": "Pts Kamera Sayısı Kaçtır",
            "kesifPTSKameraBoatSayisi":"Boat Sayısı Kaçtır",
            "kesifPTSKameraAdaptorSayisi":"Kamera Adaptör Sayısı Kaçtır",
            "kesifPTSExtraKameraAdaptorSayisi":"Extra Kamera Adaptör Sayısı Kaçtır",
            "kesifPTSKameraTipi":"Kamera Tipi Hangisidir",
            "kesifPTSExtraKameraSayisi":"Extra Kamera Sayısı Kaçtır",
            "kesifPTSExtraKameraTipi":"Kamera Tipi Nedir",
            "kesifPTSDirekSayisi":"Kullanılacak Direk Sayısı Kaçtır",
            "kesifPTSDirekUzunlugu":"Direk Uzunluğu Kaç Metredir",
            "kesifPTSFlanshSayisi":"Flansh Sayısı Kaçtır",
            "kesifPTSAdaptorSayisi":"Adaptör Sayısı Kaçtır",
            "kesifPTSDirekAçıklama":"Direkteki Extra Durum Nedir",
            "kesifPTSSwitchPortSayisi":"Switch Port Sayısı Kaçtır",
            "kesifPTSSwitchSayisi" :"Switch Sayısı Kaçtır",
            "kesifPTSSwitchPoeMi":"Switch Poe mi",
            "kesifPTSBilgisayarConfigi":"Bilgisayarda İstenen Özellikler Nelerdir",
            "kesifPTSBilgisayarSayısı":"Bilgisayar Sayısı Kaçtır",
            "kesifPTSIoKartSayısı":"IO Kart Sayısı Kaçtır",
            "kesifPTSIoKartTipi":"IO Kart Tipi Nedir",
            "kesifPTSIoKartModulSayısı":"IO Kart Modül Sayısı Kaçtır",
            "kesifPTSIoKartAdaptorSayısı":"IO Kart Adaptör Sayısı Kaçtır",
            "kesifPTSPanoTipi":"Pano Tipi Nedir",
            "kesifPTSPanoOlcusu":"Pano Ölçüsü Nedir",
            "kesifPTSPanoSayisi":"Pano Sayısı Kaçtır",
            "kesifPTSCAT6kablometre":"CAT 6 Kablosu Kaç Metredir",
            "kesifPTSEnerjikablometre":"Enerji Kablosu Kaç Metredir",
            "kesifPTSEnerjikabloTipi":"Enerji Kablo Tipi Nediri",
            "kesifPTSDT8kablometre":"DT8 Kablosu Kaç Metredir",
            "kesifPTSSpiralÇapı":"Spiral Çapı Nedir",
            "kesifPTSSpiralMetre":"Spiral Kaç Metredir",
            "kesifPTSFiberVarMi":"Fiber Kullanılacak mı",
            "kesifPTSFiberMetre":"Fiber Kablosu Kaç Metredir",
            "kesifPTSPatchPanelTipi":"Patch Panel Tipi Nedir",
            "kesifPTSPatchPanelSayisi":"Patch Panel Sayısı Nedir",
            "kesifPTSBariyerModeli":"Bariyer Modeli Nedir",
            "kesifPTSBariyerSayisi":"Bariyer Sayısı Kaçtır",
            "kesifPTSBariyerKolBoyu":"Bariyer Kol Boyu Kaç Metredir",
            "kesifPTSMantarBariyerAciklama":"Bariyer Hakkında Özel Bilgilendirme",
            "kesifPTSLoopDedektorSayisi":"Loop Dedektör Sayısı Kaçtır",
            "kesifPTSLoopTrafoSayisi":"Trafo Sayısı Kaçtır",
            "kesifPTSLoopKabloCesidi":"Loop Dedektör Kablo Çeşidi Nedir",
            "kesifPTSLoopKabloMetresi":"Loop Dedektör Kablosu Kaç Metredir",
            "kesifPTSLedEkranModeli":"Led Ekran Modeli Nedir",
            "kesifPTSLedEkranSayisi":"Led Ekran Sayısı Kaçtır",
            "kesifPTSFiberMetre":"Fiber Kablosu Kaç Metredir",
            "kesifPTSFiberKabloModeli":"Fiber Kablo Modeli Nedir",
            "kesifPTSPatchPanelSayisi":"Patch Panel Sayısı Nedir",
            "kesifPTSPatchPanelTipi":"Patch Panel Tipi Nedir",
            "kesifPTSPatchPanelEkKasetSayisi":"Extra Kaset Sayısı Nedir",
            "kesifPTSPatchCordSayisi":"Patch Cord Sayısı Nedir",
            "kesifPTSPatchCordTipi":"Patch Cord Tipi Nedir",
            "kesifPTSFiberAdaptorSayisi":"Fiber Adaptör Sayısı Kaçtır",
            "kesifPTSFiberAdaptorTipi":"Fiber Adaptör Tipi Nedir",
            "kesifPTSCibikModuleSayisi":"Cibik Modül Sayısı Kaçtır",
        }

        widgets={
            "kesifPTSKameraSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Kamera Sayısı Giriniz. ",'required': False}),
            "kesifPTSKameraBoatSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Boat Sayısı Giriniz. "}),
            "kesifPTSKameraAdaptorSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Adaptör Sayısı Giriniz. "}),
            "kesifPTSExtraKameraAdaptorSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Adaptör Sayısı Giriniz. "}),
            "kesifPTSKameraTipi":widgets.Select(attrs={"class": "form-control", "placeholder": "Kamera Tipini Seçiniz. "}),
            "kesifPTSExtraKameraSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Kamera Sayısı Giriniz. "}),
            "kesifPTSExtraKameraTipi":widgets.Select(attrs={"class": "form-control", "placeholder": "Kamera Tipini Seçiniz. "}),
            "kesifPTSDirekSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Direk Sayısı Giriniz. "}),
            "kesifPTSDirekUzunlugu":widgets.TextInput(attrs={"class": "form-control", "placeholder": "Direk Uzunluğu Giriniz. "}),
            "kesifPTSFlanshSayisi":widgets.Select(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifPTSDirekAçıklama":widgets.Textarea(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifPTSAdaptorSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Adaptör Sayısı Giriniz. "}),
            "kesifPTSSwitchPortSayisi":widgets.Select(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifPTSSwitchSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Switch Sayısını Giriniz. "}),
            "kesifPTSSwitchPoeMi":widgets.NullBooleanSelect(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifPTSBilgisayarConfigi":widgets.TextInput(attrs={"class": "form-control", "placeholder": "Bilgisayar Özelliği Giriniz. Örn; İ5 7.nesil"}),
            "kesifPTSBilgisayarSayısı":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Bilgisayar Sayısı Giriniz. "}),
            "kesifPTSIoKartSayısı":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "IO Kart Sayısı Giriniz. "}),
            "kesifPTSIoKartTipi":widgets.Select(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifPTSIoKartModulSayısı":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "IO Kart Modül Sayısı Giriniz. "}),
            "kesifPTSIoKartAdaptorSayısı":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "IO Kart Adaptör Sayısı Giriniz. "}),
            "kesifPTSPanoTipi":widgets.Select(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifPTSPanoOlcusu":widgets.TextInput(attrs={"class": "form-control", "placeholder": "Pano Ölçüsü Giriniz. Örn; 45x15x25 "}),
            "kesifPTSPanoSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Pano Sayısını Giriniz. "}),
            "kesifPTSCAT6kablometre":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Metraj Giriniz. "}),
            "kesifPTSEnerjikablometre":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Metraj Giriniz. "}),
            "kesifPTSEnerjikabloTipi":widgets.Select(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifPTSDT8kablometre":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Metraj Giriniz. "}),
            "kesifPTSSpiralÇapı":widgets.TextInput(attrs={"class": "form-control", "placeholder": "Spiral Çapı Giriniz. Örn; 32mm"}),
            "kesifPTSSpiralMetre":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Metraj Giriniz. "}),
            "kesifPTSFiberVarMi":widgets.NullBooleanSelect(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifPTSFiberMetre":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Metraj Giriniz. "}),
            "kesifPTSPatchPanelTipi":widgets.TextInput(attrs={"class": "form-control", "placeholder": "Panel Tipi Seçiniz. "}),
            "kesifPTSPatchPanelSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifPTSBariyerModeli":widgets.Select(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifPTSBariyerSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Bariyer Sayısı Giriniz. "}),
            "kesifPTSBariyerKolBoyu":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Bariyer Kol Boyu Giriniz. "}),

            "kesifPTSMantarBariyerAciklama":widgets.Textarea(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            

            "kesifPTSLoopDedektorSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Loop Dedektör Sayısı Giriniz. "}),
            "kesifPTSLoopTrafoSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Loop Trafo Sayısı Giriniz. "}),
            "kesifPTSLoopKabloCesidi":widgets.Select(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifPTSLoopKabloMetresi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Metraj Giriniz. "}),


            "kesifPTSLedEkranModeli":widgets.TextInput(attrs={"class": "form-control", "placeholder": "Led Ekran Modeli Giriniz. "}),
            "kesifPTSLedEkranSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Led Ekran Sayısı Giriniz. "}),
            
            "kesifPTSFiberMetre":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Metraj Giriniz. "}),
            "kesifPTSFiberKabloModeli":widgets.Select(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),

            "kesifPTSPatchPanelSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Panel Sayısını Giriniz. "}),
            "kesifPTSPatchPanelTipi":widgets.Select(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            
            "kesifPTSPatchPanelEkKasetSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Panel Kaset Sayısnı Giriniz. "}),
            "kesifPTSPatchCordSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder":"Patch Cord Sayısını Giriniz. "}),
            "kesifPTSPatchCordTipi":widgets.Select(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),

            "kesifPTSFiberAdaptorSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Adaptör Sayısı Giriniz. "}),
            "kesifPTSFiberAdaptorTipi":widgets.Select(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),

            "kesifPTSCibikModuleSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Cibik Modül Sayısı Giriniz. "}),


        }
class KesifOlayMalzemeForm(forms.ModelForm):
    class Meta:
        model = KesifOlayMalzeme
        fields = "__all__"
        exclude = [
            'kesifOlayyeradi'
        ]
        labels = {
        "kesifOlayKameraSayisi": "Olay Algılama Kamera Sayısı Kaçtır",
        "kesifOlayKameraBoatSayisi":"Boat Sayısı Kaçtır",
        "kesifOlayKameraAdaptorSayisi":"Kamera Adaptör Sayısı Kaçtır",
        "kesifOlayExtraKameraAdaptorSayisi":"Extra Kamera Adaptör Sayısı Kaç Olacak",
        "kesifOlayKameraTipi":"Kamera Tipi Hangisidir.",
        "kesifOlayExtraKameraSayisi":"Extra Kamera Sayısı Kaçtır",
        "kesifOlayExtraKameraTipi":"Kamera Tipi Nedir",
        "kesifOlayDirekSayisi":"Kullanılacak Direk Sayısı Kaçtır",
        "kesifOlayDirekUzunlugu":"Direk Uzunluğu Kaç Metre",
        "kesifOlayFlanshSayisi":"Flansh Sayısı Kaç",
        "kesifOlayDirekAçıklama":"Direkteki Extra Durum Nedir",
        "kesifOlayAdaptorSayisi":"Adaptör Sayısı Kaçtır",
        "kesifOlaySwitchPortSayisi":"Switch Port Sayısı Kaçtır",
        "kesifOlaySwitchSayisi":"Switch Sayısı Kaçtır",
        "kesifOlaySwitchPoeMi":"Switch Poe mi",
        "kesifOlayBilgisayarConfigi":"Bilgisayarda İstenen Özellikler Nelerdir",
        "kesifOlayBilgisayarSayısı":"Bilgisayar Sayısı Kaçtır",
        "kesifOlayIoKartSayısı":"IO Kart Sayısı Kaçtır",
        "kesifOlayIoKartTipi":"IO Kart Tipi Nedir",
        "kesifOlayIoKartModulSayısı":"IO Kart Modül Sayısı Kaçtır",
        "kesifOlayIoKartAdaptorSayısı":"IO Kart Adaptör Sayısı Kaçtır",
        "kesifOlayPanoTipi":"Pano Tipi Nedir",
        "kesifOlayPanoOlcusu":"Pano Ölçüsü Nedir",
        "kesifOlayPanoSayisi":"Pano Sayısı Kaçtır",
        "kesifOlayCAT6kablometre":"CAT 6 Kablosu Kaç Metredir",
        "kesifOlayEnerjikablometre":"Enerji Kablosu Kaç Metredir",
        "kesifOlayEnerjikabloTipi":"Enerji Kablo Tipi Nedir",
        "kesifOlayDT8kablometre":"DT8 Kablosu Kaç Metredir",
        "kesifOlaySpiralÇapı":"Spiral Çapı Nedir",
        "kesifOlaySpiralMetre":"Spiral Kaç Metredir",
        "kesifOlayFiberVarMi":"Fiber Kullanılacak mı",
        "kesifOlayFiberMetre":"Fiber Kablosu Kaç Metredir",
        "kesifOlayBariyerModeli":"Bariyer Modeli Nedir",
        "kesifOlayBariyerSayisi":"Bariyer Sayısı Kaçtır",
        "kesifOlayBariyerKolBoyu":"Bariyer Kol Boyu Kaç Metredir",
        "kesifOlayMantarBariyerAciklama":"Bariyer Hakkında Özel Bilgilendirme",
        "kesifOlayLoopDedektorSayisi":"Loop Dedektör Sayısı Kaçtır",
        "kesifOlayLoopTrafoSayisi":"Trafo Sayısı Kaçtır",
        "kesifOlayLoopKabloCesidi":"Loop Dedektör Kablo Çeşidi Nedir",
        "kesifOlayLoopKabloMetresi":"Loop Dedektör Kablo Kaç Metredir",
        "kesifOlayLedEkranModeli":"Led Ekran Modeli Nedir",
        "kesifOlayLedEkranSayisi":"Led Ekran Sayısı Kaçtır", 
        "kesifOlayFiberMetre":"Fiber Kablosu Kaç Metredir",
        "kesifOlayFiberKabloModeli":"Fiber Kablo Modeli Nedir",
        "kesifOlayPatchPanelSayisi":"Patch Panel Sayısı Nedir",
        "kesifOlayPatchPanelTipi": "Patch Panel Tipi Nedir",
        "kesifOlayPatchPanelEkKasetSayisi":"Extra Kaset Sayısı Nedir",
        "kesifOlayPatchCordSayisi":"Patch Cord Sayısı Nedir",
        "kesifOlayPatchCordTipi":"Patch Cord Tipi Nedir",
        "kesifOlayFiberAdaptorSayisi":"Fiber Adaptör Sayısı Kaçtır",
        "kesifOlayFiberAdaptorTipi":"Fiber Adaptör Tipi Nedir",
        "kesifOlayCibikModuleSayisi": "Cibik Modül Sayısı Kaçtır",
           }
        widgets={         
            "kesifOlayKameraSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Kamera Sayısı Giriniz. ",'required': False}),
            "kesifOlayKameraBoatSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Boat Sayısı Giriniz. "}),
            "kesifOlayKameraAdaptorSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Adaptör Sayısı Giriniz. "}),
            "kesifOlayExtraKameraAdaptorSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Adaptör Sayısı Giriniz. "}),
            "kesifOlayKameraTipi":widgets.Select(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifOlayExtraKameraSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Kamera Sayısı Giriniz. "}),
            "kesifOlayExtraKameraTipi":widgets.Select(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifOlayDirekSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Direk Sayısı Giriniz. "}),
            "kesifOlayDirekUzunlugu":widgets.TextInput(attrs={"class": "form-control", "placeholder": "Direk Uzunluğu Giriniz. "}),
            "kesifOlayFlanshSayisi":widgets.Select(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifOlayDirekAçıklama":widgets.Textarea(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifOlayAdaptorSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Adaptör Sayısı Giriniz. "}),
            "kesifOlaySwitchPortSayisi":widgets.Select(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifOlaySwitchSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Switch Sayısını Giriniz. "}),
            "kesifOlaySwitchPoeMi":widgets.NullBooleanSelect(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifOlayBilgisayarConfigi":widgets.TextInput(attrs={"class": "form-control", "placeholder": "Bilgisayar Özelliği Giriniz. Örn; İ5 7.nesil"}),
            "kesifOlayBilgisayarSayısı":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Bilgisayar Sayısı Giriniz. "}),
            "kesifOlayIoKartSayısı":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "IO Kart Sayısı Giriniz. "}),
            "kesifOlayIoKartTipi":widgets.Select(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifOlayIoKartModulSayısı":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "IO Kart Modül Sayısı Giriniz. "}),
            "kesifOlayIoKartAdaptorSayısı":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "IO Kart Adaptör Sayısı Giriniz. "}),
            "kesifOlayPanoTipi":widgets.Select(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifOlayPanoOlcusu":widgets.TextInput(attrs={"class": "form-control", "placeholder": "Pano Ölçüsü Giriniz. Örn; 45x15x25"}),
            "kesifOlayPanoSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Pano Sayısını Giriniz. "}),
            "kesifOlayCAT6kablometre":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Metraj Giriniz. "}),
            "kesifOlayEnerjikablometre":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Metraj Giriniz. "}),
            "kesifOlayEnerjikabloTipi":widgets.Select(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifOlayDT8kablometre":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Metraj Giriniz. "}),
            "kesifOlaySpiralÇapı":widgets.TextInput(attrs={"class": "form-control", "placeholder": "Spiral Çapı Giriniz. Örn; 32mm "}),
            "kesifOlaySpiralMetre":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Metraj Giriniz. "}),
            "kesifOlayFiberVarMi":widgets.NullBooleanSelect(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifOlayFiberMetre":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Metraj Giriniz. "}),
            "kesifOlayBariyerModeli":widgets.Select(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifOlayBariyerSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Bariyer Sayısı Giriniz. "}),
            "kesifOlayBariyerKolBoyu":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Bariyer Kol Boyu Giriniz. "}),
            "kesifOlayMantarBariyerAciklama":widgets.Textarea(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}), 
            "kesifOlayLoopDedektorSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Loop Dedektör Sayısı Giriniz. "}),
            "kesifOlayLoopTrafoSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Loop Trafo Sayısı Giriniz. "}),
            "kesifOlayLoopKabloCesidi":widgets.Select(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifOlayLoopKabloMetresi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Metraj Giriniz. "}),
            "kesifOlayLedEkranModeli":widgets.TextInput(attrs={"class": "form-control", "placeholder": "Led Ekran Modeli Giriniz. "}),
            "kesifOlayLedEkranSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Led Ekran Sayısı Giriniz. "}),            
            "kesifOlayFiberMetre":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Metraj Giriniz. "}),
            "kesifOlayFiberKabloModeli":widgets.Select(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifOlayPatchPanelSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Panel Sayısını Giriniz. "}),
            "kesifOlayPatchPanelTipi":widgets.Select(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),           
            "kesifOlayPatchPanelEkKasetSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Panel Kaset Sayısnı Giriniz. "}),
            "kesifOlayPatchCordSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Patch Cord Sayısını Giriniz. "}),
            "kesifOlayPatchCordTipi":widgets.Select(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifOlayFiberAdaptorSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Adaptör Sayısı Giriniz. "}),
            "kesifOlayFiberAdaptorTipi":widgets.Select(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifOlayCibikModuleSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Cibik Modül Sayısı Giriniz. "}),
  
        }
class KesifCCTVMalzemeForm(forms.ModelForm):
    class Meta:
        model = KesifCCTVMalzeme
        fields = "__all__"
        exclude = [
            'kesifCCTVyeradi'
        ]
        labels={
            "kesifCCTVKameraSayisi":"CCTV Kamera Sayısı Kaçtır",
            "kesifCCTVKameraBoatSayisi":"Boat Sayısı Kaçtır",
            "kesifCCTVKameraAdaptorSayisi":"Kamera Adaptör Sayısı Kaçtır",
            "kesifCCTVExtraKameraAdaptorSayisi":"Extra Kamera Adaptör Sayısı Kaçtır",
            "kesifCCTVKameraTipi":"Kamera Tipi Hangisidir.",
            "kesifCCTVExtraKameraSayisi":"Extra Kamera Sayısı Kaçtır",
            "kesifCCTVExtraKameraTipi":"Kamera Tipi Nedir",
            "kesifCCTVDirekSayisi":"Kullanılacak Direk Sayısı Kaçtır",
            "kesifCCTVDirekUzunlugu":"Direk Uzunluğu Kaç Metredir",
            "kesifCCTVFlanshSayisi":"Flansh Sayısı Kaçtır",
            "kesifCCTVDirekAçıklama":"Direkteki Extra Durum Nedir",
            "kesifCCTVAdaptorSayisi":"Adaptör Sayısı Kaçtır",
            "kesifCCTVSwitchPortSayisi":"Switch Port Sayısı Kaçtır",
            "kesifCCTVSwitchSayisi":"Switch Sayısı Kaçtır",
            "kesifCCTVSwitchPoeMi":"Switch Poe mi",
            "kesifCCTVBilgisayarConfigi":"Bilgisayarda İstenen Özellikler Nelerdir",
            "kesifCCTVBilgisayarSayısı":"Bilgisayar Sayısı Kaçtır",
            "kesifCCTVIoKartSayısı":"IO Kart Sayısı Kaçtır",
            "kesifCCTVIoKartTipi":"IO Kart Tipi Nedir",
            "kesifCCTVIoKartModulSayısı":"IO Kart Modül Sayısı Kaçtır",
            "kesifCCTVIoKartAdaptorSayısı":"IO Kart Adaptör Sayısı Kaçtır",
            "kesifCCTVPanoTipi":"Pano Tipi Nedir",
            "kesifCCTVPanoOlcusu":"Pano Ölçüsü Nedir",
            "kesifCCTVPanoSayisi":"Pano Sayısı Kaçtır",
            "kesifCCTVCCTVkablometre":"CCTV Kablosu Kaç Metredir",
            "kesifCCTVCCTVkabloTipi":"CCTV Kablo Tipi Nedir",
            "kesifCCTVEnerjikablometre":"Enerji Kablosu Kaç Metredir",
            "kesifCCTVEnerjikabloTipi":"Enerji Kablo Tipi Nedir",
            "kesifCCTVDT8kablometre":"DT8 Kablosu Kaç Metredir",
            "kesifCCTVSpiralÇapı":"Spiral Çapı Nedir",
            "kesifCCTVSpiralMetre":"Spiral Kaç Metredir",
            "kesifCCTVKayitCihaziSayisi":"CCTV Kayıt Cihazı Kaç Adettir",
            "kesifCCTVKayitCihaziModeli":"Kayıt Cihaz Modeli Nedir",
            "kesifCCTVKayitCihaziHDDTeraByte":"Kayıt Cihazı Kaç TeraBytetır",


        }
        widgets={         
            "kesifCCTVKameraSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Kamera Sayısı Giriniz. ",'required': False}),
            "kesifCCTVKameraBoatSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Boat Sayısı Giriniz. "}),
            "kesifCCTVKameraAdaptorSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Adaptör Sayısı Giriniz. "}),
            "kesifCCTVExtraKameraAdaptorSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Adaptör Sayısı Giriniz. "}),
            "kesifCCTVKameraTipi":widgets.TextInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifCCTVExtraKameraSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Kamera Sayısı Giriniz. "}),
            "kesifCCTVExtraKameraTipi":widgets.Select(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifCCTVDirekSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Direk Sayısı Giriniz. "}),
            "kesifCCTVDirekUzunlugu":widgets.TextInput(attrs={"class": "form-control", "placeholder": "Direk Uzunluğu Giriniz. "}),
            "kesifCCTVFlanshSayisi":widgets.Select(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifCCTVDirekAçıklama":widgets.Textarea(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifCCTVAdaptorSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Adaptör Sayısı Giriniz. "}),
            "kesifCCTVSwitchPortSayisi":widgets.Select(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifCCTVSwitchSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Switch Sayısını Giriniz. "}),
            "kesifCCTVSwitchPoeMi":widgets.NullBooleanSelect(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifCCTVBilgisayarConfigi":widgets.TextInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifCCTVBilgisayarSayısı":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Bilgisayar Sayısı Giriniz. "}),
            "kesifCCTVIoKartSayısı":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "IO Kart Sayısı Giriniz. "}),
            "kesifCCTVIoKartTipi":widgets.Select(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifCCTVIoKartModulSayısı":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "IO Kart Modül Sayısı Giriniz. "}),
            "kesifCCTVIoKartAdaptorSayısı":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "IO Kart Adaptör Sayısı Giriniz. "}),
            "kesifCCTVPanoTipi":widgets.Select(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifCCTVPanoOlcusu":widgets.TextInput(attrs={"class": "form-control", "placeholder": "Pano Ölçüsü Giriniz. Örn; 45x15x25"}),
            "kesifCCTVPanoSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Pano Sayısını Giriniz. "}),
            "kesifCCTVCCTVkablometre":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Metraj Giriniz. "}),
            "kesifCCTVCCTVkabloTipi":widgets.Select(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifCCTVEnerjikablometre":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Metraj Giriniz. "}),
            "kesifCCTVEnerjikabloTipi":widgets.Select(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifCCTVDT8kablometre":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Metraj Giriniz. "}),
            "kesifCCTVSpiralÇapı":widgets.TextInput(attrs={"class": "form-control", "placeholder": "Spiral Çapı Giriniz. Örn; 32mm "}),
            "kesifCCTVSpiralMetre":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Metraj Giriniz. "}),
            
            "kesifCCTVKayitCihaziSayisi":widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Kayıt Cihazı Sayısı Giriniz. "}),
            "kesifCCTVKayitCihaziModeli":widgets.Select(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
            "kesifCCTVKayitCihaziHDDTeraByte":widgets.TextInput(attrs={"class": "form-control", "placeholder": "Boyutunu Giriniz. Örn; 1TB"}),

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