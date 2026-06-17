import sympy as sp 
import customtkinter as ctk 
import matplotlib .pyplot as plt 
from matplotlib .backends .backend_tkagg import FigureCanvasTkAgg 
from matplotlib .figure import Figure 
import math 

class app (ctk .CTk ):
    def __init__ (self ):
        super ().__init__ ()

        self .title ("Límites Proyectados")
        self .geometry ("1200x720")

        ctk .set_appearance_mode ("dark")
        ctk .set_default_color_theme ("green")

        self .grid_columnconfigure (0 ,weight =1 )
        self .grid_rowconfigure (0 ,weight =1 )

        self .tabs =ctk .CTkTabview (self )
        self .tabs .grid (row =0 ,column =0 ,padx =20 ,pady =20 ,sticky ="nsew")

        self .tab_inicio =self .tabs .add ("Inicio")
        self .tab_limites =self .tabs .add ("Cálculo de Límites")

        self .crear_inicio ()
        self .crear_limite ()

    def crear_inicio (self ):
        titulo =ctk .CTkLabel (
        self .tab_inicio ,
        text ="Límites",
        font =("Arial",25 ,"bold")
        )
        titulo .pack (pady =25 )

        texto ="""Bienvenido al analizador y visualizador de límites."""

        caja =ctk .CTkTextbox (self .tab_inicio ,width =900 ,height =350 ,font =("Arial",15 ))
        caja .pack (pady =20 )
        caja .insert ("1.0",texto )
        caja .configure (state ="disabled")

    def crear_canvas (self ,frame ):
        figura =Figure (figsize =(6 ,5 ),dpi =100 )
        eje =figura .add_subplot (111 )
        canvas =FigureCanvasTkAgg (figura ,master =frame )
        canvas .get_tk_widget ().pack (fill ="both",expand =True )
        return figura ,eje ,canvas 

    def crear_limite (self ):
        contenedor =ctk .CTkFrame (self .tab_limites )
        contenedor .pack (fill ="both",expand =True ,padx =10 ,pady =10 )

        panel =ctk .CTkFrame (contenedor ,width =340 )
        panel .pack (side ="left",fill ="y",padx =10 ,pady =10 )

        grafico =ctk .CTkFrame (contenedor )
        grafico .pack (side ="right",fill ="both",expand =True ,padx =10 ,pady =10 )

        self .figura ,self .eje ,self .canvas =self .crear_canvas (grafico )

        ctk .CTkLabel (panel ,text ="Cálculo de Límite",font =("Arial",23 ,"bold")).pack (pady =15 )


        ctk .CTkLabel (panel ,text ="Función f(x):",font =("Arial",14 )).pack (pady =5 )
        self .entry_funcion =ctk .CTkEntry (panel ,width =280 ,placeholder_text ="Ej: (x**2 - 1) / (x - 1)")
        self .entry_funcion .pack (pady =5 )


        ctk .CTkLabel (panel ,text ="Valor h (tiende a):",font =("Arial",14 )).pack (pady =5 )
        self .entry_h =ctk .CTkEntry (panel ,width =280 ,placeholder_text ="Ej: 1 o oo (infinito)")
        self .entry_h .pack (pady =5 )


        self .btn_calcular =ctk .CTkButton (
        panel ,
        text ="Calcular y Graficar",
        font =("Arial",14 ,"bold"),
        command =self .procesar_calculo 
        )
        self .btn_calcular .pack (pady =20 )


        self .lbl_resultado =ctk .CTkLabel (
        panel ,
        text ="Resultado Analítico:\nEsperando acción...",
        font =("Arial",14 ,"bold"),
        text_color ="#2ECC71",
        justify ="left"
        )
        self .lbl_resultado .pack (pady =20 ,fill ="x",padx =10 )

    def procesar_calculo (self ):
        str_funcion =self .entry_funcion .get ()
        str_h =self .entry_h .get ()

        try :
            x =sp .Symbol ('x')
            str_h_clean =str_h .lower ().strip ()

            if str_h_clean in ["oo","inf","infinito"]:
                valor_h =sp .oo 
            elif str_h_clean in ["-oo","-inf","-infinito"]:
                valor_h =-sp .oo 
            else :
                valor_h =sp .sympify (str_h )

            str_funcion_limpia =str_funcion .replace ("x2","x**2").replace ("x3","x**3")
            funcion_sympy =sp .sympify (str_funcion_limpia )


            resultado_limite =sp .limit (funcion_sympy ,x ,valor_h )

            numerador ,denominador =sp .fraction (funcion_sympy )
            num_evaluado =numerador .subs (x ,valor_h )
            den_evaluado =denominador .subs (x ,valor_h )

            texto_explicativo ="---Explicacion---\n"


            if valor_h ==sp .oo or valor_h ==-sp .oo :
                texto_explicativo +=f"1. Evaluación al infinito detectada.\n"
                texto_explicativo +=f"2. Análisis analítico de grados algebraicos\n   o división por término mayor...\n"
                texto_explicativo +=f"**Resultado del Límite: {resultado_limite }**"


            elif num_evaluado ==0 and den_evaluado ==0 :
                num_factorizado =sp .factor (numerador )
                den_factorizado =sp .factor (denominador )
                funcion_simplificada =sp .simplify (num_factorizado /den_factorizado )

                texto_explicativo +=f"1. Evaluación directa: Presenta indeterminación 0/0.\n"
                texto_explicativo +=f"2. Factorización:\n   Num: {num_factorizado }\n   Den: {den_factorizado }\n"
                texto_explicativo +=f"3. Cancelando factores comunes:\n   f(x) simplificada = {funcion_simplificada }\n"
                texto_explicativo +=f"**Resultado del Límite: {resultado_limite }**"


            elif den_evaluado ==0 and num_evaluado !=0 :
                texto_explicativo +=f"1. Evaluación directa: f({valor_h }) = {num_evaluado }/0\n"
                texto_explicativo +=f"2. Se detecta una asíntota vertical.\n"
                texto_explicativo +=f"**Resultado: No existe en R (Tiende a Infinito)**"
                resultado_limite =sp .oo 


            else :
                texto_explicativo +=f"1. Evaluación directa exitosa sin indeterminación.\n"
                texto_explicativo +=f"**Resultado: {resultado_limite }**"


            self .lbl_resultado .configure (
            text =texto_explicativo ,
            text_color ="#690CD3"
            )


            self .eje .clear ()


            if valor_h ==sp .oo :
                rango_min ,rango_max =0 ,50 
            elif valor_h ==-sp .oo :
                rango_min ,rango_max =-50 ,0 
            else :
                h_float =float (valor_h )
                rango_min ,rango_max =h_float -5 ,h_float +5 

            puntos_x =[]
            puntos_y =[]


            funcion_evaluable =sp .lambdify (x ,funcion_sympy ,modules =['sympy'])
            paso =(rango_max -rango_min )/400 
            x_actual =rango_min 

            while x_actual <=rango_max :
                try :
                    y =funcion_evaluable (x_actual )
                    if isinstance (y ,(int ,float ))and not math .isnan (y )and not math .isinf (y ):
                        puntos_x .append (x_actual )
                        puntos_y .append (y )
                    else :
                        y_float =float (y )
                        puntos_x .append (x_actual )
                        puntos_y .append (y_float )
                except Exception :
                    pass 
                x_actual +=paso 


            if puntos_x :
                self .eje .plot (puntos_x ,puntos_y ,label =f"f(x) = {str_funcion }",color ="#3498DB")


            try :
                if valor_h .is_real and resultado_limite .is_real and resultado_limite .is_number :
                    self .eje .plot (float (valor_h ),float (resultado_limite ),'ro',
                    label =f"Límite ({float (valor_h ):.2f}, {float (resultado_limite ):.2f})")
            except Exception :
                pass 


            self .eje .set_title ("Comportamiento de la Función")
            self .eje .set_xlabel ("Eje X")
            self .eje .set_ylabel ("Eje Y")
            self .eje .axhline (0 ,color ='black',linewidth =0.5 )
            self .eje .axvline (0 ,color ='black',linewidth =0.5 )
            self .eje .grid (True ,linestyle ='--',alpha =0.6 )
            self .eje .legend ()


            if puntos_y :
                y_filtrados =[val for val in puntos_y if -100 <val <100 ]
                if y_filtrados :
                    self .eje .set_ylim (min (y_filtrados )-1 ,max (y_filtrados )+1 )

            self .canvas .draw ()

        except Exception as e :
            self .lbl_resultado .configure (
            text ="Error en el ingreso:\nVerifique la función o el valor de h.",
            text_color ="#C71919"
            )

if __name__ =="__main__":
    aplicacion =app ()
    aplicacion .mainloop ()