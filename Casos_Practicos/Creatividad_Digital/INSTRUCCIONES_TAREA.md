# Tarea: Caso Practico — Creatividad Digital

**Curso:** Taller de Programacion — UDeG Campus GDL
**Profesor:** Dr. Pierre Delice
**Entrega:** una semana

---

## Objetivo

Desarrollar un analisis completo de un dataset real de campanas de creatividad digital. La tarea cubre cuatro niveles de conocimiento: comprension de la estructura de datos, calculo de indicadores derivados (de simples a complejos), analisis estadistico de tendencia y dispersion, y comunicacion de resultados mediante un reporte tecnico.

---

## Dataset

El archivo `datos/campanas_creatividad_digital.csv` contiene **200 campanas** de publicidad digital. Consulta `diccionario_datos.md` para entender cada columna antes de comenzar.

---

## Instrucciones

Trabaja en un notebook `en blanco`.

---

### Parte 1 — Estructura del dataset (Seccion 2)

El primer paso de cualquier analisis es entender con que datos se trabaja.

- Muestra las dimensiones del dataframe: filas y columnas (`shape`)
- Lista el nombre y tipo de dato de cada columna (`dtypes`)
- Reporta la cantidad de valores nulos por columna (`isna().sum()`)
- Identifica cuales columnas son numericas y cuales son categoricas
- Muestra las primeras 5 filas y las ultimas 5 filas del dataframe

> **Por que importa:** conocer la estructura evita errores de tipo y revela problemas de calidad antes de calcular cualquier metrica.

---

### Parte 2 — Indicadores derivados (Seccion 3)

Los indicadores se calculan a partir de las columnas originales. Van de simples (una operacion) a compuestos (varias columnas combinadas).

#### Indicadores basicos

| Columna | Formula | Descripcion |
|---------|---------|-------------|
| `ctr` | `clicks / impresiones` | Tasa de clics |
| `cvr` | `conversiones / clicks` | Tasa de conversion |

#### Indicadores de costo

| Columna | Formula | Descripcion |
|---------|---------|-------------|
| `cpc` | `costo_usd / clicks` | Costo por click |
| `cpm` | `(costo_usd / impresiones) * 1000` | Costo por mil impresiones |

#### Indicador compuesto

| Columna | Formula | Descripcion |
|---------|---------|-------------|
| `roi` | `(ingresos_usd - costo_usd) / costo_usd` | Retorno sobre la inversion |

Agrega las cinco columnas al dataframe. Verifica que no haya valores nulos en ninguna de ellas.

> **Por que importa:** pasar de datos crudos a indicadores de negocio es la habilidad central del analista. Cada formula tiene una interpretacion economica distinta.

---

### Parte 3 — Preguntas de negocio con filtros (Seccion 4)

Usa los indicadores calculados para responder preguntas concretas. Guarda cada respuesta en una variable.

1. **q1** — Campanas con ROI negativo cuyo `costo_usd` esta por encima de la mediana. ¿Cuantas son y que plataformas concentran mas casos?
2. **q2** — Top 10 campanas por ROI unicamente en TikTok e Instagram.
3. **q3** — ¿Que formato tiene el CTR promedio mas alto? Muestra una fila por formato ordenada de mayor a menor CTR.
4. **q4** — ¿En que pais se obtuvo el mayor ingreso total? Agrupa por `pais` y suma `ingresos_usd`.

> **Por que importa:** combinar filtros, agrupaciones y ordenamientos es como se responden preguntas de negocio reales con datos.

---

### Parte 4 — Estadistica descriptiva: tendencia central (Seccion 5)

La tendencia central resume el valor "tipico" de una variable.

Para las columnas `costo_usd`, `impresiones`, `clicks`, `conversiones`, `ingresos_usd`, `ctr`, `cvr`, `cpc`, `cpm` y `roi`, calcula:

