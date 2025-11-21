import os
import threading

NUM_THREADS = 10
VIDEO_ROOT = r'../ssd/video/something/v2/20bn-something-something-v2'
FRAME_ROOT = r'../ssd/video/something/v2/20bn-something-something-v2-frames'


def split(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]


def extract(video):
    video_name_no_ext = video[:-5]
    
    input_path = os.path.join(VIDEO_ROOT, video)
    output_path = os.path.join(FRAME_ROOT, video_name_no_ext)
    output_file_pattern = os.path.join(output_path, '%06d.jpg')
    
    cmd = f'ffmpeg -i "{input_path}" -threads 1 -vf scale=-1:256 -q:v 0 "{output_file_pattern}" -loglevel error'
    
    os.system(cmd)


def target(video_list):
    for video in video_list:
        if not video.endswith('.webm'):
            continue
        
        try:
            os.makedirs(os.path.join(FRAME_ROOT, video[:-5]), exist_ok=True)
            extract(video)
        except Exception as e:
            print(f"Error processing {video}: {e}")


if __name__ == '__main__':
    if not os.path.exists(VIDEO_ROOT):
        raise ValueError('Please download videos and set VIDEO_ROOT variable.')
    if not os.path.exists(FRAME_ROOT):
        os.makedirs(FRAME_ROOT, exist_ok=True)
    
    all_files = os.listdir(VIDEO_ROOT)
    
    video_list = [f for f in all_files if f.endswith('.webm')]
    
    print(f"Total .webm videos found: {len(video_list)}")
    
    splits = list(split(video_list, NUM_THREADS))
    
    threads = []
    for i, split in enumerate(splits):
        thread = threading.Thread(target=target, args=(split,))
        thread.start()
        threads.append(thread)
    
    for thread in threads:
        thread.join()
    
    print("Extraction complete.")