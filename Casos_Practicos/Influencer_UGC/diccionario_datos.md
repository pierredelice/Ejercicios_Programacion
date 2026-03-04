# Diccionario de Datos - Caso Influencer + UGC

Archivo base: `datos/campanas_influencer_ugc.csv`

Cada fila representa una campaña/publicación de influencer para una marca en una fecha específica.

## Variables originales (dataset)

| Variable | Tipo | Descripción |
|---|---|---|
| `id_campana` | texto | Identificador único de la campaña. |
| `fecha` | fecha | Día de publicación o ejecución de la campaña. |
| `marca` | texto | Marca que financia la campaña. |
| `vertical` | texto | Industria de la marca (`Beauty`, `Food`, `Fitness`, `Tech`, `Home`). |
| `pais` | texto | País objetivo de la campaña (`MX`, `CO`, `AR`, `CL`, `PE`). |
| `influencer` | texto | Nombre del creador o creadora. |
| `tier` | categórica | Tamaño del influencer: `nano`, `micro`, `mid`, `macro`. |
| `plataforma` | categórica | Canal de publicación (`Instagram`, `TikTok`, `YouTube Shorts`). |
| `tipo_contenido` | categórica | Enfoque creativo (`UGC_Organic`, `UGC_Paid`, `Review`, `Tutorial`, `Challenge`). |
| `seguidores` | entero | Total de seguidores del influencer. |
| `fee_influencer_usd` | numérica | Pago directo al influencer (USD). |
| `costo_produccion_usd` | numérica | Costo de producción del contenido (USD). |
| `paid_boost_usd` | numérica | Inversión de pauta/impulso pagado (USD). |
| `costo_total_usd` | numérica | Costo total de campaña (fee + producción + paid boost). |
| `views` | entero | Total de visualizaciones del contenido. |
| `reach` | entero | Alcance único estimado (cuentas/personas diferentes). |
| `likes` | entero | Número de "me gusta". |
| `comments` | entero | Número de comentarios. |
| `shares` | entero | Veces compartido. |
| `saves` | entero | Veces guardado. |
| `link_clicks` | entero | Clics en enlace (bio, historia, descripción, etc.). |
| `conversiones` | entero | Acciones objetivo logradas (compra, registro, lead, etc.). |
| `ingresos_usd` | numérica | Ingreso atribuido a la campaña (USD). |
| `sentimiento_score` | numérica (0-1) | Indicador de percepción: más cercano a 1 = sentimiento más positivo. |

## Métricas derivadas (para análisis)

Estas columnas se calculan en el notebook:

| Métrica | Fórmula | Interpretación |
|---|---|---|
| `engagement_total` | `likes + comments + shares + saves` | Interacciones totales del contenido. |
| `engagement_rate` | `engagement_total / views` | Qué porcentaje de vistas genera interacción. |
| `ctr_link` | `link_clicks / views` | Proporción de vistas que hacen clic al enlace. |
| `cvr` | `conversiones / link_clicks` | Proporción de clics que se convierten en objetivo. |
| `cpc` | `costo_total_usd / link_clicks` | Costo por clic. Más bajo suele ser mejor. |
| `cpa` | `costo_total_usd / conversiones` | Costo por adquisición/conversión. Más bajo suele ser mejor. |
| `roas` | `ingresos_usd / costo_total_usd` | Retorno sobre gasto publicitario. Si `> 1`, recupera más de lo invertido. |
| `roi` | `(ingresos_usd - costo_total_usd) / costo_total_usd` | Rentabilidad neta relativa. Si `> 0`, la campaña es rentable. |

## Guía rápida de lectura para estudiantes

- Campaña rentable: `roi > 0`
- Campaña muy eficiente en ingresos: `roas` alto
- Buen contenido orgánico: `engagement_rate` alto
- Buen embudo de conversión: `ctr_link` y `cvr` altos
- Riesgo operativo: `cpa` alto con `roi` bajo o negativo
