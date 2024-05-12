"""
Basic video exporting example
"""

import pathlib
from abc import ABC, abstractmethod

class VideoExporter(ABC):
    """ Basic representation of video exporting codec."""
    
    @abstractmethod
    def prepare_export(self, video_data):
        """ Prepares video data for exporting."""
        
    @abstractmethod
    def do_export(self, folder:pathlib.Path):
        """Exports video exporting codec."""
        
class LosslessVideoExporter(VideoExporter):
    """Lossless video exporting codec."""
    
    def prepare_export(self, video_data):
        print("Preparing video data for lossless export.")
        
    def do_export(self, folder:pathlib.Path):
        print(f"Exporting video data in lossless format to {folder}.")
        
class H264VideoExporter(VideoExporter):
    """H264 video exporting codec."""
    
    def prepare_export(self, video_data):
        print("Preparing video data for H264 lossless export.")
        
    def do_export(self, folder:pathlib.Path):
        print(f"Exporting video data in lossless format to {folder}.")
    
        
class AudioExporter(ABC):
    """Basic representation of audio exporting codec."""
    
    @abstractmethod
    def prepare_export(self, audio_data):
        """Prepares audio data for exporting."""
        
    @abstractmethod
    def do_export(self, folder:pathlib.Path):
        """Exports the audio data to a folder."""
        
class AACAudioExporter(AudioExporter):
    """AAC audio exporting codec."""
    def prepare_export(self,audio_data):
        print("Preparing audio data for AAC export.")
        
    def do_export(self, folder:pathlib.Path):
        print(f"Exporting audio data in AAC format to {folder}.")
        
class WAVAudioExporter(AudioExporter):
    """WAV (lossless) audio exporting codec."""
    
    def prepare_export(self, audio_data):
        print("Preparing audio data for WAV export")
        
    def do_export(self, folder:pathlib.Path):
        print(f"Exporting audio data in WAV format to {folder}.")

class ExporterFactory(ABC):
    """
    Factory that represents a combination of video and audio codecs
    The factory does not maintain any of the instances it creates.
    """
    
    def get_video_exporter(self) -> VideoExporter:
        """Returns a new video exporter instance"""
        
    def get_audio_exporter(self) -> AudioExporter:
        """ Returns a new audio exporter instance"""        
        
class FastExporter(ExporterFactory):
    """Factory aimed at providing a high speed, lower quality export."""
    
    def get_video_exporter(self) -> VideoExporter:
        return H264VideoExporter()        
        
    def get_audio_exporter(self) -> AudioExporter:
       return AACAudioExporter()
        

class HighQualityExporter(ExporterFactory):
    """Factory aimed at providing a slow speed, high quality export."""
    
    def get_video_exporter(self) -> VideoExporter:
        return H264VideoExporter()        
        
    def get_audio_exporter(self) -> AudioExporter:
       return WAVAudioExporter()

def read_exporter() -> ExporterFactory:
    factories = {
        "low": FastExporter(),
        "high": HighQualityExporter(),
    }
    # read the desired export quality
    while True:
        export_quality = input("Please enter the desired export quality (low, high, master): ")
        if export_quality in factories:
            return factories[export_quality]
        print("Invalid export quality. Please try again.")

def main(fac:ExporterFactory) -> None:
    """Main function"""
                
    # create the video and audio exporters
    video_exporter = fac.get_video_exporter()
    audio_exporter = fac.get_audio_exporter()
    
    # prepare the export   
    video_exporter.prepare_export("placeholder_for_video_data")
    audio_exporter.prepare_export("placeholder_for_audio_data")
    
    # # do the export
    # folder = pathlib.Path('/usr/tmp/video')
    # video_exporter.do_export(folder)
    # audio_exporter.do_export(folder)
    
if __name__ == '__main__':
    fac = read_exporter()
    main(fac)  