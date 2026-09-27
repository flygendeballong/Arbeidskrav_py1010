#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Årlige totalkostnader samt årlig kostnadsdifferanse for elbil og bensinbil

Av Victoria Csisar (victoria.kc@outlook.com)

Oppdatert 2026 09 27
"""
#%% Variabler med verdier

Forsikring_elbil = 5000 # kr
Forsikring_bensinbil = 7500 # kr
Trafikkforsikringsavgift = 8.38 * 365 # kr * dager/år, begge bil-typer

Årlig_kjørelengde = 10000 # km
Elbil_forbruk = 0.2 # kWh/km
Strømpris = 2 # kr/kWh
Bensinbil_forbruk = 1 # kr/km

Drivstofforbruk_elbil = Elbil_forbruk * Strømpris * Årlig_kjørelengde
Drivstofforbruk_bensinbil = Bensinbil_forbruk * Årlig_kjørelengde

Bomavgift_elbil = 0.1 * Årlig_kjørelengde # kr/km
Bomavgift_bensinbil = 0.3 * Årlig_kjørelengde # kr/km


#%% Formler for utregning årlige totalkostnader og kostnadsdifferanse 

Totalkostnad_elbil = Forsikring_elbil + Trafikkforsikringsavgift + Drivstofforbruk_elbil + Bomavgift_elbil # Totalkostnad årlig, elbil
Totalkostnad_bensinbil = Forsikring_bensinbil + Trafikkforsikringsavgift + Drivstofforbruk_bensinbil + Bomavgift_bensinbil # Totalkostnad årlig, bensinbil
Kostnadsdifferanse = Totalkostnad_bensinbil - Totalkostnad_elbil # Kostnadsdifferanse (årlig)

#%% Utskrift - årlige totalkostnader hhv. elbil og bensinbil samt kostnadsdifferanse

print('Totalkostnad_elbil =', Totalkostnad_elbil, ' Totalkostnad_bensinbil =', Totalkostnad_bensinbil, 'og Kostnadsdifferanse =', Kostnadsdifferanse)
