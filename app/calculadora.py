"""
Módulo de operaciones matemáticas básicas para la aplicación de calculadora.
"""
# app/calculadora.py
def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return a / b
