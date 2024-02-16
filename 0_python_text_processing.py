text1 = "When you set out for Ithaka ask that your way be long, full of adventure, full of instruction. The Laistrygonians and the Cyclops, angry Poseidon - do not fear them: such as these you will never find as long as your thought is lofty, as long as a rare emotion touch your spirit and your body. Constantine P. Cavafy "
len(text1) # Finds length of text



text2 = text1.split(' ') #splitting into different words
text2



# Words more than 3 letters long
[w for w in text2 if len(w) > 3]



#Capitalized Words
[w for w in text2 if w.istitle()]



#words that end with s
[w for w in text2 if w.endswith('s')]




text3 = 'To be or not to be'
text4 = text3.split(' ') #splits word
text4



set(text4)
#note capitalized To and uncapitalized 2 are still there



len(set([w.lower() for w in text4])) #fixes that



# Other functions that can be used
# s.startswith(t)

# s.endswith(t)

# t in s -> finds substring

# s.isupper(); s.islower(); s.istitle -> first one capitalized, rest are small

# s.isalpha() -> all alphanumeric

# s.isdigit() -> just made of digits

# s.isalnum() -> made of alphabets or numbers

# s.lower() -> makes it lowercase

# s.upper() -> uppercase

# s.titlecase -> first later capitalized, makes it smaller

# s.split(t) -> splits sentencec based on smaller string t

# s.splitlines() -> splits sentence on newline/endofline charachter

# s.join(t) -> joins words in array or list

# s.strip() -> takes out all whitespace characters from front of string

# s.rstrip() -> takes out all whitespace characters from end of string

# s.find(t) -> finds particular substring t in s from front

# s.rfind(t) -> same as above but from back

# s.replace(u,v) every instance of u replaced by v



text5 = 'ouagadougou'
text6 = text5.split('ou')
text6



'ou'.join(text6)



list(text5)



[c for c in text5]




text8 = '     And if you find her poor, Ithaka hasn't deceived you. So wise you have become, of such experience, that already you'll have understood what these Ithakas mean.   '
text8.split(' ')



text9 = text8.rstrip()
text9 = text8.strip()
text9



text9.find('o')



text9.rfind('o')



text9.replace('o', 'O')


f = open('UNDHR.txt', 'r') #'r' symbolizes read mode
f.readline()


f.seek(0)
text12 = f.read()
len(text12)


text13 = text12.splitlines()
len(text13)

text13[0]






text10 = ' "Ethics are built right into the ideals and objectives of the United Nations" #UNSG @ NY Society for Ethical Culture bit.ly/2guVelr @UN @UN_WOMEN'



text11 = text10.split(' ')
text11

([word for word in text10.split() if word.startswith('#')])


[w for w in text11 if w.startswith('@')] #don't want just @


import re #import regex package
[w for w in text11 if re.search('@[A-Za-z0-9_]+', w)]

text10
text11 = text10.split(' ')

[w for w in text11 if re.search('@[A-Za-z0-9_]+', w)]


[w for w in text11 if re.search('@\w+', w)]


#Finding specific characters
text12 = 'ouagadougou'
re.findall(r'[aeiou]', text12)

re.findall(r'[^aeiou]', text12)


dateStr = '23-10-2002\n23/10/2002\n23/10/02\n10/23/2002\n23 Oct 2002\n23 October 2002\nOct23, 2002\nOctober23, 2002\n'

re.findall(r'\d{2}[/-]\d{2}[/-]\d{4}', dateStr)



re.findall(r'\d{2}[/-]\d{2}[/-]\d{2,4}', dateStr)
re.findall(r'\d{1,2}[/-]\d{1,2}[/-]\d{2,4}', dateStr)
re.findall(r'\d{2} (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) \d{4}', dateStr)

re.findall(r'\d{2} (?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) \d{4}', dateStr)


re.findall(r'\d{2} (?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* \d{4}', dateStr)

re.findall(r'(?:\d{2} )?(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* (?:\d{2}, )?\d{4}', dateStr)






