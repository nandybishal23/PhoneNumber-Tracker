import phonenumbers

from phonenumbers import geocoder
from tkinter import*
from tkinter.ttk import*
from tkinter.messagebox import*
from phonenumbers import carrier

Canvas=Tk()
Canvas.title('Phone Number Tracker')

def tracker():
    ch_nmber = phonenumbers.parse(e1.get(),"CH")
    q=Label(Canvas,text=(geocoder.description_for_number(ch_nmber,"en")),font="poppins 20")
    q.grid(row=2,column=2)
    service_nmber=phonenumbers.parse(e1.get(),"RO")
    p=Label(Canvas,text=(carrier.name_for_number(service_nmber,"en")),font="poppins 20")
    p.grid(row=3,column=2)
    

label0=Label(Canvas,text="Phone Number Tracker",font="time 40",borderwidth=5, relief="ridge",foreground="gold",background="black")
label0.grid(row=0,column=1,columnspan=3,pady=5)

label1=Label(Canvas,text="Enter Link :",font="poppins 20")
label1.grid(row=1,column=1)
e1=Entry(Canvas,width=20,font="poppins 20",background="gray")
e1.grid(row=1,column=2)

q1=Label(Canvas,text="Country : ",font="poppins 20")
q1.grid(row=2,column=1)
p1=Label(Canvas,text="Service Provider :",font="poppins 20")
p1.grid(row=3,column=1)

btn=Button(Canvas,text="Track",command=tracker,width=20)
btn.grid(row=1,column=3,padx=5)
Canvas.mainloop()