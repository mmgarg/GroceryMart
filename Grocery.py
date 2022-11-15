from tkinter import *
from tkinter import ttk
import time
import datetime
import random
import tkinter.messagebox
import webbrowser

root =Tk()
root.geometry("1400x750+0+0")
root.title("Food Billing System")
root.configure(background='green')

Tops = Frame(root,bg='light green',bd=20,pady=5,relief=RIDGE)
Tops.pack(side=TOP)

lblTitle=Label(Tops,font=('New times roman',60,'bold'),text='MADAN GENERAL MART',bd=21,bg='black',
                fg='cyan',justify=CENTER)
lblTitle.grid(row=0)

name_F=Frame(root,bg='light green',bd=4,relief=RIDGE)
name_F.pack(side=TOP)

Google_F=Frame(root,bg='light green',bd=4,relief=RIDGE)
Google_F.pack(side=TOP)

MenuFrame = Frame(root,bg='light green',bd=10,relief=RIDGE)
MenuFrame.pack(side=LEFT)
Cost_F=Frame(MenuFrame,bg='light green',bd=4)
Cost_F.pack(side=BOTTOM)
items_F=Frame(MenuFrame,bg='light green',bd=4)
items_F.pack(side=TOP)


items_F=Frame(MenuFrame,bg='light green',bd=4,relief=RIDGE)
items_F.pack(side=LEFT)
items2_F=Frame(MenuFrame,bg='light green',bd=4,relief=RIDGE)
items2_F.pack(side=RIGHT)
listofitems_F=Frame(root,bg='light green',bd=4,relief=RIDGE)
listofitems_F.pack(side=TOP)

ReceiptCal_F = Frame(root,bg='light green',bd=10,relief=RIDGE)
ReceiptCal_F.pack(side=RIGHT)
Receipt_F=Frame(ReceiptCal_F,bg='light green',bd=4,relief=RIDGE)
Receipt_F.pack(side=BOTTOM)

Buttons_F=Frame(ReceiptCal_F,bg='light green',bd=3,relief=RIDGE)
Buttons_F.pack(side=BOTTOM)

Cal_F=Frame(ReceiptCal_F,bg='light green',bd=6,relief=RIDGE)
Cal_F.pack(side=TOP)



###################################################variables################################################

var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()

DateofOrder = StringVar()
Receipt_Ref = StringVar()
PaidTax = StringVar()
SubTotal = StringVar()
TotalCost = StringVar()
Costofitems = StringVar()
packaging_charge=StringVar()
delivery_charge=StringVar()

text_Input = StringVar()
operator = ""

E_wheatflour = StringVar()
E_mustardoil = StringVar()
E_rice_basmati= StringVar()
E_rice_longgrain = StringVar()
E_rice_mogra = StringVar()
E_toothpaste = StringVar()
E_desighee = StringVar()
E_moong_dal = StringVar()
E_sugar=StringVar()
E_besan = StringVar()
E_tomato_sauce = StringVar()
E_tea = StringVar()
E_coffee = StringVar()
E_sanitizer = StringVar()
E_aluminium_foil= StringVar()
E_hair_oil = StringVar()
E_soap = StringVar()

E_wheatflour.set("0")
E_mustardoil.set("0")
E_rice_basmati.set("0")
E_rice_longgrain.set("0")
E_rice_mogra.set("0")
E_toothpaste.set("0")
E_desighee.set("0")
E_moong_dal.set("0")
E_besan.set("0")
E_tomato_sauce.set("0")
E_tea.set("0")
E_coffee.set("0")
E_sanitizer.set("0")
E_aluminium_foil.set("0")
E_hair_oil.set("0")
E_soap.set("0")

DateofOrder.set(time.strftime("%d/%m/%y"))

##########################################Function Declaration####################################################

def iExit():
    iExit=tkinter.messagebox.askyesno("Exit grocery System","Confirm if you want to exit")
    if iExit > 0:
        root.destroy()
        return

