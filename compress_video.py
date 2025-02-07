from moviepy.editor import VideoFileClip

def compress_video(input_path, output_path, target_size_mb=5):
    # Load the video
    video = VideoFileClip(input_path)
    
    # Calculate current size in MB
    current_size = video.reader.size / (1024*1024)
    
    # Calculate compression ratio
    ratio = (target_size_mb / current_size) ** 0.5
    
    # Resize video while maintaining aspect ratio
    resized_video = video.resize(ratio)
    
    # Write the compressed video
    resized_video.write_videofile(output_path, 
                                codec='libx264', 
                                audio_codec='aac',
                                bitrate=f"{target_size_mb}M")
    
    # Close the clips
    video.close()
    resized_video.close()

if __name__ == "__main__":
    input_file = "static/videos/couple2.mp4"
    output_file = "static/videos/couple2_compressed.mp4"
    compress_video(input_file, output_file)
