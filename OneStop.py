# #This program lets the user calculate the information for a new insurance policy by One Stop Insurance.
# #Date Nov 17, 2023 - Nov 18 2023
# #Written by: Mitchel Joy

import datetime

#Constants
PolicyNum = 1944
BASICPREMIUM = 869.00
ADDCARDISCOUNT = 0.25
COSTEXTLIABILITY = 130.00
COSTCLASSCOVER = 86.00
LOANERCARRATE = 58.00
HSTRATE = 0.15
PROCESSFEE = 39.99

def nextpayment(OldDate):

    PayDayDay = OldDate.day
    PayDayMonth = OldDate.month
    PayDayYear = OldDate.year

    NewPayDate = datetime.datetime(PayDayYear, PayDayMonth + 1, 1)
    NewPayDate = datetime.datetime.strftime(NewPayDate, "%Y-%m-%d")

    return NewPayDate


def phonenumdisplay(PhoneNumber):
    AreaCode = PhoneNumber[0:3]
    FirstThreeDig = PhoneNumber[3:6]
    LastDig = PhoneNumber[6:10]

    FormattedPhoneNum = f"({AreaCode}){FirstThreeDig}-{LastDig}"

    return FormattedPhoneNum

def paytypes(type):
    if type == "Monthly":
        RecBottom = f"   Monthly Payment:              {MonthlyCostDisp}"
    elif type == "Downpay":
        RecBottom = f"   Downpay Amount:             {DownpayAmountDisp}"
        RecBottom = f"   Monthly Payment:              {MonthlyCostDisp}"
    elif type == "Full":
        RecBottom = f"   Payment Amount in full:                     {TotalCostDisp}"

    return RecBottom


 #Main loop.
