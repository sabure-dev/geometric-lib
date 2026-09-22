# Геометрические формулы

## Общее описание решения
 Набор Python функций для вычисления площади и периметра фигур: круга, прямоугольника, квадрата и треугольника. Каждая фигура реализована в виде отдельных функций, принимающих определенные параметры фигуры. Тесты находятся в директории tests и вызываются следующим образом:  
```
uv run python -m unittest discover -s tests -v
```

## Описание функций с примерами вызова

### Круг

        - area(r)
        - Описание: Вычисляет площадь круга по формуле S = pi r^2.
        - Параметры: r (float) - радиус.
        - Пример вызова:
        import circle
        res = circle.area(5.0) # 78.53981633974483

        - perimeter(r)
        - Описание: Вычисляет длину окружности по формуле P = 2pi *r.
        - Параметры: r (float) — радиус.
        - Пример вызова:
        import circle
        res = circle.perimeter(5.0) # 31.41592653589793

### Прямоугольник

        - area(a, b)
        - Описание: Вычисляет площадь прямоугольника по формуле S = a * b.
        - Параметры: a (float) — первая сторона, b (float) — вторая сторона.
        - Пример вызова:
        import rectangle
        res = rectangle.area(4.0, 5.0) # 20.0

        - perimeter(a, b)
        - Описание: Вычисляет периметр прямоугольника по формуле P = 2 * (a + b).
        - Параметры: a (float) — первая сторона, b (float) — вторая сторона.
        - Пример вызова:
        import rectangle
        res = rectangle.perimeter(4.0, 5.0) # 18.0

### Квадрат

        - area(a)
        - Описание: Вычисляет площадь квадрата по формуле S = a^2.
        - Параметры: a (float) — сторона квадрата.
        - Пример вызова:
        import square
        res = square.area(4.0) # 16.0

        - perimeter(a)
        - Описание: Вычисляет периметр квадрата по формуле P = 4 * a.
        - Параметры: a (float) — сторона квадрата.
        - Пример вызова:
        import square
        res = square.perimeter(4.0) # 16.0

### Треугольник

        - area(a, h)
        - Описание: Вычисляет площадь треугольника по формуле S = a * h / 2.
        - Параметры: a (float) — сторона треугольника, h (float) — высота треугольника.
        - Пример вызова:
        import triangle
        res = triangle.area(4.0, 3.0) # 6.0

        - perimeter(a, b, c)
        - Описание: Вычисляет периметр треугольника по формуле P = a + b + c.
        - Параметры: a (float) — первая сторона, b (float) — вторая сторона, c (float) — третья сторона.
        - Пример вызова:
        import triangle
        res = triangle.perimeter(3.0, 4.0, 5.0) # 12.0

## История изменения проекта

| Commit hash | Название |
|---|---|
| `22d6d9a` | docs: add docstrings and project documentation |
| `73dd93e` | fix: fixed rectangle.py perimeter |
| `cab505b` | feat: add rectangle.py |
| `86edb1c` | L-05: Update Docs. Add user agreement info |
| `438b89a` | L-05: Add user agreement |
| `6adb962` | L-03: Docs added |
| `3049431` | L-04: Add rectangle.py |
| `b5b0fae` | L-04: Update docs for calculate.py |
| `d76db2a` | L-04: Add calculate.py |
| `51c40eb` | L-04: Doc updated for triangle |
| `d080c78` | L-04: Triangle added |
| `d078c8d` | L-03: Docs added |
| `8ba9aeb` | L-03: Circle and square added |