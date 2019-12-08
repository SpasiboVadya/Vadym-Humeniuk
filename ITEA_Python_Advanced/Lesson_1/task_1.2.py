country_dict = {
    'Austria': 'Vienna',  # All 45 countries of Europe and their capitals
    'Albania': 'Tirana',
    'Andorra': 'Andorra-la-Vella',
    'Belarus':	'Minsk',
    'Bulgaria': 'Sofia',
    'Herzegovina': 'Sarajevo',
    'Vatican': 'Vatican',
    'United Kingdom': 'London',
    'Hungary': 'Budapest',
    'Germany': 'Berlin',
    'Greece': 'Athens',
    'Denmark': 'Copenhagen',
    'Ireland': 'Dublin',
    'Iceland': 'Reykjavik',
    'Spain': 'Madrid',
    'Italy': 'Rome',
    'Kosovo': 'Pristina',
    'Latvia': 'Riga',
    'Lithuania': 'Vilnius',
    'Liechtenstein': 'Vaduz',
    'Luxembourg': 'Luxembourg',
    'Macedonia': 'Skopje',
    'Malta': 'Valletta',
    'Moldova': 'Chisinau',
    'Monaco': 'Monaco',
    'Netherlands': 'Amsterdam',
    'Norway': 'Oslo',
    'Poland': 'Warsaw',
    'Portugal': 'Lisbon',
    'Russia': 'Moscow',
    'Romania': 'Bucharest',
    'San-Marino': 'San-Marino',
    'Serbia': 'Belgrade',
    'Slovakia': 'Bratislava',
    'Slovenia': 'Ljubljana',
    'Ukraine': 'Kiev',
    'Finland': 'Helsinki',
    'France': 'Paris',
    'Croatia': 'Zagreb',
    'Montenegro': 'Podgorica',
    'Czech Republic': 'Prague',
    'Switzerland': 'Bern',
    'Sweden': 'Stockholm',
    'Estonia': 'Tallinn',

}

country_list = ['Ukraine', 'California', 'Spain', 'China', 'Monaco', 'Nigeria', 'Vatican', 'Poland', 'France']

for i in country_list:
    if i in country_dict:
        print(country_dict[i])