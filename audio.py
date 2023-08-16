from narakeet_api import AudioAPI
from playsound import playsound

# add your API key here
api_key = 'api key' 
format = "wav"
voice = "khaled"
# add your text here
script = 'نعم، بالطبع يمكنني التحدث بالعربية. كيف يمكنني مساعدتك اليوم؟'

def show_progress(progress_data):
    print(progress_data)

api = AudioAPI(api_key)

task = api.request_audio_task(format, script, voice)
task_result = api.poll_until_finished(task['statusUrl'], show_progress)

if task_result['succeeded']:
    filename = f'output.{format}'
    api.download_to_file(task_result['result'], filename)
    print(f'downloaded to {filename}')
    # play the output audio
    playsound(filename)
else:
    raise Exception(task_result['message'])