def Reset():

    PaidTax.set("")
    SubTotal.set("")
    TotalCost.set("")
    Costofitems.set("")
    packaging_charge.set("")
    delivery_charge.set('')
    txtReceipt.delete("1.0",END)

    E_wheatflour.set("0")
    E_mustardoil.set("0")
    E_rice_basmati.set("0")
    E_rice_longgrain.set("0")
    E_rice_mogra.set("0")
    E_toothpaste.set("0")
    E_desighee.set("0")
    E_moong_dal.set("0")
    E_besan.set("0")
    E_tomato_sauce.set("0")
    E_tea.set("0")
    E_coffee.set("0")
    E_sanitizer.set("0")
    E_aluminium_foil.set("0")
    E_hair_oil.set("0")
    E_soap.set("0")
    E_sugar.set("0")


    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)


    txtwheatflour.configure(state=DISABLED)
    txtmustardoil.configure(state=DISABLED)
    txtrice_basmati.configure(state=DISABLED)
    txtrice_longgrain.configure(state=DISABLED)
    txtrice_mogra.configure(state=DISABLED)
    txttoothpaste.configure(state=DISABLED)
    txtdesighee.configure(state=DISABLED)
    txtmoong_dal.configure(state=DISABLED)
    txtbesan.configure(state=DISABLED)
    txttomato_sauce.configure(state=DISABLED)
    txtcoffee.configure(state=DISABLED)
    txttea.configure(state=DISABLED)
    txtsanitizer.configure(state=DISABLED)
    txtaluminium_foil.configure(state=DISABLED)
    
    txthair_oil.configure(state=DISABLED)
    txtsoap.configure(state=DISABLED)
    

def CostofItem():
    Item1=float(E_wheatflour.get())
    Item2=float(E_mustardoil.get())
    Item3=float(E_rice_basmati.get())
    Item4=float(E_rice_longgrain.get())
    Item5=float(E_rice_mogra.get())
    Item6=float(E_toothpaste.get())
    Item7=float(E_desighee.get())
    Item8=float(E_moong_dal.get())

    Item9=float(E_besan.get())
    Item10=float(E_tomato_sauce.get())
    Item11=float(E_tea.get())
    Item12=float(E_coffee.get())
    Item13=float(E_sanitizer.get())
    Item14=float(E_aluminium_foil.get())
    Item15=float(E_hair_oil.get())
    Item16=float(E_soap.get())

    Priceofitems =(Item1 * 25) + (Item2 * 95) + (Item3 * 95) + (Item4 * 60) + (Item5 * 50) + (Item6 * 75) + (Item7 * 500) + (Item8 * 89)+(Item9 *70) + (Item10 * 95) + (Item11 * 95) + (Item12 * 200) + (Item13 * 99) + (Item14 * 75) + (Item15 * 149) + (Item16 * 49)


    

    itemprice = "Rs",str('%.2f'%(Priceofitems))
    Costofitems.set(itemprice)
    costofpackaging="Rs",str(29)
    packaging_charge.set(costofpackaging)
    DC = "Rs",str('%.2f'%(49))
    delivery_charge.set(DC)
    SubTotalofITEMS = "Rs",str('%.2f'%(Priceofitems ))
    SubTotal.set(SubTotalofITEMS)

    Tax = "Rs",str('%.2f'%((Priceofitems) * 0.15))
    PaidTax.set(Tax)

    TT=((Priceofitems) * 0.15)
    TC="Rs",str('%.2f'%(Priceofitems +29 +49+ TT))
    TotalCost.set(TC)

def chk_wheatflour():
    if(var1.get() == 1):
        txtwheatflour.configure(state = NORMAL)
        txtwheatflour.focus()
        txtwheatflour.delete('0',END)
        E_wheatflour.set("")
    elif(var1.get() == 0):
        txtwheatflour.configure(state = DISABLED)
        E_wheatflour.set("0")

def chk_mustardoil():
    if(var2.get() == 1):
        txtmustardoil.configure(state = NORMAL)
        txtmustardoil.focus()
        txtmustardoil.delete('0',END)
        E_mustardoil.set("")
    elif(var2.get() == 0):
        txtmustardoil.configure(state = DISABLED)
        E_mustardoil.set("0")

def chk_rice_basmati():
    if(var3.get() == 1):
        txtrice_basmati.configure(state = NORMAL)
        txtrice_basmati.delete('0',END)
        txtrice_basmati.focus()
    elif(var3.get() == 0):
        txtrice_basmati.configure(state = DISABLED)
        E_rice_basmati.set("0")

def chk_rice_longgrain():
    if(var4.get() == 1):
        txtrice_longgrain.configure(state = NORMAL)
        txtrice_longgrain.delete('0',END)
        txtrice_longgrain.focus()
    elif(var4.get() == 0):
        txtrice_longgrain.configure(state = DISABLED)
        E_rice_longgrain.set("0")

