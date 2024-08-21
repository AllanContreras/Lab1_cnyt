# Libreria CNYT Calculadora de numeros complejos

## Autor ***Allan Contreras***

Libreria creada con la finalidad de realizar operaciones de numeros complejos 

Cuenta con las funciones

- Suma
- Resta
- Producto
- División
- Modulo
- Conjugado
- Conversión entre polar y cartesiano
- Fase

## ¿Como se usa?

Se neceitan conocer los numeros complejos que se desean operar y escoger correctamente las funciones

## Datos

Manera en que se representan los numeros complejos

``` txt
2 + 1i
```

Denotación

``` txt
(Numero Real, Numero Complejo)
```

## Parametos Generales

>Se uso la Funcion Round para aproximar los valores con una presicion de 2, en este caso, los casos pruebas tuvieron que ser aproximados

```Python
round(Parametro,2)
```

## Contenido

### Resta

La funcion de resta se utiliza para resta dos numeros complejos

``` Python
def restcomplex(c1,c2):
    real = c1[0] - c2[0]
    imag = c1[1] - c2[1]
    return (real,imag)

```


### Suma

La funcion de suma se utiliza para sumar dos numeros complejos

``` Python
def sumcomplex(c1,c2):
    real = c1[0] + c2[0]
    imag = c1[1] + c2[1]
    return (real,imag)

```


### Division

La funcion de Division se utiliza para dividir dos numeros complejos

``` Python
def divcomplex(c1,c2):
    real = round(((c1[0] * c2[0]) + (c1[1] * c2[1])) / ((c2[0]**2) + (c2[1]**2)),2)
    imag = round(((c2[0] * c1[1]) - (c1[0] * c2[1])) / ((c2[0]**2) + (c2[1]**2)),2)
    return (real,imag)
```


### Multiplicación

La funcion de Multiplicación se utiliza para multiplicar dos numeros complejos

``` Python
def multcomplex(c1,c2):
    real = (c1[0] * c2[0]) - (c1[1] * c2[1])
    imag = (c1[0] * c2[1]) + (c1[1] * c2[0])
    return (real,imag)

```


### Modulo

La funcion de Modulo se utiliza para optener el modulo de un complejo

``` Python
def moducomplex(c):
    return round(math.sqrt((c[0] ** 2) + (c[1] ** 2)),2)
```

### Conjugado

La funcion de Conjugado se utiliza para optener el conjugado de un complejo

``` Python
def conjucomplex(c):
    return (c[0], -1 * c[1])
```

### Cartesiano a Polar

La funcion de Cartesiano a Polar se utiliza para obtener las cordenadas polares de un numero complejo

``` Python
def cartesian_to_polar_complex(c):
    x = c[0]
    y = c[1]
    r = round(math.sqrt(x**2 + y**2),2)
    theta = round(math.atan2(y, x))
    return (r, theta)

```

### Fase

La funcion de Fase retorna la fase de un numero complejos

``` Python
def fasecomplex(c):
    return round(math.atan2(c[1],c[0]),2)
```