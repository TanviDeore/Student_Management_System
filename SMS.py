from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
import numpy as np
import matplotlib.pyplot as plt
from playsound import playsound
import re


root=Tk()
root.title("Student Management System")
root.geometry("700x700+500+50")

root.resizable(False,False)
regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
#Quote of the Day

import bs4
import requests

res=requests.get("https://www.brainyquote.com/quotes_of_the_day.html")
soup=bs4.BeautifulSoup(res.text,'lxml')
quote=soup.find('img',{"class":"p-qotd"})

text=quote['alt']


#Tempreture 

import socket
import requests
try:
	cities=['mumbai']
	for city in cities:
		socket.create_connection(("www.google.com",80))
		add1="http://api.openweathermap.org/data/2.5/weather?units=metric"
		add2="&q="+city
		add3="&appid=c6e315d09197cec231495138183954bd"
		api_address=add1+add2+add3
		result1=requests.get(api_address)
		data=result1.json()
		main=data['main']
		temp=main['temp']
		lblTemp1=Label(root,text="Temperature : "+str(temp)+chr(176)+"C",font=("Times New Roman",18,"bold"))
		lblTemp1.place(height=40,width=260,x=200,y=590)
except OSError:
	messagebox.showerror("error","Check network!")

def addst():
	root.withdraw()
	addst.deiconify()
gname=[]
gmarks=[]
def f1():
	import cx_Oracle
	con=None
	cursor=None
	try:
		con=cx_Oracle.connect('system/abc123')
		try:
			r=entRno.get()
			rno=int(r)
		except ValueError:
			messagebox.showerror("error","Enter Integers Only! Check Roll no")
			entRno.delete(0,END)
			entRno.focus()
		name=entName.get()
		
		try:
			marks=int(entMarks.get())
		except ValueError:
			messagebox.showerror("error","Enter Integers Only! Check Marks")
			entMarks.delete(0,END)
			entMarks.focus()
		if rno<0:
			messagebox.showerror("error","Negative Roll numbers not allowed")
			entRno.delete(0,END)
			entRno.focus()
		elif len(name)<2:
			if name.isdigit()==True:
				messagebox.showerror("Error","Enter charachters only for name!")
				entName.delete(0,END)
				entName.focus()
			else:
				messagebox.showerror("Error","name should have atleast two charachters!")
				entName.delete(0,END)
				entName.focus()
		elif name.isdigit()==True:
			messagebox.showerror("Error","Enter characters only for name!")
			entName.delete(0,END)
			entName.focus()
		elif marks > 100 or marks< 0:
			messagebox.showerror("Error","Marks should be less than 100 or greater than 0")
			entMarks.delete(0,END)
			entMarks.focus()
		elif (name.isalnum()==True)  and (name.isdigit()==True):
			messagebox.showerror("error","Enter charachters only for name!")
			entName.delete(0,END)
			entName.focus()
		elif  (regex.search(name) != None):
			messagebox.showerror("error","No special allowed!")
			entName.delete(0,END)
			entName.focus()
		else:
			cursor=con.cursor()
			sql="insert into student values('%d','%s','%d')"
			args=(rno,name,marks)
			cursor.execute(sql % args)
			con.commit()
			msg=str(cursor.rowcount)+" record inserted"
			messagebox.showinfo("status",msg)
			clapp="clapp.mp3"
			playsound(clapp)
			entRno.delete(0,END)
			entName.delete(0,END)
			entMarks.delete(0,END)
			entRno.focus()
	except UnboundLocalError as ule:
		pass
	except cx_Oracle.DatabaseError as e:
		messagebox.showerror("Error","Check Roll number again! \n user already exists")
		entRno.delete(0,END)
		entRno.focus()
		con.rollback()
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()
def viewSt():
	root.withdraw()
	viewSt.deiconify()
	import cx_Oracle
	con=None
	cursor=None
	try:
		con=cx_Oracle.connect("system/abc123")
		cursor=con.cursor()
		stData.delete('1.0',END)
		sql="select rno,name,marks from student"
		cursor.execute(sql)
		data=cursor.fetchall()
		msg=""
		for d in data:
			msg=msg+"Roll No: "+str(d[0])+"	"+"Name: "+d[1]+"	"+"Marks: "+str(d[2])+"\n"
		stData.insert(INSERT,msg)
	except cx_Oracle.DatabaseError as e:
		message.showerror("Error",e)
		con.rollback()
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()

