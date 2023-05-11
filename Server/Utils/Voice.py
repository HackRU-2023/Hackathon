from gtts import gTTS
import os
import speech_recognition as sr
import os
from pydub import AudioSegment
from pydub.silence import split_on_silence

class Voice:
    def convert_text_to_speech(self, text, language='en', slow=False, filename='output.mp3'):
        # Create gTTS object
        tts = gTTS(text=text, lang=language, slow=slow)

        # Save the audio file
        tts.save(filename)

        # Play the audio file
        os.system(filename)

    def transcribe_audio(self, path):
        # Create a speech recognition object
        r = sr.Recognizer()

        # Use the audio file as the audio source
        with sr.AudioFile(path) as source:
            audio_listened = r.record(source)
            # Try converting it to text
            text = r.recognize_google(audio_listened)
        return text

    def get_large_audio_transcription_on_silence(self, path):
        """Splitting the large audio file into chunks and apply speech recognition on each of these chunks"""
        # Open the audio file using pydub
        sound = AudioSegment.from_file(path)
        # Split audio sound where silence is 500 milliseconds or more and get chunks
        chunks = split_on_silence(sound,
                                  # Experiment with this value for your target audio file
                                  min_silence_len=500,
                                  # Adjust this per requirement
                                  silence_thresh=sound.dBFS - 14,
                                  # Keep the silence for 1 second, adjustable as well
                                  keep_silence=500,
                                  )
        folder_name = "audio-chunks"
        # Create a directory to store the audio chunks
        if not os.path.isdir(folder_name):
            os.mkdir(folder_name)
        whole_text = ""
        # Process each chunk
        for i, audio_chunk in enumerate(chunks, start=1):
            # Export audio chunk and save it in the `folder_name` directory.
            chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
            audio_chunk.export(chunk_filename, format="wav")
            # Recognize the chunk
            try:
                text = self.transcribe_audio(chunk_filename)
            except sr.UnknownValueError as e:
                print("Error:", str(e))
            else:
                text = f"{text.capitalize()}. "
                print(chunk_filename, ":", text)
                whole_text += text
        # Return the text for all chunks detected
        return whole_text


# Example usage
voice = Voice()

# Code 1
text1 = "Don't speak like that"
voice.convert_text_to_speech(text1, language='en', slow=False, filename='welcome1.mp3')

# Code 2
filename = "LISTEN to Your SECRET VOICE.wav"
text2 = voice.transcribe_audio(filename)
print(text2)
