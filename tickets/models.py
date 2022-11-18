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
from pyexpat import model
from random import choices
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
from PIL import Image
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
    gönderiAciklama = models.TextField()
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

    COLOR_CHOICES = (
    ('yok','yok'),
    ('IPC-HFW1431TP-ZS 4MP','IPC-HFW1431TP-ZS 4MP'),
    ('IPC-HFW5231EP-Z 2MP', 'IPC-HFW5231EP-Z 2MP'),
    ('Muhafazalı Set (Box)', 'Muhafazalı Set (Box)'), 
    )
    DIREK_FLANSH_CHOICE = (
        ("1","1"),
        ("2","2"),
    )
    IO_MODUL_CHOICE = (
        ("TİNY","TİNY"),
        ("AKSİYON","AKSİYON"),
    )
    SWITCH_PORT_CHOICE = (
        ("5","5"),
        ("8","8"),
        ("5+2","5+2"),
        ("8+2","8+2"),
        ("16+2","16+2"),
        ("8+4","8+4"),
        ("16+4","16+4"),
    )
    ENERJİ_KABLO_CHOICE = (
        ("3x1.5 TTR","3x1.5 TTR"),
        ("3x2.5 TTR","3x2.5 TTR"),
        ("2x1.5 TTR","2x1.5 TTR"),
    )
    PANO_ORTAM_CHOICE = (
        ("iç ortam ","iç ortam "),
        ("dış ortam","dış ortam"),
    )
    BARIYER_MODELİ_CHOICE = (
        ("3250","3250"),
        ("G-4000","G-4000"),
        ("4040E","4040E"),
        ("2080E","2080E"),
        ("GT-4","GT-4"),
        ("GT-8","GT-8"),
    )
    MANTAR_BARIYER_MODELİ_CHOICE = (
        ("2 li","2 li"),
        ("3 lu","3 lu"),
        ("4 lu","4 lu"),
        ("5 li","5 li"),
        ("6 li","6 li"),
    )
    FIBER_KABLO_MODELİ_CHOICE = (
        ("2 Core","2 Core"),
        ("4 Core","4 Core"),
        ("8 Core","8 Core"),
        ("16 Core","16 Core"),
    )
    PATCH_PANEL_MODELİ_CHOICE = (
        ("2 li","2 li"),
        ("4 lu","4 lu"),
        ("8 li","8 li"),
        ("12 li","12 li"),
    )
    PATCH_CORD_AND_FIBER_ADAPTOR_MODELİ_CHOICE = (
        ("SC-LC","SC-LC"),
        ("SC-SC","SC-SC"),
        ("LC-LC","LC-LC"),
    )
    LOOP_KABLO_CHOICE = (
        ("0.75mm² NYAF","0.75mm² NYAF"),
        ("1mm² NYAF","1mm² NYAF"),
        ("1.5mm² NYAF","1.5mm² NYAF"),
        ("2.5mm² NYAF","2.5mm² NYAF"),

    )
    #check box dropdown menu
    kesifPTSyeradi = models.CharField(max_length=50, null=True,blank=True)
    kesifPTSKameraSayisi =  models.IntegerField(null=True,blank=True)
    kesifPTSKameraBoatSayisi =  models.IntegerField(null=True,blank=True)
    kesifPTSKameraAdaptorSayisi =  models.IntegerField(null=True,blank=True)
    kesifPTSExtraKameraAdaptorSayisi =  models.IntegerField(null=True,blank=True)
    kesifPTSKameraTipi = models.CharField(null=True,blank=True,max_length=25,choices=COLOR_CHOICES)
    kesifPTSExtraKameraSayisi =  models.IntegerField(null=True,blank=True)
    kesifPTSExtraKameraTipi = models.CharField(null=True,blank=True,max_length=25,choices=COLOR_CHOICES)
    kesifPTSDirekSayisi = models.IntegerField(null=True,blank=True)
    kesifPTSDirekUzunlugu = models.CharField(max_length=25,null=True,blank=True)
    kesifPTSFlanshSayisi = models.CharField(max_length=25,default="1",choices=DIREK_FLANSH_CHOICE)
    kesifPTSDirekAçıklama = models.TextField(max_length=200,null=True,blank=True)
    kesifPTSAdaptorSayisi = models.IntegerField(null=True,blank=True)
    kesifPTSSwitchPortSayisi = models.CharField(max_length=25, null=True,default="yok",choices=SWITCH_PORT_CHOICE)
    kesifPTSSwitchSayisi = models.IntegerField(null=True,blank=True)
    kesifPTSSwitchPoeMi = models.BooleanField(default=False)
    kesifPTSBilgisayarConfigi = models.CharField(max_length=100,null=True,blank=True)
    kesifPTSBilgisayarSayısı = models.IntegerField(null=True,blank=True)
    kesifPTSIoKartSayısı = models.IntegerField(null=True,blank=True)
    kesifPTSIoKartTipi = models.CharField(max_length=25,default="yok",choices=IO_MODUL_CHOICE)
    kesifPTSIoKartModulSayısı = models.IntegerField(null=True,blank=True)
    kesifPTSIoKartAdaptorSayısı = models.IntegerField(null=True,blank=True)
    kesifPTSPanoTipi = models.CharField(max_length=50,default="yok",choices=PANO_ORTAM_CHOICE)
    kesifPTSPanoOlcusu = models.CharField(max_length=50,null=True,blank=True)
    kesifPTSPanoSayisi = models.IntegerField(null=True,blank=True)
    kesifPTSCAT6kablometre = models.IntegerField(null=True,blank=True)
    kesifPTSEnerjikablometre = models.IntegerField(null=True,blank=True)
    kesifPTSEnerjikabloTipi = models.CharField(max_length=50,default="yok",choices=ENERJİ_KABLO_CHOICE)
    kesifPTSDT8kablometre = models.IntegerField(null=True,blank=True)
    kesifPTSSpiralMetre = models.IntegerField(null=True,blank=True)
    kesifPTSSpiralÇapı = models.CharField(max_length=25,null=True,blank=True) 

    kesifPTSBariyerSayisi =  models.IntegerField(null=True,blank=True)
    kesifPTSBariyerModeli = models.CharField(max_length=25,default="yok",choices=BARIYER_MODELİ_CHOICE) 
    kesifPTSBariyerKolBoyu =  models.IntegerField(null=True,blank=True)

    kesifPTSMantarBariyerAciklama = models.TextField(max_length=200,null=True,blank=True)


    kesifPTSLoopDedektorSayisi = models.IntegerField(null=True,blank=True)
    kesifPTSLoopTrafoSayisi = models.IntegerField(null=True,blank=True)
    kesifPTSLoopKabloCesidi = models.CharField(max_length=25, null=True,blank=True,choices=LOOP_KABLO_CHOICE)
    kesifPTSLoopKabloMetresi = models.IntegerField(null=True,blank=True)



    kesifPTSLedEkranSayisi =  models.IntegerField(null=True,blank=True)
    kesifPTSLedEkranModeli = models.CharField(max_length=25,null=True,blank=True) 

    kesifPTSFiberMetre = models.IntegerField(null=True,blank=True)
    kesifPTSFiberKabloModeli = models.CharField(max_length=25,default="yok",choices=FIBER_KABLO_MODELİ_CHOICE) 

    kesifPTSPatchPanelSayisi =  models.IntegerField(null=True,blank=True)
    kesifPTSPatchPanelTipi = models.CharField(max_length=25,default="yok",choices=PATCH_PANEL_MODELİ_CHOICE) 

    kesifPTSPatchPanelEkKasetSayisi =  models.IntegerField(null=True,blank=True)
    kesifPTSPatchCordSayisi =  models.IntegerField(null=True,blank=True)
    kesifPTSPatchCordTipi = models.CharField(max_length=25,default="yok",choices=PATCH_CORD_AND_FIBER_ADAPTOR_MODELİ_CHOICE) 

    kesifPTSFiberAdaptorSayisi =  models.IntegerField(null=True,blank=True)
    kesifPTSFiberAdaptorTipi = models.CharField(max_length=25,default="yok",choices=PATCH_CORD_AND_FIBER_ADAPTOR_MODELİ_CHOICE) 

    kesifPTSCibikModuleSayisi =  models.IntegerField(null=True,blank=True)



    slug = models.SlugField(null=False,
                            db_index=True, blank=True, editable=False)
    

    def __str__(self):
        return f"{'Pts'+self.kesifKameraSayisi}"

    def save(self, *args, **kwargs):
        super(KesifPTSMalzeme, self).save(*args, **kwargs)
        if not self.slug:
            self.slug ="Pts"+ slugify(self.kesifPTSyeradi) + "-" + str(self.id)
            self.save()