def chk_rice_mogra():
    if(var5.get() == 1):
        txtrice_mogra.configure(state = NORMAL)
        txtrice_mogra.delete('0',END)
        txtrice_mogra.focus()
    elif(var5.get() == 0):
        txtrice_mogra.configure(state = DISABLED)
        E_rice_mogra.set("0")

def chk_toothpaste():
    if(var6.get() == 1):
        txttoothpaste.configure(state = NORMAL)
        txttoothpaste.delete('0',END)
        txttoothpaste.focus()
    elif(var6.get() == 0):
        txttoothpaste.configure(state = DISABLED)
        E_toothpaste.set("0")

def chk_desighee():
    if(var7.get() == 1):
        txtdesighee.configure(state = NORMAL)
        txtdesighee.delete('0',END)
        txtdesighee.focus()
    elif(var7.get() == 0):
        txtdesighee.configure(state = DISABLED)
        E_desighee.set("0")

def chk_moong_dal():
    if(var8.get() == 1):
        txtmoong_dal.configure(state = NORMAL)
        txtmoong_dal.delete('0',END)
        txtmoong_dal.focus()
    elif(var8.get() == 0):
        txtmoong_dal.configure(state = DISABLED)
        E_moong_dal.set("0")

def chk_besan():
    if(var9.get() == 1):
        txtbesan.configure(state = NORMAL)
        txtbesan.delete('0',END)
        txtbesan.focus()
    elif(var9.get() == 0):
        txtbesan.configure(state = DISABLED)
        E_besan.set("0")

def chk_tomato_sauce():
    if(var10.get() == 1):
        txttomato_sauce.configure(state = NORMAL)
        txttomato_sauce.delete('0',END)
        txttomato_sauce.focus()
    elif(var10.get() == 0):
        txttomato_sauce.configure(state = DISABLED)
        E_tomato_sauce.set("0")

def chk_tea():
    if(var11.get() == 1):
        txttea.configure(state = NORMAL)
        txttea.delete('0',END)
        txttea.focus()
    elif(var11.get() == 0):
        txttea.configure(state = DISABLED)
        E_tea.set("0")

def chk_coffee():
    if(var12.get() == 1):
        txtcoffee.configure(state = NORMAL)
        txtcoffee.delete('0',END)
        txtcoffee.focus()
    elif(var12.get() == 0):
        txtcoffee.configure(state = DISABLED)
        E_coffee.set("0")

def chk_sanitizer():
    if(var13.get() == 1):
        txtsanitizer.configure(state = NORMAL)
        txtsanitizer.delete('0',END)
        txtsanitizer.focus()
    elif(var13.get() == 0):
        txtsanitizer.configure(state = DISABLED)
        E_sanitizer.set("0")

def chk_aluminium_foil():
    if(var14.get() == 1):
        txtaluminium_foil.configure(state = NORMAL)
        txtaluminium_foil.delete('0',END)
        txtaluminium_foil.focus()
    elif(var14.get() == 0):
        txtaluminium_foil.configure(state = DISABLED)
        E_aluminium_foil.set("0")

def chk_hair_oil():
    if(var15.get() == 1):
        txthair_oil.configure(state = NORMAL)
        txthair_oil.delete('0',END)
        txthair_oil.focus()
    elif(var15.get() == 0):
        txthair_oil.configure(state = DISABLED)
        E_hair_oil.set("0")

def chk_soap():
    if(var16.get() == 1):
        txtsoap.configure(state = NORMAL)
        txtsoap.delete('0',END)
        txtsoap.focus()
    elif(var16.get() == 0):
        txtsoap.configure(state = DISABLED)
        E_soap.set("0")