- **Media** (`mean`) — promedio aritmetico
- **Mediana** (`median`) — valor central al ordenar los datos
- **Moda** (opcional, para columnas categoricas como `plataforma` y `formato`)

Presenta los resultados en un dataframe llamado `tendencia_central`.

Luego repite el calculo de media agrupando por `plataforma` (`por_plataforma`) y por `formato` (`por_formato`).

> **Por que importa:** la media es sensible a valores extremos; la mediana es robusta. Comparar ambas revela si los datos estan sesgados.

---

### Parte 5 — Estadistica descriptiva: dispersion (Seccion 5, continuacion)

La dispersion indica que tan dispersos estan los datos alrededor del centro.

Para las mismas columnas numericas calcula:

- **Desviacion estandar** (`std`) — distancia promedio respecto a la media
- **Varianza** (`var`) — cuadrado de la desviacion estandar
- **Rango** (`max - min`) — amplitud total de los datos
- **Rango intercuartilico IQR** (`Q3 - Q1`) — amplitud del 50 % central

Presenta los resultados en un dataframe llamado `dispersion`.

Interpreta brevemente en una celda Markdown: ¿que columna tiene mayor variabilidad relativa y por que crees que es asi?

> **Por que importa:** dos campanas con la misma media de ROI pueden tener comportamientos muy distintos si una es consistente y la otra es muy variable.

---

### Parte 6 — Deteccion de outliers con IQR (Seccion 6)

Los outliers son observaciones que se alejan significativamente del patron general.

Aplica el metodo IQR a la columna `ctr`:

1. Calcula Q1 (percentil 25) y Q3 (percentil 75).
2. Calcula IQR = Q3 − Q1.
3. Define limite inferior = Q1 − 1.5 × IQR y limite superior = Q3 + 1.5 × IQR.
4. Guarda en `outliers_ctr` las filas fuera de esos limites.
5. En una celda Markdown responde: ¿cuantos outliers hay?, ¿son valores altos o bajos?, ¿que plataformas aparecen mas en los outliers?

Repite el mismo analisis para `roi` y guarda el resultado en `outliers_roi`.

> **Por que importa:** los outliers pueden ser errores de captura o campanas excepcionales; identificarlos evita que distorsionen el analisis.

---

### Parte 7 — Visualizacion (Seccion 7)

Genera al menos **cuatro graficas** con `matplotlib`. Cada una debe tener titulo, etiquetas en los ejes y leyenda si aplica.

| # | Grafica sugerida | Variable(s) |
|---|-----------------|-------------|
| 1 | Histograma | `roi` |
| 2 | Boxplot comparativo | `ctr` por `plataforma` |
| 3 | Grafica de barras | CTR promedio por `formato` |
| 4 | Serie de tiempo | ingresos mensuales totales (`fecha`) |

En una celda Markdown debajo de cada grafica escribe una oracion interpretando lo que muestra.

> **Por que importa:** las graficas hacen visible lo que los numeros ocultan y son la base del storytelling de datos.

---

### Parte 8 — Merge con tabla de clientes (nueva seccion)

El archivo `datos/clientes.csv` contiene informacion adicional sobre cada cliente/agencia. Tiene la siguiente estructura:

| Columna | Descripcion |
|---------|-------------|
| `cliente` | Nombre del cliente (llave de union con el dataset principal) |
| `industria` | Sector al que pertenece el cliente |
| `tamano` | Tamano de la empresa: `Pequena`, `Mediana` o `Grande` |
| `pais_origen` | Pais de origen del cliente |
| `nivel_contrato` | Tipo de contrato: `Basico`, `Premium` o `Enterprise` |
| `descuento_pct` | Porcentaje de descuento negociado |
| `anios_cliente` | Antiguedad del cliente en anos |

#### Ejercicios de merge

Carga el archivo y realiza las siguientes uniones. Guarda cada resultado en la variable indicada.

**m1 — Left merge** (todos los registros de campanas, agregando info del cliente si existe):

