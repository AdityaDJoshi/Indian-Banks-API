
# IFSC Object - Create a class that has the following attributes (BANK,IFSC,MICR
# CODE, BRANCH, ADDRESS, STD CODE, CITY, DISTRICT, STATE)


class IFSC():
    def __init__(self, BANKNAME, IFsC, MICR, BRANCH, ADDRESS, STD, CITY, DISTRICT, STATE):
        self.bankName = BANKNAME
        self.ifsc = IFsC
        self.micrCode = MICR
        self.branch = BRANCH
        self.addr = ADDRESS
        self.std = STD
        self.city = CITY
        self.district = DISTRICT
        self.state = STATE
