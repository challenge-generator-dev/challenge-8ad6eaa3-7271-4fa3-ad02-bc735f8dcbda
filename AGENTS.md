# AGENTS.md

Instrucciones para el agente de IA que abra este repositorio (Claude Code, Cursor, Codex, Copilot, Gemini). Se cargan solas: no hay que pegar nada en ningun chat.

## Que es este repositorio

Es el codigo base de un reto de aprendizaje de Pragma: **Implementación de consulta de saldos asincrónica**.

| | |
|---|---|
| Tema | Servicios asincronicos con FastAPI |
| Nivel | advanced-l2 |
| Chapter | Backend |
| Especialidad | Python |
| Stack | Python / FastAPI 0.115.0 |
| Patron arquitectonico | hexagonal/clean con async/await |
| Tiempo estimado | 8 horas |

## Receta del stack

Esqueleto obligatorio:

- `pyproject.toml o requirements.txt en la raiz`
- `app/main.py con la instancia de FastAPI`
- `app/domain con entidades y puertos (Protocol o ABC)`
- `app/application con casos de uso`
- `app/infrastructure con repositorios y routers`

Dependencias:

- fastapi 0.115.0
- uvicorn 0.30.6
- pydantic 2.9.2
- httpx 0.27.2
- python-dotenv 1.0.1
- pytest 8.3.2
- pytest-asyncio 0.24.0
- poetry n/a

## Tu tarea

Dejar este proyecto en estado **verificable**: que el comando de verificacion corra sin errores. Escribi los archivos en disco, en este repositorio. No generes ZIPs ni archivos adjuntos.

En orden:

1. Corre `pip install -r requirements.txt && python -c "import app.main"` y mira que falla.
2. Completa lo que falte de la lista de abajo: manifiesto de dependencias, punto de entrada, capa de interfaz y las capas del patron declarado.
3. Arregla SOLO los errores que impiden compilar o arrancar.
4. Volve a correr `pip install -r requirements.txt && python -c "import app.main"` hasta que pase.
5. Pará ahí.

## Regla dura: las fases son trabajo del humano

**PROHIBIDO implementar los entregables de las fases.** El valor del reto esta en que la persona los resuelva. Tu trabajo es que tenga un proyecto que arranca; el hueco pedagogico se queda como esta.

No resuelvas nada de esto:

- **Fase 1 — Configuración inicial y exposición de la API**: API funcional con una ruta para consultar saldos.
- **Fase 2 — Integración asincrónica con las fuentes de saldos**: API que consulta saldos de dos fuentes de manera asincrónica y maneja errores del dominio.
- **Fase 3 — Consolidación y exposición de los saldos**: API que consolida y expone los saldos de dos cuentas.

Distincion operativa:

- **Arreglar** (si): import faltante, tipo que no existe, dependencia sin declarar, error de sintaxis, archivo referenciado que no existe.
- **No tocar** (no): logica de negocio incompleta, validaciones ausentes, secretos hardcodeados, APIs deprecadas que funcionan, concurrencia insegura, patrones mejorables. Eso es lo que la persona tiene que encontrar.

## Lo que falta y tenes que completar

No se detectaron huecos: estan los archivos declarados, el boilerplate del stack y ninguna referencia quedo colgando. Igual corre el comando de verificacion — que los archivos existan no garantiza que compilen.

### Presentes (14)

- `pyproject.toml`
- `app/main.py`
- `app/config/settings.py`
- `app/domain/models.py`
- `app/__init__.py`
- `app/application/services.py`
- `app/infrastructure/external_services.py`
- `app/infrastructure/repositories.py`
- `app/presentation/api.py`
- `app/presentation/error_handlers.py`
- `tests/test_services.py`
- `tests/test_repositories.py`
- `tests/test_api.py`
- `requirements.txt`

### Capas del patron declarado

Cada una tiene que existir como directorio real con al menos un archivo. Codigo plano en la raiz no satisface el patron.

- `app/domain`
- `app/application`
- `app/infrastructure`
- `app/presentation`
- `app/config`

## Verificacion

```bash
pip install -r requirements.txt && python -c "import app.main"
```

Ese comando pasando es la definicion de "terminado" para vos.

## Convenciones que tenes que respetar

- Un solo ecosistema: no declares librerias de otro lenguaje ni mezcles gestores de paquetes.
- Toda libreria que uses tiene que estar declarada en el manifiesto de dependencias.
- Todo import declarado tiene que usarse; todo tipo usado tiene que existir o venir de una dependencia declarada.
- El patron es **hexagonal/clean con async/await**: los contratos (interfaces, puertos) los define la capa interna y los implementa la externa, nunca al revés.
- Los archivos que crees llevan implementacion real, no stubs: sin `TODO`, sin cuerpos vacios, sin `// getters y setters`.

## Contexto del candidato

Sirve para calibrar el nivel del codigo, no para resolver las fases.

- Perfil: Chapter Backend, Especialidad Desarrollador, Tecnología Python, Advanced
- Brecha que el reto ataca: Maneja operaciones de I/O sin bloquear el event loop y modela los errores del dominio de forma explicita
- Mision: Exponer la consulta de saldos consolidando dos fuentes

---

*Generado por Challenge Generator — Pragma. `README.md` tiene el enunciado completo del reto para la persona. `PROMPT_MEJORA.md` es la variante para pegar en un chat, si se prefiere ese flujo.*
