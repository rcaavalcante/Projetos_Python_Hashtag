import pandas as pd
import requests
import io
# Link disponibilizado para download: https://drive.google.com/uc?authuser=0&id=1Ru7s-x3YJuStZK1mqr_qNqiHVvdHUN66&export=download

# CSV direto direto do no link

url = ['https://drive.google.com/uc?authuser=0&id=1Ru7s-x3YJuStZK1mqr_qNqiHVvdHUN66&export=download']
cotacao_df = requests.get(url)
print(cotacao_df)

