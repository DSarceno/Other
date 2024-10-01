from src.utils import gmailAPI_authenticate

def main() -> None:
    gmailauth = gmailAPI_authenticate()

    service = gmailauth.get_authentication()

if __name__ in "__main__":
    main()