class KesifOlayMalzeme(models.Model):

    COLOR_CHOICES = (
    ('yok','yok'),
    ('IPC-HFW1431TP-ZS 4MP','IPC-HFW1431TP-ZS 4MP'),
    ('IPC-HFW5231EP-Z 2MP', 'IPC-HFW5231EP-Z 2MP'),
    ('Muhafazalı Set (Box)', 'Muhafazalı Set (Box)'), 
    )
    DIREK_FLANSH_CHOICE = (
        ("1","1"),
        ("2","2"),
    )
    IO_MODUL_CHOICE = (
        ("TİNY","TİNY"),
        ("AKSİYON","AKSİYON"),
    )
    SWITCH_PORT_CHOICE = (
        ("5","5"),
        ("8","8"),
        ("5+2","5+2"),
        ("8+2","8+2"),
        ("16+2","16+2"),
        ("8+4","8+4"),
        ("16+4","16+4"),
    )
    ENERJİ_KABLO_CHOICE = (
        ("3x1.5 TTR","3x1.5 TTR"),
        ("3x2.5 TTR","3x2.5 TTR"),
        ("2x1.5 TTR","2x1.5 TTR"),
    )
    PANO_ORTAM_CHOICE = (
        ("iç ortam ","iç ortam "),
        ("dış ortam","dış ortam"),
    )
    BARIYER_MODELİ_CHOICE = (
        ("3250","3250"),
        ("G-4000","G-4000"),
        ("4040E","4040E"),
        ("2080E","2080E"),
        ("GT-4","GT-4"),
        ("GT-8","GT-8"),
    )
    MANTAR_BARIYER_MODELİ_CHOICE = (
        ("2 li","2 li"),
        ("3 lu","3 lu"),
        ("4 lu","4 lu"),
        ("5 li","5 li"),
        ("6 li","6 li"),
    )
    FIBER_KABLO_MODELİ_CHOICE = (
        ("2 Core","2 Core"),
        ("4 Core","4 Core"),
        ("8 Core","8 Core"),
        ("16 Core","16 Core"),
    )
    PATCH_PANEL_MODELİ_CHOICE = (
        ("2 li","2 li"),
        ("4 lu","4 lu"),
        ("8 li","8 li"),
        ("12 li","12 li"),
    )
    PATCH_CORD_AND_FIBER_ADAPTOR_MODELİ_CHOICE = (
        ("SC-LC","SC-LC"),
        ("SC-SC","SC-SC"),
        ("LC-LC","LC-LC"),
    )
    LOOP_KABLO_CHOICE = (
        ("0.75mm² NYAF","0.75mm² NYAF"),
        ("1mm² NYAF","1mm² NYAF"),
        ("1.5mm² NYAF","1.5mm² NYAF"),
        ("2.5mm² NYAF","2.5mm² NYAF"),

    )  #checkox dropdown menu

    kesifOlayyeradi = models.CharField(max_length=50, null=True,blank=True)
    kesifOlayKameraSayisi =  models.IntegerField(null=True,blank=True)
    kesifOlayKameraBoatSayisi =  models.IntegerField(null=True,blank=True)
    kesifOlayKameraAdaptorSayisi =  models.IntegerField(null=True,blank=True)
    kesifOlayExtraKameraAdaptorSayisi =  models.IntegerField(null=True,blank=True)
    kesifOlayKameraTipi = models.CharField(null=True,blank=True,max_length=25,choices=COLOR_CHOICES)
    kesifOlayExtraKameraSayisi =  models.IntegerField(null=True,blank=True)
    kesifOlayExtraKameraTipi = models.CharField(null=True,blank=True,max_length=25,choices=COLOR_CHOICES)
    kesifOlayDirekSayisi = models.IntegerField(null=True,blank=True)
    kesifOlayDirekUzunlugu = models.CharField(max_length=25,null=True,blank=True)
    kesifOlayFlanshSayisi = models.CharField(max_length=25,default="1",choices=DIREK_FLANSH_CHOICE)
    kesifOlayDirekAçıklama = models.TextField(max_length=200,null=True,blank=True)
    kesifOlayAdaptorSayisi = models.IntegerField(null=True,blank=True)
    kesifOlaySwitchPortSayisi = models.CharField(max_length=25, null=True,default="yok",choices=SWITCH_PORT_CHOICE)
    kesifOlaySwitchSayisi = models.IntegerField(null=True,blank=True)
    kesifOlaySwitchPoeMi = models.BooleanField(default=False)
    kesifOlayBilgisayarConfigi = models.CharField(max_length=100,null=True,blank=True)
    kesifOlayBilgisayarSayısı = models.IntegerField(null=True,blank=True)
    kesifOlayIoKartSayısı = models.IntegerField(null=True,blank=True)
    kesifOlayIoKartTipi = models.CharField(max_length=25,default="yok",choices=IO_MODUL_CHOICE)
    kesifOlayIoKartModulSayısı = models.IntegerField(null=True,blank=True)
    kesifOlayIoKartAdaptorSayısı = models.IntegerField(null=True,blank=True)
    kesifOlayPanoTipi = models.CharField(max_length=50,default="yok",choices=PANO_ORTAM_CHOICE)
    kesifOlayPanoOlcusu = models.CharField(max_length=50,null=True,blank=True)
    kesifOlayPanoSayisi = models.IntegerField(null=True,blank=True)
    kesifOlayCAT6kablometre = models.IntegerField(null=True,blank=True)
    kesifOlayEnerjikablometre = models.IntegerField(null=True,blank=True)
    kesifOlayEnerjikabloTipi = models.CharField(max_length=50,default="yok",choices=ENERJİ_KABLO_CHOICE)
    kesifOlayDT8kablometre = models.IntegerField(null=True,blank=True)
    kesifOlaySpiralMetre = models.IntegerField(null=True,blank=True)
    kesifOlayBariyerSayisi =  models.IntegerField(null=True,blank=True)
    kesifOlaySpiralÇapı = models.CharField(max_length=25,null=True,blank=True) 
    kesifOlayBariyerModeli = models.CharField(max_length=25,default="yok",choices=BARIYER_MODELİ_CHOICE) 
    kesifOlayBariyerKolBoyu =  models.IntegerField(null=True,blank=True)
    kesifOlayMantarBariyerAciklama = models.TextField(max_length=200,null=True,blank=True)
    kesifOlayLoopDedektorSayisi = models.IntegerField(null=True,blank=True)
    kesifOlayLoopTrafoSayisi = models.IntegerField(null=True,blank=True)
    kesifOlayLoopKabloCesidi = models.CharField(max_length=25, null=True,blank=True,choices=LOOP_KABLO_CHOICE)
    kesifOlayLoopKabloMetresi = models.IntegerField(null=True,blank=True)
    kesifOlayLedEkranSayisi =  models.IntegerField(null=True,blank=True)
    kesifOlayLedEkranModeli = models.CharField(max_length=25,null=True,blank=True) 
    kesifOlayFiberMetre = models.IntegerField(null=True,blank=True)
    kesifOlayFiberKabloModeli = models.CharField(max_length=25,default="yok",choices=FIBER_KABLO_MODELİ_CHOICE) 
    kesifOlayPatchPanelSayisi =  models.IntegerField(null=True,blank=True)
    kesifOlayPatchPanelTipi = models.CharField(max_length=25,default="yok",choices=PATCH_PANEL_MODELİ_CHOICE) 
    kesifOlayPatchPanelEkKasetSayisi =  models.IntegerField(null=True,blank=True)
    kesifOlayPatchCordSayisi =  models.IntegerField(null=True,blank=True)
    kesifOlayPatchCordTipi = models.CharField(max_length=25,default="yok",choices=PATCH_CORD_AND_FIBER_ADAPTOR_MODELİ_CHOICE) 
    kesifOlayFiberAdaptorSayisi =  models.IntegerField(null=True,blank=True)
    kesifOlayFiberAdaptorTipi = models.CharField(max_length=25,default="yok",choices=PATCH_CORD_AND_FIBER_ADAPTOR_MODELİ_CHOICE) 
    kesifOlayCibikModuleSayisi =  models.IntegerField(null=True,blank=True)
      #checOlayox dropdown menu
    # kesOlaylayKameraSayisi =  models.IntegerField(default=0)
    # kesifOlayDirekSayisi = models.IntegerField(default=0)
    # kesifOlaySwitchSayisi = models.IntegerField(default=0)
    # kesifOlayBigisayarConfigi = models.CharField(max_length=100,default="yok")


    slug = models.SlugField(null=False,
                            db_index=True, blank=True, editable=False)
    

    def __str__(self):
        return f"{'Olay'+self.kesifKameraSayisi}"

    def save(self, *args, **kwargs):
        super(KesifOlayMalzeme, self).save(*args, **kwargs)
        if not self.slug:
            self.slug ="Olay"+slugify(self.kesifOlayyeradi) + "-" + str(self.id)
            self.save()


