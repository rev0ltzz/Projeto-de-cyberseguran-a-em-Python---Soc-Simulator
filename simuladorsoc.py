import random
from datetime import datetime, timedelta


USERS = ["admin", "guest", "root", "support", "analyst", "henrique"]
INTERNAL_IPS = ["192.168.1.10", "192.168.1.15", "10.0.0.5", "172.16.0.8"]
EXTERNAL_IPS = ["45.77.88.99", "185.220.101.1", "103.21.244.10", "201.55.44.12"]


def random_timestamp(base_time: datetime, seconds_offset: int) -> str:
    """Gera timestamp formatado com deslocamento em segundos."""
    event_time = base_time + timedelta(seconds=seconds_offset)
    return event_time.strftime("%Y-%m-%d %H:%M:%S")


def simulate_brute_force(base_time: datetime) -> list:
    """Gera eventos simulando brute force."""
    logs = []
    user = random.choice(["admin", "root", "support"])
    ip = random.choice(EXTERNAL_IPS)

    for i in range(5):
        timestamp = random_timestamp(base_time, i * 20)
        logs.append(f"{timestamp} FAILED_LOGIN user={user} ip={ip}")

    timestamp = random_timestamp(base_time, 120)
    logs.append(f"{timestamp} SUCCESS_LOGIN user={user} ip={ip}")
    return logs


def simulate_privileged_login_offhours(base_time: datetime) -> list:
    """Gera login privilegiado fora do horário comercial."""
    logs = []
    user = random.choice(["admin", "root"])
    ip = random.choice(EXTERNAL_IPS)

    event_time = base_time.replace(hour=23, minute=45, second=0)
    logs.append(f"{event_time.strftime('%Y-%m-%d %H:%M:%S')} SUCCESS_LOGIN user={user} ip={ip}")
    return logs


def simulate_account_creation(base_time: datetime) -> list:
    """Gera evento de criação suspeita de conta."""
    logs = []
    user = random.choice(["temp_admin", "backup_user", "svc_support"])
    ip = random.choice(INTERNAL_IPS)

    timestamp = random_timestamp(base_time, 10)
    logs.append(f"{timestamp} ACCOUNT_CREATED user={user} ip={ip}")
    return logs


def simulate_powershell_attack(base_time: datetime) -> list:
    """Gera execução suspeita de PowerShell."""
    logs = []
    user = random.choice(["support", "analyst", "admin"])
    ip = random.choice(INTERNAL_IPS)

    timestamp = random_timestamp(base_time, 15)
    logs.append(f"{timestamp} POWERSHELL_EXECUTION user={user} ip={ip}")
    logs.append(f"{timestamp} COMMAND user={user} ip={ip} detail=powershell -EncodedCommand SQBFAFgA")
    return logs


def simulate_c2_connection(base_time: datetime) -> list:
    """Gera conexão suspeita para possível C2."""
    logs = []
    user = random.choice(USERS)
    internal_ip = random.choice(INTERNAL_IPS)
    external_ip = random.choice(EXTERNAL_IPS)

    timestamp = random_timestamp(base_time, 30)
    logs.append(f"{timestamp} OUTBOUND_CONNECTION user={user} ip={internal_ip} destination={external_ip}")
    return logs


def simulate_persistence(base_time: datetime) -> list:
    """Gera evento de persistência simulada."""
    logs = []
    user = random.choice(["admin", "root", "support"])
    ip = random.choice(INTERNAL_IPS)

    timestamp = random_timestamp(base_time, 40)
    logs.append(f"{timestamp} PERSISTENCE_EVENT user={user} ip={ip} method=registry_run_key")
    return logs


def save_logs(file_path: str, logs: list) -> None:
    """Salva os logs em arquivo."""
    with open(file_path, "a", encoding="utf-8") as file:
        for log in logs:
            file.write(log + "\n")


def print_logs(logs: list) -> None:
    """Mostra os logs gerados na tela."""
    print("\nEventos gerados:")
    print("-" * 60)
    for log in logs:
        print(log)
    print("-" * 60)


def main():
    print("Simulador de Ataques para Treino de SOC")
    print("1 - Brute Force")
    print("2 - Login privilegiado fora do horário")
    print("3 - Criação de conta suspeita")
    print("4 - PowerShell suspeito")
    print("5 - Conexão suspeita para C2")
    print("6 - Persistência no sistema")

    choice = input("Escolha uma opção: ").strip()
    file_path = "attack_simulation_log.txt"
    base_time = datetime.now()

    if choice == "1":
        logs = simulate_brute_force(base_time)
    elif choice == "2":
        logs = simulate_privileged_login_offhours(base_time)
    elif choice == "3":
        logs = simulate_account_creation(base_time)
    elif choice == "4":
        logs = simulate_powershell_attack(base_time)
    elif choice == "5":
        logs = simulate_c2_connection(base_time)
    elif choice == "6":
        logs = simulate_persistence(base_time)
    else:
        print("Opção inválida.")
        return

    save_logs(file_path, logs)
    print_logs(logs)
    print(f"Os eventos foram salvos em: {file_path}")


if __name__ == "__main__":
    main()