# 📐 Math Límites — Analizador y Visualizador de Límites

> Proyecto EID — MATE1133 | Universidad Católica de Temuco

---

## 📋 Descripción

**Math Límites** es una aplicación desarrollada en Python que permite calcular y visualizar límites matemáticos de forma interactiva. La aplicación muestra el proceso de resolución paso a paso, integrando la teoría del cálculo de límites con una interfaz gráfica.

---

## ✨ Funcionalidades

- **Sustitución directa** — Evaluación inmediata de f(h)
- **Factorización** — Detección automática de diferencia de cuadrados y trinomios
- **Multiplicación por conjugado** — Para límites con raíces cuadradas
- **Límites al infinito** — Análisis dividiendo por la potencia mayor
- **Límites trigonométricos** — Identidades de sen(x)/x, (1-cos(x))/x y tan(x)/x
- **Límites laterales** — Verificación por la derecha e izquierda usando ε
- **Visualización gráfica** — Gráfica de la función con punto límite marcado
- **Paso a paso detallado** — Muestra cada operación matemática realizada

---

## 🛠️ Tecnologías utilizadas

| Librería | Uso |
|---|---|
| `CustomTkinter` | Interfaz gráfica de usuario |
| `SymPy` | Cálculo simbólico y manipulación algebraica |
| `Matplotlib` | Visualización y graficación de funciones |

> ⚠️ **Nota:** No se utiliza NumPy ni Math en este proyecto .

---

## 📁 Estructura del Proyecto

```
EID_MATE1133/
│
├── mathlimites.py           # Interfaz gráfica y lógica de la aplicación
├── calculador_limites.py    # Motor de cálculo de límites
└── README.md                # Este archivo
```

---

## ▶️ Instalación y Ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu_usuario/EID_MATE1133.git
cd EID_MATE1133
```

### 2. Instalar dependencias

```bash
pip install customtkinter sympy matplotlib
```

### 3. Ejecutar la aplicación

```bash
python mathlimites.py
```

---

## 📖 Modo de Uso

1. Ingresar la función matemática en el campo **lim(x)**
2. Ingresar el valor **h** hacia el cual tiende el límite
3. Presionar el botón **Calcular**
4. Ver el resultado y el paso a paso en el panel derecho
5. Ver la gráfica de la función en el panel izquierdo

### Ejemplos de funciones válidas

| Función | h | Tipo |
|---|---|---|
| `(x**2 - 1)/(x - 1)` | `1` | Factorización |
| `(sqrt(x+1) - 1)/x` | `0` | Conjugado |
| `(3*x**2 + 2*x)/(x**2 - 1)` | `oo` | Límite al infinito |
| `sin(x)/x` | `0` | Trigonométrico |
| `(1 - cos(x))/x` | `0` | Trigonométrico |
| `tan(x)/x` | `0` | Trigonométrico |

> Para infinito usar `oo`, para menos infinito usar `-oo`

---

## 👥 Integrantes

| Nombre | 
|---|
| Gabriel Rivas |
| Franco González |

---

## 🏫 Información Académica

- **Curso:** MATE1133
- **Evaluación:** Evaluación Integrada de Desempeño (EID)
- **Universidad:** Universidad Católica de Temuco
- **Carrera:** Ingeniería Civil Informática
