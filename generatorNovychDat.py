import requests
from bs4 import BeautifulSoup

# pip install requests beautifulsoup4 lxml
# toto sa d apouzit na bratislavsku zoo, v 'h4', class_='title' maju ulozene vsetky zvierata v lexikone na stranke https://www.zoobratislava.sk/nase-zvierata/lexikon-zvierat/
# pre zoo zlin sa to da upravit na https://www.zoozlin.eu/zvirata-dle-abecedy/ a <h3 class="article-headline"> - maju tak o polovicu zvierat menej, to bude lepsie
#toto prislo z bratislavy

####['Adax núbijský', 'Agama bradatá', 'Antilopa nilgau', 'Antilopa vraná', 'Ara zelená', 'Bažant diamantový', 'Bažant zlatý', 'Bažant zlatý broskyňový', 'Belaňa tundrová', 'Bichirek kalabarský', 'Brazílska červeno-biela tarantula ', 'Chocholačka bielooká', 'Daman stromový', 'Daniel škvrnitý', 'Dikdik Kirkov', 'Dikobraz bielochvostý', 'Diviak lesný', 'Diviak visajanský', 'Drozd čiernoprsý', 'Emu hnedý', 'Felzuma madagaskarská', 'Fretka domáca', 'Gekón obrovský', 'Gekončík nočný', 'Gibon zlatolíci', 'Hlaholka severská', 'Holub domáci - brčkáň', 'Holub domáci - francúzsky mondén', 'Holub domáci - pomoranský hrvoliak', 'Holub domáci - slovenský hrvoliak žltý', 'Hrdlička chichotavá', 'Hrdlička perlokrká', 'Hrdzavka potápavá', 'Hrošík libérijský', 'Hus labutia - domáca', 'Ibis červený', 'Indický bežec (kačica domáca)', 'Jaguár americký', 'Jeleň európsky', 'Kanárik domáci', 'Kariama červenozobá', 'Kengura červená', 'Kôň domáci', 'Kôň Przewalského', 'Koralovka červená', 'Koralovka kalifornská', 'Korela chochlatá', 'Korytnačka leopardia', 'Korytnačka uhoľná', 'Kosmáč striebristý', 'Kosmáč trpasličí', 'Koza domáca holandská', 'Koza domáca kamerunská', 'Kozorožec alpský', 'Králik domáci', 'Kraska červenozobá', 'Krkavec čierny', 'Krokodíl čelnatý', 'Kudu malý', 'Kulan turkménsky', 'Kura domáca - bregovska dzhinka', 'Kurička bieločelá', 'Kuvik obyčajný', 'Labuť čierna', 'Lama alpaka', 'Lama krotká', 'Leguán obojkový', 'Lemur kata', 'Leňoch dvojprstý', 'Leopard cejlónsky', 'Lev juhoafrický', 'Lori trojfarebný', 'Lyžičiar ružovonohý', 'Mačiak Brazzov', 'Mačka maloškvrnná', 'Makak magot', 'Mara stepná', 'Medveď hnedý', 'Mnohonôžka obria', 'Modraňa strakovitá', 'Monal lesklý', 'Morča domáce - Skinny morča', 'Morka očkatá', 'Mrenka nádherná', 'Mrenka pakistánska', 'Mrenka siamská', 'Muflón lesný', 'Muntžak malý', 'Myš zebrovaná', 'Myšiak štvorfarebný', 'Nandu pampový', 'Neónka červená', 'Nosáľ červený', 'Nosorožec tuponosý južný', 'Okáč činkvis', 'Orangutan sumatriansky', 'Oryx arabský', 'Osmák degu', 'Ovca domáca ouessantská', 'Ovca domáca valašská', 'Pancierniček malý', 'Pancierníček panda', 'Pancierniček smaragdový', 'Pancierniček Sterbov', 'Panda červená', 'Papagáj červenokrídly', 'Papagáj kráľovský', 'Pásavec štetinový', 'Páv korunkatý', 'Pelikán ružový', 'Perlička supia', 'Pes ušatý', 'Pichľavec ozdobný', 'Piesočník pestrý', 'Piraňa Nattererova', 'Pižmovka domáca', 'Plameniak ružový', 'Plamienka driemavá', 'Pôtik kapcavý', 'Potkanokengura králikovitá', 'Prísavník', 'Pštros africký', 'Pytón kráľovský', 'Pytón tmavý', 'Pytón zelený', 'Rohatka ozdobná', 'Rosnička austrálska', 'Rozela penantová', 'Rybárik smejivý', 'Rys kanadský', 'Rys ostrovid', 'Saimiri vevericovitý', 'Scink šalamúnsky', 'Šimpanz učenlivý', 'Sitatunga západná', 'Somár domáci', 'Stonožka vietnamská', 'Šťúr obrovský', 'Šťúr obrovský', 'Sumec sklovitý', 'Surikata vlnkavá', 'Takin zlatý', 'Tamarín pinčí', 'Tamarín žltoruký', 'Ťava dvojhrbá', 'Tetra konžská', 'Tetra krvavá', 'Tetra žiarivá', 'Tragopan modrolíci', 'Tráviar ružovobruchý', 'Urzon kanadský', 'Užovka červená', 'Varan ostnatochvostý', 'Veverica kanadská', 'Vlk eurázijský', 'Vodárka lečve kafuenská', 'Výr skalný sibírsky', 'Zebra Chapmanova', 'Zebrička červenozobá', 'Zemnárka krátkozobá', 'Žeriav japonský', 'Žirafa Rothschildova', 'Zubor európsky']
####['https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Addax/adax-nubijsky_zoo-bratislava_profile__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Agama-bradata/Agama-bradata_TH70019__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/South-African-sable-antelope/antilopa-nilgau-c__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/South-African-sable-antelope/antilopa-vrana-c__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/DSC9053__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Harriss-hawk/DSC_0541_2__FillMaxWzU0MCw1NDBd.JPG', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Monal-leskly/bazant_zlaty1__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Monal-leskly/Bazant-zlaty-broskynovy-VT-6__FillMaxWzU0MCw1NDBd.12.2022-4.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Belana-tundrova/belana-tundrova__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Ryby/Bichirek-kalabarsky/bichirek_kalabarsky1__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Bezstavovce/Brazilska-cerveno-biela-tarantula-/tarantula__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Ferruginous-duck/chochlacka_bielooka2__FillMaxWzU0MCw1NDBd.JPG', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/South-African-sable-antelope/Dizajn-bez-nazvu-12__FillMaxWzU0MCw1NDBd.png', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/South-African-sable-antelope/DSC1763__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Dikdik-Kirkov/dikdik-kirkov_zoo-bratislava_profile__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Dikobraz-bielochvosty/dikobraz-bielochvosty_zoo-bratislava_profile__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Diviak-visajansky/diviak-lesny_zoo-bratislava_profile__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Diviak-visajansky/Diviak-visajansky_zoo-bratislava_profile__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Drozd-ciernoprsy/blackbird__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Emu/TH75824__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Plazy-a-obojzivelniky/Felzuma-madagaskarska/felzuma-foto__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Fretka-domaca/Fretka-domaca-16__FillMaxWzU0MCw1NDBd.11.2022-VT-4.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Plazy-a-obojzivelniky/Gekon-obrovsky/gekon-obrobvsky__FillMaxWzU0MCw1NDBd.JPG', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Plazy-a-obojzivelniky/Gekoncik-nocny/head-of-leopard-gecko-eublepharis-macularius-in-front-of-black-background-MJOF000291__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Gibon-zlatolici/gibon-zlatolici_profile_zoo-bratislava__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Common-goldeneye/Hlaholka-severska-archiv-ZOO-vtak-3__FillMaxWzU0MCw1NDBd.JPG', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Holub-domaci-slovensky-hrvoliak-modry/Holub-domaci-brckan-1__FillMaxWzU0MCw1NDBd.JPG', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Holub-domaci-slovensky-hrvoliak-zlty/Holub-domaci-francuzsky-monden-16-v2__FillMaxWzU0MCw1NDBd.11.2022-VT.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Holub-domaci-francuzsky-monden/Holub-domaci-pomoransky-hrvoliak-2022-DM-4__FillMaxWzU0MCw1NDBd.JPG', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Holub-domaci-slovensky-hrvoliak-modry/Holub-domaci-slovensky-hrvoliak-zlty-16__FillMaxWzU0MCw1NDBd.11.2022-VT.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Hrdlicka-chichotava/Hrdlicka-chichotava-archiv-ZOO-vtak-3__FillMaxWzU0MCw1NDBd.JPG', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Hrdlicka-perlokrka/hrdlicka_perlokrka2a__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Hrdzavka-potapava/DSC_0133_2-v2__FillMaxWzU0MCw1NDBd.JPG', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Hrosik-liberijsky/hrosik-liberijsky-profile-img_zoo-bratislava__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Hrdzavka-potapava/Hoeckergans_Anser_cygnoides_f__FillMaxWzU0MCw1NDBd._domestica_Wildpark_Poing-01.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Scarlet-Ibis/ibis-cerveny-c__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Indicky-bezec-kacica-domaca/DSC7437__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Jaguar-americky/jaguar-americky-c__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Jelen-europsky/jelen-europsky_zoo-bratislava-profile__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Kanarik-domaci/kanarik_domaci1__FillMaxWzU0MCw1NDBd.JPG', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Harriss-hawk/Kariama-cervenozoba-8__FillMaxWzU0MCw1NDBd.6.2023-VT-4.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Red-kangaroo/kengura-cervena_zoo-bratislava_profile__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Domestic-horse/DSC_8315__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Domestic-horse/DSC0004__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Plazy-a-obojzivelniky/Koralovka-cervena/koralovka_cervena2__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Plazy-a-obojzivelniky/Koralovka-kalifornska/koralovka-foto__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Cockatiel/korela_chochlata1__FillMaxWzU0MCw1NDBd.JPG', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Plazy-a-obojzivelniky/Korytnacka-leopardia/Korytnacka-leopardia_TH79130-v2__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Plazy-a-obojzivelniky/Korytnacka-uholna/800px-Geochelone_carbonaria_1__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Kosmac-striebristy/Kosmac-striebristy_TH79170__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Kosmac-striebristy/Kosmac-trpaslici_TH79407__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Koza-domaca-kamerunska/koza-domaca-holandska-c__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Koza-domaca-kamerunska/koza-domaca-kamerunska-c-v2__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Domestic-horse/DSC1105__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/adoption/Cicavce/Kralik-domaci-40/rok/Kralik-domaci-VT__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Red-billed-blue-magpie/kraska-cervenozoba__FillMaxWzU0MCw1NDBd.png', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Collared-falconet-/krkavec3-v2__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Plazy-a-obojzivelniky/Krokodil-celnaty/Krokodil-celnaty_TH79925__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/kudu-maly-3__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Kon-domaci/DSC0290__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Bregovska-Dzhinka-Chicken/Bregovska-dzhinka-16__FillMaxWzU0MCw1NDBd.11.2022-VT10.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Collared-hill-partridge/kuricka_bielocela1__FillMaxWzU0MCw1NDBd.JPG', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Little-owl/Kuvik-obycajny_DSC9738_Hulik1__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Black-swan/DSC7692__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Llama/DSC1584__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Llama/03_TH70493__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Plazy-a-obojzivelniky/Leguan-obojkovy/leguan-foto__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Lemur-kata/Lemur-kata_cover_img__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Lemur-kata/lenoch-dvojprsty-c__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Leopard-cejlonsky/leopard-ceylonsky-cover-v2__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Lev-juhoafricky/Titulna-foto__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Harriss-hawk/Lori-trojfarebny-VT-14__FillMaxWzU0MCw1NDBd.6.2023-3.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/African-spoonbill/unnamed__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Maciak-Brazzov/maciak-brazzov-c__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Macka-maloskvrnna/Macka-maloskvrnna-cover__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Makak-magot/makak-magot-c__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Patagonian-mara/mara-stepna-c__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Medve-hnedy/DSC1022__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Bezstavovce/Mnohonozka-obria/mnohonozka-foto__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Iberian-azure-winged-magpie/Modrana-strakovita-3__FillMaxWzU0MCw1NDBd.JPG', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Monal-leskly/Monal-leskly-4__FillMaxWzU0MCw1NDBd.1.2023-VT-1.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Morca-domace-Skinny-morca/morca-domace1__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Harriss-hawk/Morka-ockata-VT-5__FillMaxWzU0MCw1NDBd.6.2022-1.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Ryby/Mrenka-nadherna/Mrenka-nadherna_Panciernicek-panda_TH79635__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Ryby/Mrenka-pakistanska/botia-lohachata__FillMaxWzU0MCw1NDBd.jpeg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Ryby/Mrenka-siamska/x44756__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Muflon-lesny/muflon-lesny-c__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Chinese-muntjac/TH75883__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Collared-falconet-/Mysiak-paetfarebny-14__FillMaxWzU0MCw1NDBd.6.2023-VT-2.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Nandu-pampovy/TH70759-2__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Ryby/Neonka-cervena/neonka_cervena__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Nosal-cerveny/nosal-cerveny-c__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Nosorozec-tuponosy-juzny/TH75723__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/samica-okaca-cinkvisa-v2__FillMaxWzU0MCw1NDBd.JPG', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Orangutan-sumatriansky/01_DSC8931__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Oryx-arabsky/Oryx-arabsky_cover_img__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Osmak-degu/Osmak-degu_TH79278__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Native-wallachian-sheep/02_DSC1062__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Native-wallachian-sheep/ovca-domaca-valaska-c__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Ryby/Panciernicek-maly/Corydoras-nanus__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Ryby/Panciernicek-panda/Longfin-Panda-Corydora-4_1024x1024__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Ryby/Panciernicek-smaragdovy/panciernicek_smaragdovy1__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Ryby/Panciernicek-Sterbov/panciernicek_sterbov1__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Panda-cervena/DSC8199__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Red-winged-parrot/papagaj_cervenokridly1__FillMaxWzU0MCw1NDBd.JPG', 'https://www.zoobratislava.sk/assets/Uploads/adoption/Invertebrates/Papagaj-kralovsky-70-/rok/Papagaj-kralovsky_DSC_0012_Dominika-Nagyova2__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Pasavec-stetinovy/03_DSC8023__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Pav-korunkaty-4__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/New-bird/DSC5343__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Perlicka-supia/Perlicka-supia-21__FillMaxWzU0MCw1NDBd.6.2022-VT-1.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Pes-usaty/pes-usaty-cover__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Plazy-a-obojzivelniky/Pichlavec-ozdobny/Pichlavec-ozdobny_TH79891__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Ryby/Pirana-Nattererova/Pirana-Nattererova-4__FillMaxWzU0MCw1NDBd.9.2023-VT.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Pizmovka-domaca/TH76802__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Greater-Flamingo/06_DSC7849__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Common-barn-owl/Plamienka-driemava-1__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Potik-kapcavy/Potik-Kapcavy_DSC_0047_Dominika-Nagyova__FillMaxWzU0MCw1NDBd.JPG', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Potkanokengura-kralikovita/potkanokengura__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Ryby/Prisavnik/Prisavnik-ancistrus_TH79470__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Pstros-africky/pstros_africky1_TH__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Plazy-a-obojzivelniky/Pyton-kralovsky/TH70834__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Plazy-a-obojzivelniky/Pyton-tmavy/DSC8599__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Plazy-a-obojzivelniky/Pyton-zeleny/TH79380__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Plazy-a-obojzivelniky/Rohatka-ozdobna/rohatka-foto__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Plazy-a-obojzivelniky/Rosnicka-australska/Rosnicka-australska-31__FillMaxWzU0MCw1NDBd.5.2023-VT-2.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Crimson-rosella/rozela_Pennantova1__FillMaxWzU0MCw1NDBd.JPG', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Harriss-hawk/Rybarik-smejivy-VT-14__FillMaxWzU0MCw1NDBd.6.2023-6.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Rys-kanadsky/rys-kanadsky-c__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Rys-kanadsky/Rys-ostrovid_profile__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Saimiri-vevericovity/05_DSC9303__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/adoption/Ryby/Scink-salamunsky-80/rok/scink-salamunsky__FillMaxWzU0MCw1NDBd.JPG', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Simpanz-ucenlivy/simpanz-ucenlivy-c__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Sitatunga-zapadna/sitatunga-zapadna-c__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Bezstavovce/Stonozka-vietnamska/stonozka-foto__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Bezstavovce/Svab-madagaskarsky/stur-obrovsky__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Ryby/Sumec-sklovity/Sumcek-sklovity_TH79501__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Surikata-vlnkava/surikata-vlnkava-c__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/adoption/Cicavce/Takin-zlaty-180/rok/Takin-zlaty-samec-18__FillMaxWzU0MCw1NDBd.9.2023-VT-4.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Tamarin-zltoruky/Tamarin-pinci_TH79655__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Tamarin-zltoruky/Tamarin-zltoruky_TH79952__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Tava-dvojhrba/tava-dvojhrba-c__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Ryby/Tetra-konzska/Tetra-konzska_DSC7888a__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Ryby/Tetra-krvava/Tetra-krvava-4-v2__FillMaxWzU0MCw1NDBd.JPG', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Ryby/Tetra-ziariva/Tetra-ziariva-3__FillMaxWzU0MCw1NDBd.JPG', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Tragopan-modrolici/TH73484__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Traviar-ruzovobruchy/Traviar-ruzovobruchy-archiv-ZOO-vtak-1__FillMaxWzU0MCw1NDBd.JPG', 'https://www.zoobratislava.sk/assets/Urzon-kanadsky__FillMaxWzU0MCw1NDBd.JPG', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Plazy-a-obojzivelniky/Rosnicka-australska/Uzovka-cervena_TH79835__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/adoption/Invertebrates/Varan-ostnatochvosty-100-/rok/Varan-ostnatochvosty-VT__FillMaxWzU0MCw1NDBd.JPG', 'https://www.zoobratislava.sk/assets/Veverica-kanadska-24__FillMaxWzU0MCw1NDBd.6.2022-VT-2.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Vlk-eurazijsky/TH79417__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Kafue-lechwe/Vodarka-lecve-kafuenska-6__FillMaxWzU0MCw1NDBd.JPG', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Harriss-hawk/Vyr-skalny-sibirsky-8__FillMaxWzU0MCw1NDBd.6.2023-VT-2.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Domestic-donkey/zebra-chapmanova-__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Harriss-hawk/zebricka_cervenozoba1__FillMaxWzU0MCw1NDBd.JPG', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Harriss-hawk/Zemnarka-kratkozoba-28__FillMaxWzU0MCw1NDBd.8.2022-VT-2.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Red-crowned-crane/zeriav-japonsky__FillMaxWzU0MCw1NDBd.png', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Takin-zlaty/TH72896__FillMaxWzU0MCw1NDBd.jpg', 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Zubor-europsky/zubor-europsky-c__FillMaxWzU0MCw1NDBd.jpg']
#####[{'name': 'Adax núbijský', 'latin_title': 'Addax nasomaculatus', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Addax/adax-nubijsky_zoo-bratislava_profile__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Agama bradatá', 'latin_title': 'Pogona vitticeps / Inland bearded dragon', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Agama-bradata/Agama-bradata_TH70019__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Antilopa nilgau', 'latin_title': 'Boselaphus tragocamelus / Nilgai', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/South-African-sable-antelope/antilopa-nilgau-c__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Antilopa vraná', 'latin_title': 'Hippotragus niger niger / South African sable antelope', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/South-African-sable-antelope/antilopa-vrana-c__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Ara zelená', 'latin_title': 'Ara militaris mexicana / Mexican Military Macaw', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/DSC9053__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Bažant diamantový', 'latin_title': 'Chrysolophus amherstiae / Lady Amherst´s pheasant', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Harriss-hawk/DSC_0541_2__FillMaxWzU0MCw1NDBd.JPG'}, {'name': 'Bažant zlatý', 'latin_title': 'Chrysolophus pictus / golden pheasant', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Monal-leskly/bazant_zlaty1__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Bažant zlatý broskyňový', 'latin_title': 'Chrysolophus pictus / Peach Golden Pheasant', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Monal-leskly/Bazant-zlaty-broskynovy-VT-6__FillMaxWzU0MCw1NDBd.12.2022-4.jpg'}, {'name': 'Belaňa tundrová', 'latin_title': 'Bubo scandiacus / Snowy owl', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Belana-tundrova/belana-tundrova__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Bichirek kalabarský', 'latin_title': 'Erpetoichthys calabaricus / Reedfish', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Ryby/Bichirek-kalabarsky/bichirek_kalabarsky1__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Brazílska červeno-biela tarantula', 'latin_title': 'Nhandu chromatus / Brazilian red and white tarantula', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Bezstavovce/Brazilska-cerveno-biela-tarantula-/tarantula__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Chocholačka bielooká', 'latin_title': 'Aythya nyroca / Ferruginous duck', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Ferruginous-duck/chochlacka_bielooka2__FillMaxWzU0MCw1NDBd.JPG'}, {'name': 'Daman stromový', 'latin_title': 'Dendrohyrax arboreus / Tree hyrax', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/South-African-sable-antelope/Dizajn-bez-nazvu-12__FillMaxWzU0MCw1NDBd.png'}, {'name': 'Daniel škvrnitý', 'latin_title': 'Dama dama / Fallow deer', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/South-African-sable-antelope/DSC1763__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Dikdik Kirkov', 'latin_title': "Madoqua kirkii / Kirk's dikdik", 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Dikdik-Kirkov/dikdik-kirkov_zoo-bratislava_profile__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Dikobraz bielochvostý', 'latin_title': 'Hystrix indica / Indian crested porcupine', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Dikobraz-bielochvosty/dikobraz-bielochvosty_zoo-bratislava_profile__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Diviak lesný', 'latin_title': 'Sus scrofa / Wild boar', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Diviak-visajansky/diviak-lesny_zoo-bratislava_profile__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Diviak visajanský', 'latin_title': 'Sus cebifrons negrinus / Visayan warty pig', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Diviak-visajansky/Diviak-visajansky_zoo-bratislava_profile__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Drozd čiernoprsý', 'latin_title': 'Turdus dissimilis / Black-breasted thrush', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Drozd-ciernoprsy/blackbird__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Emu hnedý', 'latin_title': 'Dromaius novaehollandiae / Emu', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Emu/TH75824__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Felzuma madagaskarská', 'latin_title': 'Phelsuma madagascariensis / madagascar day gecko', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Plazy-a-obojzivelniky/Felzuma-madagaskarska/felzuma-foto__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Fretka domáca', 'latin_title': 'Mustela putorius furo / Domestic ferret', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Fretka-domaca/Fretka-domaca-16__FillMaxWzU0MCw1NDBd.11.2022-VT-4.jpg'}, {'name': 'Gekón obrovský', 'latin_title': 'Gekko gecko / Tokay gecko', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Plazy-a-obojzivelniky/Gekon-obrovsky/gekon-obrobvsky__FillMaxWzU0MCw1NDBd.JPG'}, {'name': 'Gekončík nočný', 'latin_title': 'Eublepharis macularius / Leopard gecko', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Plazy-a-obojzivelniky/Gekoncik-nocny/head-of-leopard-gecko-eublepharis-macularius-in-front-of-black-background-MJOF000291__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Gibon zlatolíci', 'latin_title': 'Nomascus gabriellae / Buff-cheeked gibbon', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Gibon-zlatolici/gibon-zlatolici_profile_zoo-bratislava__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Hlaholka severská', 'latin_title': 'Bucephala clangula / Common goldeneye', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Common-goldeneye/Hlaholka-severska-archiv-ZOO-vtak-3__FillMaxWzU0MCw1NDBd.JPG'}, {'name': 'Holub domáci - brčkáň', 'latin_title': 'Columba domestica / Domestic pigeon', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Holub-domaci-slovensky-hrvoliak-modry/Holub-domaci-brckan-1__FillMaxWzU0MCw1NDBd.JPG'}, {'name': 'Holub domáci - francúzsky mondén', 'latin_title': 'Columba livia f. domestica / Domestic pigeon - French mondain', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Holub-domaci-slovensky-hrvoliak-zlty/Holub-domaci-francuzsky-monden-16-v2__FillMaxWzU0MCw1NDBd.11.2022-VT.jpg'}, {'name': 'Holub domáci - pomoranský hrvoliak', 'latin_title': 'Columba domestica / Domestic pigeon - Pomeranian Pouter', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Holub-domaci-francuzsky-monden/Holub-domaci-pomoransky-hrvoliak-2022-DM-4__FillMaxWzU0MCw1NDBd.JPG'}, {'name': 'Holub domáci - slovenský hrvoliak žltý', 'latin_title': 'Columba domestica / Domestic pigeon - Slovak Pouter', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Holub-domaci-slovensky-hrvoliak-modry/Holub-domaci-slovensky-hrvoliak-zlty-16__FillMaxWzU0MCw1NDBd.11.2022-VT.jpg'}, {'name': 'Hrdlička chichotavá', 'latin_title': 'Streptopelia roseogrisea / Pink-headed turtle dove', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Hrdlicka-chichotava/Hrdlicka-chichotava-archiv-ZOO-vtak-3__FillMaxWzU0MCw1NDBd.JPG'}, {'name': 'Hrdlička perlokrká', 'latin_title': 'Streptopelia chinensis / Spotted dove', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Hrdlicka-perlokrka/hrdlicka_perlokrka2a__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Hrdzavka potápavá', 'latin_title': 'Netta rufina / Red-crested pochard', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Hrdzavka-potapava/DSC_0133_2-v2__FillMaxWzU0MCw1NDBd.JPG'}, {'name': 'Hrošík libérijský', 'latin_title': 'Choeropsis liberiensis / Pygmy hippopotamus', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Hrosik-liberijsky/hrosik-liberijsky-profile-img_zoo-bratislava__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Hus labutia - domáca', 'latin_title': 'Anser cygnoides domestic / Domestic swan goose, white', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Hrdzavka-potapava/Hoeckergans_Anser_cygnoides_f__FillMaxWzU0MCw1NDBd._domestica_Wildpark_Poing-01.jpg'}, {'name': 'Ibis červený', 'latin_title': 'Eudocimus ruber / Scarlet ibis', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Scarlet-Ibis/ibis-cerveny-c__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Indický bežec (kačica domáca)', 'latin_title': 'Anas platyrhynchos domestic / Domestic duck', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Indicky-bezec-kacica-domaca/DSC7437__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Jaguár americký', 'latin_title': 'Panthera onca / Jaguar', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Jaguar-americky/jaguar-americky-c__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Jeleň európsky', 'latin_title': 'Cervus elaphus / Red deer', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Jelen-europsky/jelen-europsky_zoo-bratislava-profile__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Kanárik domáci', 'latin_title': 'Serinus canaria f. domestica / Domestic canary', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Kanarik-domaci/kanarik_domaci1__FillMaxWzU0MCw1NDBd.JPG'}, {'name': 'Kariama červenozobá', 'latin_title': 'Cariama cristata / Red-legged seriema', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Harriss-hawk/Kariama-cervenozoba-8__FillMaxWzU0MCw1NDBd.6.2023-VT-4.jpg'}, {'name': 'Kengura červená', 'latin_title': 'Macropus rufus / Red kangaroo', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Red-kangaroo/kengura-cervena_zoo-bratislava_profile__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Kôň domáci', 'latin_title': 'Equus caballus / Domestic horse', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Domestic-horse/DSC_8315__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Kôň Przewalského', 'latin_title': "Equus przewalskii / Przewalski's Wild Horse", 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Domestic-horse/DSC0004__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Koralovka červená', 'latin_title': 'Lampropeltis triangulum sinaloae / Sinaloan milksnake', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Plazy-a-obojzivelniky/Koralovka-cervena/koralovka_cervena2__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Koralovka kalifornská', 'latin_title': 'Lampropeltis californiae / California kingsnake', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Plazy-a-obojzivelniky/Koralovka-kalifornska/koralovka-foto__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Korela chochlatá', 'latin_title': 'Nymphicus hollandicus / Cockatiel', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Cockatiel/korela_chochlata1__FillMaxWzU0MCw1NDBd.JPG'}, {'name': 'Korytnačka leopardia', 'latin_title': 'Stigmochelys pardalis babcocki / Northern leopard tortoise', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Plazy-a-obojzivelniky/Korytnacka-leopardia/Korytnacka-leopardia_TH79130-v2__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Korytnačka uhoľná', 'latin_title': 'Geochelone carbonaria / Red-footed tortoise', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Plazy-a-obojzivelniky/Korytnacka-uholna/800px-Geochelone_carbonaria_1__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Kosmáč striebristý', 'latin_title': 'Mico argentatus / Silvery marmoset', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Kosmac-striebristy/Kosmac-striebristy_TH79170__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Kosmáč trpasličí', 'latin_title': 'Cebuella pygmaea pygmaea / Pygmy marmoset', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Kosmac-striebristy/Kosmac-trpaslici_TH79407__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Koza domáca holandská', 'latin_title': 'Capra hircus f. domestica / Dutch pygmy goat', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Koza-domaca-kamerunska/koza-domaca-holandska-c__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Koza domáca kamerunská', 'latin_title': 'Capra hircus f. domestica / West African pygmy goat', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Koza-domaca-kamerunska/koza-domaca-kamerunska-c-v2__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Kozorožec alpský', 'latin_title': 'Capra ibex / Alpine ibex', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Domestic-horse/DSC1105__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Králik domáci', 'latin_title': 'Oryctolagus cuniculus domesticus/Domestic rabbit', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/adoption/Cicavce/Kralik-domaci-40/rok/Kralik-domaci-VT__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Kraska červenozobá', 'latin_title': 'Urocissa erythroryncha / Red-billed blue magpie', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Red-billed-blue-magpie/kraska-cervenozoba__FillMaxWzU0MCw1NDBd.png'}, {'name': 'Krkavec čierny', 'latin_title': 'Corvus corax / Common Raven', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Collared-falconet-/krkavec3-v2__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Krokodíl čelnatý', 'latin_title': 'Osteolaemus tetraspis / African dwarf crocodile', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Plazy-a-obojzivelniky/Krokodil-celnaty/Krokodil-celnaty_TH79925__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Kudu malý', 'latin_title': 'Tragelaphus imberbis / Lesser kudu', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/kudu-maly-3__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Kulan turkménsky', 'latin_title': 'Equus hemionus kulan / Turkmenian kulan', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Kon-domaci/DSC0290__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Kura domáca - bregovska dzhinka', 'latin_title': 'Gallus gallus domesticus / Bregovska Dzhinka Chicken', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Bregovska-Dzhinka-Chicken/Bregovska-dzhinka-16__FillMaxWzU0MCw1NDBd.11.2022-VT10.jpg'}, {'name': 'Kurička bieločelá', 'latin_title': 'Arborophila gingica / Collared hill partridge', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Collared-hill-partridge/kuricka_bielocela1__FillMaxWzU0MCw1NDBd.JPG'}, {'name': 'Kuvik obyčajný', 'latin_title': 'Athene noctua / Little owl', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Little-owl/Kuvik-obycajny_DSC9738_Hulik1__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Labuť čierna', 'latin_title': 'Cygnus atratus / Black swan', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Black-swan/DSC7692__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Lama alpaka', 'latin_title': 'Vicugna pacos / Alpaca', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Llama/DSC1584__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Lama krotká', 'latin_title': 'Lama glama / Llama', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Llama/03_TH70493__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Leguán obojkový', 'latin_title': 'Crotaphytus collaris / Collared lizard', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Plazy-a-obojzivelniky/Leguan-obojkovy/leguan-foto__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Lemur kata', 'latin_title': 'Lemur catta / Ring-tailed lemur', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Lemur-kata/Lemur-kata_cover_img__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Leňoch dvojprstý', 'latin_title': 'Choloepus didactylus / Linne´s two-toed sloth', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Lemur-kata/lenoch-dvojprsty-c__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Leopard cejlónsky', 'latin_title': 'Panthera pardus kotiya / Sri Lankan leopard', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Leopard-cejlonsky/leopard-ceylonsky-cover-v2__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Lev juhoafrický', 'latin_title': 'Panthera leo krugeri / African lion', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Lev-juhoafricky/Titulna-foto__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Lori trojfarebný', 'latin_title': 'Lorius lory / Black-capped lory', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Harriss-hawk/Lori-trojfarebny-VT-14__FillMaxWzU0MCw1NDBd.6.2023-3.jpg'}, {'name': 'Lyžičiar ružovonohý', 'latin_title': 'Platalea alba / African spoonbill', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/African-spoonbill/unnamed__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Mačiak Brazzov', 'latin_title': "Cercopithecus neglectus / De Brazza's monkey", 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Maciak-Brazzov/maciak-brazzov-c__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Mačka maloškvrnná', 'latin_title': "Leopardus geoffroyi / Geoffroyi's cat", 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Macka-maloskvrnna/Macka-maloskvrnna-cover__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Makak magot', 'latin_title': 'Macaca sylvanus / Barbary macaque', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Makak-magot/makak-magot-c__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Mara stepná', 'latin_title': 'Dolichotis patagonum / Patagonian mara', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Patagonian-mara/mara-stepna-c__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Medveď hnedý', 'latin_title': 'Ursus arctos / Brown bear', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Medve-hnedy/DSC1022__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Mnohonôžka obria', 'latin_title': 'Archispirostreptus gigas / Giant african milipede', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Bezstavovce/Mnohonozka-obria/mnohonozka-foto__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Modraňa strakovitá', 'latin_title': 'Cyanopica cooki / Iberian azure-winged magpie', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Iberian-azure-winged-magpie/Modrana-strakovita-3__FillMaxWzU0MCw1NDBd.JPG'}, {'name': 'Monal lesklý', 'latin_title': 'Lophophorus impejanus / Himalayan Monal', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Monal-leskly/Monal-leskly-4__FillMaxWzU0MCw1NDBd.1.2023-VT-1.jpg'}, {'name': 'Morča domáce - Skinny morča', 'latin_title': 'Cavia porcellus f. domestica / Domestic guinea pig', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Morca-domace-Skinny-morca/morca-domace1__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Morka očkatá', 'latin_title': 'Meleagris ocellata / Ocellated turkey', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Harriss-hawk/Morka-ockata-VT-5__FillMaxWzU0MCw1NDBd.6.2022-1.jpg'}, {'name': 'Mrenka nádherná', 'latin_title': 'Chromobotia macracanthus / Clown loach', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Ryby/Mrenka-nadherna/Mrenka-nadherna_Panciernicek-panda_TH79635__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Mrenka pakistánska', 'latin_title': 'Botia lohachata / Reticulate loach', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Ryby/Mrenka-pakistanska/botia-lohachata__FillMaxWzU0MCw1NDBd.jpeg'}, {'name': 'Mrenka siamská', 'latin_title': 'Crossocheilus oblongus / Siamese Algae-eater', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Ryby/Mrenka-siamska/x44756__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Muflón lesný', 'latin_title': 'Ovis aries musimon / Mouflon', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Muflon-lesny/muflon-lesny-c__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Muntžak malý', 'latin_title': 'Muntiacus reevesi / Chinese muntjac', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Chinese-muntjac/TH75883__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Myšiak štvorfarebný', 'latin_title': "Parabuteo unicinctus / Harris's hawk", 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Collared-falconet-/Mysiak-paetfarebny-14__FillMaxWzU0MCw1NDBd.6.2023-VT-2.jpg'}, {'name': 'Nandu pampový', 'latin_title': 'Rhea americana / Greater rhea', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Nandu-pampovy/TH70759-2__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Neónka červená', 'latin_title': 'Paracheirodon axelrodi / Cardinal tetra', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Ryby/Neonka-cervena/neonka_cervena__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Nosáľ červený', 'latin_title': 'Nasua nasua / Brown-nosed coati', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Nosal-cerveny/nosal-cerveny-c__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Nosorožec tuponosý južný', 'latin_title': 'Ceratotherium simum simum / Southern white rhinoceros', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Nosorozec-tuponosy-juzny/TH75723__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Okáč činkvis', 'latin_title': 'Polyplectron bicalcaratum / Grey peacock pheasant', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/samica-okaca-cinkvisa-v2__FillMaxWzU0MCw1NDBd.JPG'}, {'name': 'Orangutan sumatriansky', 'latin_title': 'Pongo abelii / Sumatran orangutan', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Orangutan-sumatriansky/01_DSC8931__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Oryx arabský', 'latin_title': 'Oryx leucoryx / Arabian oryx', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Oryx-arabsky/Oryx-arabsky_cover_img__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Osmák degu', 'latin_title': 'Octodon degus / Degu', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Osmak-degu/Osmak-degu_TH79278__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Ovca domáca ouessantská', 'latin_title': 'Ovis aries ouessant / Ouessant sheep', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Native-wallachian-sheep/02_DSC1062__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Ovca domáca valašská', 'latin_title': 'Ovis aries aries / Native Wallachian\u202fsheep', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Native-wallachian-sheep/ovca-domaca-valaska-c__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Pancierniček malý', 'latin_title': 'Corydoras nanus / Dwarf catfish', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Ryby/Panciernicek-maly/Corydoras-nanus__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Pancierníček panda', 'latin_title': 'Corydoras panda / Panda catfish', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Ryby/Panciernicek-panda/Longfin-Panda-Corydora-4_1024x1024__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Pancierniček smaragdový', 'latin_title': 'Brochis splendens / Common brochis', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Ryby/Panciernicek-smaragdovy/panciernicek_smaragdovy1__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Pancierniček Sterbov', 'latin_title': 'Corydoras sterbai / Sterba´s catfish', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Ryby/Panciernicek-Sterbov/panciernicek_sterbov1__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Panda červená', 'latin_title': 'Ailurus fulgens / Red panda', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Panda-cervena/DSC8199__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Papagáj červenokrídly', 'latin_title': 'Aprosmictus erythropterus / Red-winged parrot', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Red-winged-parrot/papagaj_cervenokridly1__FillMaxWzU0MCw1NDBd.JPG'}, {'name': 'Papagáj kráľovský', 'latin_title': 'Alisterus scapularis / Australian king parrot', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/adoption/Invertebrates/Papagaj-kralovsky-70-/rok/Papagaj-kralovsky_DSC_0012_Dominika-Nagyova2__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Pásavec štetinový', 'latin_title': 'Chaetophractus villosus / Large hairy armadillo', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Pasavec-stetinovy/03_DSC8023__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Páv korunkatý', 'latin_title': 'Pavo cristatus / Indian peafowl', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Pav-korunkaty-4__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Pelikán ružový', 'latin_title': 'Pelecanus onocrotalus / Eastern white pelican', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/New-bird/DSC5343__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Perlička supia', 'latin_title': 'Acryllium vulturinum / Vulturine guineafowl', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Perlicka-supia/Perlicka-supia-21__FillMaxWzU0MCw1NDBd.6.2022-VT-1.jpg'}, {'name': 'Pes ušatý', 'latin_title': 'Otocyon megalotis / Bat-eared fox', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Pes-usaty/pes-usaty-cover__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Pichľavec ozdobný', 'latin_title': 'Uromastyx ornata / Ornate mastigure', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Plazy-a-obojzivelniky/Pichlavec-ozdobny/Pichlavec-ozdobny_TH79891__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Piraňa Nattererova', 'latin_title': 'Pygocentrus nattereri / Red piranha', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Ryby/Pirana-Nattererova/Pirana-Nattererova-4__FillMaxWzU0MCw1NDBd.9.2023-VT.jpg'}, {'name': 'Pižmovka domáca', 'latin_title': 'Cairina moschata f. domestica / Domestic muscovy duck', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Pizmovka-domaca/TH76802__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Plameniak ružový', 'latin_title': 'Phoenicopterus roseus / Greater flamingo', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Greater-Flamingo/06_DSC7849__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Plamienka driemavá', 'latin_title': 'Tyto alba / Common barn owl', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Common-barn-owl/Plamienka-driemava-1__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Pôtik kapcavý', 'latin_title': 'Aegolius funereus / Boreal owl', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Potik-kapcavy/Potik-Kapcavy_DSC_0047_Dominika-Nagyova__FillMaxWzU0MCw1NDBd.JPG'}, {'name': 'Potkanokengura králikovitá', 'latin_title': 'Bettongia penicillata / Woylie', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Potkanokengura-kralikovita/potkanokengura__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Prísavník', 'latin_title': 'Ancistrus sp. / Bristlenose catfish', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Ryby/Prisavnik/Prisavnik-ancistrus_TH79470__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Pštros africký', 'latin_title': 'Struthio camelus / Common ostrich', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Pstros-africky/pstros_africky1_TH__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Pytón kráľovský', 'latin_title': 'Python regius / Ball python', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Plazy-a-obojzivelniky/Pyton-kralovsky/TH70834__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Pytón tmavý', 'latin_title': 'Python molurus bivittatus / Burmese python', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Plazy-a-obojzivelniky/Pyton-tmavy/DSC8599__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Pytón zelený', 'latin_title': 'Morelia viridis / Green tree python', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Plazy-a-obojzivelniky/Pyton-zeleny/TH79380__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Rohatka ozdobná', 'latin_title': 'Ceratophrys ornata /  Ornate horned frog', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Plazy-a-obojzivelniky/Rohatka-ozdobna/rohatka-foto__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Rosnička austrálska', 'latin_title': 'Litoria caerulea / Australian Green Treefrog', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Plazy-a-obojzivelniky/Rosnicka-australska/Rosnicka-australska-31__FillMaxWzU0MCw1NDBd.5.2023-VT-2.jpg'}, {'name': 'Rozela penantová', 'latin_title': 'Platycercus elegans / Crimson rosella', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Crimson-rosella/rozela_Pennantova1__FillMaxWzU0MCw1NDBd.JPG'}, {'name': 'Rybárik smejivý', 'latin_title': 'Dacelo novaeguineae / Laughing Kookaburra', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Harriss-hawk/Rybarik-smejivy-VT-14__FillMaxWzU0MCw1NDBd.6.2023-6.jpg'}, {'name': 'Rys kanadský', 'latin_title': 'Lynx canadensis / Canadian lynx', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Rys-kanadsky/rys-kanadsky-c__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Rys ostrovid', 'latin_title': 'Lynx lynx carpathicus / Eurasian lynx', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Rys-kanadsky/Rys-ostrovid_profile__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Saimiri vevericovitý', 'latin_title': 'Saimiri sciureus / Common squirrel monkey', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Saimiri-vevericovity/05_DSC9303__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Scink šalamúnsky', 'latin_title': 'Corucia zebrata / Solomon Islands skink', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/adoption/Ryby/Scink-salamunsky-80/rok/scink-salamunsky__FillMaxWzU0MCw1NDBd.JPG'}, {'name': 'Šimpanz učenlivý', 'latin_title': 'Pan troglodytes / Common chimpanzee', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Simpanz-ucenlivy/simpanz-ucenlivy-c__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Sitatunga západná', 'latin_title': 'Tragelaphus spekii gratus / Western sitatunga', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Sitatunga-zapadna/sitatunga-zapadna-c__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Stonožka vietnamská', 'latin_title': 'Scolopendra subspinipes / Vietnamese centipede', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Bezstavovce/Stonozka-vietnamska/stonozka-foto__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Sumec sklovitý', 'latin_title': 'Kryptopterus bicirrhis / Glass catfish', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Ryby/Sumec-sklovity/Sumcek-sklovity_TH79501__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Surikata vlnkavá', 'latin_title': 'Suricata suricatta / Slender-tailed meerkat', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Surikata-vlnkava/surikata-vlnkava-c__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Takin zlatý', 'latin_title': 'Budorcas taxicolor bedfordi / Golden takin', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/adoption/Cicavce/Takin-zlaty-180/rok/Takin-zlaty-samec-18__FillMaxWzU0MCw1NDBd.9.2023-VT-4.jpg'}, {'name': 'Tamarín pinčí', 'latin_title': 'Saguinus oedipus / Cotton-top tamarin', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Tamarin-zltoruky/Tamarin-pinci_TH79655__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Tamarín žltoruký', 'latin_title': 'Saguinus midas / Red-handed tamarin', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Tamarin-zltoruky/Tamarin-zltoruky_TH79952__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Ťava dvojhrbá', 'latin_title': 'Camelus bactrianus / Bactrian camel', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Tava-dvojhrba/tava-dvojhrba-c__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Tetra konžská', 'latin_title': 'Phenacogrammus interruptus / Congo tetra', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Ryby/Tetra-konzska/Tetra-konzska_DSC7888a__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Tetra krvavá', 'latin_title': 'Hyphessobrycon eques / Tetra', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Ryby/Tetra-krvava/Tetra-krvava-4-v2__FillMaxWzU0MCw1NDBd.JPG'}, {'name': 'Tetra žiarivá', 'latin_title': 'Hemigrammus erythrozonus / Glowlight tetra', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Ryby/Tetra-ziariva/Tetra-ziariva-3__FillMaxWzU0MCw1NDBd.JPG'}, {'name': 'Tragopan modrolíci', 'latin_title': 'Tragopan temminckii / Temminck´s tragopan', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Tragopan-modrolici/TH73484__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Tráviar ružovobruchý', 'latin_title': 'Neopsephotus bourkii / Bourke´s parrot', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Traviar-ruzovobruchy/Traviar-ruzovobruchy-archiv-ZOO-vtak-1__FillMaxWzU0MCw1NDBd.JPG'}, {'name': 'Urzon kanadský', 'latin_title': 'Erethizon dorsatum / North american porcupine', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Urzon-kanadsky__FillMaxWzU0MCw1NDBd.JPG'}, {'name': 'Užovka červená', 'latin_title': 'Pantherophis guttatus / Cornsnake', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Plazy-a-obojzivelniky/Rosnicka-australska/Uzovka-cervena_TH79835__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Varan ostnatochvostý', 'latin_title': 'Varanus acanthurus / Spiny-tailed monitor', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/adoption/Invertebrates/Varan-ostnatochvosty-100-/rok/Varan-ostnatochvosty-VT__FillMaxWzU0MCw1NDBd.JPG'}, {'name': 'Veverica kanadská', 'latin_title': 'Tamiasciurus hudsonicus / Red squirrel', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Veverica-kanadska-24__FillMaxWzU0MCw1NDBd.6.2022-VT-2.jpg'}, {'name': 'Vlk eurázijský', 'latin_title': 'Canis lupus lupus / Eurasian wolf', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Vlk-eurazijsky/TH79417__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Vodárka lečve kafuenská', 'latin_title': 'Kobus leche kafuensis / Kafue lechwe', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Kafue-lechwe/Vodarka-lecve-kafuenska-6__FillMaxWzU0MCw1NDBd.JPG'}, {'name': 'Výr skalný sibírsky', 'latin_title': 'Bubo bubo sibiricus / Northern eagle owl', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Harriss-hawk/Vyr-skalny-sibirsky-8__FillMaxWzU0MCw1NDBd.6.2023-VT-2.jpg'}, {'name': 'Zebra Chapmanova', 'latin_title': 'Equus quagga chapmani / Chapman’s zebra', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Domestic-donkey/zebra-chapmanova-__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Zebrička červenozobá', 'latin_title': 'Taeniopygia guttata / Timor Zebra Finch', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Harriss-hawk/zebricka_cervenozoba1__FillMaxWzU0MCw1NDBd.JPG'}, {'name': 'Zemnárka krátkozobá', 'latin_title': 'Cereopsis novaehollandiae / Cereopsis goose', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Harriss-hawk/Zemnarka-kratkozoba-28__FillMaxWzU0MCw1NDBd.8.2022-VT-2.jpg'}, {'name': 'Žeriav japonský', 'latin_title': 'Grus japonensis / Red-crowned crane', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Red-crowned-crane/zeriav-japonsky__FillMaxWzU0MCw1NDBd.png'}, {'name': 'Žirafa Rothschildova', 'latin_title': 'Giraffa camelopardalis rothschildi / Baringo giraffe', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Takin-zlaty/TH72896__FillMaxWzU0MCw1NDBd.jpg'}, {'name': 'Zubor európsky', 'latin_title': 'Bison bonasus / European bison', 'english_title': None, 'image_url': 'https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Zubor-europsky/zubor-europsky-c__FillMaxWzU0MCw1NDBd.jpg'}]
'''
bratiska
[
  {
    "name": "Adax núbijský",
    "latin_title": "Addax nasomaculatus",
    "english_title": "None",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Addax/adax-nubijsky_zoo-bratislava_profile__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Agama bradatá",
    "latin_title": "Pogona vitticeps",
    "english_title": "Inland bearded dragon",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Agama-bradata/Agama-bradata_TH70019__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Antilopa nilgau",
    "latin_title": "Boselaphus tragocamelus",
    "english_title": "Nilgai",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/South-African-sable-antelope/antilopa-nilgau-c__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Antilopa vraná",
    "latin_title": "Hippotragus niger niger",
    "english_title": "South African sable antelope",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/South-African-sable-antelope/antilopa-vrana-c__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Ara zelená",
    "latin_title": "Ara militaris mexicana",
    "english_title": "Mexican Military Macaw",
    "image_url": "https://www.zoobratislava.sk/assets/DSC9053__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Bažant diamantový",
    "latin_title": "Chrysolophus amherstiae",
    "english_title": "Lady Amherst´s pheasant",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Harriss-hawk/DSC_0541_2__FillMaxWzU0MCw1NDBd.JPG"
  },
  {
    "name": "Bažant zlatý",
    "latin_title": "Chrysolophus pictus",
    "english_title": "golden pheasant",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Monal-leskly/bazant_zlaty1__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Bažant zlatý broskyňový",
    "latin_title": "Chrysolophus pictus",
    "english_title": "Peach Golden Pheasant",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Monal-leskly/Bazant-zlaty-broskynovy-VT-6__FillMaxWzU0MCw1NDBd.12.2022-4.jpg"
  },
  {
    "name": "Belaňa tundrová",
    "latin_title": "Bubo scandiacus",
    "english_title": "Snowy owl",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Belana-tundrova/belana-tundrova__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Bichirek kalabarský",
    "latin_title": "Erpetoichthys calabaricus",
    "english_title": "Reedfish",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Ryby/Bichirek-kalabarsky/bichirek_kalabarsky1__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Brazílska červeno-biela tarantula",
    "latin_title": "Nhandu chromatus",
    "english_title": "Brazilian red and white tarantula",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Bezstavovce/Brazilska-cerveno-biela-tarantula-/tarantula__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Chocholačka bielooká",
    "latin_title": "Aythya nyroca",
    "english_title": "Ferruginous duck",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Ferruginous-duck/chochlacka_bielooka2__FillMaxWzU0MCw1NDBd.JPG"
  },
  {
    "name": "Daman stromový",
    "latin_title": "Dendrohyrax arboreus",
    "english_title": "Tree hyrax",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/South-African-sable-antelope/Dizajn-bez-nazvu-12__FillMaxWzU0MCw1NDBd.png"
  },
  {
    "name": "Daniel škvrnitý",
    "latin_title": "Dama dama",
    "english_title": "Fallow deer",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/South-African-sable-antelope/DSC1763__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Dikdik Kirkov",
    "latin_title": "Madoqua kirkii",
    "english_title": "Kirk's dikdik",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Dikdik-Kirkov/dikdik-kirkov_zoo-bratislava_profile__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Dikobraz bielochvostý",
    "latin_title": "Hystrix indica",
    "english_title": "Indian crested porcupine",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Dikobraz-bielochvosty/dikobraz-bielochvosty_zoo-bratislava_profile__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Diviak lesný",
    "latin_title": "Sus scrofa",
    "english_title": "Wild boar",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Diviak-visajansky/diviak-lesny_zoo-bratislava_profile__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Diviak visajanský",
    "latin_title": "Sus cebifrons negrinus",
    "english_title": "Visayan warty pig",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Diviak-visajansky/Diviak-visajansky_zoo-bratislava_profile__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Drozd čiernoprsý",
    "latin_title": "Turdus dissimilis",
    "english_title": "Black-breasted thrush",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Drozd-ciernoprsy/blackbird__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Emu hnedý",
    "latin_title": "Dromaius novaehollandiae",
    "english_title": "Emu",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Emu/TH75824__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Felzuma madagaskarská",
    "latin_title": "Phelsuma madagascariensis",
    "english_title": "madagascar day gecko",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Plazy-a-obojzivelniky/Felzuma-madagaskarska/felzuma-foto__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Fretka domáca",
    "latin_title": "Mustela putorius furo",
    "english_title": "Domestic ferret",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Fretka-domaca/Fretka-domaca-16__FillMaxWzU0MCw1NDBd.11.2022-VT-4.jpg"
  },
  {
    "name": "Gekón obrovský",
    "latin_title": "Gekko gecko",
    "english_title": "Tokay gecko",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Plazy-a-obojzivelniky/Gekon-obrovsky/gekon-obrobvsky__FillMaxWzU0MCw1NDBd.JPG"
  },
  {
    "name": "Gekončík nočný",
    "latin_title": "Eublepharis macularius",
    "english_title": "Leopard gecko",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Plazy-a-obojzivelniky/Gekoncik-nocny/head-of-leopard-gecko-eublepharis-macularius-in-front-of-black-background-MJOF000291__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Gibon zlatolíci",
    "latin_title": "Nomascus gabriellae",
    "english_title": "Buff-cheeked gibbon",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Gibon-zlatolici/gibon-zlatolici_profile_zoo-bratislava__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Hlaholka severská",
    "latin_title": "Bucephala clangula",
    "english_title": "Common goldeneye",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Common-goldeneye/Hlaholka-severska-archiv-ZOO-vtak-3__FillMaxWzU0MCw1NDBd.JPG"
  },
  {
    "name": "Holub domáci - brčkáň",
    "latin_title": "Columba domestica",
    "english_title": "Domestic pigeon",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Holub-domaci-slovensky-hrvoliak-modry/Holub-domaci-brckan-1__FillMaxWzU0MCw1NDBd.JPG"
  },
  {
    "name": "Holub domáci - francúzsky mondén",
    "latin_title": "Columba livia f. domestica",
    "english_title": "Domestic pigeon - French mondain",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Holub-domaci-slovensky-hrvoliak-zlty/Holub-domaci-francuzsky-monden-16-v2__FillMaxWzU0MCw1NDBd.11.2022-VT.jpg"
  },
  {
    "name": "Holub domáci - pomoranský hrvoliak",
    "latin_title": "Columba domestica",
    "english_title": "Domestic pigeon - Pomeranian Pouter",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Holub-domaci-francuzsky-monden/Holub-domaci-pomoransky-hrvoliak-2022-DM-4__FillMaxWzU0MCw1NDBd.JPG"
  },
  {
    "name": "Holub domáci - slovenský hrvoliak žltý",
    "latin_title": "Columba domestica",
    "english_title": "Domestic pigeon - Slovak Pouter",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Holub-domaci-slovensky-hrvoliak-modry/Holub-domaci-slovensky-hrvoliak-zlty-16__FillMaxWzU0MCw1NDBd.11.2022-VT.jpg"
  },
  {
    "name": "Hrdlička chichotavá",
    "latin_title": "Streptopelia roseogrisea",
    "english_title": "Pink-headed turtle dove",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Hrdlicka-chichotava/Hrdlicka-chichotava-archiv-ZOO-vtak-3__FillMaxWzU0MCw1NDBd.JPG"
  },
  {
    "name": "Hrdlička perlokrká",
    "latin_title": "Streptopelia chinensis",
    "english_title": "Spotted dove",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Hrdlicka-perlokrka/hrdlicka_perlokrka2a__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Hrdzavka potápavá",
    "latin_title": "Netta rufina",
    "english_title": "Red-crested pochard",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Hrdzavka-potapava/DSC_0133_2-v2__FillMaxWzU0MCw1NDBd.JPG"
  },
  {
    "name": "Hrošík libérijský",
    "latin_title": "Choeropsis liberiensis",
    "english_title": "Pygmy hippopotamus",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Hrosik-liberijsky/hrosik-liberijsky-profile-img_zoo-bratislava__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Hus labutia - domáca",
    "latin_title": "Anser cygnoides domestic",
    "english_title": "Domestic swan goose, white",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Hrdzavka-potapava/Hoeckergans_Anser_cygnoides_f__FillMaxWzU0MCw1NDBd._domestica_Wildpark_Poing-01.jpg"
  },
  {
    "name": "Ibis červený",
    "latin_title": "Eudocimus ruber",
    "english_title": "Scarlet ibis",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Scarlet-Ibis/ibis-cerveny-c__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Indický bežec (kačica domáca)",
    "latin_title": "Anas platyrhynchos domestic",
    "english_title": "Domestic duck",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Indicky-bezec-kacica-domaca/DSC7437__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Jaguár americký",
    "latin_title": "Panthera onca",
    "english_title": "Jaguar",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Jaguar-americky/jaguar-americky-c__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Jeleň európsky",
    "latin_title": "Cervus elaphus",
    "english_title": "Red deer",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Jelen-europsky/jelen-europsky_zoo-bratislava-profile__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Kanárik domáci",
    "latin_title": "Serinus canaria f. domestica",
    "english_title": "Domestic canary",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Kanarik-domaci/kanarik_domaci1__FillMaxWzU0MCw1NDBd.JPG"
  },
  {
    "name": "Kariama červenozobá",
    "latin_title": "Cariama cristata",
    "english_title": "Red-legged seriema",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Harriss-hawk/Kariama-cervenozoba-8__FillMaxWzU0MCw1NDBd.6.2023-VT-4.jpg"
  },
  {
    "name": "Kengura červená",
    "latin_title": "Macropus rufus",
    "english_title": "Red kangaroo",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Red-kangaroo/kengura-cervena_zoo-bratislava_profile__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Kôň domáci",
    "latin_title": "Equus caballus",
    "english_title": "Domestic horse",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Domestic-horse/DSC_8315__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Kôň Przewalského",
    "latin_title": "Equus przewalskii",
    "english_title": "Przewalski's Wild Horse",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Domestic-horse/DSC0004__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Koralovka červená",
    "latin_title": "Lampropeltis triangulum sinaloae",
    "english_title": "Sinaloan milksnake",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Plazy-a-obojzivelniky/Koralovka-cervena/koralovka_cervena2__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Koralovka kalifornská",
    "latin_title": "Lampropeltis californiae",
    "english_title": "California kingsnake",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Plazy-a-obojzivelniky/Koralovka-kalifornska/koralovka-foto__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Korela chochlatá",
    "latin_title": "Nymphicus hollandicus",
    "english_title": "Cockatiel",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Cockatiel/korela_chochlata1__FillMaxWzU0MCw1NDBd.JPG"
  },
  {
    "name": "Korytnačka leopardia",
    "latin_title": "Stigmochelys pardalis babcocki",
    "english_title": "Northern leopard tortoise",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Plazy-a-obojzivelniky/Korytnacka-leopardia/Korytnacka-leopardia_TH79130-v2__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Korytnačka uhoľná",
    "latin_title": "Geochelone carbonaria",
    "english_title": "Red-footed tortoise",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Plazy-a-obojzivelniky/Korytnacka-uholna/800px-Geochelone_carbonaria_1__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Kosmáč striebristý",
    "latin_title": "Mico argentatus",
    "english_title": "Silvery marmoset",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Kosmac-striebristy/Kosmac-striebristy_TH79170__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Kosmáč trpasličí",
    "latin_title": "Cebuella pygmaea pygmaea",
    "english_title": "Pygmy marmoset",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Kosmac-striebristy/Kosmac-trpaslici_TH79407__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Koza domáca holandská",
    "latin_title": "Capra hircus f. domestica",
    "english_title": "Dutch pygmy goat",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Koza-domaca-kamerunska/koza-domaca-holandska-c__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Koza domáca kamerunská",
    "latin_title": "Capra hircus f. domestica",
    "english_title": "West African pygmy goat",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Koza-domaca-kamerunska/koza-domaca-kamerunska-c-v2__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Kozorožec alpský",
    "latin_title": "Capra ibex",
    "english_title": "Alpine ibex",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Domestic-horse/DSC1105__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Králik domáci",
    "latin_title": "Oryctolagus cuniculus domesticus/Domestic rabbit",
    "english_title": "None",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/adoption/Cicavce/Kralik-domaci-40/rok/Kralik-domaci-VT__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Kraska červenozobá",
    "latin_title": "Urocissa erythroryncha",
    "english_title": "Red-billed blue magpie",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Red-billed-blue-magpie/kraska-cervenozoba__FillMaxWzU0MCw1NDBd.png"
  },
  {
    "name": "Krkavec čierny",
    "latin_title": "Corvus corax",
    "english_title": "Common Raven",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Collared-falconet-/krkavec3-v2__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Krokodíl čelnatý",
    "latin_title": "Osteolaemus tetraspis",
    "english_title": "African dwarf crocodile",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Plazy-a-obojzivelniky/Krokodil-celnaty/Krokodil-celnaty_TH79925__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Kudu malý",
    "latin_title": "Tragelaphus imberbis",
    "english_title": "Lesser kudu",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/kudu-maly-3__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Kulan turkménsky",
    "latin_title": "Equus hemionus kulan",
    "english_title": "Turkmenian kulan",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Kon-domaci/DSC0290__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Kura domáca - bregovska dzhinka",
    "latin_title": "Gallus gallus domesticus",
    "english_title": "Bregovska Dzhinka Chicken",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Bregovska-Dzhinka-Chicken/Bregovska-dzhinka-16__FillMaxWzU0MCw1NDBd.11.2022-VT10.jpg"
  },
  {
    "name": "Kurička bieločelá",
    "latin_title": "Arborophila gingica",
    "english_title": "Collared hill partridge",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Collared-hill-partridge/kuricka_bielocela1__FillMaxWzU0MCw1NDBd.JPG"
  },
  {
    "name": "Kuvik obyčajný",
    "latin_title": "Athene noctua",
    "english_title": "Little owl",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Little-owl/Kuvik-obycajny_DSC9738_Hulik1__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Labuť čierna",
    "latin_title": "Cygnus atratus",
    "english_title": "Black swan",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Black-swan/DSC7692__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Lama alpaka",
    "latin_title": "Vicugna pacos",
    "english_title": "Alpaca",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Llama/DSC1584__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Lama krotká",
    "latin_title": "Lama glama",
    "english_title": "Llama",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Llama/03_TH70493__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Leguán obojkový",
    "latin_title": "Crotaphytus collaris",
    "english_title": "Collared lizard",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Plazy-a-obojzivelniky/Leguan-obojkovy/leguan-foto__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Lemur kata",
    "latin_title": "Lemur catta",
    "english_title": "Ring-tailed lemur",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Lemur-kata/Lemur-kata_cover_img__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Leňoch dvojprstý",
    "latin_title": "Choloepus didactylus",
    "english_title": "Linne´s two-toed sloth",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Lemur-kata/lenoch-dvojprsty-c__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Leopard cejlónsky",
    "latin_title": "Panthera pardus kotiya",
    "english_title": "Sri Lankan leopard",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Leopard-cejlonsky/leopard-ceylonsky-cover-v2__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Lev juhoafrický",
    "latin_title": "Panthera leo krugeri",
    "english_title": "African lion",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Lev-juhoafricky/Titulna-foto__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Lori trojfarebný",
    "latin_title": "Lorius lory",
    "english_title": "Black-capped lory",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Harriss-hawk/Lori-trojfarebny-VT-14__FillMaxWzU0MCw1NDBd.6.2023-3.jpg"
  },
  {
    "name": "Lyžičiar ružovonohý",
    "latin_title": "Platalea alba",
    "english_title": "African spoonbill",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/African-spoonbill/unnamed__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Mačiak Brazzov",
    "latin_title": "Cercopithecus neglectus",
    "english_title": "De Brazza's monkey",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Maciak-Brazzov/maciak-brazzov-c__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Mačka maloškvrnná",
    "latin_title": "Leopardus geoffroyi",
    "english_title": "Geoffroyi's cat",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Macka-maloskvrnna/Macka-maloskvrnna-cover__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Makak magot",
    "latin_title": "Macaca sylvanus",
    "english_title": "Barbary macaque",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Makak-magot/makak-magot-c__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Mara stepná",
    "latin_title": "Dolichotis patagonum",
    "english_title": "Patagonian mara",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Patagonian-mara/mara-stepna-c__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Medveď hnedý",
    "latin_title": "Ursus arctos",
    "english_title": "Brown bear",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Medve-hnedy/DSC1022__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Mnohonôžka obria",
    "latin_title": "Archispirostreptus gigas",
    "english_title": "Giant african milipede",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Bezstavovce/Mnohonozka-obria/mnohonozka-foto__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Modraňa strakovitá",
    "latin_title": "Cyanopica cooki",
    "english_title": "Iberian azure-winged magpie",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Iberian-azure-winged-magpie/Modrana-strakovita-3__FillMaxWzU0MCw1NDBd.JPG"
  },
  {
    "name": "Monal lesklý",
    "latin_title": "Lophophorus impejanus",
    "english_title": "Himalayan Monal",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Monal-leskly/Monal-leskly-4__FillMaxWzU0MCw1NDBd.1.2023-VT-1.jpg"
  },
  {
    "name": "Morča domáce - Skinny morča",
    "latin_title": "Cavia porcellus f. domestica",
    "english_title": "Domestic guinea pig",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Morca-domace-Skinny-morca/morca-domace1__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Morka očkatá",
    "latin_title": "Meleagris ocellata",
    "english_title": "Ocellated turkey",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Harriss-hawk/Morka-ockata-VT-5__FillMaxWzU0MCw1NDBd.6.2022-1.jpg"
  },
  {
    "name": "Mrenka nádherná",
    "latin_title": "Chromobotia macracanthus",
    "english_title": "Clown loach",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Ryby/Mrenka-nadherna/Mrenka-nadherna_Panciernicek-panda_TH79635__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Mrenka pakistánska",
    "latin_title": "Botia lohachata",
    "english_title": "Reticulate loach",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Ryby/Mrenka-pakistanska/botia-lohachata__FillMaxWzU0MCw1NDBd.jpeg"
  },
  {
    "name": "Mrenka siamská",
    "latin_title": "Crossocheilus oblongus",
    "english_title": "Siamese Algae-eater",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Ryby/Mrenka-siamska/x44756__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Muflón lesný",
    "latin_title": "Ovis aries musimon",
    "english_title": "Mouflon",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Muflon-lesny/muflon-lesny-c__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Muntžak malý",
    "latin_title": "Muntiacus reevesi",
    "english_title": "Chinese muntjac",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Chinese-muntjac/TH75883__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Myšiak štvorfarebný",
    "latin_title": "Parabuteo unicinctus",
    "english_title": "Harris's hawk",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Collared-falconet-/Mysiak-paetfarebny-14__FillMaxWzU0MCw1NDBd.6.2023-VT-2.jpg"
  },
  {
    "name": "Nandu pampový",
    "latin_title": "Rhea americana",
    "english_title": "Greater rhea",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Nandu-pampovy/TH70759-2__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Neónka červená",
    "latin_title": "Paracheirodon axelrodi",
    "english_title": "Cardinal tetra",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Ryby/Neonka-cervena/neonka_cervena__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Nosáľ červený",
    "latin_title": "Nasua nasua",
    "english_title": "Brown-nosed coati",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Nosal-cerveny/nosal-cerveny-c__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Nosorožec tuponosý južný",
    "latin_title": "Ceratotherium simum simum",
    "english_title": "Southern white rhinoceros",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Nosorozec-tuponosy-juzny/TH75723__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Okáč činkvis",
    "latin_title": "Polyplectron bicalcaratum",
    "english_title": "Grey peacock pheasant",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/samica-okaca-cinkvisa-v2__FillMaxWzU0MCw1NDBd.JPG"
  },
  {
    "name": "Orangutan sumatriansky",
    "latin_title": "Pongo abelii",
    "english_title": "Sumatran orangutan",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Orangutan-sumatriansky/01_DSC8931__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Oryx arabský",
    "latin_title": "Oryx leucoryx",
    "english_title": "Arabian oryx",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Oryx-arabsky/Oryx-arabsky_cover_img__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Osmák degu",
    "latin_title": "Octodon degus",
    "english_title": "Degu",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Osmak-degu/Osmak-degu_TH79278__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Ovca domáca ouessantská",
    "latin_title": "Ovis aries ouessant",
    "english_title": "Ouessant sheep",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Native-wallachian-sheep/02_DSC1062__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Ovca domáca valašská",
    "latin_title": "Ovis aries aries",
    "english_title": "Native Wallachian sheep",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Native-wallachian-sheep/ovca-domaca-valaska-c__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Pancierniček malý",
    "latin_title": "Corydoras nanus",
    "english_title": "Dwarf catfish",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Ryby/Panciernicek-maly/Corydoras-nanus__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Pancierníček panda",
    "latin_title": "Corydoras panda",
    "english_title": "Panda catfish",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Ryby/Panciernicek-panda/Longfin-Panda-Corydora-4_1024x1024__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Pancierniček smaragdový",
    "latin_title": "Brochis splendens",
    "english_title": "Common brochis",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Ryby/Panciernicek-smaragdovy/panciernicek_smaragdovy1__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Pancierniček Sterbov",
    "latin_title": "Corydoras sterbai",
    "english_title": "Sterba´s catfish",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Ryby/Panciernicek-Sterbov/panciernicek_sterbov1__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Panda červená",
    "latin_title": "Ailurus fulgens",
    "english_title": "Red panda",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Panda-cervena/DSC8199__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Papagáj červenokrídly",
    "latin_title": "Aprosmictus erythropterus",
    "english_title": "Red-winged parrot",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Red-winged-parrot/papagaj_cervenokridly1__FillMaxWzU0MCw1NDBd.JPG"
  },
  {
    "name": "Papagáj kráľovský",
    "latin_title": "Alisterus scapularis",
    "english_title": "Australian king parrot",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/adoption/Invertebrates/Papagaj-kralovsky-70-/rok/Papagaj-kralovsky_DSC_0012_Dominika-Nagyova2__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Pásavec štetinový",
    "latin_title": "Chaetophractus villosus",
    "english_title": "Large hairy armadillo",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Pasavec-stetinovy/03_DSC8023__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Páv korunkatý",
    "latin_title": "Pavo cristatus",
    "english_title": "Indian peafowl",
    "image_url": "https://www.zoobratislava.sk/assets/Pav-korunkaty-4__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Pelikán ružový",
    "latin_title": "Pelecanus onocrotalus",
    "english_title": "Eastern white pelican",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/New-bird/DSC5343__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Perlička supia",
    "latin_title": "Acryllium vulturinum",
    "english_title": "Vulturine guineafowl",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Perlicka-supia/Perlicka-supia-21__FillMaxWzU0MCw1NDBd.6.2022-VT-1.jpg"
  },
  {
    "name": "Pes ušatý",
    "latin_title": "Otocyon megalotis",
    "english_title": "Bat-eared fox",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Pes-usaty/pes-usaty-cover__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Pichľavec ozdobný",
    "latin_title": "Uromastyx ornata",
    "english_title": "Ornate mastigure",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Plazy-a-obojzivelniky/Pichlavec-ozdobny/Pichlavec-ozdobny_TH79891__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Piraňa Nattererova",
    "latin_title": "Pygocentrus nattereri",
    "english_title": "Red piranha",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Ryby/Pirana-Nattererova/Pirana-Nattererova-4__FillMaxWzU0MCw1NDBd.9.2023-VT.jpg"
  },
  {
    "name": "Pižmovka domáca",
    "latin_title": "Cairina moschata f. domestica",
    "english_title": "Domestic muscovy duck",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Pizmovka-domaca/TH76802__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Plameniak ružový",
    "latin_title": "Phoenicopterus roseus",
    "english_title": "Greater flamingo",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Greater-Flamingo/06_DSC7849__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Plamienka driemavá",
    "latin_title": "Tyto alba",
    "english_title": "Common barn owl",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Common-barn-owl/Plamienka-driemava-1__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Pôtik kapcavý",
    "latin_title": "Aegolius funereus",
    "english_title": "Boreal owl",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Potik-kapcavy/Potik-Kapcavy_DSC_0047_Dominika-Nagyova__FillMaxWzU0MCw1NDBd.JPG"
  },
  {
    "name": "Potkanokengura králikovitá",
    "latin_title": "Bettongia penicillata",
    "english_title": "Woylie",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Potkanokengura-kralikovita/potkanokengura__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Prísavník",
    "latin_title": "Ancistrus sp.",
    "english_title": "Bristlenose catfish",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Ryby/Prisavnik/Prisavnik-ancistrus_TH79470__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Pštros africký",
    "latin_title": "Struthio camelus",
    "english_title": "Common ostrich",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Pstros-africky/pstros_africky1_TH__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Pytón kráľovský",
    "latin_title": "Python regius",
    "english_title": "Ball python",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Plazy-a-obojzivelniky/Pyton-kralovsky/TH70834__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Pytón tmavý",
    "latin_title": "Python molurus bivittatus",
    "english_title": "Burmese python",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Plazy-a-obojzivelniky/Pyton-tmavy/DSC8599__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Pytón zelený",
    "latin_title": "Morelia viridis",
    "english_title": "Green tree python",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Plazy-a-obojzivelniky/Pyton-zeleny/TH79380__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Rohatka ozdobná",
    "latin_title": "Ceratophrys ornata",
    "english_title": " Ornate horned frog",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Plazy-a-obojzivelniky/Rohatka-ozdobna/rohatka-foto__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Rosnička austrálska",
    "latin_title": "Litoria caerulea",
    "english_title": "Australian Green Treefrog",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Plazy-a-obojzivelniky/Rosnicka-australska/Rosnicka-australska-31__FillMaxWzU0MCw1NDBd.5.2023-VT-2.jpg"
  },
  {
    "name": "Rozela penantová",
    "latin_title": "Platycercus elegans",
    "english_title": "Crimson rosella",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Crimson-rosella/rozela_Pennantova1__FillMaxWzU0MCw1NDBd.JPG"
  },
  {
    "name": "Rybárik smejivý",
    "latin_title": "Dacelo novaeguineae",
    "english_title": "Laughing Kookaburra",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Harriss-hawk/Rybarik-smejivy-VT-14__FillMaxWzU0MCw1NDBd.6.2023-6.jpg"
  },
  {
    "name": "Rys kanadský",
    "latin_title": "Lynx canadensis",
    "english_title": "Canadian lynx",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Rys-kanadsky/rys-kanadsky-c__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Rys ostrovid",
    "latin_title": "Lynx lynx carpathicus",
    "english_title": "Eurasian lynx",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Rys-kanadsky/Rys-ostrovid_profile__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Saimiri vevericovitý",
    "latin_title": "Saimiri sciureus",
    "english_title": "Common squirrel monkey",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Saimiri-vevericovity/05_DSC9303__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Scink šalamúnsky",
    "latin_title": "Corucia zebrata",
    "english_title": "Solomon Islands skink",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/adoption/Ryby/Scink-salamunsky-80/rok/scink-salamunsky__FillMaxWzU0MCw1NDBd.JPG"
  },
  {
    "name": "Šimpanz učenlivý",
    "latin_title": "Pan troglodytes",
    "english_title": "Common chimpanzee",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Simpanz-ucenlivy/simpanz-ucenlivy-c__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Sitatunga západná",
    "latin_title": "Tragelaphus spekii gratus",
    "english_title": "Western sitatunga",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Sitatunga-zapadna/sitatunga-zapadna-c__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Stonožka vietnamská",
    "latin_title": "Scolopendra subspinipes",
    "english_title": "Vietnamese centipede",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Bezstavovce/Stonozka-vietnamska/stonozka-foto__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Sumec sklovitý",
    "latin_title": "Kryptopterus bicirrhis",
    "english_title": "Glass catfish",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Ryby/Sumec-sklovity/Sumcek-sklovity_TH79501__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Surikata vlnkavá",
    "latin_title": "Suricata suricatta",
    "english_title": "Slender-tailed meerkat",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Surikata-vlnkava/surikata-vlnkava-c__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Takin zlatý",
    "latin_title": "Budorcas taxicolor bedfordi",
    "english_title": "Golden takin",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/adoption/Cicavce/Takin-zlaty-180/rok/Takin-zlaty-samec-18__FillMaxWzU0MCw1NDBd.9.2023-VT-4.jpg"
  },
  {
    "name": "Tamarín pinčí",
    "latin_title": "Saguinus oedipus",
    "english_title": "Cotton-top tamarin",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Tamarin-zltoruky/Tamarin-pinci_TH79655__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Tamarín žltoruký",
    "latin_title": "Saguinus midas",
    "english_title": "Red-handed tamarin",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Tamarin-zltoruky/Tamarin-zltoruky_TH79952__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Ťava dvojhrbá",
    "latin_title": "Camelus bactrianus",
    "english_title": "Bactrian camel",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Tava-dvojhrba/tava-dvojhrba-c__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Tetra konžská",
    "latin_title": "Phenacogrammus interruptus",
    "english_title": "Congo tetra",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Ryby/Tetra-konzska/Tetra-konzska_DSC7888a__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Tetra krvavá",
    "latin_title": "Hyphessobrycon eques",
    "english_title": "Tetra",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Ryby/Tetra-krvava/Tetra-krvava-4-v2__FillMaxWzU0MCw1NDBd.JPG"
  },
  {
    "name": "Tetra žiarivá",
    "latin_title": "Hemigrammus erythrozonus",
    "english_title": "Glowlight tetra",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Ryby/Tetra-ziariva/Tetra-ziariva-3__FillMaxWzU0MCw1NDBd.JPG"
  },
  {
    "name": "Tragopan modrolíci",
    "latin_title": "Tragopan temminckii",
    "english_title": "Temminck´s tragopan",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Tragopan-modrolici/TH73484__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Tráviar ružovobruchý",
    "latin_title": "Neopsephotus bourkii",
    "english_title": "Bourke´s parrot",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Traviar-ruzovobruchy/Traviar-ruzovobruchy-archiv-ZOO-vtak-1__FillMaxWzU0MCw1NDBd.JPG"
  },
  {
    "name": "Urzon kanadský",
    "latin_title": "Erethizon dorsatum",
    "english_title": "North american porcupine",
    "image_url": "https://www.zoobratislava.sk/assets/Urzon-kanadsky__FillMaxWzU0MCw1NDBd.JPG"
  },
  {
    "name": "Užovka červená",
    "latin_title": "Pantherophis guttatus",
    "english_title": "Cornsnake",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Plazy-a-obojzivelniky/Rosnicka-australska/Uzovka-cervena_TH79835__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Varan ostnatochvostý",
    "latin_title": "Varanus acanthurus",
    "english_title": "Spiny-tailed monitor",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/adoption/Invertebrates/Varan-ostnatochvosty-100-/rok/Varan-ostnatochvosty-VT__FillMaxWzU0MCw1NDBd.JPG"
  },
  {
    "name": "Veverica kanadská",
    "latin_title": "Tamiasciurus hudsonicus",
    "english_title": "Red squirrel",
    "image_url": "https://www.zoobratislava.sk/assets/Veverica-kanadska-24__FillMaxWzU0MCw1NDBd.6.2022-VT-2.jpg"
  },
  {
    "name": "Vlk eurázijský",
    "latin_title": "Canis lupus lupus",
    "english_title": "Eurasian wolf",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Vlk-eurazijsky/TH79417__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Vodárka lečve kafuenská",
    "latin_title": "Kobus leche kafuensis",
    "english_title": "Kafue lechwe",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Kafue-lechwe/Vodarka-lecve-kafuenska-6__FillMaxWzU0MCw1NDBd.JPG"
  },
  {
    "name": "Výr skalný sibírsky",
    "latin_title": "Bubo bubo sibiricus",
    "english_title": "Northern eagle owl",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Harriss-hawk/Vyr-skalny-sibirsky-8__FillMaxWzU0MCw1NDBd.6.2023-VT-2.jpg"
  },
  {
    "name": "Zebra Chapmanova",
    "latin_title": "Equus quagga chapmani",
    "english_title": "Chapman’s zebra",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Domestic-donkey/zebra-chapmanova-__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Zebrička červenozobá",
    "latin_title": "Taeniopygia guttata",
    "english_title": "Timor Zebra Finch",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Harriss-hawk/zebricka_cervenozoba1__FillMaxWzU0MCw1NDBd.JPG"
  },
  {
    "name": "Zemnárka krátkozobá",
    "latin_title": "Cereopsis novaehollandiae",
    "english_title": "Cereopsis goose",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Harriss-hawk/Zemnarka-kratkozoba-28__FillMaxWzU0MCw1NDBd.8.2022-VT-2.jpg"
  },
  {
    "name": "Žeriav japonský",
    "latin_title": "Grus japonensis",
    "english_title": "Red-crowned crane",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Vtaky/Red-crowned-crane/zeriav-japonsky__FillMaxWzU0MCw1NDBd.png"
  },
  {
    "name": "Žirafa Rothschildova",
    "latin_title": "Giraffa camelopardalis rothschildi",
    "english_title": "Baringo giraffe",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Takin-zlaty/TH72896__FillMaxWzU0MCw1NDBd.jpg"
  },
  {
    "name": "Zubor európsky",
    "latin_title": "Bison bonasus",
    "english_title": "European bison",
    "image_url": "https://www.zoobratislava.sk/assets/Uploads/Lexikon/Cicavce/Zubor-europsky/zubor-europsky-c__FillMaxWzU0MCw1NDBd.jpg"
  }
]
---------------------------------------------------------------------------------------------------------------------------
zlin:
[
  {
    "name": "Aligátor americký",
    "latin_title": "Alligator mississippiensis",
    "img_src": "https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1531/df290bc36916a88c398cb684f1748640-t2.jpeg",
    "english_title": "American Alligator"
  },
  {
    "name": "Ara arakanga",
    "latin_title": "Ara macao",
    "img_src": "https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1490/537ac3ba0d2aa54a8cbacf6679a0e3bd-t2.jpeg",
    "english_title": "Scarlet Macaw"
  },
  {
    "name": "Ara hyacintový",
    "latin_title": "Anodorhynchus hyacinthinus",
    "img_src": "https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1511/acd026f4ab9175a07e54e661e408e9bc-t2.jpeg",
    "english_title": "Hyacinth Macaw"
  },
  {
    "name": "Bongo horský",
    "latin_title": "Tragelaphus eurycerus isaaci",
    "img_src": "https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1459/9204ed8c9e241963cd4afc838ed6ed81-t2.jpeg",
    "english_title": "Bongo"
  },
  {
    "name": "Čája bělolící",
    "latin_title": "Chauna chavaria",
    "img_src": "https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1583/dfd0fe19446f313586c9b87bd6e91059-t2.jpeg",
    "english_title": "Northern Screamer"
  },
  {
    "name": "Čáp sedlatý",
    "latin_title": "Ephippiorhynchus senegalensis",
    "img_src": "https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1534/798eeb4188bf8b004b0eb0dc3d04587b-t2.jpeg",
    "english_title": "Saddle-billed Stork"
  },
  {
    "name": "Dingo novoguinejský",
    "latin_title": "Canis dingo hallstromi",
    "img_src": "https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1509/45b290deaa526bc660baaa5022092014-t2.jpeg",
    "english_title": "New Guinea Singing Dog"
  },
  {
    "name": "Dvojzoborožec indický",
    "latin_title": "Buceros bicornis",
    "img_src": "https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1508/912dcd431c3e85af1322eb0672f6b310-t2.jpeg",
    "english_title": "Great Hornbill"
  },
  {
    "name": "Dvojzoborožec nosorožčí",
    "latin_title": "Buceros rhinoceros",
    "img_src": "https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1515/229575d1b8df9c4304f48e0f3bd9491d-t2.jpeg",
    "english_title": "Rhinoceros Hornbill"
  },
  {
    "name": "Dželada hnědá",
    "latin_title": "Theropithecus gelada",
    "img_src": "https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1514/7b2179277fa49a1763ae6fedf643984b-t2.jpeg",
    "english_title": "Gelada Baboon"
  },
  {
    "name": "Emu hnědý",
    "latin_title": "Dromaius novaehollandiae",
    "img_src": "https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1516/b7efd021fddfe7a90fab61c21d125e50-t2.jpeg",
    "english_title": "Emu"
  },
  {
    "name": "Flétnák australský",
    "latin_title": "Gymnorhina tibicen",
    "img_src": "https://www.zoozlin.eu/media/photos/animal/item/gallery/images-654/680184c4a0366ab6766a7ad2f9892ed6-t2.jpeg",
    "english_title": "Australian Magpie"
  },
  {
    "name": "Gaur indický",
    "latin_title": "Bos gaurus gaurus",
    "img_src": "https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1461/7a7bcb9394b37f359304fbde48d5943c-t2.jpeg",
    "english_title": "Indian Gaur"
  },
  {
    "name": "Gibon stříbrný",
    "latin_title": "Hylobates moloch",
    "img_src": "https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1494/03d0991e103f244d5631cca2f333ad42-t2.jpeg",
    "english_title": "Silver Gibbon"
  },
  {
    "name": "Hoko pospolitý",
    "latin_title": "Crax alector",
    "img_src": "https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1658/1af87cf1e1eeafe705fa0910411e60d0-t2.jpeg",
    "english_title": "Black Curassow"
  },
  {
    "name": "Hyena skvrnitá",
    "latin_title": "Crocuta crocuta",
    "img_src": "https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1491/80307262424f6b75318596c832773573-t2.jpeg",
    "english_title": "Spotted Hyena"
  },
  {
    "name": "Hyenka hřivnatá",
    "latin_title": "Proteles cristata",
    "img_src": "https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1968/7733889390ad992dd38854e8a9778585-t2.jpeg"
  },
  {
    "name": "Chápan vlnatý",
    "latin_title": "Lagothrix lagothricha",
    "img_src": "https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1465/f5263b4fc22a60da1521385a527f8457-t2.jpeg"
  },
  {
    "name": "Chvostan bělolící",
    "latin_title": "Pithecia pithecia",
    "img_src": "https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1502/72ae85b30731ec30f988d67dc95d66e2-t2.jpeg",
    "english_title": "Guianan Saki"
  },
  {
    "name": "Jaguár americký",
    "latin_title": "Panthera Onca",
    "img_src": "https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1706/3093a1ee72c44c1619f2a58b8d17517f-t2.jpeg"
  },
  {
    "name": "Jeřáb královský",
    "latin_title": "Balearica regulorum gibbericeps",
    "img_src": "https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1499/bced492c20d399036ffeac28e1f1f796-t2.jpeg",
    "english_title": "Grey Crowned-crane"
  },
  {
    "name": "Jeřáb laločnatý",
    "latin_title": "Bugeranus carunculatus",
    "img_src": "https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1498/1fc77524183ed7399552f80516fdf7dc-t2.jpeg",
    "english_title": "Wattled Crane"
  },
  {
    "name": "Kapybara",
    "latin_title": "Hydrochaeris hydrochaeris",
    "img_src": "https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1464/10e30b30e6b5baf859c6f1c6ed7d59ed-t2.jpeg",
    "english_title": "Capybara"
  },
  {
    "name": "Kasuár přilbový",
    "latin_title": "Casuarius casuarius",
    "img_src": "https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1510/d7868efa16731558155cc25ee00f5e2b-t2.jpeg",
    "english_title": "Southern Cassowary"
  },
  {
    "name": "Kivi hnědý",
    "latin_title": "Apteryx mantelli",
    "img_src": "https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1607/d2c3dc346f9fd871c6ad13ec850f2d6b-t2.jpeg",
    "english_title": "North Island Kiwi"
  },
  {
    "name": "Klokan rudokrký",
    "latin_title": "Macropus rufogriseus",
    "img_src": "https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1507/52efdcb0d963fb6ae32b7e5168562fd6-t2.jpeg",
    "english_title": "Red-necked Wallaby"
  },
  {
    "name": "Kotinga tříbarvá",
    "latin_title": "Perissocephalus tricolor",
    "img_src": "https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1536/d243ca859d4e5a15d9147a60b7ee2ae5-t2.jpeg",
    "english_title": "Capuchin Bird"
  },
  {
    "name": "Kotul veverovitý",
    "latin_title": "Saimiri sciureus",
    "img_src": "https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1493/fb9ad13fcd68c416be2293dd1f25340a-t2.jpeg",
    "english_title": "Common Squirrel Monkey"
  },
  {
    "name": "Kudu velký",
    "latin_title": "Tragelaphus strepsiceros",
    "img_src": "https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1519/2cecfbebf9233533333a9f093c89bddd-t2.jpeg",
    "english_title": "Greater Kudu"
  },
  {
    "name": "Lachtan hřivnatý",
    "latin_title": "Otaria byronia",
    "img_src": "https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1660/e2c8dc4ef3dee97a7a346bb245016eec-t2.jpeg",
    "english_title": "South American Sea Lion"
  },
  {
    "name": "Lemur kata",
    "latin_title": "Lemur catta",
    "img_src": "https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1497/ac4da6233f1c567faae8c09c93ada06d-t2.jpeg",
    "english_title": "Ring-tailed Lemur"
  },
  {
    "name": "Lenochod dvouprstý",
    "latin_title": "Choloepus didactylus",
    "img_src": "https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1506/87d80778f5615ad2aa4b8cba3e72fc3d-t2.jpeg",
    "english_title": "Southern Two-toed Sloth"
  },
  {
    "name": "Lev konžský",
    "latin_title": "Panthera leo bleyenberghi",
    "img_src": "https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1503/be1571a1b5de8b2951c610ea8dd8a5c2-t2.jpeg",
    "english_title": "Katanga Lion"
  },
  {
    "name": "Medvěd pyskatý",
    "latin_title": "Melursus ursinus",
    "img_src": "https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1501/cfa99536deea7539a15057d7478dd0af-t2.jpeg",
    "english_title": "Sloth Bear"
  },
  {
    "name": "Mravenečník čtyřprstý",
    "latin_title": "Tamandua tetradactyla",
    "img_src": "https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1500/4f93585e48c850a06bcf541dae6ac041-t2.jpeg",
    "english_title": "Southern Tamandua"
  },
  {
    "name": "Mravenečník velký",
    "latin_title": "Myrmecophaga tridactyla",
    "img_src": "https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1677/4f201f3637846c5960c8de7c4046147d-t2.jpeg",
    "english_title": "Giant Anteater"
  },
  {
    "name": "Nandu Darwinův",
    "latin_title": "Pterocnemia pennata pennata",
    "img_src": "https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1537/bce5c8475d26ee10fb30bf1491f52902-t2.jpeg",
    "english_title": "Lesser Rhea"
  },
  {
    "name": "Nestor kea",
    "latin_title": "Nestor notabilis",
    "img_src": "https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1533/833fe1978304462d5d25c3ec92187d71-t2.jpeg",
    "english_title": "Nestor Kea"
  },
  {
    "name": "Nesyt bílý",
    "latin_title": "Mycteria cinerea",
    "img_src": "https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1661/fcf937b4b94897c9acf84fb11aec51d0-t2.jpeg",
    "english_title": "Milky Stork"
  },
  {
    "name": "Nesyt indomalajský",
    "latin_title": "Mycteria leucocephala",
    "img_src": "https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1541/cb9efb6a4746daacc177e3778967ee18-t2.jpeg",
    "english_title": "Painted Stork"
  },
  {
    "name": "Nosorožec tuponosý jižní",
    "latin_title": "Ceratotherium simum simum",
    "img_src": "https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1525/80bee7370665e8a8bfb8095c16c34adb-t2.jpeg",
    "english_title": "Southern white rhinoceros"
  },
  {
    "name": "Orel korunkatý",
    "latin_title": "Stephanoaetus coronatus",
    "img_src": "https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1505/4adaac1a114bef5a76e88554f24df4c6-t2.jpeg",
    "english_title": "Crowned eagle"
  },
  {
    "name": "Panda červená",
    "latin_title": "Ailurus fulgens",
    "img_src": "https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1463/0213cd9b4f89f7a6abdf7d7b88ad4b18-t2.jpeg",
    "english_title": "Red panda"
  },
  {
    "name": "Pelikán australský",
    "latin_title": "Pelecanus conspicillatus",
    "img_src": "https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1520/0a6e5999e11dfed7c5707b8e43496e8c-t2.jpeg",
    "english_title": "Australian Pelican"
  },
  {
    "name": "Pižmovka bělokřídlá",
    "latin_title": "Asarcornis scutulata",
    "img_src": "https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1512/baf06cf5a73c951f22ff17d01c5fabae-t2.jpeg",
    "english_title": "White-winged Duck"
  },
  {
    "name": "Plameňák malý",
    "latin_title": "Phoeniconaias minor",
    "img_src": "https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1513/407298b1d134fc49f6af53c0cf644718-t2.jpeg",
    "english_title": "Lesser Flamingo"
  },
  {
    "name": "Plameňák růžový",
    "latin_title": "Phoenicopterus roseus",
    "img_src": "https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1522/402bc344b16ec04f2711970f04b02fdf-t2.jpeg",
    "english_title": "Greater Flamingo"
  },
  {
    "name": "Siba ománská",
    "latin_title": "Rhinoptera jayakari",
    "img_src": "https://www.zoozlin.eu/media/photos/animal/item/gallery/images-490/14cd031b762db25ed890f9c0cd846a33-t2.jpeg",
    "english_title": "Oman Cownose Ray"
  },
  {
    "name": "Slon africký",
    "latin_title": "Loxodonta africana",
    "img_src": "https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1466/66d56e8d82e596fbc9d9dd77c17761d2-t2.jpeg",
    "english_title": "African Elephant"
  },
  {
    "name": "Sup bělohlavý",
    "latin_title": "Gyps fulvus",
    "img_src": "https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1538/bdabf5774d7813dbb0980e099b5d57a7-t2.jpeg",
    "english_title": "Griffon Vulture"
  },
  {
    "name": "Sup himálajský",
    "latin_title": "Gyps himalayensis",
    "img_src": "https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1539/3180ea7537a7bae3d56ffc79180c7bd3-t2.jpeg",
    "english_title": "Himalayan Griffon"
  },
  {
    "name": "Sup hnědý",
    "latin_title": "Aegypius monachus",
    "img_src": "https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1540/2567f8d1f7309e1e6f6c1e852ecde987-t2.jpeg",
    "english_title": "Black Vulture"
  },
  {
    "name": "Sup chocholatý",
    "latin_title": "Trigonoceps occipitalis",
    "img_src": "https://www.zoozlin.eu/media/photos/animal/item/gallery/images-647/4c149a633b3a2d2c98b8aa7d11e4b51e-t2.jpeg",
    "english_title": "White-headed Vulture"
  },
  {
    "name": "Sup kapucín",
    "latin_title": "Necrosyrtes monachus",
    "img_src": "https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1528/93482f7069aefa7246cea7684af535d5-t2.jpeg",
    "english_title": "Hooded Vulture"
  },
  {
    "name": "Sup mrchožravý",
    "latin_title": "Neophron percnopterus",
    "img_src": "https://www.zoozlin.eu/media/photos/animal/item/gallery/images-648/8a2dedfdd778dab9c25e2ab80885f2bd-t2.jpeg"
  },
  {
    "name": "Sup Rüppellův",
    "latin_title": "Gyps rueppellii",
    "img_src": "https://www.zoozlin.eu/media/photos/animal/item/gallery/images-649/5d78ade7cf6f2842c060cc546b088368-t2.jpeg"
  },
  {
    "name": "Surikata",
    "latin_title": "Suricata suricatta",
    "img_src": "https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1485/271d4c6d7bb29f5109f1933a7a3dbc5b-t2.jpeg",
    "english_title": "Meerkat"
  },
  {
    "name": "Tamarín pestrý",
    "latin_title": "Saguinus bicolor",
    "img_src": "https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1486/ede60c8c95ad3e2fc5473c6b85a9d58e-t2.jpeg",
    "english_title": "Brazilian Bare-faced Tamarin"
  },
  {
    "name": "Tapír čabrakový",
    "latin_title": "Tapirus indicus",
    "img_src": "https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1521/b5fbcabf026a727b4ab6658099dd4034-t2.jpeg",
    "english_title": "Malayan Tapir"
  },
  {
    "name": "Tapír jihoamerický",
    "latin_title": "Tapirus terrestris",
    "img_src": "https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1489/7989b81a4606050e12df98bb44f7f527-t2.jpeg",
    "english_title": "South American Tapir"
  },
  {
    "name": "Tučňák Humboldtův",
    "latin_title": "Spheniscus humboldti",
    "img_src": "https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1524/c2999045951080a04a4a4e71d6fb1737-t2.jpeg",
    "english_title": "Humboldt Penguin"
  },
  {
    "name": "Tygr ussurijský",
    "latin_title": "Panthera tigris altaica",
    "img_src": "https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1504/bfacf956e16e85760d8da67f5973c133-t2.jpeg",
    "english_title": "Siberian Tiger"
  },
  {
    "name": "Velbloud dvouhrbý",
    "latin_title": "Camelus bactrianus",
    "img_src": "https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1518/4d6d541e6e7d9c07cb6e9536c2ec7ed9-t2.jpeg",
    "english_title": "Bactrian Camel"
  },
  {
    "name": "Veverka šedobřichá",
    "latin_title": "Tamiops swinhoei",
    "img_src": "https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1523/a096b9493b2d2bab30d0a82c060fc183-t2.jpeg",
    "english_title": "Swinhoe's Striped Squirrel"
  },
  {
    "name": "Vikuňa",
    "latin_title": "Vicugna vicugna",
    "img_src": "https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1462/d146c6ed6c5c1df3de8e4b9d27b3c787-t2.jpeg",
    "english_title": "Vicugna"
  },
  {
    "name": "Vlhovec žlutohřbetý",
    "latin_title": "Cacicus cela",
    "img_src": "https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1688/66952edb726ed08f6a5d6c26d16fdaef-t2.jpeg",
    "english_title": "Yellow-rumped Cacique"
  },
  {
    "name": "Vydra obrovská",
    "latin_title": "Pteronura brasiliensis",
    "img_src": "https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1460/85cd6bc06ee172d0938879ed4615eec8-t2.jpeg",
    "english_title": "Giant Otter"
  },
  {
    "name": "Zoborožec havraní",
    "latin_title": "Bucorvus abyssinicus",
    "img_src": "https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1529/ee5df0d8afd256d812a909ead66465c7-t2.jpeg",
    "english_title": "Abyssinian Ground Hornbill"
  },
  {
    "name": "Želva mohutná",
    "latin_title": "Manouria emys",
    "img_src": "https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1659/6989a9c4df9cf9a325021d16707efea9-t2.jpeg",
    "english_title": "Burmese Brown Tortoise"
  },
  {
    "name": "Žirafa Rothschildova",
    "latin_title": "Giraffa camelopardalis rothschildi",
    "img_src": "https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1487/0580c33de433853d2c641a06a7efed7c-t2.jpeg",
    "english_title": "Rothschild's Giraffe"
  }
]

'''