```python
clientes = pd.read_csv('datos/clientes.csv')
m1 = pd.merge(df, clientes, on='cliente', how='left')
```

Verifica: `m1` debe tener el mismo numero de filas que `df`.

**m2 — Inner merge** (solo campanas cuyos clientes tienen registro en `clientes.csv`):

```python
m2 = pd.merge(df, clientes, on='cliente', how='inner')
```

Verifica: ¿cuantas filas tiene `m2`? ¿Es igual a `m1`? Explica la diferencia en una celda Markdown.

**m3 — Outer merge** (todos los registros de ambas tablas, con NaN donde no haya coincidencia):

```python
m3 = pd.merge(df, clientes, on='cliente', how='outer')
```

Verifica: ¿que clientes de `clientes.csv` no tienen campanas en el dataset principal? Usa `m3[m3['id_campana'].isna()]` para encontrarlos.

#### Analisis post-merge

Con el resultado de `m1` responde las siguientes preguntas:

1. **pm1** — ROI promedio agrupado por `industria`. ¿Que industria tiene mejor desempeno?
2. **pm2** — CTR promedio agrupado por `nivel_contrato`. ¿Los clientes Enterprise obtienen mejor CTR?
3. **pm3** — Campanas de clientes con `tamano = 'Grande'` y ROI positivo. ¿Cuantas son y que porcentaje representan del total de campanas de clientes grandes?

> **Por que importa:** en la practica los datos nunca vienen en una sola tabla. El `merge` es la operacion fundamental para combinar fuentes y enriquecer el analisis con contexto adicional. Los distintos tipos (`left`, `inner`, `outer`) controlan que filas se conservan y revelan inconsistencias entre fuentes.

---

### Parte 9 — Reporte Markdown (Seccion 8)

Genera el archivo `reporte_caso_creatividad.md` usando la plantilla `plantilla_reporte_caso_creatividad.md`. El reporte debe integrar todo el analisis anterior y contener:

- **Descripcion del dataset** — estructura, periodo, columnas principales
- **Hallazgos de tendencia central** — valores tipicos de las metricas clave
- **Hallazgos de dispersion** — que metricas son mas variables y que implica
- **Outliers identificados** — cuantos, en que metrica, patron observado
- **3 insights accionables** para el equipo de marketing (sustentados con numeros)
- **2 recomendaciones** de decision basadas en los datos

Todos los numeros citados en el reporte deben coincidir con los resultados del notebook.

> **Por que importa:** un analisis sin reporte no existe. Comunicar hallazgos con claridad es tan importante como calcularlos.

---

## Entregables

Sube a la plataforma del curso los siguientes dos archivos:

1. `live_coding_caso_creatividad_digital_student.ipynb` — con todas las celdas ejecutadas sin errores
2. `reporte_caso_creatividad.md` — reporte completo con numeros del analisis

---

## Criterios de evaluacion

| Criterio | Puntos |
|----------|--------|
| Estructura del dataset documentada | 10 |
| Indicadores basicos correctos (CTR, CVR) | 10 |
| Indicadores de costo y ROI correctos | 10 |
| Preguntas de negocio respondidas | 10 |
| Tendencia central calculada e interpretada | 10 |
| Dispersion calculada e interpretada | 10 |
| Outliers identificados en CTR y ROI | 10 |
| Merge left/inner/outer correctos y comparados | 15 |
| Analisis post-merge (pm1, pm2, pm3) | 10 |
| Minimo 4 graficas con formato y texto | 5 |
| Reporte coherente con el analisis | 5 |
| **Total** | **105 (5 puntos extra)** |

---

## Notas

- Ejecuta el notebook de principio a fin antes de entregar (`Kernel > Restart & Run All`).
- Si no tienes `matplotlib`: `pip install matplotlib`
- Usa celdas Markdown para explicar tu razonamiento; el codigo solo no es suficiente.
- Trabaja de forma individual.
