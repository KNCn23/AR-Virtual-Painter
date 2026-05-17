# AR Virtual Painter

An augmented reality drawing application built with Python, OpenCV, and MediaPipe. It tracks hand gestures through a webcam and translates index finger movement into real-time strokes on a virtual canvas overlaid on the live camera feed.

## Features

- Real-time hand tracking with no external hardware beyond a standard webcam
- Color selection and brush size control via hand gestures
- Canvas clear gesture
- Smooth stroke rendering using OpenCV drawing primitives

## Requirements

Python 3.8+ and a webcam with reasonable lighting.

```bash
pip install -r requirements.txt
python main.py
```

## Tech

| Library | Role |
|---------|------|
| OpenCV | Video capture, frame rendering, drawing |
| MediaPipe | Hand landmark detection |

## License

MIT
