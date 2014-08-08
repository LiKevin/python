__author__ = 'k22li'


#######################################################################################################################
# function implementations
# purpose is to:
#   implement a method with which to define the calculations of encrypting a strings                                 #
#######################################################################################################################
NONENCRYPTED_STRING = '''
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''

def string_encrypting(str_a):

        return "".join([ encrypting_codes(char) for char in str_a ])

def encrypting_codes(chr_a):

    char_dict = {}
    for first_char in (65, 97):
        for char_index  in range(26):
            char_dict[chr(first_char+char_index)] = chr((char_index+13)%26+first_char)

    return char_dict.get(chr_a, chr_a) # while the first param stands for the "key" to look for; and the 2nd param \
    # stands for the default values in case the "key" isn't available, Never an index error to raise


if __name__ == '__main__':

    print string_encrypting(NONENCRYPTED_STRING)

    ###################################################################################################################
    # Output:
    #Gur Mra bs Clguba, ol Gvz Crgref
    #
    #Ornhgvshy vf orggre guna htyl.
    #Rkcyvpvg vf orggre guna vzcyvpvg.
    #Fvzcyr vf orggre guna pbzcyrk.
    #Pbzcyrk vf orggre guna pbzcyvpngrq.
    #Syng vf orggre guna arfgrq.
    #Fcnefr vf orggre guna qrafr.
    #Ernqnovyvgl pbhagf.
    #Fcrpvny pnfrf nera'g fcrpvny rabhtu gb oernx gur ehyrf.
    #Nygubhtu cenpgvpnyvgl orngf chevgl.
    #Reebef fubhyq arire cnff fvyragyl.
    #Hayrff rkcyvpvgyl fvyraprq.
    #Va gur snpr bs nzovthvgl, ershfr gur grzcgngvba gb thrff.
    #Gurer fubhyq or bar-- naq cersrenoyl bayl bar --boivbhf jnl gb qb vg.
    #Nygubhtu gung jnl znl abg or boivbhf ng svefg hayrff lbh'er Qhgpu.
    #Abj vf orggre guna arire.
    #Nygubhtu arire vf bsgra orggre guna *evtug* abj.
    #Vs gur vzcyrzragngvba vf uneq gb rkcynva, vg'f n onq vqrn.
    #Vs gur vzcyrzragngvba vf rnfl gb rkcynva, vg znl or n tbbq vqrn.
    #Anzrfcnprf ner bar ubaxvat terng vqrn -- yrg'f qb zber bs gubfr!
    ###################################################################################################################