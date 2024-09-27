from src.extract_data import footballData
from src.utils import Others


def main() -> None:
    # archivo de configuracion
    config_name = 'config.yaml'
    others = Others()
    config = others.load_config(config_name)


    # instanciamos la clase
    fbd = footballData()

    ### ejecutamos los metodos ###
    # traemos los links
    links = fbd.getLinks()
    # traemos la data
    data = fbd.getData(links = links, df_name=config['data']['footballdata_xlsx'])



if __name__ == "__main__":
    main()
