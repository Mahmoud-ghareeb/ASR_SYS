from src.transcripe import TranscripeService
from src.llm import LLMService

import json

class PipeLine:
    def __init__(self, audio_path, output_file):
        self.whisper = TranscripeService()
        self.llm = LLMService()

        self.audio_path = audio_path
        self.output_file = output_file

    def run(self):
        text = self.whisper.transcribe(self.audio_path)
        output = self.llm.get_open_ai_response(text)

        self.save_to_json(output)

    def save_to_json(self, output):
        with open(self.output_file, 'w', encoding='utf-8') as f:
            json.dump(json.loads(output), f, ensure_ascii=False, indent=4)


if __name__ == "__main__":

    audio_path = "test_audios/6k_SBA_100_2.wav"
    output_path = "output.json"

    PipeLine(audio_path, output_path).run()

    print(f"output file saved to {output_path} GO check it!")
