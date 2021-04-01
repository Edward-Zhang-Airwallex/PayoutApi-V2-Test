VALIDATION_SCHEMA = {
    "iban": [
        {'AD, AE, AL, AT, AZ, BA, BE, BG, BH, CH, CY, CZ, DE, DK, DO, EE, ES, FI, '
         'FR, GE, GI, GR, GT, HR, HU, IE, IL, IS, IT, JO, KW, KZ, LB, LI, LT, LU, '
         'LV, MC, MD, MK, MT, MU, NL, NO, PL, PT, QA, RO, RS, SA, SC, SE, SI, SK, SM, TN, PK/*/*/*/*'
        :{
            'pattern':'^country[0-9]{2}[A-Z0-9]{9,30}([A-Z0-9]{3,5}){2,7}([A-Z0-9]{1,3})?$',
            'required':'true',
        }},
        {'GG,JE,IM/SWIFT/*/GBP/*': {
            'pattern': '^(country|GB)[0-9]{2}[A-Z0-9]{9,30}([A-Z0-9]{3,5}){2,7}([A-Z0-9]{1,3})?$',
            'required': 'true',
        }},
        {'GG,JE,IM/*/*/*/*': {
            'pattern': '^(country|GB)[0-9]{2}[A-Z0-9]{9,30}([A-Z0-9]{3,5}){2,7}([A-Z0-9]{1,3})?$',
            'required': 'true',
        }},
        {'GB/SWIFT/*/GBP/*': {
            'pattern': '^GB[0-9]{2}[A-Z0-9]{9,30}([A-Z0-9]{3,5}){2,7}([A-Z0-9]{1,3})?$',
            'required': 'true',
        }},
        {'GB/*/*/*/*': {
            'pattern': '^GB[0-9]{2}[A-Z0-9]{9,30}([A-Z0-9]{3,5}){2,7}([A-Z0-9]{1,3})?$',
            'required': 'true',
        }},
        {'TR/*/*/*/*': {
            'pattern': '^(TR|TK)[0-9]{2}[A-Z0-9]{9,30}([A-Z0-9]{3,5}){2,7}([A-Z0-9]{1,3})?$',
            'required': 'true',
        }},
        {'MQ, PM, TF, YT/*/*/*/*': {
            'pattern': '^FR[0-9]{2}[A-Z0-9]{9,30}([A-Z0-9]{3,5}){2,7}([A-Z0-9]{1,3})?$',
            'required': 'true',
        }},
    ],
    "swift_code":[
        {'AU, JP, KR, US/LOCAL/*/*/*': {
            'pattern': '',
            'required': 'true',
        }},
        {'HK/LOCAL/ACH, FPS/*/*': {
            'pattern': '',
            'required': 'true',
        }},
        {'CA/LOCAL/*/CAD/*': {
            'pattern': '',
            'required': 'true',
        }},
        {'NP/LOCAL/*/*/*': {
            'pattern': '',
            'required': 'true',
        }},
        {'GB, GG, IM, JE/LOCAL/*/GBP/*': {
            'pattern': '',
            'required': 'true',
        }},
        {'HK/LOCAL/RTGS/*/*': {
            'pattern': '^[A-Z]{4}HK[A-Z0-9]{2}([A-Z0-9]{3})?$',
            'required': 'true',
        }},
        {'ID, IN, MY, PH, TH, VN, BD, PK, LK, TR/LOCAL/*/*/*': {
            'pattern': '^[A-Z]{4}country[A-Z0-9]{2}([A-Z0-9]{3})?$',
            'required': 'true',
        }},
        {'SG/LOCAL/*/SGD/*': {
            'pattern': '^[A-Z]{4}SG[A-Z0-9]{2}([A-Z0-9]{3})?$',
            'required': 'true',
        }},
        {'CN/LOCAL/*/CNY/*': {
            'pattern': '',
            'required': 'true',
        }},
        {'*/LOCAL/*/*/*': {
            'pattern': '^[A-Z]{4}country[A-Z0-9]{2}([A-Z0-9]{3})?$',
            'required': 'true',
        }},
        {'*/SWIFT/*/*/*': {
            'pattern': '^[A-Z]{4}country[A-Z0-9]{2}([A-Z0-9]{3})?$',
            'required': 'true',
        }},

    ],
    'account_number':[
        {'AM, AW, AG, AI, AN, AO, AR, BO, BR, CL, CO, CR, CW, DM, DZ, EC, EG, FJ, GD, GQ, GY, HN, JM, KE, KG, KH, MA, '
         'MO, MV, NI, NP, OM, PA, PE, PF, PR, PY, SV, TJ, UG, UY, UZ, VE, VU, ZA, ZM/*/*/*/*': {
            'pattern': '^[0-9A-Za-z]{1,50}$',
            'required': 'true',
        }},
        {'AU/LOCAL/BPAY/*/*': {
            'pattern': '',
            'required': 'true',
        }},
        {'AU/LOCAL/BANK_TRANSFER/*/*': {
            'pattern': '^[0-9]{6,9}$',
            'required': 'true',
        }},
        {'AU/SWIFT/*/*/*': {
            'pattern': '^[0-9A-Za-z]{6,20}$',
            'required': 'true',
        }},
        {'NZ/*/*/NZD/*': {
            'pattern': '^[0-9]{15,16}$',
            'required': 'true',
        }},
        {'NZ/*/*/*/*': {
            'pattern': '^[0-9A-Za-z]{1,50}$',
            'required': 'true',
        }},
        {'CA/LOCAL/*/*/*': {
            'pattern': '^[0-9]{7,21}$',
            'required': 'true',
        }},
        {'CA/SWIFT/*/*/*': {
            'pattern': '^[0-9]{7,35}$',
            'required': 'true',
        }},
        {'CN/SWIFT/*/*/*': {
            'pattern': '^[0-9A-Za-z]{8,34}$',
            'required': 'true',
        }},
        {'CN/LOCAL/*/*/*': {
            'pattern': '^[0-9]{8,34}$',
            'required': 'true',
        }},
        {'GB, GG, IM, JE/LOCAL/*/GBP/*': {
            'pattern': '^[0-9]{8}$',
            'required': 'true',
        }},
        {'HK/LOCAL/RTGS/*/*': {
            'pattern': '^[0-9]{9,16}$',
            'required': 'true',
        }},
        {'HK/LOCAL/ACH/*/*': {
            'pattern': '^[0-9]{9,12}$',
            'required': 'true',
        }},
        {'HK/LOCAL/FPS/*/*': {
            'pattern': '^[0-9]{9,13}$',
            'required': 'true',
        }},
        {'HK/SWIFT/*/*/*': {
            'pattern': '^[0-9]{8,16}$',
            'required': 'true',
        }},
        {'ID/*/*/*/*': {
            'pattern': '^[0-9]{1,22}$',
            'required': 'true',
        }},
        {'IN/LOCAL/*/*/*': {
            'pattern': '^[0-9]{9,18}$',
            'required': 'true',
        }},
        {'IN/SWIFT/*/*/*': {
            'pattern': '^[0-9A-Za-z]{9,29}$',
            'required': 'true',
        }},
        {'JP/LOCAL/*/*/*': {
            'pattern': '^[0-9]{7}$',
            'required': 'true',
        }},
        {'JP/SWIFT/*/JPY/*': {
            'pattern': '^[0-9A-Za-z]{5,19}$',
            'required': 'true',
        }},
        {'JP/SWIFT/*/*/*': {
            'pattern': '^[0-9]{5,19}$',
            'required': 'true',
        }},
        {'KR/SWIFT/*/USD/*': {
            'pattern': '^[0-9A-Za-z]{7,16}$',
            'required': 'true',
        }},
        {'KR/LOCAL/*/KRW/*': {
            'pattern': '^[0-9A-Za-z]{7,16}$',
            'required': 'true',
        }},
        {'KR/*/*/*/*': {
            'pattern': '^[0-9]{7,16}$',
            'required': 'true',
        }},
        {'MX/*/*/*/*': {
            'pattern': '^[0-9]{1,20}$',
            'required': 'true',
        }},
        {'MY/SWIFT/*/USD/*': {
            'pattern': '^[0-9]{5,19}$',
            'required': 'true',
        }},
        {'MY/*/*/*/*': {
            'pattern': '^[0-9]{5,17}$',
            'required': 'true',
        }},
        {'NG/*/*/*/*': {
            'pattern': '^[0-9]{10}$',
            'required': 'true',
        }},
        {'NZ/*/*/NZD/*': {
            'pattern': '^[0-9]{15,16}$',
            'required': 'true',
        }},
        {'NZ/*/*/*/*': {
            'pattern': '^[0-9A-Za-z]{1,60}$',
            'required': 'true',
        }},
        {'PH/*/*/*/*': {
            'pattern': '^[0-9]{8,16}$',
            'required': 'true',
        }},
        {'SG/LOCAL/GIRO FAST/*/*': {
            'pattern': '^[0-9A-Za-z]{7,17}$',
            'required': 'true',
        }},
        {'SG/LOCAL/RTGS/*/*': {
            'pattern': '^[0-9A-Za-z]{6,23}$',
            'required': 'true',
        }},
        {'SG/SWIFT/*/*/*': {
            'pattern': '^[0-9A-Za-z]{6,23}$',
            'required': 'true',
        }},
        {'TH/LOCAL/*/*/*': {
            'pattern': '^[0-9]{7,12}$',
            'required': 'true',
        }},
        {'TH/SWIFT/*/*/*': {
            'pattern': '^[0-9]{7,15}$',
            'required': 'true',
        }},
        {'TW/*/*/*/*': {
            'pattern': '^[0-9]{8,20}$',
            'required': 'true',
        }},
        {'US/LOCAL/ACH/*/*': {
            'pattern': '^[0-9]{1,17}$',
            'required': 'true',
        }},
        {'US/LOCAL/FEDWIRE/*/*': {
            'pattern': '^[0-9]{1,26}$',
            'required': 'true',
        }},
        {'US/SWIFT/*/*/*': {
            'pattern': '^[0-9A-Za-z]{1,26}$',
            'required': 'true',
        }},
        {'VN/*/*/*/*': {
            'pattern': '^[0-9]{1,20}$',
            'required': 'true',
        }},
        {'LK, BD, NP/*/*/*/*': {
            'pattern': '^[0-9A-Za-z]{1,50}$',
            'required': 'true',
        }},
        {'TZ, NA, UA, BZ, RU, ME/SWIFT/*/*/*': {
            'pattern': '^[0-9A-Za-z]{1,50}$',
            'required': 'true',
        }},

    ],
    'account_name': [
        {'KR/LOCAL/*/*/*': {
            'pattern': "^[a-zA-Z0-9!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~]{2,100}$",
            'required': 'true',
        }},
        {'CN/LOCAL/*/*/*': {
            'pattern': '^[\〇\一-\鿿\㐀-\䶿\豈-\﫿\⼀-\⿕\⺀-\⻳\＂\＃\＄\％\＆\＇\（\）\＊\＋\，\－\／\：\；\＜\＝\＞\＠\［\＼\］\＾\
     ＿\｀\｛\｜\｝\～\｟\｠\｢\｣\､\　\、\〃\〈\〉\《\》\「\」\『\』\【\】\〔\〕\〖\〗\〘\〙\〚\〛\〜\〝\〞\〟\〰\〾\〿\–\—\‘\’\‛\
     “\”\„\‟\…\‧\﹏\﹑\﹔\·\！\？\｡\。]{2,50}$',
            'required': 'true',
        }},
        {'PK, TR, LK, BD, NP/*/*/*/*': {
            'pattern': "^[a-zA-Z0-9!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~]{2,100}$",
            'required': 'true',
        }},
        {'ID, IN, MY, PH, TH, VN/*/*/*/*': {
            'pattern': "^[a-zA-Z0-9!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~]{2,100}$",
            'required': 'true',
        }},
        {'TZ, NA, UA, BZ, RU, ME/SWIFT/*/*/*': {
            'pattern': "^[a-zA-Z0-9!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~]{2,100}$",
            'required': 'true',
        }},
    ],
    'account_routing_type1':[
        {'AU/LOCAL/BANK_TRANSFER/*/*': {
            'pattern': '^bsb$',
            'required': 'true',
        }},
        {'AU/LOCAL/BPAY/*/*': {
            'pattern': '^bpay_biller_code$',
            'required': 'true',
        }},
        {'CA/LOCAL/*/*/*': {
            'pattern': '^routing_number$',
            'required': 'true',
        }},
        {'CN/LOCAL/*/*/*': {
            'pattern': '^cnaps$',
            'required': 'true',
        }},
        {'GB, GG, IM, JE/LOCAL/*/GBP/*': {
            'pattern': '^sort_code$',
            'required': 'true',
        }},
        {'HK/LOCAL/ACH,FPS/*/*': {
            'pattern': '^bank_code$',
            'required': 'true',
        }},
        {'JP/LOCAL/*/*/*': {
            'pattern': '^zengin_code$',
            'required': 'true',
        }},
        {'KR, IN, NP/LOCAL/*/*/*': {
            'pattern': '^bank_code$',
            'required': 'true',
        }},
        {'US/LOCAL/ACH, FEDWIRE/*/*': {
            'pattern': '^aba$',
            'required': 'true',
        }},
        {'BD/LOCAL/*/*/*': {
            'pattern': '^routing_number$',
            'required': 'true',
        }}
    ],
    'account_routing_type2':[
        {'AU/LOCAL/BPAY/*/*': {
            'pattern': '^bpay_customer_reference$',
            'required': 'true',
        }}
    ],
    'account_routing_value1': [
        {'AU/LOCAL/BANK_TRANSFER/*/*': {
            'pattern': '^[0-9]{6}$',
            'required': 'true',
        }},
        {'AU/LOCAL/BPAY/*/*': {
            'pattern': '^[0-9]{1,10}$',
            'required': 'true',
        }},
        {'CA/LOCAL/BANK_TRANSFER/*/*': {
            'pattern': '^[0-9]{9}$',
            'required': 'true',
        }},
        {' GB, GG, IM, JE /LOCAL/*/GBP/*': {
            'pattern': '^[0-9]{6}$',
            'required': 'true',
        }},
        {'HK/LOCAL/ACH, FPS/*/*': {
            'pattern': '^[0-9]{3}$',
            'required': 'true',
        }},
        {'IN/LOCAL/*/*/*': {
            'pattern': '^[0-9A-Za-z]{11}$',
            'required': 'true',
        }},
        {'JP/LOCAL/*/*/*': {
            'pattern': '^[0-9]{7}$',
            'required': 'true',
        }},
        {'KR/LOCAL/*/*/*': {
            'pattern': '^[0-9]{3}$',
            'required': 'true',
        }},
        {'US/LOCAL/ACH,FEDWIRE/*/*': {
            'pattern': '^[0-9]{9}$',
            'required': 'true',
        }},
        {'BD/LOCAL/*/*/*': {
            'pattern': '^[0-9]{9}$',
            'required': 'true',
        }},
        {'CN/LOCAL/*/CNY/*': {
            'pattern': '^[0-9]{12}$',
            'required': 'true',
        }},


    ],
    'account_routing_value2': [
        {'AU/LOCAL/BPAY/*/*': {
            'pattern': '^[0-9]{1,20}$',
            'required': 'true',
        }},
    ],
    'state': [
        {'AS,AU,BO,BR,BZ,CA,CC,CL,CN,CO,CR,CU,CX,ES,ET,FM,GU,IN,JO,KH,IR,IT,KZ,ME,MK,MP,MX,MY,NA,NF,NG,NP,PA,PR,PW,RU,'
         'SV,TH,TR,TZ,UA,UM,US,VE,VI,VN/*/*/*/*': {
            'pattern': '^.{1,50}$',
            'required': 'true',
        }},
    ],
    'postcode': [
        {'AD,AF,AI,AL,AM,AR,AS,AT,AU,AX,AZ,BA,BB,BD,BE,BG,BH,BL,BM,BN,BR,BT,BY,BZ,CA,CC,CH,CI,CL,CN,CO,CR,CU,CV,CX,CY,'
         'CZ,DE,DK,DO,DZ,EC,EE,EG,ES,ET,FI,FK,FM,FO,FR,GA,GB,GE,GF,GG,GI,GL,GN,GP,GR,GS,GT,GU,GW,HM,HN,HR,HT,HU,ID,IE,'
         'IL,IM,IN,IO,IQ,IR,IS,IT,JE,JO,JP,KE,KG,KH,KN,KR,KW,KY,KZ,LA,LI,LK,LR,LS,LT,LU,LV,MA,MC,MD,ME,MF,MG,MH,MK,MM,'
         'MN,MP,MQ,MS,MT,MU,MV,MX,MY,MZ,NA,NC,NE,NF,NG,NL,NO,NP,NU,NZ,OM,PA,PE,PF,PG,PH,PK,PL,PM,PN,PR,PT,PW,PY,RE,RO,'
         'RS,RU,SA,SD,SE,SG,SH,SI,SJ,SK,SM,SN,SO,SV,SZ,TC,TH,TJ,TM,TN,TR,TT,TW,TZ,UA,UM,US,UY,UZ,VC,VE,VG,VI,VN,WF,WS,'
         'YT,ZA,ZM/*/*/*/*': {
            'pattern': '^.{1,50}$',
            'required': 'true',
        }},
    ],

}
