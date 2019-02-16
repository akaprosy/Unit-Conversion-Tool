#Unit conversion tool. by Alex Kaprosy
class UnitConverter:
    def __init__(self, units_from, units_to, factor):
       self.units_from = units_from
       self.units_to = units_to
       self.factor = factor

    def description(self):
       return 'Convert ' + self.units_from + ' to ' + self.units_to

    def convert(self, value):
       return float(value) * float(self.factor)


#menu

print('Quick Conversion:')
my_unit = input('''Choose a conversion tool: 
    (A) - lbs. to Newtons
    (B) - Newtons to lbs.
    (C) - lb-ft to Newton meters
    (D) - Newton meters to lb-ft
    (E) - inches to millimeters
    (F) - millimeters to inches
    (G) - square inches to square millimeters
    (H) - square millimeters to square inches
    (I) - psi to Megapascals
    (J) - Megapascals to psi
    (K) - psi to kilopascals
    (L) - kilopascals to psi
    (M) - psi to bar
    (N) - bar to psi
    (O) - cubic inches to cubic centimeters
    (P) - cubic centimeters to cubic inches
    (Q) - gpm to lpm
    (R) - lpm to gpm
    (S) - feet per second to meters per second
    (T) - meters per second to feet per second
    (U) - horsepower to watts
    (V) - watts to horsepower
    (W) - horsepower to kilowatts
    (X) - kilowatts to horsepower
    ''')



if my_unit == 'A' or my_unit == 'a':
      lbs_to_newtons = UnitConverter('lbs.', 'Newtons',4.4482)
      print(lbs_to_newtons.description())
      lbs1 = input('Enter unit to be converted: ')
      print(str(lbs_to_newtons.convert(lbs1)) + lbs_to_newtons.units_to)
    
elif my_unit == 'B' or my_unit == 'b':
    newtons_to_lbs = UnitConverter('Newtons', 'lbs.',0.2248)
    print(newtons_to_lbs.description())
    newtons1 = input('Enter unit to be converted: ')
    print(str(newtons_to_lbs.convert(newtons1)) + newtons_to_lbs.units_to)
              
elif my_unit == 'C' or my_unit == 'c':
    lbsft_to_Newton_meters = UnitConverter('lbs-ft', 'Nm',1.3558)
    print(lbsft_to_Newton_meters.description())
    lbsft1 = input('Enter unit to be converted: ')
    print(str(lbsft_to_Newton_meters.convert(lbsft1)) + lbsft_to_Newton_meters.units_to)
              
elif my_unit == 'D' or my_unit == 'd':
    newton_meters_to_lbsft = UnitConverter('Nm', 'lbs-ft',0.7375)
    print(newton_meters_to_lbsft.description())
    nm1 = input('Enter unit to be converted: ')
    print(str(newton_meters_to_lbsft.convert(nm1)) + newton_meters_to_lbsft.units_to)
              
elif my_unit == 'E' or my_unit == 'e':
    in_to_mm = UnitConverter('inches', 'mm',25.4)
    print(in_to_mm.description())
    inches1 = input('Enter unit to be converted: ')
    print(str(in_to_mm.convert(inches1)) + in_to_mm.units_to)

elif my_unit == 'F' or my_unit == 'e':
    mm_to_in = UnitConverter('mm', 'inches', 0.0393)     
    print(mm_to_in.description())
    mm1 = input('Enter unit to be converted: ')
    print(str(mm_to_in.convert(mm1)) + mm_to_in.units_to)
            
elif my_unit == 'G' or my_unit == 'g':
    inches_squared_to_mm_squared = UnitConverter('square inches', 'square millimeters',645.16)
    print(inches_squared_to_mm_squared.description())
    inches2 = input('Enter unit to be converted: ')
    print(str(inches_squared_to_mm_squared.convert(inches2)) + inches_squared_to_mm_squared.units_to)
             
elif my_unit == 'H' or my_unit == 'h':
    mm_squared_to_inches_squared = UnitConverter('square millimeters', 'square inches',0.0016)
    print(mm_squared_to_inches_squared.description())
    mm2 = input('Enter unit to be converted: ')
    print(str(mm_squared_to_inches_squared.convert(mm2)) + mm_squared_to_inches_squared.units_to)
              
elif my_unit == 'I' or my_unit == 'i':
    psi_to_megapascal = UnitConverter('psi', 'Megapascal',0.0068)
    print(psi_to_megapascal.description())
    psi1 = input('Enter unit to be converted: ')
    print(str(psi_to_megapascal.convert(psi1)) + psi_to_megapascal.units_to)
    
elif my_unit == 'J' or my_unit == 'j':
    mega_pascal_to_psi = UnitConverter('Megapascal', 'psi', 145.0377)
    print(mega_pascal_to_psi.description())
    megapascal = input('Enter unit to be converted: ')
    print(str(mega_pascal_to_psi.convert(megapascal)) + mega_pascal_to_psi.units_to)
             