class KesifCCTVMalzeme(models.Model):

    COLOR_CHOICES = (
    ('yok','yok'),
    ('IPC-HFW1431TP-ZS 4MP','IPC-HFW1431TP-ZS 4MP'),
    ('IPC-HFW5231EP-Z 2MP', 'IPC-HFW5231EP-Z 2MP'),
    ('Muhafazalı Set (Box)', 'Muhafazalı Set (Box)'), 
    )
    DIREK_FLANSH_CHOICE = (
        ("1","1"),
        ("2","2"),
    )
    IO_MODUL_CHOICE = (
        ("TİNY","TİNY"),
        ("AKSİYON","AKSİYON"),
    )
    SWITCH_PORT_CHOICE = (
        ("5","5"),
        ("8","8"),
        ("5+2","5+2"),
        ("8+2","8+2"),
        ("16+2","16+2"),
        ("8+4","8+4"),
        ("16+4","16+4"),
    )
    ENERJİ_KABLO_CHOICE = (
        ("3x1.5 TTR","3x1.5 TTR"),
        ("3x2.5 TTR","3x2.5 TTR"),
        ("2x1.5 TTR","2x1.5 TTR"),
    )
    PANO_ORTAM_CHOICE = (
        ("iç ortam ","iç ortam "),
        ("dış ortam","dış ortam"),
    )
    BARIYER_MODELİ_CHOICE = (
        ("3250","3250"),
        ("G-4000","G-4000"),
        ("4040E","4040E"),
        ("2080E","2080E"),
        ("GT-4","GT-4"),
        ("GT-8","GT-8"),
    )
    MANTAR_BARIYER_MODELİ_CHOICE = (
        ("2 li","2 li"),
        ("3 lu","3 lu"),
        ("4 lu","4 lu"),
        ("5 li","5 li"),
        ("6 li","6 li"),
    )
    FIBER_KABLO_MODELİ_CHOICE = (
        ("2 Core","2 Core"),
        ("4 Core","4 Core"),
        ("8 Core","8 Core"),
        ("16 Core","16 Core"),
    )
    PATCH_PANEL_MODELİ_CHOICE = (
        ("2 li","2 li"),
        ("4 lu","4 lu"),
        ("8 li","8 li"),
        ("12 li","12 li"),
    )
    PATCH_CORD_AND_FIBER_ADAPTOR_MODELİ_CHOICE = (
        ("SC-LC","SC-LC"),
        ("SC-SC","SC-SC"),
        ("LC-LC","LC-LC"),
    )
    LOOP_KABLO_CHOICE = (
        ("0.75mm² NYAF","0.75mm² NYAF"),
        ("1mm² NYAF","1mm² NYAF"),
        ("1.5mm² NYAF","1.5mm² NYAF"),
        ("2.5mm² NYAF","2.5mm² NYAF"),
    )  
    CCTV_KABLO_CHOICE = (
        ("2+1","2+1"),
        ("4+1","4+1"),

    )  
    CCTV_KAYIT_CIHAZ_MODELI_CHOICE = (
        ("4 lu","4 lu"),
        ("8 li","8 li"),
        ("16 lı","16 lı"),
        ("32 li","32 li"),
        ("64 lü","64 lü"),
    )
    kesifCCTVyeradi = models.CharField(max_length=50, null=True,blank=True)
    kesifCCTVKameraSayisi =  models.IntegerField(null=True,blank=True)
    kesifCCTVKameraBoatSayisi =  models.IntegerField(null=True,blank=True)
    kesifCCTVKameraAdaptorSayisi =  models.IntegerField(null=True,blank=True)
    kesifCCTVExtraKameraAdaptorSayisi =  models.IntegerField(null=True,blank=True)
    kesifCCTVKameraTipi = models.CharField(null=True,blank=True,max_length=25)
    kesifCCTVExtraKameraSayisi =  models.IntegerField(null=True,blank=True)
    kesifCCTVExtraKameraTipi = models.CharField(null=True,blank=True,max_length=25,choices=COLOR_CHOICES)
    kesifCCTVDirekSayisi = models.IntegerField(null=True,blank=True)
    kesifCCTVDirekUzunlugu = models.CharField(max_length=25,null=True,blank=True)
    kesifCCTVFlanshSayisi = models.CharField(max_length=25,default="1",choices=DIREK_FLANSH_CHOICE)
    kesifCCTVDirekAçıklama = models.TextField(max_length=200,null=True,blank=True)
    kesifCCTVAdaptorSayisi = models.IntegerField(null=True,blank=True)
    kesifCCTVPanoTipi = models.CharField(max_length=50,default="yok",choices=PANO_ORTAM_CHOICE)
    kesifCCTVPanoOlcusu = models.CharField(max_length=50,null=True,blank=True)
    kesifCCTVPanoSayisi = models.IntegerField(null=True,blank=True)
    kesifCCTVCCTVkablometre = models.IntegerField(null=True,blank=True)
    kesifCCTVCCTVkabloTipi = models.CharField(max_length=50,default="yok",choices=CCTV_KABLO_CHOICE)
    kesifCCTVEnerjikablometre = models.IntegerField(null=True,blank=True)
    kesifCCTVEnerjikabloTipi = models.CharField(max_length=50,default="yok",choices=ENERJİ_KABLO_CHOICE)
    kesifCCTVDT8kablometre = models.IntegerField(null=True,blank=True)
    kesifCCTVSpiralMetre = models.IntegerField(null=True,blank=True)
    kesifCCTVBariyerSayisi =  models.IntegerField(null=True,blank=True)
    kesifCCTVSpiralÇapı = models.CharField(max_length=25,null=True,blank=True) 
    kesifCCTVKayitCihaziSayisi =  models.IntegerField(null=True,blank=True)
    kesifCCTVKayitCihaziModeli = models.CharField(max_length=25,null=True,blank=True,choices=CCTV_KAYIT_CIHAZ_MODELI_CHOICE)
    kesifCCTVKayitCihaziHDDTeraByte =  models.CharField(max_length=25,null=True,blank=True) 

  

    slug = models.SlugField(null=False,
                            db_index=True, blank=True, editable=False)
    

    def __str__(self):
        return f"{'CCTV'+self.kesifKameraSayisi}"

    def save(self, *args, **kwargs):
        super(KesifCCTVMalzeme, self).save(*args, **kwargs)
        if not self.slug:
            self.slug ="CCTV"+slugify(self.kesifCCTVyeradi) + "-" + str(self.id)
            self.save()


