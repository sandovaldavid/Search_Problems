# Problema 02

## Rompecabezas de las jarras de agua

El **rompecabezas de las jarras de agua** es un problema clásico de lógica que implica medir una cantidad exacta de agua usando jarras de diferentes capacidades. A pesar de que las jarras no tienen marcas intermedias, puedes llenar, vaciar o transferir agua entre ellas para alcanzar la cantidad objetivo.

### Planteamiento del problema

Supongamos que tienes dos jarras:

- **Jarra A** con capacidad de `m` litros.
- **Jarra B** con capacidad de `n` litros.

Tu objetivo es medir exactamente `d` litros de agua, donde:

- `0 < d ≤ max(m, n)`.
- Es posible lograrlo usando las operaciones permitidas.

### Operaciones permitidas

1. **Llenar**: Puedes llenar cualquiera de las jarras hasta su capacidad máxima.
2. **Vaciar**: Puedes vaciar cualquiera de las jarras completamente.
3. **Transferir**: Puedes verter agua de una jarra a otra hasta que:
   - La primera jarra se vacíe, o
   - La segunda jarra alcance su capacidad máxima.

### Ejemplo clásico

Tienes una jarra de **3 litros** y otra de **5 litros**, y necesitas medir exactamente **4 litros**.

#### Solución

1. Llena la jarra de 5 litros (5, 0).
2. Transfiere agua de la jarra de 5 litros a la de 3 litros (2, 3).
3. Vacía la jarra de 3 litros (2, 0).
4. Transfiere el agua restante de la jarra de 5 litros a la jarra de 3 litros (0, 2).
5. Llena la jarra de 5 litros nuevamente (5, 2).
6. Transfiere agua de la jarra de 5 litros a la de 3 litros (4, 3).

### Relación matemática

El problema tiene solución si y solo si:

1. `d` es un múltiplo del máximo común divisor (**MCD**) de `m` y `n`.
2. `d` no excede la capacidad máxima de las jarras.
