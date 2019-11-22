import vamp
import librosa
import matplotlib.pyplot as plt
import numpy as np
import os
import pathlib
import csv
import pandas as pd

# brew install ffmpeg

def generate_melody(audio_file_path):
	# This is the audio file we'll be analyzing. 
	# You can download it here: http://labrosa.ee.columbia.edu/projects/melody/mirex05TrainFiles.zip
	audio_file = audio_file_path

	# This is how we load audio using Librosa
	audio, sr = librosa.load(audio_file, offset=30.0, duration=50.0, sr=44100, mono=True)

	# Exracting the melody using Melodia with default parameter values
	data = vamp.collect(audio, sr, "mtg-melodia:melodia")

	# print(data)

	# vector is a tuple of two values: the hop size used for analysis and the array of pitch values
	# Note that the hop size is *always* equal to 128/44100.0 = 2.9 ms
	hop, melody = data['vector']
	# print(hop)
	# print(melody)

	# timestamps = 8 * 128/44100.0 + np.arange(len(melody)) * (128/44100.0)

	# Extracting the melody using Melodia with custom parameter values
	# parameter values are specified by providing a dicionary to the optional "parameters" parameter:
	# params = {"minfqr": 100.0, "maxfqr": 800.0, "voicing": 0.2, "minpeaksalience": 0.0}

	# data = vamp.collect(audio, sr, "mtg-melodia:melodia", parameters=params)
	# hop, melody = data['vector']

	# Melodia returns unvoiced (=no melody) sections as negative values. So by default, we get:
	# plt.figure(figsize=(18,6))
	# plt.plot(timestamps, melody)
	# plt.xlabel('Time (s)')
	# plt.ylabel('Frequency (Hz)')
	# plt.show()

	# A clearer option is to get rid of the negative values before plotting
	# melody_pos = melody[:]
	# melody_pos[melody<=0] = None
	# plt.figure(figsize=(18,6))
	# plt.plot(timestamps, melody_pos)
	# plt.xlabel('Time (s)')
	# plt.ylabel('Frequency (Hz)')
	# plt.show()

	# Finally, you might want to plot the pitch sequence in cents rather than in Hz. 
	# This especially makes sense if you are comparing two or more pitch sequences 
	# to each other (e.g. comparing an estimate against a reference).
	# melody_cents = 1200*np.log2(melody/55.0)
	# melody_cents[melody<=0] = None
	# plt.figure(figsize=(18,6))
	# plt.plot(timestamps, melody_cents)
	# plt.xlabel('Time (s)')
	# plt.ylabel('Frequency (cents relative to 55 Hz)')
	# plt.show()
	return melody

file = open('./music/database_samples/data.csv', 'w', newline='')
file.close()

print("Starting......")
for genre in os.listdir(f'./music/database_samples/dest/'):
	for filename in os.listdir(f'./music/database_samples/dest/{genre}'):
		songname = './music/database_samples/dest/'+genre+'/'+filename
		melody = generate_melody(songname)   
		to_append = f'{filename} {genre}'
		for e in melody:
			to_append += f' {e}'
		file = open('./music/database_samples/data.csv', 'a', newline='')
		with file:
			writer = csv.writer(file)
			writer.writerow(to_append.split())
		file.close()
		print(filename+" in "+genre+" ...........Done.")
print("CSV generated")


