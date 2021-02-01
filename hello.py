import re

def wordSearcher(text):
    nameRegex= re.compile(r'\d')
    mo = nameRegex.findall(text)
    if mo: 
        return(print(mo(1)))
    else: 
        return("sorry, no nums.")

wordSearcher("Hi, here's an example. It's number 1!")


batManRegex = re.compile(r'(Bat(man|woman|girl|boy|mobile|copter|cave))')
mo = batManRegex.findall('Batman We need to get to the Batcopter. Batwoman is there.')
print(mo)
