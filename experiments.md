### Klasszifikáció

|                                 | precision          | recall             | accuracy           | gpu* inference | cpu** inference |
|---------------------------------|--------------------|--------------------|--------------------|----------------|-----------------|
| NYTK/PULI-GPT-3SX finomhangolva | 0.776              | 0.878              | 0.966              |                |                 |
| llama 7B finomhangolva          | 0.860              | 0.810              | 0.971              | 1.90 it/s      | 0.03878 it/s    |
| huBERT                          | 0.739              | 0.950              | 0.963              | 126.85 it/s    | 7.10 it/s       |

\* Nvidia 3060 12gb

** Ampere A1 (Oracle cloud)

### Kulcsszó generálás, NYTK/PULI-GPT-3SX, finomhangolás, szöveg törzs

                                            precision    recall  f1-score   support

                                                 0.89      0.60      0.72       130
                                    uszoda       0.00      0.00      0.00         0
                                dohányipar       0.40      0.50      0.44         4
                                   stadion       0.50      0.60      0.55         5
                                sikkasztás       0.92      0.69      0.79        32
                                 takarítás       0.67      0.50      0.57         4
                               diplomatika       0.00      0.00      0.00         0
                                        tú       0.00      0.00      0.00         0
                                adóhatóság       0.00      0.00      0.00         0
                                   bíróság       0.29      0.39      0.33        18
         lekenyerezés / presztízsberuházás       0.00      0.00      0.00        12
                                  sikerdíj       0.50      0.50      0.50         2
                             adatvizsgálat       0.00      0.00      0.00         0
                               vesztegetés       0.82      0.51      0.63        88
                     biztosítók/biztosítás       1.00      1.00      1.00         4
                        jármű / gépgyártás       0.00      0.00      0.00         1
                               elfogultság       0.00      0.00      0.00         7
                        közlekedési tender       0.00      0.00      0.00         0
                                 protekció       0.00      0.00      0.00        16
                           tiltott verseny       0.00      0.00      0.00         0
                                   szociál       0.00      0.00      0.00         9
                 hivatali kötelességszegés       0.00      0.00      0.00         0
                 választások - népszavazás       0.71      0.31      0.43        16
                                      hird       0.00      0.00      0.00         0
                                     erőmű       0.50      0.33      0.40         3
                                 pénzmosás       0.75      0.38      0.50         8
                              adóamnesztia       0.00      0.00      0.00         0
          versenyfelügyeleti eljárás (GVH)       0.67      0.33      0.44         6
                             pótmagánvádas       0.00      0.00      0.00         0
                           befolyás vásárl       0.00      0.00      0.00         0
                                    csalás       0.51      0.46      0.48        70
                               károsultság       0.00      0.00      0.00         0
                                      tanú       0.00      0.00      0.00         0
                                 átlagosan       0.00      0.00      0.00         0
                                 cukoripar       0.00      0.00      0.00         1
                                     metró       0.69      0.82      0.75        11
                       adatvédelmi eljárás       0.00      0.00      0.00         0
                           nyomásgyakorlás       0.00      0.00      0.00        13
                          egészségturizmus       0.00      0.00      0.00         1
                            műemlékvédelem       0.00      0.00      0.00         5
                             NAV-vizsgálat       0.00      0.00      0.00         0
