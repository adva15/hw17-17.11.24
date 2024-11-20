israel_dict= {'name': 'Israel',
              'birth': 1948, 'population_millions': 9.3,
            'capital': 'Jerusalem' ,
            'language': 'Hebrew' ,
            'cities': {'Jerusalem', 'Tel Aviv', 'Haifa' , 'Rishon LeZion', 'Petah Tikva', 'Ashdod'},
            'currency': 'ILS' ,
             'area_Kilometer': '22,145' ,
              'gdp_billion': '450' }
#a.
print('Capital city=', list(israel_dict.get('capital')))

#b.
for key in israel_dict.keys():
    print(f" All keys={key}: {israel_dict.get(key)}")

#c
print('values=', list(israel_dict.values()))

#d
for key, value in israel_dict.items():
    print(f'All value pairs in a loop: key = {key}, value = {value}')

#e
israel_dict_new=israel_dict.copy()
print('Copy to new dictionary=',israel_dict_new)

#f
print('Delete the gdp_billion from new dictionary.=',israel_dict_new.pop('gdp_billion'))

#g
print(israel_dict_new.fromkeys(israel_dict_new.keys(), None))


israel_dict_new = israel_dict_new.copy()  # the same dict
israel_dict_new['cities'] = "{osaka', 'Cantù', 'Tohoku}"
print(israel_dict_new['cities'], israel_dict['cities'])



print(str(israel_dict_new).replace("Israel", "japan").replace("1948", "700")
      .replace("9.3", '123.533') .replace("Jerusalem", 'tokio')
      .replace("Hebrew", 'Japanese') .replace("cities",  "cities")
    .replace("ILS", 'JPY').replace("22,14", '377,915').replace("450", '4,212,945'))







