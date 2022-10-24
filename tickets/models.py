# from collections import UserList
# from datetime import date
# from email.policy import default
# from pickle import TRUE
# from sqlite3 import Timestamp
# from turtle import mode, ondrag, st, update
# from unicodedata import category
# from venv import create
# from webbrowser import get
# from xml.parsers.expat import model
# from xmlrpc.client import Boolean
# from django.conf import UserSettingsHolder
from email.policy import default
from unittest.util import _MAX_LENGTH
from xmlrpc.client import boolean
from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
# from PIL import Image
# from django.contrib.auth.models import User
# from django.db.models import Count
# from pkg_resources import safe_name
from django.contrib.auth import get_user_model
from django_userforeignkey.models.fields import UserForeignKey
# from django.core.mail import send_mail
# from django.conf import settings


User = get_user_model()


class Status(models.Model):
    name = models.CharField(max_length=100)

# gelenFoto/1.jpeg
# göndericiFoto/1.jpeg


class Firma(models.Model):
    FirmaName = models.CharField(max_length=100, null=True, blank=True)
    FirmaYetkilisi = models.CharField(max_length=50, null=True, blank=True)
    FirmaİletisimMail = models.CharField(max_length=50, null=True, blank=True)
    FirmaİletisimTelefon = models.CharField(
        max_length=50, null=True, blank=True)
    #FirmaSayısı = Ariza.objects.aggregate(total_count=Count('id'))

    slug = models.SlugField(null=False,
                            db_index=True, blank=True, editable=False)

    def __str__(self):
        return f"{self.FirmaName}"

    def save(self, *args, **kwargs):
        self.FirmaName = self.FirmaName.upper()
        self.slug = slugify(self.FirmaName)
        super().save(*args, **kwargs)


class Ariza(models.Model):

    gelenMail = models.CharField(max_length=50)
    #gelenFoto = models.ImageField(upload_to="Arizas")
    gelenAdSoyad = models.CharField(max_length=50)
    gelenTelefon = models.CharField(max_length=12)
    gelenKonu = models.CharField(max_length=50)
    gelenAciklama = models.TextField(max_length=2000)
    slug = models.SlugField(null=True,
                            db_index=True, blank=True, editable=False, unique=True)
    firma_bilgi = models.ForeignKey(
        Firma, null=True, on_delete=models.CASCADE, blank=True, default=35, editable=False)
    update_time = models.DateTimeField(auto_now_add=False, auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True, auto_now=False)
    CozumVarMı = models.BooleanField(default=False)
    Arsivmi = models.BooleanField(default=False)
    #gelenFirma = models.CharField(max_length=50, default="Belirtilmemiş")
    # slug = models.SlugField(null=True, unique=True, db_index=True)
    # önce null False olursa migrationda sorun çıkıyor önce true ile nullar doldurulup sonra false çevirilmeli

    def __str__(self):
        return f"{self.gelenAdSoyad}"

    def save(self, *args, **kwargs):
        super(Ariza, self).save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(self.gelenKonu) + "-" + str(self.id)
            self.save()


class Category(models.Model):
    categoryName = models.CharField(max_length=100, default="Genel")
    slug = models.SlugField(null=False, unique=True,
                            db_index=True, blank=True, editable=False)
    UrunTip = models.CharField(max_length=100, default="came")

    def __str__(self):
        return f"{self.categoryName}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.categoryName)
        super().save(*args, **kwargs)


class Paylasim(models.Model):
    göndericiAdi = models.CharField(max_length=100, null=False, blank=False)
    gönderiKonu = models.CharField(max_length=100, null=False, blank=False)
    gönderiAciklama = RichTextField()
    gönderiFoto = models.ImageField(
        upload_to="Paylasim/", blank=True, null=True, default="Paylasim/akslogo.png")
    gönderiDurumu = models.BooleanField(default=True)
    yazılımUrunumu = models.BooleanField(default=False)
    cameUrunumu = models.BooleanField(default=False)
    sssmi = models.BooleanField(default=False)
    slug = models.SlugField(null=False, unique=True,
                            db_index=True, blank=True, editable=False)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=False, blank=False, editable=True)
    göndericiUser = UserForeignKey(auto_user_add=True)
    # ek modul eklendi

    def __str__(self):
        return f"{self.gönderiKonu}"

    def save(self, *args, **kwargs):
        super(Paylasim, self).save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(self.gönderiKonu) + "-" + str(self.id)
            self.save()


