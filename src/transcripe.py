from faster_whisper import WhisperModel


class TranscripeService:

    def __init__(self, model_size="large-v2", device="cuda", compute_type="float16"):
        self.device = device
        self.model_size = model_size
        self.compute_type = compute_type

    def transcribe(self, file):

        model = WhisperModel(self.model_size, device=self.device, compute_type=self.compute_type)
        segments, info = model.transcribe(file, beam_size=5)

        print("Detected language '%s' with probability %f" % (info.language, info.language_probability))

        text = ""
        for segment in segments:
            # print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))

            text += segment.text + " "

        return text