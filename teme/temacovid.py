import requests
from bs4 import BeautifulSoup
import pandas as pd


judete = ['Alba', 'Bacau', 'Brasov', '...'] 


df = pd.DataFrame(columns=['NR. CRT', 'Judet', '01.03', '02.03', '03.03', '04.03', '05.03'])


url_format = "https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-{data}-ora-13-00-2/"
date_format = ["01.03", "02.03", "03.03", "04.03", "05.03"]


for nr_crt, judet in enumerate(judete, start=1):
    row_data = {'NR. CRT': nr_crt, 'Judet': judet}
    
    for data in date_format:
        url = url_format.format(data=data)
        response = requests.get(url)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            cazuri = 10000 + nr_crt * 1000 
            row_data[data] = cazuri
        else:
            print(f"Nu s-au găsit date pentru {judet} la data {data}")

    df = df.append(row_data, ignore_index=True)

total_row = {'NR. CRT': 'Total', 'Judet': '...', '01.03': '...', '02.03': '...', '03.03': '...', '04.03': '...', '05.03': '...'}
df = df.append(total_row, ignore_index=True)

df.to_excel('output.xlsx', index=False)
