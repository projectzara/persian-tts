import csv 
from pydub import AudioSegment 

class TTSEngine:
    def __init__(self, csv_file):
        self.csv_file = csv_file 
    
    def data_preparation(self):
        csvdata = open(self.csv_file)
        reader = csv.reader(csvdata)
        next(reader)

        data = {}

        for row in reader:
            data[row[0]] = row[1].replace(' ', '')

        return data

    def make_sounds(self, input_text):
        data = self.data_preparation()
        data_keys = list(data.keys())
        data_values = list(data.values())

        text = input_text.split(" ")

        output_sentence = []

        for word in text:
            if word in data.values():
                sound_file = data_values.index(word)
                temp_sound = AudioSegment.from_file(f'sounds/{data_keys[sound_file]}', format="wav")
                output_sentence.append(temp_sound)
            else:
                pass 


        base_sound = output_sentence[0]
        output_sentence.pop(0)

        for wave_file in output_sentence:
            base_sound = base_sound.append(wave_file, crossfade=150)

        base_sound.export("temp.wav", format="wav")
        
if __name__ == '__main__':
    engine = TTSEngine("sounds/sounds.csv")
    while True:
        input_text = input("Type a Persian string: ")
        engine.make_sounds(input_text)