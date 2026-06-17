from sympy import cancel ,expand ,factor ,simplify ,symbols ,trigsimp 
import sympy as sp 
import math 






x =symbols ("x")


def es_indeterminado (valor ):
    """Determina si un valor simbolico es una indeterminacion."""

    if valor is None :
        return True 


    if valor in [sp .nan ,sp .zoo ]:
        return True 


    if str (valor )in ["nan","zoo"]:
        return True 


    if isinstance (valor ,sp .AccumBounds ):
        return True 


    try :
        if valor .has (sp .nan )or valor .has (sp .zoo ):
            return True 
    except Exception :
        pass 

    return False 


def sustitucion_directa (expresion ,h_val ):
    """
    PASO 1: Intentar sustitucion directa x -> h.
    Retorna (resultado, exito).
    """
    try :

        resultado =expresion .subs (x ,h_val )
        resultado =sp .simplify (resultado )


        if es_indeterminado (resultado ):
            return None ,False 

        if resultado in [sp .zoo ,sp .nan ]:
            return None ,False 


        if resultado in [sp .oo ,-sp .oo ]:
            return None ,False 

        return resultado ,True 
    except Exception :
        return None ,False 


def aplicar_algebra (expresion ):
    """
    PASO 2: Aplicar transformaciones algebraicas con SymPy.
    Retorna una lista de expresiones transformadas para intentar.
    """
    transformaciones =[]



    try :
        transformaciones .append (("Factorizacion",factor (expresion )))
    except Exception :
        pass 

    try :
        transformaciones .append (("Cancelacion",cancel (expresion )))
    except Exception :
        pass 

    try :
        transformaciones .append (
        ("Expansion + Simplificacion",simplify (expand (expresion )))
        )
    except Exception :
        pass 

    try :
        transformaciones .append (("Simplif. Trigonometrica",trigsimp (expresion )))
    except Exception :
        pass 

    return transformaciones 


def evaluar_en_punto (expresion ,valor_x ):
    """Evalua la funcion en un punto y retorna un numero real."""
    try :

        resultado =sp .N (expresion .subs (x ,sp .Float (valor_x ,30 )),30 )

        if es_indeterminado (resultado ):
            return None 

        if resultado .is_real is False or resultado in [sp .oo ,-sp .oo ]:
            return None 

        valor_decimal =float (resultado )
        return valor_decimal 
    except Exception :
        return None 


def generar_aproximaciones (expresion ,h_val ,direccion ):
    """Genera valores de la funcion cada vez mas cercanos al punto h."""
    aproximaciones =[]


    if h_val in [sp .oo ,-sp .oo ]:
        signo =1 if h_val ==sp .oo else -1 
        for potencia in range (1 ,9 ):
            valor_x =signo *(10 **potencia )
            valor_y =evaluar_en_punto (expresion ,valor_x )
            if valor_y is not None :
                aproximaciones .append ((valor_x ,valor_y ))
        return aproximaciones 


    for potencia in range (1 ,9 ):
        distancia =sp .Rational (1 ,10 **potencia )
        if direccion =="-":
            valor_x =h_val -distancia 
        else :
            valor_x =h_val +distancia 

        valor_y =evaluar_en_punto (expresion ,valor_x )
        if valor_y is not None :
            aproximaciones .append ((valor_x ,valor_y ))

    return aproximaciones 


def analizar_aproximaciones (aproximaciones ):
    """Decide si una lista de aproximaciones converge o tiende a infinito."""
    if len (aproximaciones )<3 :
        return None 

    valores =[valor_y for valor_x ,valor_y in aproximaciones ]
    ultimos =valores [-4 :]

    if math .isinf (ultimos [-1 ]):
        return sp .oo if ultimos [-1 ]>0 else -sp .oo 


    mismo_signo =all (valor >0 for valor in ultimos )or all (
    valor <0 for valor in ultimos 
    )
    magnitudes_crecientes =all (
    abs (ultimos [i ])<abs (ultimos [i +1 ])
    for i in range (len (ultimos )-1 )
    )
    aumentos_magnitud =[
    abs (ultimos [i +1 ])-abs (ultimos [i ])
    for i in range (len (ultimos )-1 )
    ]
    crecimiento_no_se_frena =aumentos_magnitud [-1 ]>=0.8 *aumentos_magnitud [0 ]
    if (
    mismo_signo 
    and magnitudes_crecientes 
    and (
    abs (ultimos [-1 ])>1e6 
    or (abs (ultimos [-1 ])>10 and crecimiento_no_se_frena )
    )
    ):
        return sp .oo if ultimos [-1 ]>0 else -sp .oo 




    magnitudes_decrecientes =all (
    abs (ultimos [i ])>abs (ultimos [i +1 ])
    for i in range (len (ultimos )-1 )
    )
    if magnitudes_decrecientes and abs (ultimos [-1 ])<=abs (ultimos [0 ])/10 :
        return sp .S .Zero 


    tolerancia =0.0001 
    diferencias =[
    abs (ultimos [i +1 ]-ultimos [i ])
    for i in range (len (ultimos )-1 )
    ]
    escala =1 +abs (ultimos [-1 ])
    if all (diferencia <=tolerancia *escala for diferencia in diferencias ):
        if abs (ultimos [-1 ])<=tolerancia :
            return sp .S .Zero 
        aproximacion =sp .nsimplify (
        ultimos [-1 ],tolerance =tolerancia ,full =False ,rational =True 
        )
        if aproximacion .is_Rational and abs (float (aproximacion )-ultimos [-1 ])<=tolerancia :


            if abs (aproximacion .q )<=100 :
                return aproximacion 
        return round (ultimos [-1 ],6 )



    valores_x =[valor_x for valor_x ,valor_y in aproximaciones ]
    es_aproximacion_infinita =abs (valores_x [-1 ])>=10 **6 
    creciente =all (ultimos [i ]<ultimos [i +1 ]for i in range (len (ultimos )-1 ))
    decreciente =all (ultimos [i ]>ultimos [i +1 ]for i in range (len (ultimos )-1 ))
    if es_aproximacion_infinita and creciente and ultimos [-1 ]>10 :
        return sp .oo 
    if es_aproximacion_infinita and decreciente and ultimos [-1 ]<-10 :
        return -sp .oo 

    return None 


