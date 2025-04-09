import requests
from bs4 import BeautifulSoup

# pip install requests beautifulsoup4 lxml
# toto sa d apouzit na bratislavsku zoo, v 'h4', class_='title' maju ulozene vsetky zvierata v lexikone na stranke https://www.zoobratislava.sk/nase-zvierata/lexikon-zvierat/
# pre zoo zlin sa to da upravit na https://www.zoozlin.eu/zvirata-dle-abecedy/ a <h3 class="article-headline"> - maju tak o polovicu zvierat menej, to bude lepsie
#toto prislo z bratislavy

####['Adax núbijský', 'Agama bradatá', 'Antilopa nilgau', 'Antilopa vraná', 'Ara zelená', 'Bažant diamantový', 'Bažant zlatý', 'Bažant zlatý broskyňový', 'Belaňa tundrová', 'Bichirek kalabarský', 'Brazílska červeno-biela tarantula ', 'Chocholačka bielooká', 'Daman stromový', 'Daniel škvrnitý', 'Dikdik Kirkov', 'Dikobraz bielochvostý', 'Diviak lesný', 'Diviak visajanský', 'Drozd čiernoprsý', 'Emu hnedý', 'Felzuma madagaskarská', 'Fretka domáca', 'Gekón obrovský', 'Gekončík nočný', 'Gibon zlatolíci', 'Hlaholka severská', 'Holub domáci - brčkáň', 'Holub domáci - francúzsky mondén', 'Holub domáci - pomoranský hrvoliak', 'Holub domáci - slovenský hrvoliak žltý', 'Hrdlička chichotavá', 'Hrdlička perlokrká', 'Hrdzavka potápavá', 'Hrošík libérijský', 'Hus labutia - domáca', 'Ibis červený', 'Indický bežec (kačica domáca)', 'Jaguár americký', 'Jeleň európsky', 'Kanárik domáci', 'Kariama červenozobá', 'Kengura červená', 'Kôň domáci', 'Kôň Przewalského', 'Koralovka červená', 'Koralovka kalifornská', 'Korela chochlatá', 'Korytnačka leopardia', 'Korytnačka uhoľná', 'Kosmáč striebristý', 'Kosmáč trpasličí', 'Koza domáca holandská', 'Koza domáca kamerunská', 'Kozorožec alpský', 'Králik domáci', 'Kraska červenozobá', 'Krkavec čierny', 'Krokodíl čelnatý', 'Kudu malý', 'Kulan turkménsky', 'Kura domáca - bregovska dzhinka', 'Kurička bieločelá', 'Kuvik obyčajný', 'Labuť čierna', 'Lama alpaka', 'Lama krotká', 'Leguán obojkový', 'Lemur kata', 'Leňoch dvojprstý', 'Leopard cejlónsky', 'Lev juhoafrický', 'Lori trojfarebný', 'Lyžičiar ružovonohý', 'Mačiak Brazzov', 'Mačka maloškvrnná', 'Makak magot', 'Mara stepná', 'Medveď hnedý', 'Mnohonôžka obria', 'Modraňa strakovitá', 'Monal lesklý', 'Morča domáce - Skinny morča', 'Morka očkatá', 'Mrenka nádherná', 'Mrenka pakistánska', 'Mrenka siamská', 'Muflón lesný', 'Muntžak malý', 'Myš zebrovaná', 'Myšiak štvorfarebný', 'Nandu pampový', 'Neónka červená', 'Nosáľ červený', 'Nosorožec tuponosý južný', 'Okáč činkvis', 'Orangutan sumatriansky', 'Oryx arabský', 'Osmák degu', 'Ovca domáca ouessantská', 'Ovca domáca valašská', 'Pancierniček malý', 'Pancierníček panda', 'Pancierniček smaragdový', 'Pancierniček Sterbov', 'Panda červená', 'Papagáj červenokrídly', 'Papagáj kráľovský', 'Pásavec štetinový', 'Páv korunkatý', 'Pelikán ružový', 'Perlička supia', 'Pes ušatý', 'Pichľavec ozdobný', 'Piesočník pestrý', 'Piraňa Nattererova', 'Pižmovka domáca', 'Plameniak ružový', 'Plamienka driemavá', 'Pôtik kapcavý', 'Potkanokengura králikovitá', 'Prísavník', 'Pštros africký', 'Pytón kráľovský', 'Pytón tmavý', 'Pytón zelený', 'Rohatka ozdobná', 'Rosnička austrálska', 'Rozela penantová', 'Rybárik smejivý', 'Rys kanadský', 'Rys ostrovid', 'Saimiri vevericovitý', 'Scink šalamúnsky', 'Šimpanz učenlivý', 'Sitatunga západná', 'Somár domáci', 'Stonožka vietnamská', 'Šťúr obrovský', 'Šťúr obrovský', 'Sumec sklovitý', 'Surikata vlnkavá', 'Takin zlatý', 'Tamarín pinčí', 'Tamarín žltoruký', 'Ťava dvojhrbá', 'Tetra konžská', 'Tetra krvavá', 'Tetra žiarivá', 'Tragopan modrolíci', 'Tráviar ružovobruchý', 'Urzon kanadský', 'Užovka červená', 'Varan ostnatochvostý', 'Veverica kanadská', 'Vlk eurázijský', 'Vodárka lečve kafuenská', 'Výr skalný sibírsky', 'Zebra Chapmanova', 'Zebrička červenozobá', 'Zemnárka krátkozobá', 'Žeriav japonský', 'Žirafa Rothschildova', 'Zubor európsky']


