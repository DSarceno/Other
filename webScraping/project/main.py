from src.extract_data import footballData
from src.utils import Others


def main() -> None:
    # archivo de configuracion
    config_name = 'config.yaml'
    others = Others()
    config = others.load_config(config_name)


    # instanciamos la clase
    fbd = footballData(all=True)

    ### ejecutamos los metodos ###
    # traemos los links
    print('Extrayendo los links de la página...')
    links = fbd.getLinks()
    print('Links extraídos exitosamente...')
    print(links)
    # traemos la data
    print('Extrayendo la data...')
    data = fbd.getData(links = links, df_name=config['data']['footballdata_xlsx'])
    print('Data extraída exitosamente...')
    print(data.info())


if __name__ == "__main__":
    main()
