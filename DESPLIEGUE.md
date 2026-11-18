# Guía de despliegue — Entrega final

Fecha límite: sábado 21 de noviembre de 2026.

## 1. Backend en Render

El archivo `render.yaml` define dos servicios gratuitos:

| Servicio | Carpeta | Base de datos |
|---|---|---|
| `api-videojuegos-grupo5` | `Maria/` | Neon (misma que en local) |
| `api-animales-grupo5` | `Thomas/` | Neon (misma que en local) |

Pasos:

1. Crear cuenta en https://render.com (se puede entrar con GitHub).
2. **New → Blueprint** y conectar el repositorio `Maria-0922/Ejemplos-API-grupo5`.
3. Render detectará `render.yaml` y pedirá los valores de `DATABASE_URL` (`sync: false`).
   Pegar en ambos la cadena que está en `Maria/.env`:
   ```
   postgresql://neondb_owner:...@ep-noisy-rain-.../neondb?sslmode=require
   ```
4. Esperar a que ambos servicios digan **Live** (puede tardar 5-10 min la primera vez).
5. Copiar las URLs que terminen en `.onrender.com` de cada servicio.

Comprobar: abrir `https://<servicio>.onrender.com/docs`. Debe cargar Swagger.

> En el plan gratuito Render duerme el servicio tras ~15 min sin uso;
> la primera petición después de eso tarda ~30 s en responder. Es normal.

## 2. Actualizar las URLs del frontend

Editar `Frontend-GRUPO5-A-SW/src/environments/environment.ts` con las URLs reales:

```ts
export const environment = {
  apiUrl: 'https://URL-DEL-SERVICIO-ANIMALES.onrender.com',
  videojuegosApiUrl: 'https://URL-DEL-SERVICIO-VIDEOJUEGOS.onrender.com',
};
```

Luego:

```powershell
cd Frontend-GRUPO5-A-SW
npm run build
```

## 3. Frontend en Firebase Hosting

1. Crear un proyecto en https://console.firebase.google.com (plan Spark, gratis).
2. Instalar la CLI (si no está): `npm install -g firebase-tools`
3. Iniciar sesión: `firebase login`
4. Seleccionar el proyecto: `firebase use --add` (elegir el proyecto creado).
5. Desplegar: `firebase deploy --only hosting`

El archivo `firebase.json` ya está configurado:
- `public`: `dist/frontend/browser`
- `rewrites`: todas las rutas → `index.html` (necesario para Angular)

Firebase mostrará la URL final: `https://<proyecto>.web.app`

## 4. Verificación final

Abrir la URL de Firebase y comprobar:

- [ ] `/inicio` carga
- [ ] `/animales` lista datos del backend de Render
- [ ] `/videojuegos` muestra "Conectado" y lista datos del backend de Render
- [ ] Se puede crear, editar, eliminar y buscar por ID
- [ ] `https://<backend>.onrender.com/docs` responde

Entregar: **la URL `https://<proyecto>.web.app`** (mencionando también las URLs de los backends).