class Comment(models.Model):
    hangi_ariza = models.ForeignKey(
        Ariza, on_delete=models.CASCADE, related_name='comments')
    göndericiUser = UserForeignKey(auto_user_add=True)
    yorum = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.göndericiUser, self.hangi_ariza)

class KesifPTSMalzeme(models.Model):

    #check box dropdown menu
    kesifPTSyeradi = models.CharField(max_length=50, null=True)
    kesifKameraSayisi =  models.IntegerField(default=0)
    kesifDirekSayisi = models.IntegerField(default=0)
    kesifAdaptorSayisi = models.IntegerField(default=0)
    kesifDirekUzunlugu = models.CharField(max_length=25,default="yok")
    kesifSwitchTipi = models.CharField(max_length=25, null=True,default="yok")
    kesifSwitchSayisi = models.IntegerField(default=0)
    kesifBigisayarConfigi = models.CharField(max_length=100,default="yok")
    kesifIoKartTipi = models.CharField(max_length=25,default="yok")
    kesifIoKartmodulaciklamasi = models.CharField(max_length=50,default="yok")
    kesifIoKartSayisi = models.IntegerField(default=0)
    kesifPanoTipi = models.CharField(max_length=50,default="yok")
    kesifPanoSayisi = models.IntegerField(default=0)
    kesifCAT6kablometre = models.IntegerField(default=0)
    kesifEnerjikablometre = models.IntegerField(default=0)
    kesifDT8kablometre = models.IntegerField(default=0)
    kesifSprellTipi = models.CharField(max_length=25,default="yok") 
    kesifSprellmetre = models.IntegerField(default=0)
    kesifFiberVarMi = models.BooleanField(default=False)
    kesifFiberMetre = models.IntegerField(default=0)
    kesifPatchPanelTipi = models.CharField(max_length=25, null=True,default="yok") 
    kesifPatchPanelSayisi =  models.IntegerField(default=0)
    kesifCibikModuleVarMi = models.BooleanField(default=False)
    kesifCibikModuleSayisi =  models.IntegerField(default=0)

    slug = models.SlugField(null=False, unique=True,
                            db_index=True, blank=True, editable=False)
    

    def __str__(self):
        return f"{self.kesifKameraSayisi}"

    def save(self, *args, **kwargs):
        super(KesifPTSMalzeme, self).save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(self.kesifPTSyeradi) + "-" + str(self.id)
            self.save()

class KesifOlayMalzeme(models.Model):

    #check box dropdown menu
    kesifKameraSayisi =  models.IntegerField(default=0)
    kesifDirekSayisi = models.IntegerField(default=0)
    kesifSwitchSayisi = models.IntegerField(default=0)
    kesifBigisayarConfigi = models.CharField(max_length=100,default="yok")


    slug = models.SlugField(null=False, unique=True,
                            db_index=True, blank=True, editable=False)
    

    def __str__(self):
        return f"{self.kesifKameraSayisi}"

    def save(self, *args, **kwargs):
        super(KesifOlayMalzeme, self).save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(self.kesifKameraSayisi) + "-" + str(self.id)
            self.save()

class Kesif(models.Model):

    #check box dropdown menu
    kesifYapilanYerAdi = models.CharField(max_length=50)
    kesifYapanKisi = models.CharField(max_length=50)
    kesifSenaryosu = models.CharField(max_length=2000)
    kesifYapilanYerTarihi = models.DateTimeField(auto_now_add=True, auto_now=False)
    kesifPTSVarMi = models.BooleanField(default=False)
    kesifOlayVarMi = models.BooleanField(default=False)
    kesifCctvVarMi = models.BooleanField(default=False)
    KesifPTSMalzemelerid = models.ForeignKey(
        KesifPTSMalzeme,null=True, on_delete=models.CASCADE, blank=True, editable=False)
    KesifOlayMalzemelerid = models.ForeignKey(
        KesifOlayMalzeme,null=True, on_delete=models.CASCADE, blank=True, editable=False)
    

    slug = models.SlugField(null=False, unique=True,
                            db_index=True, blank=True, editable=False)
    

    def __str__(self):
        return f"{self.kesifYapilanYerAdi}"

    def save(self, *args, **kwargs):
        super(Kesif, self).save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(self.kesifYapilanYerAdi) + "-" + str(self.id)
            self.save()