def Receipt():
    txtReceipt.delete("1.0",END)
    x=random.randint(10908,500876)
    randomRef= str(x)
    Receipt_Ref.set("Bill"+ randomRef)

    txtReceipt.insert(END,'Receipt Ref:\t\t\t'+Receipt_Ref.get() +'\t'+ DateofOrder.get() +'\n')
    txtReceipt.insert(END,'Items\t\t\t\t'+"Cost of Items \n")
 
 
    if E_wheatflour.get()!= '0':
        
        txtReceipt.insert(END,'Wheatflour:\t\t\t\t\t' + E_wheatflour.get() +'\n')
    else:
        pass
    
    if E_mustardoil.get()!='0':
        txtReceipt.insert(END,'Mustardoil:\t\t\t\t\t'+ E_mustardoil.get()+'\n')
    else:
        pass
    
    if E_rice_basmati.get()!='0':
        txtReceipt.insert(END,'Rice_Basmati:\t\t\t\t\t'+ E_rice_basmati.get()+'\n')
    else:
        pass

    if E_rice_longgrain.get()!='0':
        txtReceipt.insert(END,'Rice_Longgrain:\t\t\t\t\t'+ E_rice_longgrain.get()+'\n')

    else:
        pass
    if E_rice_mogra.get()!='0':
        txtReceipt.insert(END,'Rice_Mogra:\t\t\t\t\t'+ E_rice_mogra.get()+'\n')

    else:
        pass

    if E_toothpaste.get()!='0':
        txtReceipt.insert(END,'Toothpaste:\t\t\t\t\t'+ E_toothpaste.get()+'\n')

    else:
        pass

    if  E_desighee.get()!='0':
        txtReceipt.insert(END,'Desighee:\t\t\t\t\t'+ E_desighee.get()+'\n')

    else:
        pass

    if E_moong_dal.get()!='0':
        txtReceipt.insert(END,'Moong_dal:\t\t\t\t\t'+ E_moong_dal.get()+'\n')
    else:
        pass

    if  E_besan.get()!='0':
        txtReceipt.insert(END,'Besan:\t\t\t\t\t'+ E_besan.get()+'\n')
    else:
        pass
    if E_tomato_sauce.get()!='0':
        txtReceipt.insert(END,'Tomato_sauce:\t\t\t\t\t'+ E_tomato_sauce.get()+'\n')
    else:
        pass
        
    if E_tea.get()!='0':
        txtReceipt.insert(END,'Tea:\t\t\t\t\t'+ E_tea.get()+'\n')
    else:
        pass
    if E_coffee.get()!='0':
        txtReceipt.insert(END,'Coffee:\t\t\t\t\t'+ E_coffee.get()+'\n')
    else:
        pass

    if E_sanitizer.get()!='0':
        txtReceipt.insert(END,'Sanitizer:\t\t\t\t\t'+ E_sanitizer.get()+'\n')
    else:
        pass
    
    if E_aluminium_foil.get()!='0':
        txtReceipt.insert(END,'Aluminium_foil:\t\t\t\t\t'+ E_aluminium_foil.get()+'\n')
    else:
        pass
    
    if E_hair_oil.get()!='0':
        txtReceipt.insert(END,'Hair_oil:\t\t\t\t\t'+ E_hair_oil.get()+'\n')
    else:
        pass
    
    if E_soap.get()!='0':
        txtReceipt.insert(END,'Soap:\t\t\t\t\t'+ E_soap.get()+'\n')
    else:
        pass
        
    txtReceipt.insert(END,'packaging_Charge:\t\t\t\t'+ packaging_charge.get()+'\n')
    txtReceipt.insert(END,'Cost of items:\t\t\t\t'+ Costofitems.get()+'\nTax Paid:\t\t\t\t'+PaidTax.get()+"\n")
    txtReceipt.insert(END,'Delivery_Charge:\t\t\t\t'+ delivery_charge.get()+'\nTotal Cost:\t\t\t\t'+str(TotalCost.get())+"\n")


#########################################items####################################################################
wheatflour=Checkbutton(items_F,text='Wheatflour',variable=var1,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='light green',command=chk_wheatflour).grid(row=0,sticky=W)
mustardoil=Checkbutton(items_F,text='Mustardoil',variable=var2,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='light green',command=chk_mustardoil).grid(row=1,sticky=W)
rice_basmati=Checkbutton(items_F,text='Rice_Basmati',variable=var3,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='light green',command=chk_rice_basmati).grid(row=2,sticky=W)
rice_longgrain=Checkbutton(items_F,text='Rice_Longgrain',variable=var4,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='light green',command=chk_rice_longgrain).grid(row=3,sticky=W)
rice_mogra=Checkbutton(items_F,text='Rice_Mogra',variable=var5,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='light green',command=chk_rice_mogra).grid(row=4,sticky=W)
toothpaste=Checkbutton(items_F,text='Toothpaste',variable=var6,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='light green',command=chk_toothpaste).grid(row=5,sticky=W)
desighee=Checkbutton(items_F,text='Desighee',variable=var7,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='light green',command=chk_desighee).grid(row=6,sticky=W)
moong_dal=Checkbutton(items_F,text='Moong_dal',variable=var8,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='light green',command=chk_moong_dal).grid(row=7,sticky=W)
besan=Checkbutton(items2_F,text="Besan ",variable=var9,onvalue = 1, offvalue=0,font=('arial',18,'bold'),
                  bg='light green',command=chk_besan).grid(row=0,sticky=W)
