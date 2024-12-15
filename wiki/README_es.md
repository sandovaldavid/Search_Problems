# Problema 01

## El problema de los misioneros y caníbales

El **problema de los misioneros y caníbales** es otro acertijo clásico de lógica que involucra mover a un grupo de personas a través de un río mientras se respetan ciertas restricciones. Es muy similar al problema del granjero, el lobo, la cabra y la col, pero con una narrativa diferente y un conjunto de restricciones únicas.

---

### **Descripción del problema**

Tres misioneros y tres caníbales necesitan cruzar un río usando un bote que tiene capacidad para dos personas. Hay una importante restricción: en ningún momento el número de caníbales en un lado del río puede superar el número de misioneros (si los misioneros están presentes), ya que los caníbales se comerían a los misioneros.

#### **Reglas:**

1. El bote puede llevar a una o dos personas en cada viaje.
2. Debe haber al menos una persona en el bote para que pueda moverse.
3. El número de caníbales no puede exceder el número de misioneros en ninguno de los lados del río.
4. El objetivo es llevar a todos (misioneros y caníbales) al otro lado del río sin que los misioneros sean comidos.

---

### **Estado inicial y estado objetivo**

- **Estado inicial:**  
  Todos los misioneros y caníbales están en el lado izquierdo del río:  
  `(Misión_L, Caníb_L, Bote)` = `(3, 3, L)`

- **Estado objetivo:**  
  Todos los misioneros y caníbales están en el lado derecho del río:  
  `(Misión_L, Caníb_L, Bote)` = `(0, 0, R)`

---

### **Solución paso a paso**

La solución implica mover personas de un lado al otro mientras se cumplen las reglas. Por ejemplo:

1. **Primer viaje:** 2 caníbales cruzan el río.  
   Estado: `(3, 1, L)` en el lado izquierdo; `(0, 2, R)` en el lado derecho.

2. **Regreso:** 1 caníbal regresa.  
   Estado: `(3, 2, L)` y `(0, 1, R)`.

3. **Segundo viaje:** 2 caníbales cruzan nuevamente.  
   Estado: `(3, 0, L)` y `(0, 3, R)`.

4. **Regreso:** 1 caníbal regresa.  
   Estado: `(3, 1, L)` y `(0, 2, R)`.

5. **Tercer viaje:** 2 misioneros cruzan el río.  
   Estado: `(1, 1, L)` y `(2, 2, R)`.

6. **Regreso:** 1 misionero y 1 caníbal regresan.  
   Estado: `(2, 2, L)` y `(1, 1, R)`.

... y así sucesivamente hasta que todos hayan cruzado.

---

### **Representación formal**

Cada estado se representa como una tupla `(Misión_L, Caníb_L, Bote)`, donde:

- `Misión_L` es el número de misioneros en el lado izquierdo.
- `Caníb_L` es el número de caníbales en el lado izquierdo.
- `Bote` indica la posición del bote (`L` o `R`).

El estado objetivo es `(0, 0, R)`.

---

### **Resolución con BFS o DFS**

El problema se puede resolver utilizando búsqueda por amplitud (BFS) o profundidad (DFS) para explorar todos los posibles estados y encontrar una solución válida que cumpla las restricciones.
