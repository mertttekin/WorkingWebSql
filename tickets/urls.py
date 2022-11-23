# from unicodedata import name
# from django.contrib import admin
from django.urls import path
from django.conf.urls import url
# from django.views import View
from . import views

# from .views import GeneratePdf


urlpatterns = [
     path('', views.arizakayit, name="tickets"),
     path('home/', views.home, name="home"),
     path('tickets/', views.arizakayit, name="tickets"),
     path('panel/details/<slug:slug>', views.details, name="details"),
     path('came/', views.came, name="came"),
     path('came/<slug:slug>', views.cameCategory, name="cameCategory"),
     path('panel/arizalar/', views.arizalar, name="arizalar"),
     path('yazilim/', views.yazilim, name="yazilim"),
     path('yazilim/<slug:slug>', views.yazılımCategory, name="yazılımCategory"),
     path('panel/arizalar/<slug:slug>', views.arızaFirma, name="arızaFirma"),
     path('panel/ariza/detay/<slug:slug>', views.arizaDetay, name="arizaDetay"),
     path('panel/paylasimgir/', views.paylasimgir, name="paylasimgir"),
     path('panel/paylasimgir/editt/<slug:slug>', views.editt, name="editt"),
     path('arizalar/arsiv/ekle/<slug:slug>',
          views.ArsiveEkle, name="ArsiveEkle"),
     path('panel/arsiv/', views.arsiv, name="arsiv"),
     path('panel/arsiv/<slug:slug>', views.arsivFirma, name="arsivFirma"),
     path('panel/arsiv/arsivdencikar/<slug:slug>',
          views.arsivdenCikar, name="arsivdenCikar"),
     path('sss', views.sss, name="sss"),
     path('panel/paylasimgir/sil/<slug:slug>', views.paylasimSil, name="paylasimSil"),
     path('ariza/detaysil/<int:id>',
          views.yorumSil, name="yorumSil"),
     path('paylasim/search/', views.post_search, name="post_search"),
     path('panel/',views.panel,name="panel"),
     path('panel/kesifekle',views.panelkesifekle,name="panelkesifekle"),
     path('panel/kesifliste',views.panelkesifliste,name="panelkesifliste"),
     path('panel/kesifliste/<slug:slug>',views.panelkesifdetails,name="panelkesifdetails"),
     path('panel/edit/<slug:slug>', views.panelkesifedit, name="panelkesifedit"),
     path('panel/kesifliste/<slug:slug>/indir',views.panelkesifindir,name="panelkesifindir"),
     path('panel/kesifliste/<slug:slug>/onayla',views.panelkesifonayla,name="panelkesifonayla"),
     path('panel/kesifliste/<slug:slug>/arsivle',views.panelkesifarsivle,name="panelkesifarsivle"),
     path('panel/dash',views.dash,name="dash"),


    

]
# path(url,foksiyon,path ismi)
