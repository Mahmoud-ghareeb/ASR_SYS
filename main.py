from src.transcripe_service import TranscripeService
from src.llm_service import LLMService

import json

class PipeLine:
    """
    Pipeline to run the asr system

    there are 2 available llms:
    1- open_ai
    2- sambanova

    you can switch between them using the use parameter

    example:
        1- using open ai:     PipeLine(audio_path, output_path, use="open_ai").run()

        2- using sambanova:   PipeLine(audio_path, output_path, use="sambanova").run()

    output a json file named: output.json
    """

    def __init__(self, audio_path, output_file, use="open_ai"):
        self.whisper = TranscripeService()
        self.llm = LLMService()

        self.audio_path = audio_path
        self.output_file = output_file
        self.use = use

    def run(self):
        text = self.whisper.transcribe(self.audio_path)

        if self.use == "open_ai":
            output = self.llm.get_open_ai_response(text)
        else:
            output = self.llm.get_sambanova_response(text)

        self.save_to_json(output)

    def save_to_json(self, output):
        
        try:
            if isinstance(output, str):
                output = output.replace("'", '"').replace('"{', '{').replace('}"', '}')
                output = json.loads(output)
            elif not isinstance(output, dict):
                raise ValueError("Output is not in a valid format (string or dictionary).")
        except:
            print("error in json decoding, use open_ai for no errors :)")

        with open(self.output_file, 'w', encoding='utf-8') as f:
            json.dump(output, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":

    audio_path = "test_audios/6k_SBA_100_2.wav"
    output_path = "output.json"

    PipeLine(audio_path, output_path, use="sambanova").run()

    print(f"output file saved to {output_path} GO check it!")
