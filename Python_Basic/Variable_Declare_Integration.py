__author__ = 'k22li'

# 1) make sure the variable which has been defined in the Branches are truely declared, otherwise the in the following
# steps where those variables calling there might be "undefined" exception pops-up...

if self.check('Let\'s get set up. What\'s your language?'):
    textsExist=self.read.texts()
    for item in textsExist:
        if item!='English' and item in self.langDict.keys():
            targetLang=item
            break
    else:
        targetLang = ''
else:
    targetLang = ''