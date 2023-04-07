import numpy as np


def Amtab(rholog,th):
  if th>1.95:
    th=1.95
  if rholog>-0.5:
    if th>1:
      th=1
    Amlog=(-2.04*th - 0.656)*rholog -1.768
  elif rholog>-2.5:
    z1=[ 0.26429362,  2.308469,    7.81413499, 12.39250353, \
  7.90442493, -0.52179895,-1.52831614]
    pAm1=np.poly1d(z1)
    uplim=pAm1(rholog)
    if rholog>-1.05:
      Amlog=(0.945454545454545*th - 1.70909090909091)*rholog +1.49272727272727*th - 2.29454545454545
      if th >0.8:
        th1=th-0.8
        Amlog=(1.12727272727273*th1 - 0.952727272727273)*rholog+\
        1.58363636363636*th1 - 1.10036363636364

    else:
      if th <=0.8:
        Amlog=(0.121 - 0.227*th)/(0.338 - 0.11*th)*rholog+\
        0.5*th + 1.05*(0.121 - 0.227*th)/(0.338 - 0.11*th) - 0.5
        if 6.6090909090909165*rholog+8.55241818181819<Amlog:
          th1=th
          Amlog=(0.537*th1 - 0.702)/(0.587 - 0.421*th1)*rholog+\
          0.727*th1 - 0.621 - (0.11*th1 - 1.388)*(0.537*th1 - 0.702)/(0.587 - 0.421*th1)
      else:
        th1=th-0.8
        Amlog=(0.0756*th1 - 0.0606)/(0.25 - 0.0566*th1)*rholog+\
        0.4*th1 - 0.1 + 1.05*(0.0756*th1 - 0.0606)/(0.25 - 0.0566*th1)
        if 6.6090909090909165*rholog+8.55241818181819<Amlog:
          Amlog=(0.2864*th1 - 0.2724)/(0.2502 - 0.0496*th1)*rholog+\
        0.3244*th1 - 0.0394 - (0.0566*th1 - 1.3)*(0.2864*th1 - 0.2724)/(0.2502 - 0.0496*th1)

    if Amlog>uplim:
      Amlog=uplim
  else:
    z=[1.34528857e-01, 3.15915033e+00, 3.06754303e+01, 1.57055386e+02,\
 4.45961390e+02, 6.64211300e+02, 4.04541785e+02]
    pAm=np.poly1d(z)
    Amlog=pAm(rholog)
  return Amlog

def etaOtab(rholog):
  if rholog>-2.217:
    etaOlog=-0.10996372*rholog**2+  0.49186494*rholog+ 16.82894602
  else:
    etaOlog=-0.82772958*rholog**4  -11.48813613*rholog**3  -58.24798054*rholog**2 -124.86627111*rholog  -80.52351483
  return etaOlog