def delete():
	import cx_Oracle
	con=None
	cursor=None
	try:
		con=cx_Oracle.connect('system/abc123')
		cursor=con.cursor()
		r=entDRno.get()
		rno=int(r)	
		sql="select count(*) from student where rno='%d'"
		args =(rno)
		cursor.execute(sql % args)
		data=cursor.fetchone()
		print(data[0])
		if (data[0] == 0):
			raise AttributeError
		else:
			try:
				sql="DELETE FROM student WHERE rno='%d'"
				args=(rno)
				cursor.execute(sql % args)
				con.commit()
				m=str(cursor.rowcount)+" record deleted"
				messagebox.showinfo("status",m)
				entDRno.delete(0,END)
				entDRno.focus()
			except ValueError:
				messagebox.showerror("Error","Enter Integers Only! Check Roll no")
				entDRno.delete(0,END)
				entDRno.focus()
	except AttributeError as ae:
		messagebox.showerror("Error","Record doesn't exist")
		entDRno.delete(0,END)
		entDRno.focus()	
	except cx_Oracle.DatabaseError as e:
		messagebox.showerror("Error",e)
		con.rollback()
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()

def update():
	import cx_Oracle
	con=None
	cursor=None
	try:
		con=cx_Oracle.connect('system/abc123')
		r=entURno.get()
		rno=int(r)
		cursor=con.cursor()	
		sql="select count(*) from student where rno='%d'"
		args = (rno)
		cursor.execute(sql % args)
		data = cursor.fetchone()
		if (data[0]==0):
			raise AttributeError
		else:	
			name=entUName.get()
			try:
				marks=int(entUMarks.get())
			except ValueError:
				messagebox.showerror("error","Enter Integers Only! Check Marks")
				entUMarks.delete(0,END)
				entUMarks.focus()
		if rno<0:
			messagebox.showerror("error","Negative Roll numbers not allowed")
			entURno.delete(0,END)
			entURno.focus()
		elif len(name)<2:
			if name.isdigit()==True:
				messagebox.showerror("Error","Enter charachters only for name!")
				entUName.delete(0,END)
				entUName.focus()
			else:
				messagebox.showerror("Error","name should have atleast two charachters!")
				entUName.delete(0,END)
				entUName.focus()
		elif name.isdigit()==True:
			messagebox.showerror("Error","Enter characters only for name!")
			entUName.delete(0,END)
			entUName.focus()
		elif marks > 100 or marks< 0:
			messagebox.showerror("Error","Marks should be less than 100 or greater than 0")
			entUMarks.delete(0,END)
			entUMarks.focus()
		elif (name.isalnum()==True)  and (name.isdigit()==True):
			messagebox.showerror("error","Enter charachters only for name!")
			entUName.delete(0,END)
			entUName.focus()
		elif (regex.search(name) != None):
			messagebox.showerror("error","No special allowed!")
			entUName.delete(0,END)
			entUName.focus()
		else:	
			cursor=con.cursor()
			sql="update student set name='%s',marks='%d' where rno='%d' "  
			args=(name,marks,rno)
			cursor.execute(sql % args)
			con.commit()
			msg=str(cursor.rowcount) + " record updated"
			messagebox.showinfo("status",msg)
			clapp="clapp.mp3"
			playsound(clapp)
			entURno.delete(0,END)
			entUName.delete(0,END)
			entUMarks.delete(0,END)
	except ValueError as ve:
		messagebox.showerror("Error","Only integers allowed")
		entURno.delete(0,END)
		entURno.focus()
	except AttributeError as ae:
		messagebox.showerror("error","Record doesn't exist")
		entURno.delete(0,END)
		entURno.focus()
	except UnboundLocalError as ule:
		pass 
	except cx_Oracle.DatabaseError as e:
		messagebox.showerror("error",e)
		entURno.delete(0,END)
		entURno.focus()
		con.rollback()
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()

def back_r():
	addst.withdraw()
	root.deiconify()

def UpdateSt():
	root.withdraw()
	UpdateSt.deiconify()

def deleteSt():
	root.withdraw()
	deleteSt.deiconify()


def bargraph():
	import cx_Oracle
	con=None
	cursor=None
	try:
		con=cx_Oracle.connect("system/abc123")
		cursor=con.cursor()
		sql="select name,marks from student"
		cursor.execute(sql)
		data=cursor.fetchall()
		Names=[]
		Marks=[]
		for d in data:
			Names.append(d[0])
			Marks.append(d[1])
		plt.bar(Names,Marks,width=0.5)
		plt.xlabel("Names")
		plt.ylabel("Marks")
		plt.title("Student's Performance")
		plt.show()
	except cx_Oracle.DatabaseError as e:
		con.rollback()
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()	




	
btnAdd=Button(root,text="Add",font=("Times New Roman",15,"bold"),width=15,height=2,command=addst)
btnView=Button(root,text="View",font=("Times New Roman",15,"bold"),width=15,height=2,command=viewSt)
btnUpdate=Button(root,text="Update",font=("Times New Roman",15,"bold"),width=15,height=2,command=UpdateSt)
btnDelete=Button(root,text="Delete",font=("Times New Roman",15,"bold"),width=15,height=2,command=deleteSt)
btnGraph=Button(root,text="Graph",font=("Times New Roman",15,"bold"),width=15,height=2,command=bargraph)

lblQotd=Label(root,text="QOTD : ",font=("Times New Roman",15,"bold"))
lblQotd1=Label(root,text=" "+text,font=("Times New Roman",12,"bold"))
#lblTemp=Label(root,text="Temp",font=("Times New Roman",15,"bold"),width=15,height=2)



