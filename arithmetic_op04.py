#"Raqam" deb nomlangan o'zgaruvchi yarating va unga uch xonali raqamni belgilang.
raqam = 123
#"Raqam"ning birinchi raqamini toping va x1 ga belgilang.
x1 = (raqam % 100)
#"Raqam"ning ikkinchi raqamini toping va x2 ga belgilang.
x2 = (raqam % 10)
#"Raqam"ning uchinchi raqamini toping va x3 ga belgilang.
x3 = (raqam % 1)
#"Javob" deb nomlangan o'zgaruvchi yarating va unga x1, x2, x3 uchta raqam yig'indisini belgilang.
javob = x1 + x2 + x3
#Javobning qiymatini chop eting.
print (javob)