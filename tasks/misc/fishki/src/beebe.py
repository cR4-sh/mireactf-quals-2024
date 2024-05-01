import moviepy.editor as moviepy
import os


# Загружаем исходное видео и удаляем аудио
for i in os.listdir("./backend/resources/"):
    clip = moviepy.VideoFileClip(f"./backend/resources/{i}").without_audio()

    # Опционально, изменяем размер видео для дополнительного сжатия
    # Можно адаптировать разрешение, например, до 320x240 или ещё меньше, в зависимости от исходного разрешения видео
    clip_resized = clip.resize(height=720) # Изменение размера видео

    # Пишем видеофайл с конкретными настройками для сжатия
    # Экспериментируем с параметрами, такими как bitrate и fps, для достижения желаемого размера файла
    clip_resized.write_videofile(i, bitrate="6000k", fps=60, preset="ultrafast")