#toto prislo zo zlina
####['Aligátor americký', 'Ara arakanga', 'Ara hyacintový', 'Bongo horský', 'Čája bělolící', 'Čáp sedlatý', 'Dingo novoguinejský', 'Dvojzoborožec indický', 'Dvojzoborožec nosorožčí', 'Dželada hnědá', 'Emu hnědý', 'Flétnák australský', 'Gaur indický', 'Gibon stříbrný', 'Hoko pospolitý', 'Hyena skvrnitá', 'Hyenka hřivnatá', 'Chápan vlnatý', 'Chvostan bělolící', 'Jaguár americký', 'Jeřáb královský', 'Jeřáb laločnatý', 'Kapybara', 'Kasuár přilbový', 'Kivi hnědý', 'Klokan rudokrký', 'Kotinga tříbarvá', 'Kotul veverovitý', 'Kudu velký', 'Lachtan hřivnatý', 'Lemur kata', 'Lenochod dvouprstý', 'Lev konžský', 'Medvěd pyskatý', 'Mravenečník čtyřprstý', 'Mravenečník velký', 'Nandu Darwinův', 'Nestor kea', 'Nesyt bílý', 'Nesyt indomalajský', 'Nosorožec tuponosý jižní', 'Orel korunkatý', 'Panda červená', 'Pelikán australský', 'Pižmovka bělokřídlá', 'Plameňák malý', 'Plameňák růžový', 'Siba ománská', 'Slon africký', 'Sup bělohlavý', 'Sup himálajský', 'Sup hnědý', 'Sup chocholatý', 'Sup kapucín', 'Sup mrchožravý', 'Sup Rüppellův', 'Surikata', 'Tamarín pestrý', 'Tapír čabrakový', 'Tapír jihoamerický', 'Tučňák Humboldtův', 'Tygr ussurijský', 'Velbloud dvouhrbý', 'Veverka šedobřichá', 'Vikuňa', 'Vlhovec žlutohřbetý', 'Vydra obrovská', 'Zoborožec havraní', 'Želva mohutná', 'Žirafa Rothschildova']
####['https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1531/df290bc36916a88c398cb684f1748640-t1.jpeg', 'https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1490/537ac3ba0d2aa54a8cbacf6679a0e3bd-t1.jpeg', 'https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1511/acd026f4ab9175a07e54e661e408e9bc-t1.jpeg', 'https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1459/9204ed8c9e241963cd4afc838ed6ed81-t1.jpeg', 'https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1583/dfd0fe19446f313586c9b87bd6e91059-t1.jpeg', 'https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1534/798eeb4188bf8b004b0eb0dc3d04587b-t1.jpeg', 'https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1509/45b290deaa526bc660baaa5022092014-t1.jpeg', 'https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1508/912dcd431c3e85af1322eb0672f6b310-t1.jpeg', 'https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1515/229575d1b8df9c4304f48e0f3bd9491d-t1.jpeg', 'https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1514/7b2179277fa49a1763ae6fedf643984b-t1.jpeg', 'https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1516/b7efd021fddfe7a90fab61c21d125e50-t1.jpeg', 'https://www.zoozlin.eu/media/photos/animal/item/gallery/images-654/680184c4a0366ab6766a7ad2f9892ed6-t1.jpeg', 'https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1461/7a7bcb9394b37f359304fbde48d5943c-t1.jpeg', 'https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1494/03d0991e103f244d5631cca2f333ad42-t1.jpeg', 'https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1658/1af87cf1e1eeafe705fa0910411e60d0-t1.jpeg', 'https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1491/80307262424f6b75318596c832773573-t1.jpeg', 'https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1968/7733889390ad992dd38854e8a9778585-t1.jpeg', 'https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1465/f5263b4fc22a60da1521385a527f8457-t1.jpeg', 'https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1502/72ae85b30731ec30f988d67dc95d66e2-t1.jpeg', 'https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1706/3093a1ee72c44c1619f2a58b8d17517f-t1.jpeg', 'https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1499/bced492c20d399036ffeac28e1f1f796-t1.jpeg', 'https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1498/1fc77524183ed7399552f80516fdf7dc-t1.jpeg', 'https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1464/10e30b30e6b5baf859c6f1c6ed7d59ed-t1.jpeg', 'https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1510/d7868efa16731558155cc25ee00f5e2b-t1.jpeg', 'https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1607/d2c3dc346f9fd871c6ad13ec850f2d6b-t1.jpeg', 'https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1507/52efdcb0d963fb6ae32b7e5168562fd6-t1.jpeg', 'https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1536/d243ca859d4e5a15d9147a60b7ee2ae5-t1.jpeg', 'https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1493/fb9ad13fcd68c416be2293dd1f25340a-t1.jpeg', 'https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1519/2cecfbebf9233533333a9f093c89bddd-t1.jpeg', 'https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1660/e2c8dc4ef3dee97a7a346bb245016eec-t1.jpeg', 'https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1497/ac4da6233f1c567faae8c09c93ada06d-t1.jpeg', 'https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1506/87d80778f5615ad2aa4b8cba3e72fc3d-t1.jpeg', 'https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1503/be1571a1b5de8b2951c610ea8dd8a5c2-t1.jpeg', 'https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1501/cfa99536deea7539a15057d7478dd0af-t1.jpeg', 'https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1500/4f93585e48c850a06bcf541dae6ac041-t1.jpeg', 'https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1677/4f201f3637846c5960c8de7c4046147d-t1.jpeg', 'https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1537/bce5c8475d26ee10fb30bf1491f52902-t1.jpeg', 'https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1533/833fe1978304462d5d25c3ec92187d71-t1.jpeg', 'https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1661/fcf937b4b94897c9acf84fb11aec51d0-t1.jpeg', 'https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1541/cb9efb6a4746daacc177e3778967ee18-t1.jpeg', 'https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1525/80bee7370665e8a8bfb8095c16c34adb-t1.jpeg', 'https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1505/4adaac1a114bef5a76e88554f24df4c6-t1.jpeg', 'https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1463/0213cd9b4f89f7a6abdf7d7b88ad4b18-t1.jpeg', 'https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1520/0a6e5999e11dfed7c5707b8e43496e8c-t1.jpeg', 'https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1512/baf06cf5a73c951f22ff17d01c5fabae-t1.jpeg', 'https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1513/407298b1d134fc49f6af53c0cf644718-t1.jpeg', 'https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1522/402bc344b16ec04f2711970f04b02fdf-t1.jpeg', 'https://www.zoozlin.eu/media/photos/animal/item/gallery/images-490/14cd031b762db25ed890f9c0cd846a33-t1.jpeg', 'https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1466/66d56e8d82e596fbc9d9dd77c17761d2-t1.jpeg', 'https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1538/bdabf5774d7813dbb0980e099b5d57a7-t1.jpeg', 'https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1539/3180ea7537a7bae3d56ffc79180c7bd3-t1.jpeg', 'https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1540/2567f8d1f7309e1e6f6c1e852ecde987-t1.jpeg', 'https://www.zoozlin.eu/media/photos/animal/item/gallery/images-647/4c149a633b3a2d2c98b8aa7d11e4b51e-t1.jpeg', 'https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1528/93482f7069aefa7246cea7684af535d5-t1.jpeg', 'https://www.zoozlin.eu/media/photos/animal/item/gallery/images-648/8a2dedfdd778dab9c25e2ab80885f2bd-t1.jpeg', 'https://www.zoozlin.eu/media/photos/animal/item/gallery/images-649/5d78ade7cf6f2842c060cc546b088368-t1.jpeg', 'https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1485/271d4c6d7bb29f5109f1933a7a3dbc5b-t1.jpeg', 'https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1486/ede60c8c95ad3e2fc5473c6b85a9d58e-t1.jpeg', 'https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1521/b5fbcabf026a727b4ab6658099dd4034-t1.jpeg', 'https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1489/7989b81a4606050e12df98bb44f7f527-t1.jpeg', 'https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1524/c2999045951080a04a4a4e71d6fb1737-t1.jpeg', 'https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1504/bfacf956e16e85760d8da67f5973c133-t1.jpeg', 'https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1518/4d6d541e6e7d9c07cb6e9536c2ec7ed9-t1.jpeg', 'https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1523/a096b9493b2d2bab30d0a82c060fc183-t1.jpeg', 'https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1462/d146c6ed6c5c1df3de8e4b9d27b3c787-t1.jpeg', 'https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1688/66952edb726ed08f6a5d6c26d16fdaef-t1.jpeg', 'https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1460/85cd6bc06ee172d0938879ed4615eec8-t1.jpeg', 'https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1529/ee5df0d8afd256d812a909ead66465c7-t1.jpeg', 'https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1659/6989a9c4df9cf9a325021d16707efea9-t1.jpeg', 'https://www.zoozlin.eu/media/photos/animal/item/gallery/images-1487/0580c33de433853d2c641a06a7efed7c-t1.jpeg']