elif my_unit == 'K' or my_unit == 'k':
    psi_to_kilopascal = UnitConverter('psi', 'kilopascal',6.8947)
    print(psi_to_kilopascal.description())
    psi2 = input('Enter unit to be converted: ')
    print(str(psi_to_kilopascal.convert(psi2)) + psi_to_kilopascal.units_to)
             
elif my_unit == 'L' or my_unit == 'l':
    kilopascal_to_psi = UnitConverter('kilopascal', 'psi',0.145)
    print(kilopascal_to_psi.description())
    kilopascal = input('Enter unit to be converted: ')
    print(str(kilopascal_to_psi.convert(kilopascal)) + kilopascal_to_psi.units_to)
            
elif my_unit == 'M' or my_unit == 'm':
    psi_to_bar = UnitConverter('psi', 'bar',0.0689)
    print(psi_to_bar.description())
    psi3 = input('Enter unit to be converted: ')
    print(str(psi_to_bar.convert(psi3)) + psi_to_bar.units_to)
            
elif my_unit == 'N' or my_unit == 'n':
    bar_to_psi = UnitConverter('bar', 'psi',14.5037)
    print(bar_to_psi.description())
    bar = input('Enter unit to be converted: ')
    print(str(bar_to_psi.convert(bar)) + bar_to_psi.units_to)
              
elif my_unit == 'O' or my_unit == 'o':
    inches_cubed_to_cm_cubed = UnitConverter('cubic inches', 'cubic centimeters',16.387)
    print(inches_cubed_to_cm_cubed.description())
    inches3 = input('Enter unit to be converted: ')
    print(str(inches_cubed_to_cm_cubed.convert(inches3)) + inches_cubed_to_cm_cubed.units_to)
             
elif my_unit == 'P' or my_unit == 'p':
    cm_cubed_to_inches_cubed = UnitConverter('cubic centimeters', 'cubic inches', 0.061)
    print(cm_cubed_to_inches_cubed.description())
    cm3 = input('Enter unit to be converted: ')
    print(str(cm_cubed_to_inches_cubed.convert(cm3)) + cm_cubed_to_inches_cubed.units_to)
             
elif my_unit == 'Q' or my_unit == 'q':
    gpm_to_lpm = UnitConverter('gpm', 'lbm',3.7854)
    print(gpm_to_lpm.description())
    gpm1 = input('Enter unit to be converted: ')
    print(str(gpm_to_lpm.convert(gpm1)) + gpm_to_lpm.units_to)
              
elif my_unit == 'R' or my_unit == 'r':
    lpm_to_gpm = UnitConverter('lpm', 'gpm',0.2641)
    print(lpm_to_gpm.description())
    lpm1 = input('Enter unit to be converted: ')
    print(str(lpm_to_gpm.convert(lpm1)) + lpm_to_gpm.units_to)
              
elif my_unit == 'S' or my_unit == 's':
    fts_to_ms = UnitConverter('feet per second', 'meters per second',0.3048)
    print(fts_to_ms.description())
    fts1 = input('Enter unit to be converted: ')
    print(str(fts_to_ms.convert(fts1)) + fts_to_ms.units_to)
              
elif my_unitr == 'T' or my_unit == 't':
    ms_to_fts = UnitConverter('meters per second', 'feet per second',3.28080)
    print(ms_to_fts.description())
    ms1 = input('Enter unit to be converted: ')
    print(str(ms_to_fts.convert(ms1)) + ms_to_fts.units_to)
             
elif my_unit == 'U' or my_unit == 'u':
    hp_to_watts = UnitConverter('hp', 'watts',745.69)
    print(hp_to_watts.description())
    hp1 = input('Enter unit to be converted: ')
    print(str(hp_to_watts.convert(hp1)) + hp_to_watts.units_to)
             
elif my_unit == 'V' or my_unit == 'v':
    watts_to_hp = UnitConverter('watts', 'hp',0.0013)
    print(watts_to_hp.description())
    watts = input('Enter unit to be converted: ')
    print(str(watts_to_hp.convert(watts)) + watts_to_hp.units_to)
             
elif my_unit == 'W' or my_unit == 'w':
    hp_kw = UnitConverter('hp', 'kw',0.7457)
    print(hp_kw.description())
    hp2 = input('Enter unit to be converted: ')
    print(str(hp_kw.convert(hp2)) + hp_kw.units_to)
             
else:
    kw_hp = UnitConverter('kw', 'hp',1.341)
    print(kw_hp.description())
    kw2 = input('Enter unit to be converted: ')
    print(str(kw_hp.convert(kw2)) + kw_hp.units_to)

input()
