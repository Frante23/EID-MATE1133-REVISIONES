import customtkinter as ctk 
import matplotlib .figure as plt 
from matplotlib .backends .backend_tkagg import FigureCanvasTkAgg 
import sympy as sp 

cEID =ctk .CTk ()
cEID .geometry ("1280x720")
cEID .title ("Programa Cálculo EID")
ctk .set_appearance_mode ("dark")
ctk .set_default_color_theme ("blue")
cEID .grid_columnconfigure (0 ,weight =1 )
cEID .grid_rowconfigure (0 ,weight =1 )

x =sp .Symbol ('x')

cEID .grid_columnconfigure (0 ,weight =1 )
cEID .grid_columnconfigure (1 ,weight =4 )
cEID .grid_rowconfigure (0 ,weight =1 )

frame_izquierdo =ctk .CTkFrame (cEID ,fg_color ="transparent")
frame_izquierdo .grid (row =0 ,column =0 ,sticky ="nsew",padx =10 ,pady =10 )

frame_derecho =ctk .CTkFrame (cEID ,fg_color ="#1a1a1a")
frame_derecho .grid (row =0 ,column =1 ,sticky ="nsew",padx =10 ,pady =10 )

titulo =ctk .CTkLabel (master =frame_izquierdo ,text ="Calculadora EID",font =("ARIAL",24 ,"bold"),text_color ="#D92B4F")
titulo .pack (pady =20 ,padx =20 ,anchor ="nw")
ingfunc =ctk .CTkLabel (master =frame_izquierdo ,text ="Ingrese la función:",font =("ARIAL",16 ),text_color ="#C2294C")
ingfunc .pack (pady =10 ,padx =20 ,anchor ="nw")
cajatexto =ctk .CTkTextbox (frame_izquierdo ,width =400 ,height =50 )
cajatexto .pack (pady =10 ,padx =47 ,anchor ="nw")
ingtend =ctk .CTkLabel (master =frame_izquierdo ,text ="Ingrese la tendencia:",font =("ARIAL",16 ),text_color ="#C2294C")
ingtend .pack (pady =10 ,padx =20 ,anchor ="nw")
cajatextoten =ctk .CTkTextbox (frame_izquierdo ,width =400 ,height =50 )
cajatextoten .pack (pady =10 ,padx =47 ,anchor ="nw")
atajos =ctk .CTkLabel (master =frame_izquierdo ,text ="Atajos y opciones:",font =("ARIAL",16 ),text_color ="#C2294C")
atajos .pack (pady =10 ,padx =20 ,anchor ="nw")
frame_botones =ctk .CTkFrame (frame_izquierdo ,fg_color ="transparent")
frame_botones .pack (pady =10 ,padx =20 ,anchor ="nw")
resultados =ctk .CTkLabel (master =frame_izquierdo ,text ="Resultados:",font =("ARIAL",16 ),text_color ="#C2294C")
resultados .pack (pady =10 ,padx =20 ,anchor ="nw")
label_resultado =ctk .CTkLabel (frame_izquierdo ,text ="Resultado del cálculo:",font =("ARIAL",16 ),text_color ="#CAC4C5",fg_color ="#2B2B2B",corner_radius =8 ,width =400 ,height =50 )
label_resultado .pack (pady =10 ,padx =45 ,anchor ="nw")

fig =plt .Figure (figsize =(5 ,4 ),dpi =100 )
ax =fig .add_subplot (111 )
fig .patch .set_facecolor ('#1a1a1a')
ax .set_facecolor ('#121212')
ax .tick_params (colors ='white')
ax .grid (True ,color ='#444444')

canvas =FigureCanvasTkAgg (fig ,master =frame_derecho )
canvas .draw ()
canvas .get_tk_widget ().pack (fill ="both",expand =True ,padx =5 ,pady =5 )

def calcular_limite_algoritmo (funcion_sympy ,punto_c ):
    tolerancia =0.05 
    limite_izq =None 
    h =0.1 
    for _ in range (5 ):
        punto_eval =punto_c -h 
        limite_izq =float (funcion_sympy .subs (x ,punto_eval ).evalf ())
        h /=10 

    limite_der =None 
    h =0.1 
    for _ in range (5 ):
        punto_eval =punto_c +h 
        limite_der =float (funcion_sympy .subs (x ,punto_eval ).evalf ())
        h /=10 

    if abs (limite_izq -limite_der )<tolerancia :
        return round ((limite_izq +limite_der )/2 ,4 )
    else :
        return "No existe (Límites distintos)"

