#a front vowel (e, é, i, í, ö, ő, ü, ű) the suffix is -nek
#a back vowel (a, á, o, ó, u, ú) the suffix is -nak

# -*- coding: utf-8 -*-
def dative(word):
    front_vowel = ['e', 'é', 'i', 'í', 'ö', 'ő', 'ü', 'ű']
    back_vowel = ['a', 'á', 'o', 'ó', 'u', 'ú']
    for x in word[::-1]:
        if x in front_vowel:
            return word+'nek'
        elif x in back_vowel:
            return word+'nak'
def dat(word):
    for c in word[::-1]:
        if c in 'eéiíöőüű':
            return word+'nek'
        elif c in 'aáoóuú':
            return word+'nak'

print(dat('ablak'))

print(dative('ablak'))
print(dative('tükör'))
print(dative('keret'))
print(dative('otthon'))
print(dative('virág'))
print(dative('tett'))
print(dative('rokkant'))
print(dative('rossz'))

#[u"ablak", u"ablaknak"],
#[u"tükör", u"tükörnek"],
#[u"keret", u"keretnek"],
#[u"otthon", u"otthonnak"],
#[u"virág", u"virágnak"],
#[u"tett", u"tettnek"],
#[u"rokkant", u"rokkantnak"],
#u"rossz", u"rossznak"],