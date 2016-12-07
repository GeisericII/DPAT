#!/usr/bin/python

import random,hashlib,binascii

f_first = open("base/first.txt")
f_last = open("base/last.txt")
f_passwords = open("base/subset-rockyou.txt")
f_das= open("Domain Admins.txt","w")

first_list=list(f_first)
count_first = 0
domains = [ "parent.domain.com","child.domain.com","sister.domain.com"]
domain_admins = {
    'Agnes.Aarons-admin':'reallylongone',
    'Cliff.Adames-admin':'PasswordsAreHardToRemember',
    'Alex.Revis-admin':'57kdhfls*%2',
    'Gilbert.Settle-admin':'Ford57andGolf',
    'Cory.Ruhoff-admin':'NewPassword4Work',
    'Damian.Scarver-admin':'domainAdminPass',
    'Oscar.Veyna-admin':'ShirtsNSkins',
    'Rex.Vidot-admin':'1997hereo',
    'Scot.Viles-admin':'sparklesparkleZAP',
    'Burton.Vonner-admin':'VonnerPass16',
    'Dayna.Wade-admin':'Winter16',
    'Dustin.Wahlund-admin':'Frank-did-it',
    'Earnestine.Waiau-admin':'HappyTogether16',
    'Emerson.Wala-admin':'Washington87',
    'Sallie.Zych-admin':'77qwerty88',
    'Samuel.Zysk-admin':'Zundk8*&^',
    'Rosalinda.Zusman-admin':'Making Up Passwords is Hard',
    'Roman.Zurek-admin':'goFigure8',
    'Celia.Mcintosh-admin':'WikiWiki4What',
    'Celeste.Mcintire-admin':'2beornot2be',
    'Cecil.Mcinnis-admin':';kleknklk',
    'Brendan.Mcgriff-admin':'DontForget1',
    'Booker.Mcgraph-admin':'DaisyMisty1',
    'Bobbie.Mcgrane-admin':'P@sswo0rd16',
    'Clint.Hollifield-admin':'1997Married',
    'Coleen.Hollinghead-admin':'MickyMouse56',
    'Jackie.Dimodica-admin':'JerermyNHanna2',
    'Isabella.Dimitroff-admin':'Anastasia',
    'Horace.Dimarco-admin':'LovedByYou',
    'Herbert.Dils-admin':'DiamondRIO3',
    'Hazel.Dillman-admin':'L1ke1T',
    'Rex.Beadling-admin':'ITdoma1n@dmin',
    'Reggie.Beacher-admin':'WorldTurn@round',
    'Raul.Beaber-admin':'Lovemybug2003',
    'Pete.Baysmore-admin':'Hard24get',
    'August.Mcginnis-admin':'W$%23eu&*!rhs0'
}
lm_dict = { 'NotTooHard':'5B9D1AFCC9784729ADD5B1A41F2CB2C0','GoBeavErs1997':'94068F2F1CD1EAF27F76AAABE8E8789D','W$%23eu&*!rhs0':'4CE5B0C344FDD1038930410E6B652F2C','edward!':'67449A7AB9FDFA3AAAD3B435B51404EE','edhardy':'3AF628952D3CBDADAAD3B435B51404EE','ededed':'564B1B69A0CD5B23AAD3B435B51404EE','eddie22':'E3F874C4772EDC14AAD3B435B51404EE','earth1':'01EB2BDB90E4B363AAD3B435B51404EE','eagles36':'99223CC16C15AFCDC81667E9D738C5D9','dylanc':'BA0997645137628BAAD3B435B51404EE','dylanb':'4C72E2913A32E8A4AAD3B435B51404EE','dulceteamo':'0F8C1562718B774A6905068007DD26FD','dude1234':'4107C659B6183D65FF17365FAF1FFE89','druglord':'AC1F31C2E70BCB654A3B108F3FA6CB6D','droppie':'07E0ED6353B36D0AAAD3B435B51404EE','drink':'62B7CD49704064BDAAD3B435B51404EE','dragon17':'4097A469B4C52C1D7C3113B4A1A5E3A0','dracko':'A9327557F0E7E4FDAAD3B435B51404EE','downlow':'B44617E2CA667704AAD3B435B51404EE','douloveme':'62D3291BD468609863E11CD7E7F6092C','dothack':'6EAD70E9C296822BAAD3B435B51404EE','dotaallstar':'2987CC09184A44DE2201161DEDBA27A2','dorin':'947EB89A035D9D34AAD3B435B51404EE','dontspeak':'3B4F679F335D1535F04D685C382B531C','donnalyn':'A8E4E642B0A16CB6E72C57EF50F76A05','donnabelle':'97C88C474C40FE9589AF081E0305AC84','donika':'E5BF9342F4E51BA6AAD3B435B51404EE','dominate':'8C0D796F72023FB017306D272A9441BB','dolphy':'E75827B521C31229AAD3B435B51404EE','dollars1':'D456D433BC6A41B9C2265B23734E0DAC','doitbig':'E13F262D76132450AAD3B435B51404EE','doinita':'CA217F811088BC03AAD3B435B51404EE','dogandcat':'78028473533F1F269D4D37E81433E320','dobby':'CB94142B12F47F70AAD3B435B51404EE','dmarie':'B6ECEACBE041745CAAD3B435B51404EE','djones':'976EC97B7362B073AAD3B435B51404EE','divya':'DB9BDEDFC37408AFAAD3B435B51404EE','disney365':'DA505805AB7FCF926AB0B9B4DA013120','discoball':'82D8597A58DDB87C066B9E64566C2479','diogenes':'452265562B3B49B293E28745B8BF4BA6','dingaling':'D220E3D19587CFFCDD4218F5E59DD23A','dinamovista':'DD28D12979294E0C9A7853FCD68523F6','dimsum':'14BB788F701AC833AAD3B435B51404EE','dientes':'316A62A9E5078672AAD3B435B51404EE','diegoandres':'631D8A94ACF9ADF45F6B9B201665ECFF','diego14':'AE310716574EDF80AAD3B435B51404EE','diego13':'B466FE535D0D691CAAD3B435B51404EE','dick12':'8A49C00370347B9BAAD3B435B51404EE','dianna1':'713505C5D104BA61AAD3B435B51404EE','diablo69':'A3BE40622851765909752A3293831D17','dhianne':'8D78D2735A3A4379AAD3B435B51404EE','devon7':'CC6DC07DB80BEF75AAD3B435B51404EE','devin11':'67B2EF958AF6F612AAD3B435B51404EE','deventer':'2013970F2DB4971C944E2DF489A880E4','devan1':'0ADD5FD620A482C2AAD3B435B51404EE','destined':'830BA0309744B2C24A3B108F3FA6CB6D','dessire':'975DB741FFD6D065AAD3B435B51404EE','design1':'4C1AB3AC6E05EB1DAAD3B435B51404EE','desiderio':'6A1C2D9A85892C26DF61CA35DEE5AA58','derry':'8416E3769D5FB679AAD3B435B51404EE','derrty':'28F566AF5658CCBAAAD3B435B51404EE','derek3':'9CF17DB1CB859EABAAD3B435B51404EE','derek22':'1B033D2858D542D9AAD3B435B51404EE','dennis01':'C8396E60C4987FB8C2265B23734E0DAC','denisuca':'9DC7423CB84514547584248B8D2C9F9E','denise14':'4E61A3280511BCC9FF17365FAF1FFE89','deniece':'6537F0EC75253266AAD3B435B51404EE','dementia':'75EEA72B6DE5C2EC7584248B8D2C9F9E','della1':'69666E0FCE54D3F1AAD3B435B51404EE','deliverance':'FC29BE7F95F1A281354EF550D6D616DF','delgadillo':'E77BDBF6AE2B3D930279963575FF2D48','deldel':'CDEA18537CB83F8FAAD3B435B51404EE','deion':'CE5205F9E3F1D158AAD3B435B51404EE','defoe18':'5811452C87D01332AAD3B435B51404EE','deeper':'A1886219150AE350AAD3B435B51404EE','deejay1':'B2DF80A944C9CB0CAAD3B435B51404EE','dee-dee':'1F17C1545FC9D496AAD3B435B51404EE','death2u':'539706F3890A934BAAD3B435B51404EE','dearly':'ACB63C873C70EDFFAAD3B435B51404EE','deadline':'D9989D2AEB2F392817306D272A9441BB','dead666':'56D719A22A00943EAAD3B435B51404EE','dayday123':'C7C9EB383B9066CCB75E0C8D76954A50','dayani':'269D8839491A9E6CAAD3B435B51404EE','day123':'76B6E26A7386D775AAD3B435B51404EE','daville':'1523F21BDB224D64AAD3B435B51404EE','davegrohl':'45B69A7B44018AB1EB90FCD89E798A49','dave21':'1173D0A5814FC7A5AAD3B435B51404EE','dario1':'684AAF0C9563CC51AAD3B435B51404EE','darin':'B29A4A5669527F0AAAD3B435B51404EE','darel':'963D8FB64DF80D69AAD3B435B51404EE','danyale':'1F1C9E6BDAF385BFAAD3B435B51404EE','dannyteamo':'C5660362EC7308AF6905068007DD26FD','danielle05':'41A5DF84E34D4393B0D866F8E2272AD6','daniel87':'D78FF2C06D3B72B27C3113B4A1A5E3A0','dani23':'F100ACF2FF2ADE44AAD3B435B51404EE','dani1':'175E69F189D25399AAD3B435B51404EE','dancok':'91824FD4185EE910AAD3B435B51404EE','dancingdiva':'81380963DA03E29697440C3488F02677','dancewithme':'C8B325EBE380D5C756496D0A2CF27A20','dancer26':'FEAE74B8E1947D9BC81667E9D738C5D9','dancer03':'894CBEC1AC35440D1AA818381E4E281B','dancechick':'449EC1BFA0F80FB272F8DA9D69F474D7','dancarter':'0F261E270277EE3E8963805A19B0ED49','dana1':'68E66D68E3AD2A0FAAD3B435B51404EE','dallas41':'73F3C9B1038B4422C2265B23734E0DAC','dallas15':'59CC3F718A14BD029C5014AE4718A7EE','dallas08':'C6FB9E6F7DB3F27036077A718CCDF409','dallas07':'C6FB9E6F7DB3F2707C3113B4A1A5E3A0','daisy!':'8EBDE0B1057D172EAAD3B435B51404EE','daine':'A6D663D5197DEA9AAAD3B435B51404EE','dailyn':'09F11E1A2F255F7FAAD3B435B51404EE','daddysboy':'69B507AAFDD2F72E655265D1314726C0','daddylove':'805D046BD8B55712B6FE535A75CB5552','daddy1234':'E42F9B3895F1F7B219F10A933D4868DC','daddy03':'82E76E96B3FCEFF3AAD3B435B51404EE','cynthia3':'BF65484F9EAA59351AA818381E4E281B','cymone':'DC9AF42629FA0778AAD3B435B51404EE','cutiepie16':'287ACD99E5A71EA619DB94ADC99423BF','cuters':'C435D7E4789C5286AAD3B435B51404EE','cupcake4':'E0009F6A725132CBFF17365FAF1FFE89','cunt69':'06AC388690048B3DAAD3B435B51404EE','cuddlebug':'375A10B1E5F43E45D17FDCAAB966EFA7','cuckoo':'E749D93A7BE08AC5AAD3B435B51404EE','cuadra':'C5D055D5402EA371AAD3B435B51404EE','cstrike':'4A3F0486D35169C7AAD3B435B51404EE','crystal11':'87650E47E4D141585D3872C04445E010','crystal01':'87650E47E4D1415873251AA2B4314B90','cristea':'64EC8CB777E8E2EDAAD3B435B51404EE','creeds':'FA0F7946A915FD06AAD3B435B51404EE','crazy4ever':'99EBBDF7699BA6D0B12FAE38C8ABEE13','crawfish':'0E4BABFD43EEC5C15ACDCD7C247FA83A','craig2':'2373F7A3D68F3C2BAAD3B435B51404EE','crackwhore':'47CA74079D90D70D5468F2AD1F3B98BA','cowgirl07':'131BE2583DE651E718FCD526FB48A829','cowboys5':'CC954BF64510840D9C5014AE4718A7EE','courtney4':'063DE5A00E0BBA01744F2D424178DE49','cotita':'F6E1814A19F0DC3DAAD3B435B51404EE','costas':'03B9455205B8464AAAD3B435B51404EE','corona12':'D60C67A63F8821691D71060D896B7A46','cornbread1':'75ED8AC86B42E2B9042370C4583C388F','corey13':'372336BE0DB2D2C8AAD3B435B51404EE','coolaid':'27F0F886CD1DE9C3AAD3B435B51404EE','cookie04':'4DBF38B0A644F62FFF17365FAF1FFE89','contagious':'496CE23950764D4A5BE30F58D2A941D5','contabilitate':'332F012EDCC53D731DAB72D6A1727041','connor02':'17A1143A6E6E42821D71060D896B7A46','conner2':'62CFCE559EC73CADAAD3B435B51404EE','comunidad':'8AD5C85747A9E2BD9C749B84168D712D','common1':'9E39676A49F99C52AAD3B435B51404EE','columbus1':'CADD68BDB2673CA30CC3EB564B0F9047','colon':'1AB94AAF9FE60AE1AAD3B435B51404EE','coley1':'51BD657CEB4457CFAAD3B435B51404EE','coldheart':'0532CF033F5955B35F034D624633DBF9','codylinley':'B671C9AF04D37B08F15DB3BDBAD92750','cody07':'DB455B1B86B8A058AAD3B435B51404EE','cody04':'3DC6DD72755CCFE9AAD3B435B51404EE','coco08':'F26B193B103F6AD4AAD3B435B51404EE','cocknose':'A2D4DFAFA94D7B5D17306D272A9441BB','clubber':'4027C45050D0DC04AAD3B435B51404EE','cleo':'3CAB28372DB1715EAAD3B435B51404EE','clears':'E9596D59EDCD0C22AAD3B435B51404EE','claudia12':'FDAA24DE0BCBEB854207FD0DF35A59A8','civics':'A21064406DD6C682AAD3B435B51404EE','citron':'9840ABA3424EBA78AAD3B435B51404EE','cintakamu':'9564A655D10805450BBD7D4C25A4DEFA','ciclope':'C155BC1446E5101CAAD3B435B51404EE','chute':'8DBDFBAA0CF03C76AAD3B435B51404EE','chula12':'5A4C094D73768C02AAD3B435B51404EE','chuche':'0652223D8E88744DAAD3B435B51404EE','christians':'630505E57DC5617E8E4DD189F947B5EC','chrischris':'B6760E35ED0103CD85BB7C52C41086D7','chris83':'E2F432F581BF8148AAD3B435B51404EE','chris2005':'41973827B8184CF96FB9A7EF37043CD6','chonchis':'80AAA6EB2DC0233093E28745B8BF4BA6','chocorrol':'501E06987BD244E97BB1D8438F805B5C','chocolatelover':'81D330F45391D6CDD21334332AE253C7','choclate1':'B1067D8E77DD0072A202B0A0CC08E46E','chivas15':'BA237827413B85849C5014AE4718A7EE','chimes':'7C03C765BFC529A9AAD3B435B51404EE','chikitalinda':'6A5DF180A72046188315F2B502B247DC','chikis1':'04AE55C4E6F75BB5AAD3B435B51404EE','chickenwings':'5E9019CC921146AC00F4888F92F39DF9','chicharron':'A138C2D50AC9C5063140C07381B6A165','chica15':'B3D2CC98E2BC3F63AAD3B435B51404EE','chevygirl':'725DA578E9D54C1D2DCA4431C6F3913D','cherry9':'616778FE4E03EB13AAD3B435B51404EE','cherries2':'328FB4F46E4A4EDA74F23606C66022B0','cherie1':'A30A2797D55E44E1AAD3B435B51404EE','cheetah2':'0BEBB7B76F9F09A01D71060D896B7A46','cheeseontoast':'34DC70895752909D63C3F1914814DF78','cheese23':'1B8DB7D20C6C244B1AA818381E4E281B','cheese14':'3A5F48756650F617FF17365FAF1FFE89','cheer55':'ADF3815AE0113EE6AAD3B435B51404EE','cheene':'214BA788DBF79432AAD3B435B51404EE','chean':'4A07877A1FD2D2E0AAD3B435B51404EE','chassy':'3569B3396667A9A2AAD3B435B51404EE','charlie88':'528A05A387553DC56C4691C0029EBE9F','charlie27':'528A05A387553DC5025A32A63FE04BEC','charlie20':'528A05A387553DC5143F8BD9AE9E0363','charlie18':'528A05A387553DC58347BB1E72CC9F76','chaparra1':'CEF00CDAA153648F65C4A55F32B3BF85','chaochao':'A3EB50453623B039E68AA26A841A86FA','changed1':'67B011CF3539A3E3C2265B23734E0DAC','chalie':'E80D509ABABDE9C4AAD3B435B51404EE','chakas':'5ED7F084F1839FD7AAD3B435B51404EE','chad69':'BF34878165770EEEAAD3B435B51404EE','chachie':'3091167271E136C2AAD3B435B51404EE','chabe':'BF1008C067449CFFAAD3B435B51404EE','cha123':'84126D3AA15B64D0AAD3B435B51404EE','cha-cha':'F7E38693146CED75AAD3B435B51404EE','cfc123':'B10D8883941986DCAAD3B435B51404EE','cesar2':'745B312CE52C3F88AAD3B435B51404EE','ceriwis':'D0BA7E97FC3E9290AAD3B435B51404EE','centinela':'E7D941ADA594566EB09321E47427AF3C','cena11':'4656FDC59974A241AAD3B435B51404EE','cena01':'268D5E2B37583A0AAAD3B435B51404EE','celtic08':'4467856BF476733B36077A718CCDF409','cedes':'8A337C28CE3265FFAAD3B435B51404EE','cecilita':'6D02B4EFE4C3AE017584248B8D2C9F9E','cdcdcd':'4DAB65D458627A62AAD3B435B51404EE','cbr900rr':'ADF862771AC0FA35944E2DF489A880E4','cazares':'19E925C350B4A289AAD3B435B51404EE','UpPeRlOwEr':'3630E260BC5D7049249A4622CE4C83C8','HarD222cRacK':'051B0FC10EAE6A6D22EF373F485DF6BD','resgocswit7hWQ':'90C0059BFB22BB44F657FC2061517840','lastBUTnotLEAS':'47AAF1C238FCBAB597FAF9A0F46316C1'}