# ked ziskam vsetky nazvy, viem pomocou pydentic vygenerovat ostatne data - popisy a ine

# Použitie BeautifulSoup na analýzu HTML
soup = BeautifulSoup(html_content, 'lxml')


image_links = soup.find_all('a', class_='animal')

# Vytvoríme zoznam, do ktorého pridáme všetky URL obrázkov
image_urls = []

# Pre každý odkaz získame obrázok a jeho URL
for link in image_links:
    img = link.find('img')  # Hľadáme tag <img> v rámci odkazu
    if img and img.get('src'):  # Uistíme sa, že obrázok má atribút 'src'
        img_src = img.get('src')  # Získame hodnotu atribútu 'src'
        full_img_url = f"https://www.zoozlin.eu{img_src}"  # Zostavíme celkový URL
        image_urls.append(full_img_url)  # Pridáme do zoznamu




# Výpis výsledkov
print(image_urls)

pripona = 't1.jpeg'
for i in range(len(image_urls)):
    image_urls[i] = image_urls[i][:-7] + pripona 

print(image_urls)

















from pydantic import BaseModel
from typing import List
from faker import Faker
import random
import json

fake = Faker()

class Animal(BaseModel):
    name: str
    species: str
    age: int
    location: str

class Zoo(BaseModel):
    name: str
    animals: List[Animal]

def generate_animal() -> Animal:
    species_list = ["Lion", "Elephant", "Zebra", "Tiger", "Giraffe", "Panda", "Kangaroo"]
    location_list = ["Savanna Area", "Jungle Area", "Forest Area", "Aquatic Area", "Arctic Zone"]
    
    name = fake.first_name()  # Náhodné meno
    species = random.choice(species_list)  # Náhodný druh zvieraťa
    age = random.randint(1, 15)  # Náhodný vek zvieraťa
    location = random.choice(location_list)  # Náhodná lokalizácia v zoo
    
    return Animal(name=name, species=species, age=age, location=location)

def generate_zoo(num_animals: int) -> Zoo:
    animals = [generate_animal() for _ in range(num_animals)]
    return Zoo(name=fake.company(), animals=animals)  # Generovanie názvu zoo

zoo = generate_zoo(10)

zoo_json = zoo.json(indent=4)


print(zoo_json)

with open("generated_zoo_data.json", "w") as f:
    f.write(zoo_json)
