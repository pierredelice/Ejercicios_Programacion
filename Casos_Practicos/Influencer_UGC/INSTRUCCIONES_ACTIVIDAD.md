# Instrucciones de Actividad - Caso Practico Influencer + UGC

## Contexto
Trabajarás con una base de campañas de influencer marketing y contenido UGC para simular un análisis real de negocio digital.

## Objetivo general
Analizar el desempeño de campañas y proponer decisiones de optimización de presupuesto con base en métricas, filtros, estadística y visualización.

## Archivos que vas a usar
- `datos/campanas_influencer_ugc.csv`
- `diccionario_datos.md`
- `plantilla_reporte_caso_influencer_ugc.md`

## Lo que tienes que hacer
1. Abre `caso_influencer_ugc_student.ipynb`.
2. Ejecuta la carga de datos y valida que el DataFrame se lea correctamente.
3. Completa la exploración inicial:
   - tamaño de la base
   - tipos de datos
   - valores nulos
   - categorías disponibles (`tier`, `plataforma`, `tipo_contenido`)
4. Crea métricas derivadas:
   - `engagement_total`
   - `engagement_rate`
   - `ctr_link`
   - `cvr`
   - `cpc`
   - `cpa`
   - `roas`
   - `roi`
5. Resuelve filtros de negocio:
   - top campañas por ROAS con costo superior a la mediana
   - mejor `tier` por ROI promedio
   - mejor tipo de contenido por engagement y conversión
6. Calcula estadística descriptiva:
   - resumen global
   - comparativos por `plataforma`, `tier` y `pais`
7. Detecta outliers con IQR (al menos sobre ROI o CPA).
8. Genera al menos 3 gráficas:
   - tendencia mensual costo vs ingresos
   - barras de ROI por tier
   - scatter de seguidores vs conversiones
9. Redacta tu reporte en Markdown usando la plantilla.

## Entregables
1. Notebook resuelto: `caso_influencer_ugc_student.ipynb`
2. Reporte final: `reporte_caso_influencer_ugc.md`

## Requisitos del reporte
- Resumen ejecutivo breve
- Hallazgos con datos (no solo opinión)
- 3 insights accionables
- 2 recomendaciones concretas de negocio

## Criterios mínimos de revisión
- El notebook corre sin errores en sus celdas principales
- Las métricas derivadas están bien calculadas
- Los filtros responden preguntas reales de negocio
- Las gráficas se interpretan correctamente
- El reporte conecta análisis con decisiones

## Tiempo sugerido
- 90 a 120 minutos

## Nota
Si no tienes `matplotlib`, completa todo el análisis y deja documentado qué gráficas habrías generado.