def limite_lateral (expresion ,h_val ,direccion ):
    """Calcula un limite lateral mediante aproximaciones generadas con ciclos."""
    aproximaciones =generar_aproximaciones (expresion ,h_val ,direccion )
    resultado =analizar_aproximaciones (aproximaciones )
    if resultado is not None :
        return resultado 



    valor_punto ,existe_valor =sustitucion_directa (expresion ,h_val )
    if existe_valor and len (aproximaciones )>=4 :
        try :
            valor_objetivo =float (valor_punto )
            distancias =[
            abs (valor_y -valor_objetivo )
            for valor_x ,valor_y in aproximaciones 
            ]
            se_acerca =all (
            distancias [i ]>distancias [i +1 ]
            for i in range (len (distancias )-1 )
            )
            if se_acerca and distancias [-1 ]<=distancias [0 ]/3 :
                return valor_punto 
        except Exception :
            pass 

    return None 


def limites_laterales_iguales (lim_izq ,lim_der ):
    """Comprueba si ambos limites laterales representan el mismo resultado."""
    if lim_izq is None or lim_der is None :
        return False 


    if lim_izq ==lim_der :
        return True 

    try :
        diferencia =sp .N (lim_izq -lim_der )
        return abs (float (diferencia ))<=0.0001 
    except Exception :
        return False 


def calcular_limite_propio (expresion ,h_val ):
    """
    Construye una explicacion del procedimiento utilizado para calcular el limite.
    Retorna (resultado_final, explicacion).
    """
    explicacion =[]
    resultado_final =None 


    explicacion .append ("Sustitución directa")
    explicacion .append ("")
    explicacion .append (f"Se reemplaza x por {h_val } en la funcion.")
    resultado ,exito =sustitucion_directa (expresion ,h_val )

    if exito :
        explicacion .append (f"El resultado obtenido es {resultado }.")
        explicacion .append ("")
        explicacion .append ("Aunque la función está definida en el punto,")
        explicacion .append ("se deben verificar ambos límites laterales.")
        resultado_final =resultado 
    else :
        explicacion .append ("La sustitución produce una indeterminación.")
        explicacion .append ("")
        explicacion .append ("Transformaciones algebraicas")
        explicacion .append ("")
        explicacion .append ("Se intenta simplificar la función para")
        explicacion .append ("eliminar la indeterminación encontrada.")
        transformaciones =aplicar_algebra (expresion )


        for nombre ,expresion_transformada in transformaciones :
            resultado ,exito =sustitucion_directa (expresion_transformada ,h_val )
            if exito :
                explicacion .append (f"Método utilizado: {nombre }.")
                explicacion .append (f"Expresión obtenida: {expresion_transformada }")
                explicacion .append (f"Resultado al reemplazar: {resultado }")
                resultado_final =resultado 
                break 

    explicacion .append ("")
    explicacion .append ("Verificación con límites laterales")
    explicacion .append ("")
    explicacion .append ("Se generan valores cada vez más cercanos")
    explicacion .append ("al punto utilizando ciclos.")
    explicacion .append ("")
    lim_izq =limite_lateral (expresion ,h_val ,"-")
    lim_der =limite_lateral (expresion ,h_val ,"+")
    explicacion .append (f"Por la izquierda: {lim_izq }")
    explicacion .append (f"Por la derecha: {lim_der }")

    if lim_izq is not None and lim_der is not None :

        if limites_laterales_iguales (lim_izq ,lim_der ):
            explicacion .append ("")
            explicacion .append ("Ambos lados entregan el mismo valor,")
            explicacion .append ("por lo tanto el límite existe.")


            resultado_final =lim_izq 
        else :
            explicacion .append ("")
            explicacion .append ("Los resultados laterales son diferentes,")
            explicacion .append ("por lo tanto el límite no existe.")
            return None ,explicacion 
    else :
        explicacion .append ("")
        explicacion .append ("La función no puede aproximarse por ambos lados,")
        explicacion .append ("por lo tanto el límite bilateral no existe.")
        return None ,explicacion 

    return resultado_final ,explicacion 
