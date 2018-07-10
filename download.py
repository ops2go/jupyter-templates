from google.colab import files

with open('example.txt', 'w') as f:
  f.write('some content')

files.download('example.txt')
