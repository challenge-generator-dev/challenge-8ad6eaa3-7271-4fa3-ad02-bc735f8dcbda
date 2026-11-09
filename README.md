# Implementación de consulta de saldos asincrónica

El sistema bancario requiere una API que permita a los clientes consultar sus saldos consolidados de dos cuentas diferentes sin bloquear el event loop. Las cuentas son 'Cuenta Corriente' y 'Cuenta de Ahorro'. Los saldos se obtienen de dos fuentes distintas: 'Sistema de Cuentas Corrientes' y 'Sistema de Cuentas de Ahorro'. El sistema debe manejar los errores del dominio de forma explícita, como saldos no disponibles o errores de conexión con las fuentes.

## Informacion General

| Campo | Valor |
|-------|-------|
| **Tema** | Servicios asincronicos con FastAPI |
| **Nivel** | advanced-l2 |
| **Tipo** | practical |
| **Tiempo estimado** | 8 horas |

## Fases del Reto

### Fase 0: Configuración del Proyecto

**Objetivo:** Obtener el proyecto base funcional enviando el Código Base a un asistente de IA, que lo analizará, corregirá errores y entregará cada archivo con su ruta.

**Tiempo estimado:** 15-30 minutos

**Instrucciones:**

- Asegúrate de tener instalado para ejecutar el proyecto: Python 3.10+, pip, VS Code o similar.
- Copia todo el contenido del campo **Código Base** de este reto — incluyendo el texto de instrucciones que aparece al inicio.
- Abre un asistente de IA (Claude en claude.ai, ChatGPT o Gemini — se recomienda Claude), pega el contenido copiado en el chat y envíalo.
- El asistente analizará los archivos, corregirá errores y entregará cada archivo con su ruta. Guárdalos en la carpeta donde quieras trabajar, respetando las rutas.
- Ejecuta `pip install -r requirements.txt` y luego arranca el proyecto. Si no hay errores, estás listo.

**Entregable:** El proyecto compila/arranca sin errores.

<details>
<summary>Pistas de conocimiento</summary>

- Copia el Código Base completo incluyendo el texto de instrucciones al inicio — esas instrucciones le indican al asistente exactamente qué hacer con los archivos.
- Si el asistente no entrega todos los archivos al terminar el análisis, escríbele: "entrégame todos los archivos con su ruta".
- Si el proyecto tiene errores al arrancar, comparte el mensaje de error con el mismo asistente para que lo corrija.

</details>

### Fase 1: Configuración inicial y exposición de la API

**Objetivo:** Configurar el entorno de desarrollo y exponer una API básica para consultar saldos.

**Tiempo estimado:** 2 horas

**Instrucciones:**

- Configurar el entorno de desarrollo con FastAPI.
- Crear una ruta básica para consultar saldos que devuelva un mensaje de éxito.

**Entregable:** API funcional con una ruta para consultar saldos.

<details>
<summary>Pistas de conocimiento</summary>

- FastAPI permite definir rutas y handlers de manera sencilla.
- El event loop de Python debe mantenerse libre para manejar operaciones asincrónicas.

</details>

### Fase 2: Integración asincrónica con las fuentes de saldos

**Objetivo:** Integrar la API con las fuentes de saldos de manera asincrónica.

**Tiempo estimado:** 3 horas

**Instrucciones:**

- Implementar la lógica para consultar los saldos de 'Cuenta Corriente' y 'Cuenta de Ahorro' de manera asincrónica.
- Manejar los errores de conexión y los saldos no disponibles de forma explícita.

**Entregable:** API que consulta saldos de dos fuentes de manera asincrónica y maneja errores del dominio.

<details>
<summary>Pistas de conocimiento</summary>

- Utiliza async/await para realizar consultas asincrónicas.
- Define excepciones personalizadas para manejar los errores del dominio.

</details>

### Fase 3: Consolidación y exposición de los saldos

**Objetivo:** Consolidar los saldos de las dos cuentas y exponerlos a través de la API.

**Tiempo estimado:** 3 horas

**Instrucciones:**

- Implementar la lógica para consolidar los saldos de 'Cuenta Corriente' y 'Cuenta de Ahorro'.
- Exponer el saldo consolidado a través de la API.

**Entregable:** API que consolida y expone los saldos de dos cuentas.

<details>
<summary>Pistas de conocimiento</summary>

- Utiliza la lógica asincrónica implementada en la fase anterior para obtener los saldos.
- Asegúrate de que la API devuelva el saldo consolidado de manera eficiente.

</details>

## Dimensiones Evaluadas

- **queEs**: ¿Qué es una operación asincrónica en el contexto de FastAPI y cómo se implementa?
- **paraQueSirve**: ¿Para qué sirve manejar los errores del dominio de forma explícita en una API asincrónica?
- **comoSeUsa**: ¿Cómo se usa async/await en FastAPI para realizar consultas asincrónicas?
- **erroresComunes**: ¿Cuáles son los errores comunes que se pueden encontrar al integrar una API con fuentes externas y cómo se manejan?
- **queDecisionesImplica**: ¿Qué decisiones implica la consolidación de saldos de dos cuentas diferentes en una API asincrónica?

## Criterios de Evaluacion

- Configuración correcta del entorno de desarrollo con FastAPI.
- Exposición de una ruta básica para consultar saldos.
- Implementación de consultas asincrónicas a las fuentes de saldos.
- Manejo explícito de errores del dominio.
- Consolidación y exposición de los saldos de dos cuentas a través de la API.

## Como trabajar con un asistente de IA

Hay dos caminos, elegi uno:

- **AGENTS.md** (recomendado) — instrucciones nativas del repo. Abri esta carpeta con tu agente local (Claude Code, Cursor, Codex, Copilot, Gemini) y las carga solo. Sabe que archivos faltan y con que comando se verifica, y completa el scaffold escribiendo en disco.
- **PROMPT_MEJORA.md** — para copiar y pegar en un chat (claude.ai, ChatGPT) si no tenes un agente en el IDE. Declara lo mismo que AGENTS.md; los archivos que te devuelva el chat los guardas en esta carpeta respetando las rutas.

Ninguno de los dos resuelve las fases del reto: eso es tu trabajo.

## Verificacion

El proyecto esta listo para trabajar cuando este comando corre sin errores:

```bash
pip install -r requirements.txt && python -c "import app.main"
```

---

*Reto generado automaticamente por Challenge Generator - Pragma*