while True: 
#     Set up the customer information.
    FirstName = input("Enter the customer's first name: ").title()
    LastName = input("Enter the customer's last name: ").title()
    Address = input("Enter the customer's address: ")
    City = input("Enter the customer's city: ").title()

    while True:
        ProvList = ["AB", "BC", "MB", "NB", "NL", "NT", "NS", "NU", "ON", "PE", "QC", "SK", "YT"]
        Province = input("Enter the customer's province (XX): ").upper()
        if Province not in ProvList:
            print("The province entered is invalid. Please re-enter.")
        else:
            print("Province successfully entered.")
            break
    PostCode = input("Enter the customer's postal code: ")
    PhoneNum = input("Enter the customer's 10 digit phone number (Dont include symbols. EX: 1234567890): ")

    while True:
        try:
            NumCars = float(input("Enter the number of cars being insured: "))
        except:
            print("Number of cars is invalid. Please re-enter.")
        else:
            break

    #Yes or No Validation.
    YayorNay = ["Y", "N"]
    while True:
        ExtLiability = input("Would the customer like extra liability? (type Y for yes N for no): ").upper()
        if ExtLiability not in YayorNay:
            print("Option for extra liability is invalid please type Y or N.")
        else:
            break

    while True:
        GlassCover = input("Would the customer like optional glass coverage? (type Y for yes N for no): ").upper()
        if GlassCover not in YayorNay:
            print("Option for glass coverage is invalid please type Y or N")
        else:
            break
        
    while True:
        LoanerCar = input("Would the customer like a loaner car? (type Y for yes N for no): ").upper()
        if LoanerCar not in YayorNay:
            print("Option for loaner car is invalid please type Y or N")
        else:
            break

    while True:
        PayList = ["Full", "Monthly", "Downpay"]
        PayType =input("Would the customer like to pay in full, monthly, or downpay? ").title()
        if PayType not in PayList:
            print("The payment type entered in invalid. Please re-enter as either full, monthly, or downpay. ")
        else:
            if PayType == "Downpay":
                try:
                    DownpayAmount = float(input("Enter the amount of the customer's downpay: "))
                except:
                    print("The entered amount is invalid. Please re-enter.")
                else:
                    break
            else:
                DownpayAmount = 0.0
                break


    #     #PREVIOUS CLAIMS> ADD THE DATE OF CLAIM AND THE COST OF THAT CLAIM TYPE ENTER TO FINISh
    PrevClaimDates = []
    PrevClaimCosts = []

    while True:
        while True:
            try:
                Date = input("Enter the date of previous insurance claim. (YYYY-MM-DD)  (If skip please leave blank)")
                DateDisp = datetime.datetime.strptime(Date, "%Y-%m-%d")
            except:
                if Date == "":
                    break
                else:
                    print("The entered date is invalid. Please re-enter.")
            else:
                break
        PrevClaimDates.append(Date)
        if Date == "":
            break
        while True:
            try:
                PrevCost = float(input("Enter the previous cost of previous claims: "))
            except:
                print("The entered previous cost is invalid. Please re-enter.")
            else: 
                if PrevCost < 0:
                    print("The entered previous value must be above $0. Please re-enter.")
                else:
                    break
        PrevClaimCosts.append(PrevCost)

        break

    print(PrevClaimDates)
    print(PrevClaimCosts)    








    NumCars = 5
    ExtLiability = "Y"
    GlassCover = "Y"
    LoanerCar = "Y"

    #Calculations
    #Cost of car and extra cars
    if NumCars > 1:
        AutoCost = BASICPREMIUM + (NumCars - 1)*(BASICPREMIUM - (BASICPREMIUM * ADDCARDISCOUNT))
    else:
        AutoCost = BASICPREMIUM

    #Extra Options
    if ExtLiability == "Y":
        ExtLiabCost = 130.00
    else:
        ExtLiability = 0.00
    FinalLiabilityCost = ExtLiabCost * NumCars

    if GlassCover == "Y":
        GlassCovCost = 86.00
    else:
        GlassCovCost = 0
    FinalGlassCost = GlassCovCost * NumCars

    if LoanerCar == "Y":
        LoanerCost = 58.00
    else:
        LoanerCost = 0.00

    TotalExtCost = FinalLiabilityCost + FinalGlassCost + LoanerCost

    InsurancePremium = AutoCost + TotalExtCost
    #Taxes
    Taxes = InsurancePremium * HSTRATE
    TotalCost = InsurancePremium + Taxes
    if PayType == "Monthly":
        MonthlyCost = (TotalCost + PROCESSFEE)/8
    elif PayType == "Downpay":
        MonthlyCost = ((TotalCost - DownpayAmount) + PROCESSFEE) /8
    else: MonthlyCost = 0.00
        
    InvoiceDate = datetime.datetime.today()
    InvoiceDateDisp = datetime.datetime.strftime(InvoiceDate, "%Y-%m-%d")

    FirstPayDate = nextpayment(InvoiceDate)
    print(FirstPayDate)



    #Reciept



    PhoneNumDisp = phonenumdisplay(PhoneNum)
    print(PhoneNumDisp)

    AutoCostDisp = f"${AutoCost:>8,.2f}"
    ExtLiabCostDisp = f"${FinalLiabilityCost:>7,.2f}"
    GlassCovCostDisp = f"${FinalGlassCost:>7,.2f}"
    LoanerCostDisp = f"${LoanerCost:>7,.2f}"
    TotalExtCostDisp = f"${TotalExtCost:>8,.2f}"
    InsurancePremiumDisp = f"${InsurancePremium:>9,.2f}"
    TaxesDisp = f"${Taxes:7,.2f}"
    TotalCostDisp = f"${TotalCost:9,.2f}"
    DownpayAmountDisp = f"${DownpayAmount:9,.2f}"
    MonthlyCostDisp = f"${MonthlyCost:7,.2f}"


    print(f"                    One Stop Insurance")
    print(f"                  Insurance Claim Reciept")
    print(f"__________________________________________________________")
    print(f"")
    print(f"Customer information:")
    print(f"")
    print(f"   First Name:                            {FirstName:>15s}")
    print(f"   Last Name                              {LastName:>15s}")
    print(f"")
    print(f"   Mailing Address: {Address:>20}s,{City:>15s}")
    print(f"                                        {Province:>s}         {PostCode:>6s}")
    print(f"")
    print(f"   Phone Number                             {PhoneNumDisp:>13s}")
    print(f"__________________________________________________________")
    print(f"")
    print(f"   Claim information:")
    print(f"")
    print(f"   Number of vehicles on claim:                       {NumCars:>3d}")
    print(f"")
    print(f"   Premiums:                                    {AutoCostDisp}")
    print(f"")
    print(f"   Extra Liability:                              {ExtLiabCostDisp}")
    print(f"   Glass coverage:                               {GlassCovCostDisp}")
    print(f"   Loaner car:                                   {LoanerCostDisp}")
    print(f"")
    print(f"   Total extra costs:                           {TotalExtCostDisp}")
    print(f"")
    print(f"   Total Insurance premiums                    {InsurancePremiumDisp}")
    print(f"   HST:                                          {TaxesDisp}")
    print(f"   Final Cost:                                 {TotalCostDisp}")
    print(f"__________________________________________________________")
    print(f"")
    print(f"   Payment Type:                                  {PayType:>7s}")

    #Payment method on reciept changes based on chosen payment method.
    print(paytypes(PayType))
    print(f"")
    print(f"__________________________________________________________")
    print(f"                  Thank you for choosing")
    print(f"                    One Stop Insurance")
    print(f"")
    print(f"")
    print(f"                     Previous Claims")
    print(f"")
    print(f"   Claim #              Claim Dates          Claim Costs")
    print(f"__________________________________________________________")
    DatesNum = 1
    ListNum = 0
    for Objects in PrevClaimDates:
        print(f"   {DatesNum:>2d}.                   {PrevClaimDates[ListNum]}           ${PrevClaimCosts[ListNum]:>9,.2f}")
        DatesNum += 1
        ListNum += 1

    NextCust = input("Would you like to enter another customer? (Y for yes N for No)")
    if NextCust not in YayorNay:
        print("Option for entering a new customer is invalid please type either Y or N")
    else:
        if NextCust == "N":
            break








    


