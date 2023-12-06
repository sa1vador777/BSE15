#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def func_show(func):
    def wrapper(*args, **kwargs): 
        return f"Площадь треугольника: {func(*args, **kwargs)}"
    return wrapper


@func_show
def get_sq(width: float, height: float) -> float:
    return width*height


if __name__ == "__main__":
    width = float(input("Введите ширину прямоугольника: "))
    height = float(input("Введите высоту прямоугольника: "))
    print(get_sq(width, height))
