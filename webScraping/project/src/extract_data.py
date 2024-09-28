import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from datetime import datetime


class footballData:
    def __init__(self, all : bool = True) -> None:
        self.all = all
        self.url_base = 'https://www.football-data.co.uk/'
        self.url = self.url_base + 'downloadm.php'
    

    def getLinks(self) -> list[str]:
        # realizamos la solicitud de informacion
        try:
            # tomamos la informacion de la url
            response = requests.get(self.url)
            
            # parseamos la info
            soup = BeautifulSoup(response.text, 'html.parser')
        except Exception as e:
            print(e)


        # tomamos los links del html
        links = soup.find_all('a', href=True)

        # donde se almacenaran todos los links utiles
        useful_links = []

        # dependiendo si necesitamos toda la data o solo la de la ultima temporada
        if self.all == True:
            pattern = 'all-euro-data'
        else:
            today = datetime.today()
            pattern = f'all-euro-data-{today.year}-{today.year + 1}'
        

        # tomamos unicamente los links que nos son utiles
        for link in links:
            l = link['href']
            match1 = re.search(pattern, l)
            if match1:
                useful_links.append(self.url_base + l)


        return useful_links
    
    def getData(self, links : list[str], df_name : str) -> pd.DataFrame:
        # dependiendo del valor de all llamamos la informacion
        if self.all == True:
            # donde se almacenaran los dataframes
            dfs = []

            # llamamos toda la info de cada link/excel
            # por ello el sheet_name = None
            for link in links:
                all_sheets = pd.read_excel(link, sheet_name=None)
                for _, df in all_sheets.items():
                    dfs.append(df)

            # unimos toda la informacion
            df = pd.concat(dfs, ignore_index=True)

            # exportamos la data
            df.to_excel(df_name, index=False)

            return df
        else:
            # exportamos la info de la ultima temporada
            df = pd.read_excel(links[0], sheet_name=None)

            # importamos el dataframe con toda la informacion
            fulldf = pd.read_excel(df_name)

            # concatenamos ambos dataframes
            fulldf = pd.concat([fulldf, df], ignore_index=True)

            # quitamos los registros duplicados
            fulldf = fulldf.drop_duplicates(subset=['Div', 'Date', 'Time', 'HomeTeam', 'AwayTeam'], keep='first')

            # exportamos la data en el mismo archivo que antes sobreescribiendolo
            fulldf.to_excel(df_name, index=False)

            return fulldf