btnAdd.pack(pady=10)
btnView.pack(pady=10)
btnUpdate.pack(pady=10)
btnDelete.pack(pady=10)
btnGraph.pack(pady=20)
lblQotd.place(x=25, y=500)
lblQotd1.place(height=50,width=600,x=100,y=490)
#entQotd.place(height=40,width=260,x=200,y=500)
#lblTemp.place(height=50, x=40, y=590)







addst=Toplevel(root)
addst.title("Add Student")
addst.geometry("500x700+500+50")
addst.resizable(False,False)
addst.withdraw()

lblRno=Label(addst,text="Enter Rno",font=("arial",15,"bold"),width=15,height=2)
lblName=Label(addst,text="Enter Name",font=("arial",15,"bold"),width=15,height=2)
lblMarks=Label(addst,text="Enter Marks",font=("arial",15,"bold"),width=15,height=2)
entRno=Entry(addst,bd=5,font=("arial",18,"bold"))
entName=Entry(addst,bd=5,font=("arial",18,"bold"))
entMarks=Entry(addst,bd=5,font=("arial",18,"bold"))
btnSave=Button(addst,text="Save",font=("arial",15,"bold"),command=f1)
btnBack=Button(addst,text="Back",font=("arial",15,"bold"),width=15,height=2,command=back_r)


lblRno.place(height=20,width=150,x=200,y=50)
entRno.place(height=50,width=250,x=150,y=100)
#entRno.pack(pady=10)
lblName.place(height=20,width=150,x=200,y=200)
entName.place(height=50,width=250,x=150,y=250)
lblMarks.place(height=20,width=150,x=200,y=350)
entMarks.place(height=50,width=250,x=150,y=400)
btnSave.place(height=50,width=100,x=200,y=500)
btnBack.place(height=50,width=100,x=200,y=600)


UpdateSt=Toplevel(root)
UpdateSt.title("Update Student")
UpdateSt.geometry("500x700+500+50")
UpdateSt.resizable(False,False)
UpdateSt.withdraw()
messagebox.showinfo("Hello Sir/Madam!","Welcome to Student Management System")

lblRno=Label(UpdateSt,text="Enter Rno",font=("arial",15,"bold"),width=15,height=2)
lblName=Label(UpdateSt,text="Enter Name",font=("arial",15,"bold"),width=15,height=2)
lblMarks=Label(UpdateSt,text="Enter Marks",font=("arial",15,"bold"),width=15,height=2)
entURno=Entry(UpdateSt,bd=5,width=100,font=("arial",15,"bold"))
entUName=Entry(UpdateSt,bd=5,width=100,font=("arial",15,"bold"))
entUMarks=Entry(UpdateSt,bd=5,width=100,font=("arial",15,"bold"))
btnSave=Button(UpdateSt,text="Save",font=("arial",15,"bold"),width=15,height=2,command=update)
btnBack=Button(UpdateSt,text="Back",font=("arial",15,"bold"),width=15,height=2,command=back_r)


lblRno.place(height=20,width=150,x=200,y=50)
entURno.place(height=50,width=250,x=150,y=100)
lblName.place(height=20,width=150,x=200,y=200)
entUName.place(height=50,width=250,x=150,y=250)
lblMarks.place(height=20,width=150,x=200,y=350)
entUMarks.place(height=50,width=250,x=150,y=400)
btnSave.place(height=50,width=100,x=200,y=500)
btnBack.place(height=50,width=100,x=200,y=600)



deleteSt=Toplevel(root)
deleteSt.title("Delete Student")
deleteSt.geometry("500x700+500+50")
deleteSt.resizable(False,False)
deleteSt.withdraw()

lblRno=Label(deleteSt,text="Enter Rno",font=("arial",15,"bold"),width=15,height=2)
entDRno=Entry(deleteSt,bd=5,width=100,font=("arial",15,"bold"))
btnSave=Button(deleteSt,text="Save",font=("arial",15,"bold"),width=15,height=2,command=delete)
btnBack=Button(deleteSt,text="Back",font=("arial",15,"bold"),width=15,height=2,command=back_r)

lblRno.place(height=20,width=150,x=200,y=150)
entDRno.place(height=50,width=250,x=150,y=200)
btnSave.place(height=50,width=100,x=200,y=300)
btnBack.place(height=50,width=100,x=200,y=400)


viewSt=Toplevel(root)
viewSt.title("View Student")
viewSt.geometry("500x700+500+50")
viewSt.resizable(False,False)
viewSt.withdraw()

stData=scrolledtext.ScrolledText(viewSt,height=25,width=40,font=("Times New Roman",15,"bold"))
btnBack=Button(viewSt,text="Back",font=("arial",15,"bold"),width=15,height=2,command=back_r)

stData.pack(pady=30)
btnBack.place(height=50,width=100,x=200,y=620)





root.mainloop()
