import os
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

class WatermarkConfig:
    font = os.getenv('FONT', 'Arial')
    font_color = os.getenv('FONT_COLOR', 'white')
    font_size = int(os.getenv('FONT_SIZE', 28))
    back_color = eval(os.getenv('BACK_COLOR', '(0,0,0)'))
    col_opacity = float(os.getenv('COL_OPACITY', 0.6))
    fps = int(os.getenv('FPS', 30))
    codec = os.getenv('CODEC', 'libx264')
    video_input = os.getenv('VIDEO_INPUT', 'myvideo.mp4')
    video_output = os.getenv('VIDEO_OUTPUT', 'output.mp4')


class VideoClipFactory:
    @staticmethod
    def create_video_clip(file_name):
        return VideoFileClip(file_name, audio=True)


class WatermarkText:
    def __init__(self, text: str):
        self.text = text

    def create_text_clip(self):
        return TextClip(self.text, font=WatermarkConfig.font, color=WatermarkConfig.font_color,
                        fontsize=WatermarkConfig.font_size)


class WatermarkPositionStrategy:
    def set_position(self, clip, width, height):
        raise NotImplementedError("This method should be overridden by subclasses")


class BottomRightPosition(WatermarkPositionStrategy):
    def set_position(self, clip, width, height):
        return lambda pos: (max(width/30, int(width - 0.5 * width * pos)), max(5 * height / 6, int(100 * pos)))


def create_watermark(clip, text):
    width, height = clip.size
    watermark_text = WatermarkText(text).create_text_clip()
    
    set_color = watermark_text.on_color(size=(clip.w + watermark_text.w, watermark_text.h-10),
                                        color=WatermarkConfig.back_color, pos=(6, 'center'),
                                        col_opacity=WatermarkConfig.col_opacity)
    set_text_pos = set_color.set_pos(BottomRightPosition().set_position(clip, width, height))
    return CompositeVideoClip([clip, set_text_pos])


def main():
    video_clip = VideoClipFactory.create_video_clip(WatermarkConfig.video_input)
    watermark = create_watermark(video_clip, "WaterMark")
    watermark.duration = video_clip.duration
    watermark.write_videofile(WatermarkConfig.video_output, fps=WatermarkConfig.fps, codec=WatermarkConfig.codec)

if __name__ == "__main__":
    main()
