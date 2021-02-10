import csv 
from pydub import AudioSegment 

class TTSEngine:
    def __init__(csv_file, input_text):
        self.csv_file = csv_file 
        self.input_text = input_text
    
    def data_preparation(self):
        csvdata = open(self.csv_file)
        reader = csv.reader(csvdata)
        next(reader)

        data = {}

        for row in reader:
            data[row[0]] = row[1].replace(' ', '')

        return data

    def make_sounds(self):
        data = self.data_preparation
        data_keys = list(data.keys())
        data_values = list(data.values())

        text = self.input_text.split(" ")

        output_sentence = []

        for word in text:
            if word in data.values():
                sound_file = data_values.index(word)
                print(data_keys[sound_file])
                temp_sound = AudioSegment.from_file(f'sounds/{data_keys[sound_file]}', format="wav")
                output_sentence.append(temp_sound)


        base_sound = output_sentence[0]
        output_sentence.pop(0)

        for wave_file in output_sentence:
            print(wave_file)
            base_sound = base_sound.append(wave_file, crossfade=150)

        base_sound.export("temp.wav", format="wav")
        