tomato_sauce = Checkbutton(items2_F,text="Tomato_sauce",variable=var10,onvalue = 1, offvalue=0,font=('arial',18,'bold'),
                           bg='light green',command=chk_tomato_sauce).grid(row=1,sticky=W)
tea = Checkbutton(items2_F,text="Tea ",variable=var11,onvalue = 1, offvalue=0,font=('arial',18,'bold'),
                  bg='light green',command=chk_tea).grid(row=2,sticky=W)
coffee=Checkbutton(items2_F,text='Coffee',variable=var12,onvalue=1, offvalue=0,font=('arial',18,'bold'),
                   bg='light green',command=chk_coffee).grid(row=3,sticky=W)

sanitizer = Checkbutton(items2_F,text="Sanitizer ",variable=var13,onvalue = 1, offvalue=0,font=('arial',18,'bold'),
                        bg='light green',command=chk_sanitizer).grid(row=4,sticky=W)
aluminium_foil = Checkbutton(items2_F,text="Aluminium foil",variable=var14,onvalue = 1, offvalue=0,font=('arial',18,'bold'),
                             bg='light green',command=chk_aluminium_foil).grid(row=5,sticky=W)
hair_oil = Checkbutton(items2_F,text="Hair_oil",variable=var15,onvalue = 1, offvalue=0,
                    font=('arial',18,'bold'),bg='light green',command=chk_hair_oil).grid(row=6,sticky=W)
soap= Checkbutton(items2_F,text="Soap",variable=var16,onvalue = 1, offvalue=0,
                    font=('arial',18,'bold'),bg='light green',command=chk_soap).grid(row=7,sticky=W)
##############################################items Entry###############################################################

txtwheatflour = Entry(items_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_wheatflour)
txtwheatflour.grid(row=0,column=1)

txtmustardoil = Entry(items_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_mustardoil)
txtmustardoil.grid(row=1,column=1)

txtrice_basmati= Entry(items_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_rice_basmati)
txtrice_basmati.grid(row=2,column=1)

txtrice_longgrain= Entry(items_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_rice_longgrain)
txtrice_longgrain.grid(row=3,column=1)

txtrice_mogra = Entry(items_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_rice_mogra)
txtrice_mogra.grid(row=4,column=1)

txttoothpaste = Entry(items_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_toothpaste)
txttoothpaste.grid(row=5,column=1)

txtdesighee = Entry(items_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_desighee)
txtdesighee.grid(row=6,column=1)

txtmoong_dal = Entry(items_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_moong_dal)
txtmoong_dal.grid(row=7,column=1)

txtbesan = Entry(items2_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
               ,textvariable=E_besan)
txtbesan.grid(row=0,column=1)

txttomato_sauce=Entry(items2_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_tomato_sauce)
txttomato_sauce.grid(row=1,column=1)

txttea=Entry(items2_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_tea)
txttea.grid(row=2,column=1)
txtcoffee=Entry(items2_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_coffee)
txtcoffee.grid(row=3,column=1)



txtsanitizer=Entry(items2_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_sanitizer)
txtsanitizer.grid(row=4,column=1)

txtaluminium_foil=Entry(items2_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_aluminium_foil)
txtaluminium_foil.grid(row=5,column=1)

txthair_oil=Entry(items2_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_hair_oil)
txthair_oil.grid(row=6,column=1)

txtsoap=Entry(items2_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_soap)
txtsoap.grid(row=7,column=1)
###########################################ToTal Cost################################################################################

lblpackaging_charge=Label(Cost_F,font=('arial',14,'bold'),text='Cost of packaging  ',bg='light green',
                fg='black',justify=CENTER)
lblpackaging_charge.grid(row=0,column=0,sticky=W)
txtpackaging_charge=Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'),
                        insertwidth=2,justify=RIGHT,textvariable=packaging_charge)
txtpackaging_charge.grid(row=0,column=1)

lblCostofitems=Label(Cost_F,font=('arial',14,'bold'),text='Cost of items  ',bg='light green',
                fg='black',justify=CENTER)
lblCostofitems.grid(row=1,column=0,sticky=W)
txtCostofitems=Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'),insertwidth=2,justify=RIGHT,textvariable=Costofitems)
txtCostofitems.grid(row=1,column=1)

