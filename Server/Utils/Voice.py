import json
import azure.cognitiveservices.speech as speechsdk


class Voice:
    def __init__(self, config):
        # Access the configuration options
        self.speech_key = config['SPEECH_KEY']
        self.speech_region = config['SPEECH_REGION']

    def generate_emotional_speech(self, text, speech_synthesis_voice_name, filename=None):
        # This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
        speech_config = speechsdk.SpeechConfig(subscription=self.speech_key, region=self.speech_region)

        if filename is None:
            audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
        else:
            audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True, filename=filename)

        # The language of the voice that speaks.
        speech_config.speech_synthesis_voice_name = speech_synthesis_voice_name
        speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

        speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()

        if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            print("Speech synthesized for text [{}]".format(text))
        elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = speech_synthesis_result.cancellation_details
            print("Speech synthesis canceled: {}".format(cancellation_details.reason))
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                if cancellation_details.error_details:
                    print("Error details: {}".format(cancellation_details.error_details))
                    print("Did you set the speech resource key and region values?")

    def recognize_from_microphone_or_audio_file(self, audio_file_path=None):
        # This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
        speech_config = speechsdk.SpeechConfig(subscription=self.speech_key, region=self.speech_region)
        speech_config.speech_recognition_language = "en-US"
        if audio_file_path is not None:
            audio_config = speechsdk.audio.AudioConfig(use_default_microphone=False, filename=audio_file_path)
        else:
            audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)

        speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

        # print("Speak into your microphone.")
        speech_recognition_result = speech_recognizer.recognize_once_async().get()

        if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
            print("Recognized: {}".format(speech_recognition_result.text))
        elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
            print("No speech could be recognized: {}".format(speech_recognition_result.no_match_details))
        elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = speech_recognition_result.cancellation_details
            print("Speech Recognition canceled: {}".format(cancellation_details.reason))
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                print("Error details: {}".format(cancellation_details.error_details))
                print("Did you set the speech resource key and region values?")

