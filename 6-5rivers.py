#6-5 Rivers

#Declare dictionary
rivers = {
  'Krishna':'India',
  'Iriri':'Brazil',
  'Narmada':'India',
  'Ottawa':'Canada',
  'Zeya':'Russia',
  'Juruena':'Brazil',
  'Grande':'Brazil',
  'Yamuna':'India',
  'Sutlej':'India',
  'Indus':'India',
  'Indus':'Pakistan',
  'Sutlej':'Pakistan',
  'Vyatka':'Russia',
  'Fraser':'Canada',
  'Churchill':'Canada',
  'Khatanga':'Russia',
  'Pechora':'Russia',
  'Kama':'Russia',
  'Don':'Russia',
  }

#key in for loop is the river and the value extracted with the iterated key
for key in rivers:
    print(f"The river {key} runs through {rivers[key]}.")
print("\nRivers:")

#using set() to get unique river entries (keys are "rivers")
for river in set(rivers):
    print("\t-" + river.title())

#using set() to get unique countries (values are "countries")
print("\nCountries:")
for country in set(rivers.values()):
    print("\t-" + country.title())
