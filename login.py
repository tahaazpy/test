import flet as ft
import sqlite3
def Login(page: ft.page):
        
        def click(e):
                if e.control.data == "no":
                        sto.value = ""
                if e.control.data == "no":
                        username.value = ""
                if e.control.data == "no":
                        password.value = ""
                page.update() 
        
        def save(e):
         
            if e.control.data == "ok":
                a= list()    
                username.value
                print(a)
                page.update()
                

        page.title = "مدریت مالی"
        page.window_height =425
        page.window_width =320
        page.window_resizable = False
        page.update()
        page.bgcolor = "#232323"
        page.theme_mode= ft.ThemeMode.DARK
        labl=ft.Text(value=" مدیریت مالی",size=25,weight=ft.FontWeight.W_600)
        page.add(labl)
        username = ft.TextField(label="نام هزینه یا درآمد", width=300,height=50,border_color="#FDA403")
        password = ft.TextField(label=" مبلغ ", width=300,height=50,border_color="#FDA403" )
        sto = ft.TextField(label=" توضیح ", width=300,height=50,border_color="#FDA403" )
        
        page.add(username,password,sto)
        
        botn_tagh = ft.ElevatedButton(
                text="ذخیره",width=125,bgcolor="#232323",height=35,color="#FDA403",data="ok",on_click=save)
        
       
        botn_na = ft.ElevatedButton(
                text="انصراف",width=120,bgcolor="#232323",height=35,color="#FDA403",data="no",on_click=click)
         
        
        
        r1 = ft.Row(controls=(botn_tagh,botn_na),
                       alignment=ft.MainAxisAlignment.CENTER)
        page.navigation_bar = ft.NavigationBar(bgcolor="#232323")
        
        
        page.add(r1)
        
        page.update()
        
        
ft.app(target=Login) 
 