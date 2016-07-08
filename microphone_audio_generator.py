
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
audio = r.listen(source)
os.chdir(audio)
    for video in glob.glob(extension):
        wav_filename = os.path.splitext(os.path.basename(video))[0] + '.wav'
        AudioSegment.from_file(video).export(wav_filename, format='wav')


preddf = pd.DataFrame(predictions, columns=face_data.columns[:-1])
results = pd.DataFrame(columns=['RowId', 'Location'])

for i in range(lookup.shape[0]):
    d = lookup.ix[i, :]
    r = pd.Series([d['RowId'], preddf.ix[d['ImageId']-1, :][d['FeatureName']]],
                  index=results.columns)
    results = results.append(r, ignore_index=True)

results['RowId'] = results['RowId'].astype(int)
results.to_csv('predictions.csv', index=False)