# # -*- coding: utf-8 -*-
# """
# edited on 1400/11/10 ---- 01/30/2022
#
# @author: mahmoud esmaeili
# """
from market_data import*

# ------------------------------------------market split to group---------------------------------------
group_code_list = [1,10,13,14,17,19,20,21,22,23,25,27,28,29,31,32,33,34,35,
              36,38,39,40,42,43,44,45,47,49,53,54,56,57,58,60,64,65,67,70,72,73,74,11,66,]
# group_name_list = [زراعت,ذغال سنگ,كانه فلزي,ساير معادن,منسوجات,محصولات چرمي,محصولات چوبي,محصولات كاغذ,انتشار و چاپ,فراورده نفتي,لاستيك,فلزات اساسي,محصولات فلزي,ماشين آلات,دستگاههاي برقي,وسايل ارتباطي,ابزار پزشكي,خودرو,حمل و نقل,مبلمان,قند و شكر,چند رشته اي ,تامين آب-برق- گاز,غذايي بجز قند,مواد دارويي,شيميايي,پيمانكاري,خرده فروشي به جز وسايل نقليه,كاشي و سراميك,سيمان,كاني غيرفلزي,سرمايه,گذاريها,بانكها,سايرمالي,حمل و نقل,راديويي,مالي,اداره بازارهاي مالي,انبوه سازي,رايانه,اطلاعات و ارتباطات,فني مهندسي,استخراج نفت جزكشف,بيمه و بازنشستگی
# ]
#------------------------------------------------------------------------------------------------------
zeraat = set_group_list(1)
print('zeraat is;',len(zeraat),zeraat)
#------------------------------------------------------------------------------------------------------
zoghal_sang = set_group_list(10)
print('zoghal_sang is;',len(zoghal_sang),zoghal_sang)
#------------------------------------------------------------------------------------------------------
kaneh_felezi = set_group_list(13)
print('kaneh_felezi is;',len(kaneh_felezi),kaneh_felezi)
#------------------------------------------------------------------------------------------------------
sayer_maden = set_group_list(14)
print('sayer_maden is;',len(sayer_maden),sayer_maden)
#------------------------------------------------------------------------------------------------------
mansojat = set_group_list(17)
print('mansojat is;',len(mansojat),mansojat)
#------------------------------------------------------------------------------------------------------
charm = set_group_list(19)
print('charm is;',len(charm),charm)
#------------------------------------------------------------------------------------------------------
choob = set_group_list(20)
print('choob is;',len(choob),choob)
#------------------------------------------------------------------------------------------------------
kaghaz = set_group_list(21)
print('kaghaz is;',len(kaghaz),kaghaz)
#------------------------------------------------------------------------------------------------------
chaap = set_group_list(22)
print('chaap is;',len(chaap),chaap)
#------------------------------------------------------------------------------------------------------
naft = set_group_list(23)
print('naft is;',len(naft),naft)
#------------------------------------------------------------------------------------------------------
lastik = set_group_list(25)
print('lastik is;',len(lastik),lastik)
#------------------------------------------------------------------------------------------------------
flazat_asasi = set_group_list(27)
print('flazat_asasi is;',len(flazat_asasi),flazat_asasi)
#------------------------------------------------------------------------------------------------------
felzat_mahsol = set_group_list(28)
print('felzat_mahsol is;',len(felzat_mahsol),felzat_mahsol)
#------------------------------------------------------------------------------------------------------
machins = set_group_list(29)
print('machins is;',len(machins),machins)
#------------------------------------------------------------------------------------------------------
barghi = set_group_list(31)
print('barghi is;',len(barghi),barghi)
#------------------------------------------------------------------------------------------------------
ertebati = set_group_list(32)
print('ertebati is;',len(ertebati),ertebati)
#------------------------------------------------------------------------------------------------------
pezeshki = set_group_list(33)
print('pezeshki is;',len(pezeshki),pezeshki)
#------------------------------------------------------------------------------------------------------
khodro = set_group_list(34)
print('khodro is;',len(khodro),khodro)
#------------------------------------------------------------------------------------------------------
hamlonaghli = set_group_list(35)
print('hamlonaghli is;',len(hamlonaghli),hamlonaghli)
#------------------------------------------------------------------------------------------------------
mobleman = set_group_list(36)
print('mobleman is;',len(mobleman),mobleman)
#------------------------------------------------------------------------------------------------------
ghandi = set_group_list(38)
print('ghandi is;',len(ghandi),ghandi)
#------------------------------------------------------------------------------------------------------
chandreshteh = set_group_list(39)
print('chandreshteh is;',len(chandreshteh),chandreshteh)
#------------------------------------------------------------------------------------------------------
utiliti = set_group_list(40)
print('utiliti is;',len(utiliti),utiliti)
#------------------------------------------------------------------------------------------------------
ghazaei = set_group_list(42)
print('ghazaei is;',len(ghazaei),ghazaei)
#------------------------------------------------------------------------------------------------------
daroei = set_group_list(43)
print('daroei is;',len(daroei),daroei)
#------------------------------------------------------------------------------------------------------
shimiaei = set_group_list(44)
print('shimiaei is;',len(shimiaei),shimiaei)
#------------------------------------------------------------------------------------------------------
peymankari = set_group_list(45)
print('peymankari is;',len(peymankari),peymankari)
#------------------------------------------------------------------------------------------------------
retailing = set_group_list(47)
print('retailing is;',len(retailing),retailing)
#------------------------------------------------------------------------------------------------------
kashi = set_group_list(49)
print('kashi is;',len(kashi),kashi)
#------------------------------------------------------------------------------------------------------
siman = set_group_list(53)
print('siman is;',len(siman),siman)
#------------------------------------------------------------------------------------------------------
kani = set_group_list(54)
print('kani is;',len(kani),kani)
#------------------------------------------------------------------------------------------------------
investing = set_group_list(56)
print('investing is;',len(investing),investing)
#------------------------------------------------------------------------------------------------------
banks = set_group_list(57)
print('banks is;',len(banks),banks)
#------------------------------------------------------------------------------------------------------
mali_sayer = set_group_list(58)
print('mali_sayer is;',len(mali_sayer),mali_sayer)
#------------------------------------------------------------------------------------------------------
reyli = set_group_list(60)
print('reyli is;',len(reyli),reyli)
#------------------------------------------------------------------------------------------------------
radioei = set_group_list(64)
print('radioei is;',len(radioei),radioei)
#------------------------------------------------------------------------------------------------------
mali = set_group_list(65)
print('mali is;',len(mali),mali)
#------------------------------------------------------------------------------------------------------
mali_ofice = set_group_list(67)
print('mali_ofice is;',len(mali_ofice),mali_ofice)
#------------------------------------------------------------------------------------------------------
anbohsazi = set_group_list(70)
print('anbohsazi is;',len(anbohsazi),anbohsazi)
#------------------------------------------------------------------------------------------------------
rayaneh = set_group_list(72)
print('rayaneh is;',len(rayaneh),rayaneh)
#------------------------------------------------------------------------------------------------------
data = set_group_list(73)
print('data is;',len(data),data)
#------------------------------------------------------------------------------------------------------
engineering = set_group_list(74)
print('engineering is;',len(engineering),engineering)
#------------------------------------------------------------------------------------------------------
estekhraj = set_group_list(11)
print('estekhraj is;',len(estekhraj),estekhraj)
#------------------------------------------------------------------------------------------------------
bimeh = set_group_list(66)
print('bimeh is;',len(bimeh),bimeh)
#------------------------------------------------------------------------------------------------------