class Kesif(models.Model):

    #check box dropdown menu
    kesifYapilanYerAdi = models.CharField(max_length=50)
    kesifYapanKisi = models.CharField(max_length=50)
    kesifSenaryosu = models.TextField()
    kesifYapilanYerTarihi = models.DateTimeField(auto_now_add=True, auto_now=False)
    kesifPTSVarMi = models.BooleanField(default=False)
    kesifOlayVarMi = models.BooleanField(default=False)
    kesifCctvVarMi = models.BooleanField(default=False)
    # kesifCreateTime = models.DateTimeField(auto_now_add=True, auto_now=False,null=True)

    KesifPTSMalzemelerid = models.ForeignKey(
        KesifPTSMalzeme,null=True, on_delete=models.CASCADE, blank=True, editable=False)
    KesifOlayMalzemelerid = models.ForeignKey(
        KesifOlayMalzeme,null=True, on_delete=models.CASCADE, blank=True, editable=False)
    KesifCCTVMalzemelerid = models.ForeignKey(
        KesifCCTVMalzeme,null=True, on_delete=models.CASCADE, blank=True, editable=False)
    

    slug = models.SlugField(null=False,
                            db_index=True, blank=True, editable=False)

    kesifOnaylandiMi = models.BooleanField(default=False)
    kesifArsivMi = models.BooleanField(default=False)
    

    def __str__(self):
        return f"{self.kesifYapilanYerAdi}"

    def save(self, *args, **kwargs):
        super(Kesif, self).save(*args, **kwargs)
        if not self.slug:
            self.slug ="Kesif"+ slugify(self.kesifYapilanYerAdi) + "-" + str(self.id)
            self.save()


class ImageKesif(models.Model):
    aitKesif = models.ForeignKey(Kesif,on_delete=models.CASCADE)
    kesifImage = models.ImageField(upload_to="Kesif/",null=True,blank = True)

    def __str__(self):
        return f"{self.aitKesif}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.kesifImage.path)

        if img.height > 600 or img.width >600:
            output_size = (600,600)
            img.thumbnail(output_size)
            img.save(self.kesifImage.path)