#toto prislo zo zlina
####['Aligátor americký', 'Ara arakanga', 'Ara hyacintový', 'Bongo horský', 'Čája bělolící', 'Čáp sedlatý', 'Dingo novoguinejský', 'Dvojzoborožec indický', 'Dvojzoborožec nosorožčí', 'Dželada hnědá', 'Emu hnědý', 'Flétnák australský', 'Gaur indický', 'Gibon stříbrný', 'Hoko pospolitý', 'Hyena skvrnitá', 'Hyenka hřivnatá', 'Chápan vlnatý', 'Chvostan bělolící', 'Jaguár americký', 'Jeřáb královský', 'Jeřáb laločnatý', 'Kapybara', 'Kasuár přilbový', 'Kivi hnědý', 'Klokan rudokrký', 'Kotinga tříbarvá', 'Kotul veverovitý', 'Kudu velký', 'Lachtan hřivnatý', 'Lemur kata', 'Lenochod dvouprstý', 'Lev konžský', 'Medvěd pyskatý', 'Mravenečník čtyřprstý', 'Mravenečník velký', 'Nandu Darwinův', 'Nestor kea', 'Nesyt bílý', 'Nesyt indomalajský', 'Nosorožec tuponosý jižní', 'Orel korunkatý', 'Panda červená', 'Pelikán australský', 'Pižmovka bělokřídlá', 'Plameňák malý', 'Plameňák růžový', 'Siba ománská', 'Slon africký', 'Sup bělohlavý', 'Sup himálajský', 'Sup hnědý', 'Sup chocholatý', 'Sup kapucín', 'Sup mrchožravý', 'Sup Rüppellův', 'Surikata', 'Tamarín pestrý', 'Tapír čabrakový', 'Tapír jihoamerický', 'Tučňák Humboldtův', 'Tygr ussurijský', 'Velbloud dvouhrbý', 'Veverka šedobřichá', 'Vikuňa', 'Vlhovec žlutohřbetý', 'Vydra obrovská', 'Zoborožec havraní', 'Želva mohutná', 'Žirafa Rothschildova']


# ked ziskam vsetky nazvy, viem pomocou pydentic vygenerovat ostatne data - popisy a ine


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
