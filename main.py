# Hey KAI!
# Voice assistant for PCs

import sounddevice as sd
import openwakeword
from openwakeword.model import Model

CHUNK = 1280
WAKEWORD = "hey_jarvis"   # placeholder, poi sarà models/hey_kai.onnx


def wait_for_wakeword(oww, threshold=0.5, debug=False):
    with sd.InputStream(samplerate=16000, channels=1, dtype="int16",
                        blocksize=CHUNK) as stream:
        while True:
            audio, _ = stream.read(CHUNK)
            scores = oww.predict(audio[:, 0])
            if debug:
                print({k: round(float(v), 2) for k, v in scores.items()}, end="\r")
            for name, score in scores.items():
                if score > threshold:
                    oww.reset()
                    return name


if __name__ == "__main__":
    openwakeword.utils.download_models()   # scarica solo se mancano
    oww = Model(wakeword_models=[WAKEWORD], inference_framework="onnx")

    print("In ascolto... di' 'hey jarvis' (Ctrl+C per uscire)")
    while True:
        name = wait_for_wakeword(oww, debug=True)
        print(f"\nRilevato: {name}")