"""
NFC CRACK - Python (3.11.2)

    @author  : Baku-Stark
    @version : 0.0.1
"""

import nfc # pip install -U nfcpy

with nfc.ContactlessFrontend('udp') as udp:
    print(udp)
    udp.close()

# Open a local device
clf = nfc.ContactlessFrontend(path='usb:001:005')
def open_local_device():
    try:
        # lsusb
        
        # print(clf.open('usb:001:005'))
        # print(clf.open('usb:148f:5370'))
        # print(clf.open('usb:001'))
        # print(clf.open('usb:148f'))
        # print(clf.open('usb'))
        
        print(clf)

    except AssertionError as e:
        print(e)

    else:
        clf.close()

open_local_device()