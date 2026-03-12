# Diccionario de Datos — Campanas de Creatividad Digital

Dataset: `datos/campanas_creatividad_digital.csv`
Filas: 200 campanas | Periodo: 2025

---

## Columnas originales del dataset

| Columna | Tipo | Descripcion | Ejemplo |
|---------|------|-------------|---------|
| `id_campana` | string | Identificador unico de la campana | `CAMP-0001` |
| `fecha` | fecha | Fecha de inicio de la campana | `2025-01-02` |
| `cliente` | string | Nombre de la agencia o cliente | `LumaAds` |
| `plataforma` | string | Red social donde se publico | `YouTube`, `Facebook`, `TikTok`, `Instagram` |
| `formato` | string | Tipo de pieza creativa | `Reel`, `Video Largo`, `Imagen`, `Carrusel` |
| `duracion_seg` | entero | Duracion del video en segundos | `30` |
| `objetivo` | string | Objetivo de la campana | `Traffic`, `Ventas`, `Awareness`, `Leads` |
| `pais` | string | Pais donde se difundio (codigo ISO) | `MX`, `AR`, `PE`, `CO` |
| `presupuesto_usd` | flotante | Presupuesto asignado en dolares | `2449.27` |
| `costo_usd` | flotante | Gasto real en dolares | `2356.84` |
| `impresiones` | entero | Numero de veces que se mostro el anuncio | `319655` |
| `alcance` | entero | Usuarios unicos que vieron el anuncio | `212076` |
| `clicks` | entero | Clicks totales en el anuncio | `4073` |
| `reproducciones_3s` | entero | Reproducciones de al menos 3 segundos | `171648` |
| `reproducciones_100` | entero | Reproducciones completas (100%) | `26034` |
| `conversiones` | entero | Acciones objetivo completadas (compras, registros, etc.) | `82` |
| `ingresos_usd` | flotante | Ingresos generados atribuidos a la campana | `626.92` |
| `calificacion_creativa` | entero | Puntuacion interna del equipo creativo (0–100) | `79` |

---

## Metricas derivadas (calculadas en el notebook)

Estas columnas **no estan en el CSV**; las calcula el estudiante en la Seccion 3.

### CTR — Click-Through Rate

**Tasa de clics:** porcentaje de impresiones que resultaron en un click.

```
ctr = clicks / impresiones
```

- Valores tipicos: 0.005 – 0.05 (0.5 % – 5 %)
- Un CTR alto indica que el creativo es relevante para la audiencia.

---

### CVR — Conversion Rate

**Tasa de conversion:** porcentaje de clicks que terminaron en una conversion.

```
cvr = conversiones / clicks
```

- Valores tipicos: 0.01 – 0.10 (1 % – 10 %)
- Un CVR alto indica que la pagina de destino y la oferta son efectivas.

---

### CPC — Costo por Click

**Costo unitario por cada click obtenido**, en dolares.

```
cpc = costo_usd / clicks
```

- Un CPC bajo es mejor: mas trafico al mismo costo.

---

### CPM — Costo por Mil Impresiones

**Costo por cada 1 000 veces que se mostro el anuncio**, en dolares.

```
cpm = (costo_usd / impresiones) * 1000
```

- Metrica estandar para comparar eficiencia de medios entre plataformas.

---

### ROI — Retorno sobre Inversion

**Ganancia neta como fraccion del costo invertido.**

```
roi = (ingresos_usd - costo_usd) / costo_usd
```

- ROI = 0 → se recupera exactamente lo invertido.
- ROI > 0 → la campana es rentable.
- ROI < 0 → la campana perdio dinero.

---

## Valores posibles en columnas categoricas

### `plataforma`

| Valor | Descripcion |
|-------|-------------|
| `YouTube` | Videos de larga o corta duracion |
| `Facebook` | Feed, Stories y Reels |
| `TikTok` | Videos cortos verticales |
| `Instagram` | Feed, Reels y Stories |

### `formato`

| Valor | Descripcion |
|-------|-------------|
| `Reel` | Video corto vertical (15–60 s) |
| `Video Largo` | Video horizontal de larga duracion (>60 s) |
| `Imagen` | Anuncio estatico |
| `Carrusel` | Secuencia de imagenes o videos |

### `objetivo`

| Valor | Descripcion |
|-------|-------------|
| `Awareness` | Dar a conocer la marca |
| `Traffic` | Llevar visitas a un sitio web |
| `Ventas` | Generar conversiones directas |
| `Leads` | Capturar datos de clientes potenciales |

### `pais`

| Codigo | Pais |
|--------|------|
| `MX` | Mexico |
| `AR` | Argentina |
| `PE` | Peru |
| `CO` | Colombia |