lbldelivery_charge=Label(Cost_F,font=('arial',14,'bold'),text='Delivery Charge',bg='light green',fg='black',justify=CENTER)
lbldelivery_charge.grid(row=2,column=0,sticky=W)
txtdelivery_charge=Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'),insertwidth=2,justify=RIGHT,textvariable=delivery_charge)
txtdelivery_charge.grid(row=2,column=1)
###########################################################Payment information###################################################

lblPaidTax=Label(Cost_F,font=('arial',14,'bold'),text='\tPaid Tax',bg='light green',bd=7,
                fg='black',justify=CENTER)
lblPaidTax.grid(row=0,column=2,sticky=W)
txtPaidTax=Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'),
                        insertwidth=2,justify=RIGHT,textvariable=PaidTax)
txtPaidTax.grid(row=0,column=3)

lblSubTotal=Label(Cost_F,font=('arial',14,'bold'),text='\tSub Total',bg='light green',bd=7,
                fg='black',justify=CENTER)
lblSubTotal.grid(row=1,column=2,sticky=W)
txtSubTotal=Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'),
                        insertwidth=2,justify=RIGHT,textvariable=SubTotal)
txtSubTotal.grid(row=1,column=3)

lblTotalCost=Label(Cost_F,font=('arial',14,'bold'),text='\tTotal',bg='light green',bd=7,fg='black',justify=CENTER)
lblTotalCost.grid(row=2,column=2,sticky=W)
txtTotalCost=Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'),insertwidth=2,justify=RIGHT,textvariable=TotalCost)
txtTotalCost.grid(row=2,column=3)

#############################################RECEIPT###############################################################################
txtReceipt=Text(Receipt_F,width=46,height=12,bg='white',bd=4,font=('arial',12,'bold'))
txtReceipt.grid(row=0,column=0)


###########################################BUTTONS################################################################################
btnTotal=Button(Buttons_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='Total',
                        bg='light green',command=CostofItem).grid(row=0,column=0)
btnReceipt=Button(Buttons_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='Receipt',
                        bg='light green',command=Receipt).grid(row=0,column=1)
btnReset=Button(Buttons_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='Reset',
                        bg='light green',command=Reset).grid(row=0,column=2)
btnExit=Button(Buttons_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='Exit',
                        bg='light green',command=iExit).grid(row=0,column=3)

###################################list of items dislay################################################################################



data=[["1","Wheat Flour","Rs 25 per kg"],
      ["2","Mustard oil","Rs 95 per L"],
      ["3","Rice_Basmati","Rs 95 per kg"],
      ["4","Rice_Longrain","Rs 60 per kg"],
      ["5","Rice_Mogra","Rs 50 per kg"],
      ["6","Toothpaste","Rs 75 per one"],
      ["7","Desighee","Rs 500 per L"],
      ["8","moong_Dal","Rs 89 per kg"],
      ["9","Besan","Rs 70 per kg"],
      ["10","Tomato_Suace","Rs 95 per 1 Bottle(750 g)"],
      ["11","Tea","Rs 95 per 250g"],
      ["12","Coffee","Rs 200 per 100g"],
      ["13","Sanitizer","Rs 99 per one"],
      ["14","Aluminium_Foil","Rs 75 per one"],
      ["15","Hair_Oil","Rs 149 per one(250ml)"],
      ["16","Soap","Rs 49 per one"]]

frame=Frame(listofitems_F)
frame.pack()

tree=ttk.Treeview(frame,columns=(1,2,3),height=6,show="headings")
tree.pack(side='left')
tree.heading(1,text="Sno")
tree.heading(2,text="Item")
tree.heading(3,text="Price")

tree.column(1,width=70)
tree.column(2,width=100)
tree.column(3,width=100)

scroll=ttk.Scrollbar(frame,orient="vertical",command=tree.yview)
scroll.pack(side='right',fill='y')
tree.configure(yscrollcommand=scroll.set)

for val in data:
    tree.insert('','end',values =(val[0],val[1],val[2]))

frame1=Frame(name_F)
frame1.pack()
name=Label(frame1,font=('new times roman',12,'bold'),text='PRESENTED BY Madanmohan Garg',bg='light green',bd=7,
                fg='black',justify=LEFT)
name.grid(row=0,column=0,sticky=W)


new=1
url="https://www.google.com"
def openweb():
    webbrowser.open(url,new=new)
Btn=Button(Google_F,padx=16,pady=1,bg='cyan',fg='black',font=('new times roman',12,'bold'),width=50,text=" CLICK HERE ! TO CHECK OUR SERVED DELIVERY LOCATIONS",command=openweb)
Btn.pack()
root.mainloop()