befolyással üzérkedés - befolyás vásárlása       0.56      0.50      0.53        10
                                  útépítés       1.00      0.20      0.33        10
                                     közmű       0.00      0.00      0.00         2
                                  bûntetés       0.00      0.00      0.00         0
                                   ajándék       0.00      0.00      0.00         5
                                 ügyészség       0.00      0.00      0.00         5
                                        bű       0.00      0.00      0.00         0
                            szerencsejáték       1.00      0.67      0.80         9
                              üzleti etika       0.00      0.00      0.00         2
                                       OTP       0.00      0.00      0.00         0
                   bennfentes kereskedelem       1.00      1.00      1.00         2
                        kényszerintézkedés       0.00      0.00      0.00         0
                           közokirat-hamis       0.00      0.00      0.00         0
                               üzemeltetés       0.00      0.00      0.00         1
                                       lős       0.00      0.00      0.00         0
                                     hírek       0.00      0.00      0.00         0
                             nav-vizsgálat       0.00      0.00      0.00         4
                                biztosítók       0.00      0.00      0.00         0
                                       íté       0.00      0.00      0.00         0
                                 hitelezés       0.67      0.12      0.20        17
                                   adósság       0.25      0.09      0.13        11
                                   nyugdíj       0.50      0.25      0.33         4
                                  vegyipar       0.00      0.00      0.00         1
                                 diplomata       0.00      0.00      0.00         0
          vagyonosodás / vagyonnyilatkozat       0.89      0.29      0.43        56
                        fegyver - hadiipar       0.00      0.00      0.00         1
                               csődbűntett       0.67      0.29      0.40         7
                     túlárazás / pénznyelő       0.09      0.18      0.12        22
                              államadósság       0.00      0.00      0.00         2
              adózás - költségvetési hiány       0.00      0.00      0.00         0
                      társadalombiztosítás       0.00      0.00      0.00         0
                                 katonaság       0.00      0.00      0.00         0
                                  tudomány       0.75      0.30      0.43        10
                                   bűnszöv       0.00      0.00      0.00         0
                                 strómanok       0.75      0.75      0.75         4
                          versenyfelületek       0.00      0.00      0.00         0
                                történelem       0.00      0.00      0.00         2
                              önkormányzat       0.51      0.70      0.59       125
                               végrehajtás       1.00      0.50      0.67         4
                                 hanyagság       1.00      0.50      0.67         4
                               kiszervezés       0.00      0.00      0.00         7
                           állattenyésztés       0.00      0.00      0.00         1
                                       PPP       0.00      0.00      0.00         2
                                 forgóajtó       0.00      0.00      0.00         1
                                    óvadék       0.00      0.00      0.00         2
                                  kémkedés       1.00      0.25      0.40         4
                             adóellenőrzés       0.00      0.00      0.00         0
                           versenyfelülete       0.00      0.00      0.00         0
                                  pályázat       0.35      0.45      0.40        80
                               bűnpártolás       0.00      0.00      0.00         2
                                 hírszerző       0.00      0.00      0.00         0
                  tiltott állami támogatás       1.00      0.67      0.80         3
            számviteli fegyelem megsértése       0.00      0.00      0.00         3
                       közokirat-hamisítás       0.71      0.44      0.55        27
                                    adóügy       0.00      0.00      0.00         0
                                jogalkotás       0.49      0.37      0.42        49
                               nyelvvizsga       0.00      0.00      0.00         1
                                 túlárazás       0.00      0.00      0.00         0
                              adatigénylés       0.20      0.29      0.24        14
                                 üzletszer       0.00      0.00      0.00         0
                                 közbeszer       0.00      0.00      0.00         0
                            hírszerkesztés       0.00      0.00      0.00         0
                                    közbes       0.00      0.00      0.00         0
                                   civilek       0.59      0.38      0.47        26
                       hatalomkoncentráció       0.24      0.36      0.29        14
                                  művészet       0.00      0.00      0.00         0
                                       köz       0.00      0.00      0.00         0
                                  pazarlás       0.00      0.00      0.00         0
                        kultúra - művészet       0.33      0.09      0.14        11
                   befolyással üzérkedés -       0.00      0.00      0.00         0
                         adósságtörlesztés       0.00      0.00      0.00         0
                                   energia       0.57      0.74      0.64        34
                                  hirdetés       0.36      0.38      0.37        26
                            idegenforgalom       0.62      0.50      0.56        20
                                  covid-19       1.00      0.40      0.57         5
                                  masszázs       0.00      0.00      0.00         0
                        repülőtér / légügy       0.00      0.00      0.00         3
                                adóhivatal       0.00      0.00      0.00         0
      befolyás vásárlása - befolyás vásárl       0.00      0.00      0.00         0
                          ingyenes laptop,       0.00      0.00      0.00         0
                                   távozás       0.00      0.00      0.00         0
                                      kína       0.00      0.00      0.00         0
                                  zsarolás       1.00      0.33      0.50         3
         jogosulatlan pénzügyi tevékenység       0.00      0.00      0.00         1
                            foglalkoztatás       0.00      0.00      0.00        27
                hatalommal való visszaélés       0.00      0.00      0.00         3
           hamis magánokirat felhasználása       0.20      0.33      0.25         3
                                       ker       0.00      0.00      0.00         0
                                   kartell       0.00      0.00      0.00         0
       vagyonátadás / közérdekű alapítvány       0.00      0.00      0.00         3
                                 játszótér       0.00      0.00      0.00         1
                           hivatali vissza       0.00      0.00      0.00         0
                                      titk       0.00      0.00      0.00         0
                       pénzügyi felügyelet       0.00      0.00      0.00         0
                                        ro       0.00      0.00      0.00         0
                          vagyongyarapodás       0.00      0.00      0.00         0
                      adatok titkosítására       0.00      0.00      0.00         0
                          fegyelmi eljárás       0.00      0.00      0.00         0
           állami / önkormányzati vállalat       0.74      0.37      0.50        75
                          államtitoksértés       0.00      0.00      0.00         2
                                  ügyvédek       0.67      0.17      0.27        12
                 rágalmazás / becsületsért       0.00      0.00      0.00         0
                                koncesszió       1.00      0.40      0.57        10
                               informatika       0.73      0.42      0.53        19
                                 távközlés       0.00      0.00      0.00         1
                                        bí       0.00      0.00      0.00         0
                                      túlá       0.00      0.00      0.00         0
                              üzleti titok       0.00      0.00      0.00         7
                                 adatbázis       0.00      0.00      0.00         0
                              nemzeti park       0.00      0.00      0.00         1
                                  autóipar       0.00      0.00      0.00         0
                                       NFT       0.00      0.00      0.00         1
                               egészségügy       0.90      0.53      0.67        36
                              adózás - adó       0.00      0.00      0.00         0
                                szakszerve       0.00      0.00      0.00         0
                                     lobbi       0.50      0.18      0.27        11
                             tanulmányírás       1.00      0.25      0.40         8
                                 repülőgép       0.00      0.00      0.00         0
                                kábítószer       1.00      0.50      0.67         2
                             adósságtörlés       0.00      0.00      0.00         0
                           titkosszolgálat       0.33      0.45      0.38        11
                                 építőipar       0.47      0.76      0.58        74
                           hűtlen kezelés,       0.00      0.00      0.00         0
                                pénzátadás       0.00      0.00      0.00         0
                                    gazdál       0.00      0.00      0.00         0
                                   napelem       0.00      0.00      0.00         0
                                     lopás       0.00      0.00      0.00         0
                                    jegyző       1.00      0.25      0.40         4
                                 vendéglát       0.00      0.00      0.00         0
                                 képviselő       0.00      0.00      0.00         0
                      hivatali visszaélés,       0.00      0.00      0.00         0
               hamis védettségi igazolvány       0.00      0.00      0.00         0
                            KEHI-vizsgálat       1.00      0.10      0.18        10
                                    vízügy       0.00      0.00      0.00         1
                                     repül       0.00      0.00      0.00         0
                 2021-2027-es uniós ciklus       0.00      0.00      0.00         1
                                    tőzsde       0.14      0.20      0.17         5
                   fogyasztóvédelmi bírság       0.00      0.00      0.00         0
                           Balaton-sztorik       0.40      0.67      0.50         3
                                      maff       0.00      0.00      0.00         0
                             hulladéküzlet       1.00      0.67      0.80         6
                       hulladékgazdálkodás       0.00      0.00      0.00         0
                             önkormányzat,       0.00      0.00      0.00         0
                         jó hírnév sérelme       0.00      0.00      0.00         3
                                        PR       0.45      0.41      0.43        22
                                  hivatali       0.00      0.00      0.00         0
                         kiemelt beruházás       0.00      0.00      0.00         1
                                   rokonok       0.27      0.28      0.27        58
               bűnszervezet / bűnszövetség       0.25      0.38      0.30        13
                              tényfeltárás       0.00      0.00      0.00         0
                             OBH-vizsgálat       0.00      0.00      0.00         0
                                diplomácia       0.62      0.28      0.38        18
                            OLAF-vizsgálat       0.71      0.91      0.80        11
                   jogellenes fogva tartás       0.00      0.00      0.00         0
                               jogosítvány       0.00      0.00      0.00         0
                                      adat       0.00      0.00      0.00         0
                               magánokirat       0.00      0.00      0.00         0
                                        be       0.00      0.00      0.00         0
                      háborús nyerészkedés       0.00      0.00      0.00         0
                              privatizáció       0.56      0.40      0.47        35
                               adatszerzés       0.00      0.00      0.00         0
                                   pártfin       0.00      0.00      0.00         0
               rágalmazás / becsületsértés       0.00      0.00      0.00         9
                                    ítélet       0.00      0.00      0.00         0
                        környezetkárosítás       1.00      0.17      0.29         6
                            adatgyanúsítás       0.00      0.00      0.00         0
                                     pápák       0.00      0.00      0.00         0
                              közvilágítás       0.00      0.00      0.00         2
                                  tőkealap       0.50      0.33      0.40         3
                    adóhivatalt/adóhivatal       0.00      0.00      0.00         0
                                         t       0.00      0.00      0.00         0
                             adózás - adó,       0.00      0.00      0.00         0
                             ítélet/döntés       0.36      0.57      0.44        67
                       műsor / filmgyártás       0.00      0.00      0.00         6
                                   ítélet/       0.00      0.00      0.00         0
                                  juttatás       0.46      0.64      0.54        53
                            visszajuttatás       0.00      0.00      0.00         3
                            hanyag kezelés       0.00      0.00      0.00         0
                                  bûnösség       0.00      0.00      0.00         0
          állami/önkormányzati szerződések       0.12      0.02      0.03        54
                                közlekedés       0.30      0.33      0.32        30
                                   hajózás       0.00      0.00      0.00         3
                               házi őrizet       0.00      0.00      0.00         0
                             végkielégítés       1.00      0.33      0.50         6
                            könyvvizsgálás       0.00      0.00      0.00         3
             hatalomwekkel való visszaélés       0.00      0.00      0.00         0
                                   túláraz       0.00      0.00      0.00         0
                                   lósport       0.00      0.00      0.00         1
                                 klientúra       0.43      0.52      0.47       145
                            versenyhivatal       0.00      0.00      0.00         0
                               őrzés-védés       1.00      0.40      0.57         5
             hatalomkoncentrációs jelenség       0.00      0.00      0.00         0
                              kereskedelem       0.29      0.46      0.35        13
                        választások - néps       0.00      0.00      0.00         0
                                       tan       0.00      0.00      0.00         0
                                bennfentes       0.00      0.00      0.00         0
                               gazdálkodás       0.43      0.19      0.27       103
                                     közle       0.00      0.00      0.00         0
                      hirdetési tanácsadás       0.00      0.00      0.00         0
                                      atom       0.85      0.85      0.85        13
                     magánokirat-hamisítás       0.67      0.38      0.48        16
                                   kaszinó       0.00      0.00      0.00         0
                              mezőgazdaság       0.59      0.54      0.57        35
               felszámolás - végelszámolás       0.67      0.33      0.44         6
        befektetési bankok - pénzintézetek       0.00      0.00      0.00         0
                                    bírság       0.38      0.33      0.35         9
                           szemétszállítás       0.00      0.00      0.00         0
                                közoktatás       0.00      0.00      0.00         0
                         pártfinanszírozás       0.31      0.38      0.34        29
                              közbeszerzés       0.56      0.85      0.67       131
                 2014-2020-as uniós ciklus       0.00      0.00      0.00         8
                            hűtlen kezelés       0.82      0.86      0.84        87
                              közigazgatás       0.00      0.00      0.00        11
                                  közmédia       0.00      0.00      0.00         0
                                 autópálya       0.00      0.00      0.00         5
                            lélegeztetőgép       0.00      0.00      0.00         1
                        hirdetési pályázat       0.00      0.00      0.00         0
                                versenyügy       0.00      0.00      0.00         0
                             szakszervezet       0.00      0.00      0.00         1
                                   plágium       1.00      0.78      0.88         9
                                         p       0.00      0.00      0.00         0
                                     orvos       0.00      0.00      0.00         0
                              kártalanítás       0.50      0.17      0.25         6
                                   gazdálk       0.00      0.00      0.00         0
                                 bűnszerve       0.00      0.00      0.00         0
                        adósságvégrehajtás       0.00      0.00      0.00         0
                             brókerbotrány       0.00      0.00      0.00         0
                                       adó       0.10      0.75      0.18        16
                             antikorrupció       0.74      0.45      0.56        44
         versenyfelügyeleti eljárás (GVH),       0.00      0.00      0.00         0
                                honvédelem       0.00      0.00      0.00         1
                                titkosítás       0.00      0.00      0.00         0
                                   kemping       0.00      0.00      0.00         0
                                    utazás       0.56      0.77      0.65        13
             piacfelügyeleti eljárás (MNB)       0.00      0.00      0.00         2
                                 repülőtér       0.00      0.00      0.00         0
                                 gazdálkod       0.00      0.00      0.00         0
                                  Facebook       0.00      0.00      0.00         0
                        hirdetési rendszer       0.00      0.00      0.00         0
                    hallgatói önkormányzat       0.00      0.00      0.00         2
                    bankok - pénzintézetek       0.49      0.73      0.59        33
                            önkormányzatok       0.00      0.00      0.00         0
                 tiltott pártfinanszírozás       0.00      0.00      0.00         0
                             közbeszerzés,       0.00      0.00      0.00         0
                                 hamis vád       0.00      0.00      0.00         1
                                 mulasztás       0.00      0.00      0.00         1
                                    háttér       0.27      0.22      0.24        95
                      vízum-állampolgárság       0.00      0.00      0.00         3
             adózás - költségvetési csalás       0.00      0.00      0.00         0
                                   fémipar       0.00      0.00      0.00         2
                            élelmiszeripar       0.00      0.00      0.00         4
                               vendéglátás       0.80      0.40      0.53        10
                                  filmipar       0.00      0.00      0.00         0
                       napelem / megújulók       0.00      0.00      0.00         3
                                      átlá       0.00      0.00      0.00         0
                                    adózás       0.00      0.00      0.00         0
                                 támogatás       0.48      0.50      0.49       111
                                temetkezés       0.00      0.00      0.00         3
                           háttérintézmény       0.00      0.00      0.00         0
                                      párt       0.00      0.00      0.00         0
                            hütlen kezelés       0.00      0.00      0.00         0
                                hírszerzés       0.00      0.00      0.00         0
                                      priv       0.00      0.00      0.00         0
                                     média       0.77      0.65      0.70        51
              jogosulatlan gazdasági előny       0.00      0.00      0.00         5
                     szolgálati visszaélés       0.00      0.00      0.00         2
                          környezetvédelem       0.00      0.00      0.00         9
                                államtitok       0.00      0.00      0.00         2
                              mentelmi jog       0.43      0.33      0.38         9
                                   oktatás       0.59      0.52      0.55        33
                                    trafik       0.00      0.00      0.00         0
                                tanácsadás       0.67      0.54      0.60        26
                            ÁSZ-ellenőrzés       0.00      0.00      0.00         3
                jogosulatlan pénzügyi tevé       0.00      0.00      0.00         0
                             hamis tanúzás       0.00      0.00      0.00         0
                                   zugírás       0.00      0.00      0.00         0
                                 adócsalás       0.00      0.00      0.00         0
                    magánokirat-hamisítás,       0.00      0.00      0.00         0
                                 kárpótlás       0.50      1.00      0.67         1
                                    egyház       1.00      0.11      0.20         9
                          túlárazás / pénz       0.00      0.00      0.00         0
                                      olaj       0.00      0.00      0.00         0
          adócsalás - költségvetési csalás       0.53      0.75      0.62        57
                           katonai bűnözés       0.00      0.00      0.00         0
                                  ingatlan       0.51      0.82      0.63       120
                                  vadászat       0.00      0.00      0.00         1
                                  offshore       0.79      0.63      0.70        35
                                     sport       0.80      0.78      0.79        63
                     örökségvédelmi dolgok       0.00      0.00      0.00         0
                                     vasút       1.00      0.50      0.67         8
                                 adásvétel       0.00      0.00      0.00         0
                                       TAO       0.00      0.00      0.00         0
                                  hálapénz       0.86      0.75      0.80         8
                               államosítás       0.00      0.00      0.00         2
                          hatalomkoncentrá       0.00      0.00      0.00         0
                                   pénzügy       0.00      0.00      0.00         0
                           antiszemitizmus       0.00      0.00      0.00         0
                               adatgyűjtés       0.05      0.40      0.10         5
                              kényszerítés       0.00      0.00      0.00         1
                                         k       0.00      0.00      0.00         0
                                  parkolás       0.83      1.00      0.91         5
                        papír és irodaszer       0.00      0.00      0.00         1
                                  engedély       0.00      0.00      0.00        13
                            titokminiszter       0.00      0.00      0.00         0
                                 NER HOTEL       0.40      0.50      0.44         8
                                    maffia       0.33      0.29      0.31         7
                                      pály       0.00      0.00      0.00         0
            adózás - költségvetési csalás,       0.00      0.00      0.00         0
                              magánokirat-       0.00      0.00      0.00         0
                            olaf-vizsgálat       0.00      0.00      0.00         0
                         vizsgálóbizottság       0.00      0.00      0.00         5
                      kampányfinanszírozás       0.67      0.69      0.68        26
                                  erdészet       0.00      0.00      0.00         2
                       hivatali visszaélés       0.37      0.52      0.43        27
                        befolyás vásárlása       0.00      0.00      0.00         0
                                   kastély       0.57      0.80      0.67         5
                               Natura 2000       0.00      0.00      0.00         0
                       rendezvényszervezés       0.00      0.00      0.00         9
                                   adomány       0.00      0.00      0.00         0
                               könyvkiadás       0.00      0.00      0.00         1
                                      hűtő       0.00      0.00      0.00         0
                              adósságvetés       0.00      0.00      0.00         0
                              átláthatóság       0.30      0.50      0.38       113
                       összeférhetetlenség       0.50      0.10      0.17        20
                                      vers       0.00      0.00      0.00         0
                               infografika       0.00      0.00      0.00         2
                                   hivatal       0.00      0.00      0.00         0
               versenykorlátozás - kartell       0.00      0.00      0.00        16
                    (igazságügyi) szakértő       0.00      0.00      0.00         1
                               adatvédelem       0.15      0.86      0.26         7
                                csempészet       0.00      0.00      0.00         5
                                      túra       0.00      0.00      0.00         0
                                        EU       0.44      0.69      0.53        51

                                 micro avg       0.46      0.47      0.47      3620
                                 macro avg       0.19      0.15      0.15      3620
                              weighted avg       0.51      0.47      0.46      3620
                               samples avg       0.53      0.52      0.49      3620

