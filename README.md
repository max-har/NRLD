# NRLD

[The uploaded CSV file _CWC\_National-Register-of-Large-Dams\_2019.csv_ is a manually revised version of the file produced by the script (the problems of the script are described below). If you find data errors in the file, please contact me via email (mail@max-har.de).]

__Data__
URL: http://cwc.gov.in/sites/default/files/nrld06042019.pdf

Contact:
	Government of India
	Central Water Commission
	Central Dam Safety Organization
	National Register of Large Dams
	June 2019
	Dam Safety Monitoring Directorate
	4th Floor (S), Sewa R. K. Puram New Delhi – 110066

_I do not own the data used in this repository. If you are the owner of the data and want this repository to be removed, please contact me via email (mail@max-har.de)._

__Method__
[Python 3.8]
1. The file _extract-csv.py_ uses the Python library _Camelot_ to extract PDF tables (URL: https://camelot-py.readthedocs.io/en/master/) from the _National Register of Large Dams_ (June 2019) in the form of CSV files. It creates a raw CSV file for each Indian state in the folder _camelot/raw_.
2. The file _clean-csv.py_ uses the Python library _Pandas_ to manipulate (misplaced) data and to correct data errors with the help of data frames. It creates a single CSV file (optional: a CSV file for each Indian state; uncomment line 24 in _clean-csv.py_) in the folder _camelot/clean_.

__Problems__
- _Camelot_ cannot extract PDF tables with a single row. This leads to missing data in the case of Haryana (HR), Mizoram (MZ), Nagaland (NL), Tripura (TR), and (the last page of) Chhattisgarh (CG)
- The programme cannot automatically extract "Nearest City" from "River". This leads to data errors in 71 cases (see "PIC"s in _List 1_).
- The programme cannot automatically extract "River Basin" from "River". This leads to data errors in five cases (see "PIC"s in _List 2_).
- The programme cannot automatically extract misplaced data from "Effective Storage Capacity". This leads to data errors in two cases (see "PIC"s in _List 3_).
- The programme cannot automatically extract misplaced data from "Dam Length". This leads to data errors in two cases (see "PIC"s in _List 4_).
- The programme cannot automatically extract misplaced data from "Purpose". This leads to data errors in one case (see "PIC"s in _List 5_).
- The programme cannot deal with a typo in "PIC" _BR02HH0025_ (misspelled as _BR02HH025_).

[It is best to look at the lists below in the source code of this file.]

__Abbreviation__ (used in column "Purpose")
I	Irrigation
H	Hydropower
S	Water Supply
F	Fish Production
C	Flood Control
O	Other Benefits
T	Tourism
N	Navigation
TE	Earth
ER	Rock Fill
PG	Gravity / Masonry

__Units__
m	Height above lowest foundation-meters
m	Length of dam-meters
m3	Volume content of dam-Cubic-meter
m3	Gross Storage capacity-Cubic-meter
m2	Reservoir Area	Square meter
m3	Effective Storage capacity-Cubic-meter
m3/s	Designed Spillway capacity-Cumecs

__Index__
AN	57	Andaman and Nicobar Island
AP	58-64	Andhra Pradesh
AR	65	Arunanchal Pradesh
AS	66	Assam
BR	67	Bihar
--	68	Chandigarh [no large dams]
CG	69-76	Chhattisgarh
--	77	Dadara and Nagar Havelli [no large dams]
--	78	Daman and Diu [no large dams]
GA	79	Goa
GJ	80-102	Gujarat
HR	103	Haryana
HP	104	Himachal Pradesh
JK	105	Jammu and Kashmir
JH	106-108	Jharkhand
KA	109-120	Karnataka
KL	121-123	Kerala
--	124	Lakshadweep [no large dams]
MP	125-149	Madhya Pradesh
MH	150-242	Maharashtra
MN	243	Manipur
ML	244	Meghalaya
MZ	245	Mizoram
NL	246	Nagaland
--	247	Delhi [no large dams]
OR	248-256	Odisha
--	257	Puducherry [no large dams]
PB	258	Punjab
RA	259-264	Rajasthan
SK	265	Sikkim
TN	266-273	Tamil Nadu
TR	274	Tripura
UP	275-278	Uttar Pradesh
UA	279	Uttarakhand
WB	280	West Bengal
TL	281-286	Telangana

__List 1__
UP13MH0046
UP13MH0040
UP13LH0025
MP08MH0242
OR10MH0182
AS30HH0005
SK30HH0002
ML22HH0002
ML22HH0008
RA11LH0044
UP13MH0073
KA06MH0081
KL07MH0020
MP08LH0446
MP08HH0597
UA30HH0020
TL47LH0122
TL47LH0140
TL47LH0150
TL47LH0128
TL47MH0075
TL47LH0156
TL47LH0083
TL47LH0152
TL47LH0091
TL47LH0139
TL47LH0123
TL47LH0110
TL47LH0114
TL47MH0144
UP13MH0123
CG03MH0128
UP13MH0017
MH09MH1488
UP13LH0044
TN12HH0070
MP08MH0115
MP08MH0062
MP08MH0444
MP08LH0708
MP08MH0152
TL47MH0026
GJ04MH0269
BR02MH0007
JH05MH0025
KA06MH0033
KA06LH0002
MH09MH1886
GJ04HH0138
GJ04MH0545
WB14MH0024
GJ04MH0107
AP01MH0148
ML22HH0006
WB14LH0004
TN12MH0105
PB26MH0016
MP08MH0399
TN12HH0036
MH09MH1230
MH09MH0729
MP08MH0461
JH05MH0010
JH05HH0016
TN12HH0100
ML22HH0005
TN12MH0102
MH09LH2056
MH09MH2036
KA06MH0150
GA18MH0003

__List 2__
AS30HH0005
MP08MH0399
ML22HH0002
ML22HH0008
SK30HH0002


__List 3__
MP39HH0676
MP08HH0326

__List 4__
KA06HH0107
KL29VH0027

__List 5__
TN12HH0014
