import gdown
import zipfile

url = 'https://drive.google.com/uc?id=1RtMSVh_KMv3pOHVs2qIAjCG9TggQaJnd'
output = './assets/objects.zip'
gdown.download(url, output, quiet=False)

with zipfile.ZipFile(output, 'r') as zip_ref:
  zip_ref.extractall(f'./assets/objects')