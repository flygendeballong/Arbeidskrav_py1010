#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Årlige totalkostnader samt årlig kostnadsdifferanse for elbil og bensinbil

Av Victoria Csisar (victoria.kc@outlook.com)

Oppdatert 2026 09 20
"""
#%% Variabler med verdier

F_e = 5000 # Forsikring elbil
F_b = 7500 # Forsikring bensinbil
T= 8.38*365 # Trafikkforsikringsavgift (begge typer)
D_e = 0.2*2*10000 # Drivstofforbruk elbil
D_b = 1*10000 # Drivstofforbruk bensinbil
B_e = 0.1*10000 # Bomavgift elbil
B_b = 0.3*10000 # Bomavgift bensinbil

#%% Formler for utregning årlige totalkostnader og kostnadsdifferanse 

Tk_e = F_e + T + D_e + B_e # Totalkostnad årlig, elbil
Tk_b = F_b + T + D_b + B_b # Totalkostnad årlig, bensinbil
Kd = Tk_b - Tk_e # Kostnadsdifferanse (årlig)

#%% Utskrift - årlige totalkostnader hhv. elbil og bensinbil samt kostnadsdifferanse

print('Tk_e =', Tk_e, ' Tk_b =', Tk_b, 'og Kd =', Kd)


