import sympy as sp 
import customtkinter as ctk 
import matplotlib .pyplot as plt 
from matplotlib .backends .backend_tkagg import FigureCanvasTkAgg 

window =ctk .CTk ()
window .title ("EID Cálculo Básico - Evaluación de Límites")
window .geometry ("1000x700")

x =sp .Symbol ('x')





frame_entrada =ctk .CTkFrame (window )
frame_entrada .pack (side =ctk .LEFT ,fill =ctk .BOTH ,padx =10 ,pady =10 )

ctk .CTkLabel (frame_entrada ,text ="Ingrese la función f(x)",font =("Arial",14 ,"bold")
).pack (pady =5 )

entrada_funcion =ctk .CTkEntry (frame_entrada ,width =300 ,)
entrada_funcion .pack (pady =5 )

ctk .CTkLabel (frame_entrada ,text ="Ingrese el valor hacia el que tiende x",font =("Arial",14 ,"bold")
).pack (pady =5 )

entrada_tendencia =ctk .CTkEntry (frame_entrada ,width =300 ,)
entrada_tendencia .pack (pady =5 )

txt_presentacion ="""
Este software permite evaluar límites matemáticos y visualizar
el comportamiento de una función cuando x tiende a un valor dado.
"""

ctk .CTkLabel (frame_entrada ,text =txt_presentacion ,wraplength =320 
).pack (pady =10 )






frame_resultados =ctk .CTkFrame (window )
frame_resultados .pack (side =ctk .RIGHT ,fill =ctk .BOTH ,expand =True ,padx =10 ,pady =10 )

label_resultado =ctk .CTkLabel (frame_resultados ,text ="Resultado:",font =("Arial",16 ,"bold"))
label_resultado .pack (pady =10 )

txt_explicacion =ctk .CTkTextbox (frame_resultados ,width =400 ,height =180 )
txt_explicacion .pack (pady =10 ,fill =ctk .BOTH ,expand =True )

frame_grafica =ctk .CTkFrame (frame_resultados )
frame_grafica .pack (fill =ctk .BOTH ,expand =True ,padx =5 ,pady =5 )





def limpiar_grafica ():
    for widget in frame_grafica .winfo_children ():
        widget .destroy ()

def calcular ():
    try :
        funcion_str =entrada_funcion .get ()
        tendencia_str =entrada_tendencia .get ()

        if funcion_str ==""or tendencia_str =="":
            label_resultado .configure (
            text ="Error: Complete todos los campos")
            return 


        funcion_expr =sp .sympify (funcion_str )

        if tendencia_str .lower ()=="inf":
            valor =sp .oo 
        elif tendencia_str .lower ()=="-inf":
            valor =-sp .oo 
        else :
            valor =float (tendencia_str )

        limite =sp .limit (funcion_expr ,x ,valor )

        label_resultado .configure (
        text =f"Resultado: {limite }")

        txt_explicacion .delete ("1.0",ctk .END )
        txt_explicacion .insert (
        "1.0",
        f"""FUNCIÓN INGRESADA

f(x) = {funcion_expr }

VALOR DE TENDENCIA

x → {tendencia_str }

LÍMITE CALCULADO

lim f(x) = {limite }
"""
        )
        graficar_funcion (funcion_expr ,tendencia_str ,limite )

    except Exception as e :
        label_resultado .configure (text ="Error en el cálculo")
        txt_explicacion .delete ("1.0",ctk .END )
        txt_explicacion .insert ("1.0",str (e ))

def graficar_funcion (funcion_expr ,tendencia_str ,limite ):
    try :
        limpiar_grafica ()

        if tendencia_str .lower ()=="inf":
            valor =10 
        elif tendencia_str .lower ()=="-inf":
            valor =-10 
        else :
            valor =float (tendencia_str )

        f_num =sp .lambdify (x ,funcion_expr ,"math")

        inicio =valor -5 
        fin =valor +5 

        cantidad_puntos =500 
        paso =(fin -inicio )/(cantidad_puntos -1 )

        x_vals =[]
        y_vals =[]

        actual =inicio 

        for _ in range (cantidad_puntos ):
            x_vals .append (actual )

            try :
                y =f_num (actual )
                if abs (y )>100 :
                    y_vals .append (float ("nan"))
                else :
                    y_vals .append (y )
            except :
                y_vals .append (float ("nan"))
            actual +=paso 

        fig ,ax =plt .subplots (figsize =(8 ,5 ))

        ax .plot (
        x_vals ,
        y_vals ,
        linewidth =2 ,
        label =f"f(x) = {funcion_expr }"
        )

        try :
            if limite .is_real and limite .is_finite :
                ax .plot (
                valor ,
                float (limite ),
                marker ="o",
                markersize =8 ,
                label =f"Límite = {limite }")
        except :
            pass 

        ax .axhline (
        y =0 ,
        linewidth =0.5 )
        ax .axvline (
        x =0 ,
        linewidth =0.5 )

        ax .grid (True )

        ax .set_title (
        f"Gráfica de {funcion_expr }")

        ax .set_xlabel ("x")
        ax .set_ylabel ("f(x)")
        ax .legend ()

        canvas =FigureCanvasTkAgg (
        fig ,
        master =frame_grafica )

        canvas .draw ()

        canvas .get_tk_widget ().pack (
        fill =ctk .BOTH ,
        expand =True )

    except Exception as e :
        txt_explicacion .insert (
        ctk .END ,
        f"\n\nError al graficar:\n{e }")





boton_calcular =ctk .CTkButton (
frame_entrada ,
text ="Calcular Límite y Graficar",
command =calcular ,
height =40 ,
font =("Arial",14 ,"bold")
)

boton_calcular .pack (pady =20 )


window .mainloop ()