dontCrackWithNT = ["W$%23eu&*!rhs0","UpPeRlOwEr","HarD222cRacK","resgocswit7hWQ","lastBUTnotLEAS"]
dontNTCrackTheseUsers = ["Bobbie.Mcgrane-admin","Rosalinda.Zusman-admin","Cecil.Mcinnis-admin", "Cory.Ruhoff-admin","Cliff.Adames-admin","Samuel.Zysk-admin"]

f = open("customer.ntds","w")
f2 = open("oclHashcat.pot","w")
wroteRHS = False

for last in f_last:
    add_admin = False
    if count_first < len(first_list):
        firstName = first_list[count_first].rstrip().title()
        count_first = count_first + 1
    else:
        count_first = 0
        firstName = first_list[count_first].rstrip().title()
    lastName = last.rstrip().title()
    userName = firstName + "." + lastName
    if userName + "-admin" in domain_admins:
        userName = userName + "-admin"
    password = f_passwords.readline().rstrip()
    if domain_admins.has_key(password):
        print "Warn: duplicated password for administrator: " + password
    rid = str(random.randint(10000,500000))
    domain = domains[random.randint(0,len(domains)-1)]
    if domain_admins.has_key(userName):
        password=domain_admins[userName]
        domain=domains[1]
        f_das.write(domain + "\\" + userName + "\n")
        if userName in ["Agnes.Aarons-admin","Alex.Revis-admin","Burton.Vonner-admin","Pete.Baysmore-admin"]:
            add_admin = True
    nt_hash = binascii.hexlify(hashlib.new('md4', password.encode('utf-16le')).digest())
    lm_hash = "aad3b435b51404eeaad3b435b51404ee" # this is the LM hash of a blank password
    if lm_dict.has_key(password):
        lm_hash = lm_dict[password]
    f.write(domain + "\\" + userName + ":" + rid + ":" + lm_hash.lower() + ":" + nt_hash + ":::\n")
    if  (password not in dontCrackWithNT) and (userName not in dontNTCrackTheseUsers) and (password in lm_dict or random.randrange(1,100)<78):
        f2.write(nt_hash + ":" + password + "\n")
    if  password in dontCrackWithNT:
        left_pass=password[0:8].upper()
        right_pass=password[8:15].upper()
        left_hash=lm_dict[password][0:16].lower()
        right_hash=lm_dict[password][16:32].lower()
        if password != "W$%23eu&*!rhs0" or not wroteRHS:
            f2.write(left_hash + ":" + left_pass + "\n")
            f2.write(right_hash + ":" + right_pass + "\n")
        if password == "W$%23eu&*!rhs0":
            wroteRHS = True
    if add_admin:
        f.write(domain + userName.rstrip("-admin") + ":" + rid + ":" + lm_hash.lower() + ":" + nt_hash + ":::\n")
f2.write("aad3b435b51404ee:\n")
f.close()
f2.close()
f_first.close()
f_last.close()
f_passwords.close()