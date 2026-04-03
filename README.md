# Squat Coach AI

Squat Coach AI es un proyecto de analisis de sentadilla con vision por computadora usando Python, OpenCV y MediaPipe. Procesa un video lateral pregrabado, detecta landmarks de pose por frame y genera un video anotado junto con resultados exportables.

## Objetivo del MVP

- Ejecutar procesamiento local, sin backend ni base de datos.
- Leer un video de sentadilla desde una camara lateral fija.
- Detectar pose por frame con MediaPipe Pose.
- Exportar landmarks a JSON.
- Generar video anotado.

## Stack

- Python
- OpenCV
- MediaPipe

## Estructura del proyecto

```text
squat-coach-ai/
  app/
    main.py
    config.py
    pipeline/
      video_reader.py
      pose_estimator.py
    utils/
      drawing.py
      mp_compat.py
  data/
    raw/
  outputs/
    json/
    videos/
  tests/
  requirements.txt
  README.md
  LICENSE
  NOTICE
  CONTRIBUTING.md
```

## Como ejecutar

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python -m app.main --input data/raw/mi_video.mp4
```

Salidas esperadas:

- `outputs/json/landmarks.json`
- `outputs/videos/annotated.mp4`

## Autor

Abel Romero Ruiz

## Licencia

Este proyecto se distribuye bajo la licencia MIT. Consulta el archivo `LICENSE` para el texto completo.

## Atribucion

En cualquier redistribucion o trabajo derivado se debe conservar el aviso de copyright y la licencia MIT incluidos en este repositorio.

## Nota sobre herramientas de asistencia

"Este proyecto fue desarrollado con apoyo de herramientas de asistencia de codigo, incluyendo Codex, pero la arquitectura, decisiones tecnicas e integracion fueron realizadas por Abel Romero Ruiz."
