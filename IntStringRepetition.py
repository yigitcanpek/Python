# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 14:35:35 2021

@author: deat_
"""
"1"
sentence = "YigiTcanpeKguzel,gmail.com  "
stripsentence =sentence.strip()
lowersentence = stripsentence.lower()
print(lowersentence.islower(),lowersentence)
finalsentence=lowersentence.replace(",","@")
print(sentence,finalsentence)

"2"
overridesentence="Python"
newoverridesentence=overridesentence.lower()
print("@".join([newoverridesentence,"gmail.com"]))

uppercasesentence ="PYTHON"
print(uppercasesentence[0:2])
print(uppercasesentence)
jfunc="@".join([uppercasesentence,"gmail.com"]).lower()
print(jfunc)
print(jfunc.isnumeric())

jfunc=jfunc.split("@")
print(jfunc)
sentencendstart="python was sweet"
print(sentencendstart.startswith("p"))
print(sentencendstart.endswith("r"))


print(sum([2,5,6]))
print(max(2,5,6),min(2, 5, 6))
print(round(4.6),round(4.3))
print(abs(-6),abs(6))