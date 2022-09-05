counter = {"а":0,"б":0,"в":0,"г":0,"д":0,"е":0,"ё":0,"ж":0,"з":0,"и":0,"й":0,"к":0,"л":0,"м":0,
		   "н":0,"о":0,"п":0,"р":0,"с":0,"т":0,"у":0,"ф":0,"х":0,"ц":0,"ч":0,"ш":0,"щ":0,"ъ":0,
		   "ы":0,"ь":0,"э":0,"ю":0,"я":0,

		   "a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,
		   "o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0}
letter_count = 0

text = input("Введите текст для частотного анализа без переносов строки: ").lower()
for symbol in text:
	if symbol in counter.keys():
		counter[symbol] += 1
		letter_count += 1
for key in counter.keys():
	if counter[key]:
		print(f"{key}:", counter[key], f"{round(counter[key]/letter_count*100, 1)}%")
input()