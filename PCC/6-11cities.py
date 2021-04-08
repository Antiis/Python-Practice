#Ex. 6-11 Cities

cities = {
    'zagreb':{
        'country':'croatia',
        'population':'1.1M',
        'fact':'Povijesno gledajući, grad Zagreb je izrastao iz dva naselja na susjednim brežuljcima, Gradeca i Kaptola.',
    },
    'ljubljana':{
        'country':'slovenia',
        'population':'280K',
        'fact':'Grad leži na rijeci Ljubljanici, približno 10 km od utoka u Savu.',
    },
    'sarajevo':{
        'country':'Bosnia',
        'population':'275K',
        'fact':'Nalazi se na rijeci Miljacki, desnom pritoku Bosne, u istočnom dijelu sarajevsko-zeničke kotline.',
    },
}

for city, city_info in cities.items():
    print(f"City of {city.title()} is the capital of {city_info['country'].title()} with a population around {city_info['population']}.\nFact (in Croatian):\n{city_info['fact']}\n")