def Calcular ():
    texto_func =cajatexto .get ("0.0","end-1c").strip ()
    texto_tend =cajatextoten .get ("0.0","end-1c").strip ()

    if not texto_func or not texto_tend :
        label_resultado .configure (text ="Error: Rellene campos.")
        return 

    try :
        func_parseada =texto_func .replace ('^','**')
        funcion_sympy =sp .sympify (func_parseada )
        punto_c =float (texto_tend )

        resultado =calcular_limite_algoritmo (funcion_sympy ,punto_c )
        label_resultado .configure (text =f"lim = {resultado }")
    except Exception as e :
        label_resultado .configure (text ="Error en los datos.")

    ax .clear ()
    ax .grid (True ,color ='#444444')

    texto_func =cajatexto .get ("0.0","end-1c").strip ()
    texto_tend =cajatextoten .get ("0.0","end-1c").strip ()

    if not texto_func :
        return 

    try :
        func_parseada =texto_func .replace ('^','**')
        funcion_sympy =sp .sympify (func_parseada )
        punto_c =float (texto_tend )if texto_tend else 0.0 

        x_valores =[]
        y_valores =[]

        if punto_c ==9999.0 or punto_c ==-9999.0 :
            inicio_x =-10.0 
            fin_x =10.0 
        else :
            inicio_x =punto_c -5 
            fin_x =punto_c +5 

        paso =0.05 
        actual_x =inicio_x 
        while actual_x <=fin_x :
            try :
                if abs (actual_x )<0.01 and texto_func =="1/x":
                    actual_x +=paso 
                    continue 

                res_y =funcion_sympy .subs (x ,actual_x ).evalf ()
                if res_y .is_real :
                    x_valores .append (actual_x )
                    y_valores .append (float (res_y ))
            except :
                pass 
            actual_x +=paso 

        ax .plot (x_valores ,y_valores ,color ="#D92B4F",linewidth =2 ,label =f"f(x)={texto_func }")

        ax .set_xlim (inicio_x ,fin_x )
        ax .set_ylim (-10 ,10 )
        ax .axhline (0 ,color ='white',linewidth =1.2 ,linestyle ='--')
        ax .axvline (0 ,color ='white',linewidth =1.2 ,linestyle ='--')

        texto_res =label_resultado .cget ("text")
        if "lim ="in texto_res and "No existe"not in texto_res :
            if punto_c !=9999.0 and punto_c !=-9999.0 :
                valor_lim =float (texto_res .split ("=")[1 ])
                ax .plot (punto_c ,valor_lim ,'go',markersize =8 ,label =f"Límite ({punto_c }, {valor_lim })")

        ax .legend (facecolor ='#1a1a1a',labelcolor ='white')
        canvas .draw ()

    except Exception as e :
        label_resultado .configure (text ="Error al graficar.")

def Limpiar ():
    cajatexto .delete ("0.0",ctk .END )
    cajatextoten .delete ("0.0",ctk .END )
    label_resultado .configure (text ="Resultado del cálculo:")
    ax .clear ()
    ax .grid (True ,color ='#444444')
    canvas .draw ()

def InfinitoNegativo ():
    cajatextoten .delete ("0.0",ctk .END )
    cajatextoten .insert (ctk .END ,"-9999")

def InfinitoPositivo ():
    cajatextoten .delete ("0.0",ctk .END )
    cajatextoten .insert (ctk .END ,"9999")

def Sin ():
    cajatexto .insert (ctk .END ,"sin(x)")

def Cos ():
    cajatexto .insert (ctk .END ,"cos(x)")

def Tg ():
    cajatexto .insert (ctk .END ,"tan(x)")

def Raiz ():
    cajatexto .insert (ctk .END ,"sqrt(x)")

boton_calcular =ctk .CTkButton (master =frame_botones ,text ="Calcular",command =Calcular ,width =100 ,fg_color ="#D92B4F",hover_color ="#C2294C")
boton_calcular .grid (row =0 ,column =0 ,padx =5 ,pady =5 )
boton_limpiar =ctk .CTkButton (master =frame_botones ,text ="Limpiar",command =Limpiar ,width =100 ,fg_color ="#D92B4F",hover_color ="#C2294C")
boton_limpiar .grid (row =0 ,column =2 ,padx =5 ,pady =5 )

boton_infinito_negativo =ctk .CTkButton (master =frame_botones ,text ="-oo",command =InfinitoNegativo ,fg_color ="#D92B4F",hover_color ="#C2294C")
boton_infinito_negativo .grid (row =1 ,column =0 ,padx =5 ,pady =5 )
boton_infinito_positivo =ctk .CTkButton (master =frame_botones ,text ="+oo",command =InfinitoPositivo ,fg_color ="#D92B4F",hover_color ="#C2294C")
boton_infinito_positivo .grid (row =1 ,column =2 ,padx =5 ,pady =5 )

boton_sin =ctk .CTkButton (master =frame_botones ,text ="sen(x)",command =Sin ,fg_color ="#D92B4F",hover_color ="#C2294C")
boton_sin .grid (row =2 ,column =0 ,padx =5 ,pady =5 )
boton_cos =ctk .CTkButton (master =frame_botones ,text ="cos(x)",command =Cos ,fg_color ="#D92B4F",hover_color ="#C2294C")
boton_cos .grid (row =2 ,column =1 ,padx =5 ,pady =5 )
boton_tg =ctk .CTkButton (master =frame_botones ,text ="tan(x)",command =Tg ,fg_color ="#D92B4F",hover_color ="#C2294C")
boton_tg .grid (row =2 ,column =2 ,padx =5 ,pady =5 )

boton_raiz =ctk .CTkButton (master =frame_botones ,text ="√x",command =Raiz ,fg_color ="#D92B4F",hover_color ="#C2294C")
boton_raiz .grid (row =1 ,column =1 ,pady =5 ,padx =5 )

cEID .mainloop ()