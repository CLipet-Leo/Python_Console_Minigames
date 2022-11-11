import time

"""
time.time()
    .sleep()
    .localtime()
    .mktime()
    .strftime()

%d : jours (01 à 31)
%m : mois (01 à 12)
%Y : année (ex : 2018) - %y (00 à 99)
%H : heures (00 à 23)
%I : minutes (00 à 59)
%S : secondes (00 à 59)
%p : AM/PM

%A : jours semaines / %a (jour abrégé)
%B : mois / %b (mois abrégé)

%Z : fuseau horaire (timezone)
"""

print(time.strftime("%Y-%m-%d"))