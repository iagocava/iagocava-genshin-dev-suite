from iagocava_genshin.core.calculator import calculate_pull_summary
from iagocava_genshin.core.models import CharacterGoal
from iagocava_genshin.core.pity import BannerState


def ask_non_negative_integer(message: str) -> int:
    while True:
        try:
            value = int(input(message))

            if value < 0:
                print("Digite um valor igual ou maior que zero.")
                continue

            return value
        except ValueError:
            print("Digite um número inteiro válido.")


def ask_constellation() -> int:
    while True:
        value = ask_non_negative_integer("Constelação desejada (0 a 6): ")

        if value <= 6:
            return value

        print("A constelação deve estar entre C0 e C6.")


def ask_guaranteed() -> bool:
    while True:
        answer = input("Próximo 5★ está garantido? (s/n): ").strip().lower()

        if answer == "s":
            return True

        if answer == "n":
            return False

        print("Digite apenas 's' para sim ou 'n' para não.")


def main() -> None:
    print()
    print("=== IagoCava Genshin Pull Calculator ===")
    print()

    primogems = ask_non_negative_integer("Primogemas disponíveis: ")
    intertwined_fates = ask_non_negative_integer("Destinos Entrelaçados disponíveis: ")
    current_pity = ask_non_negative_integer("Pity atual: ")
    is_guaranteed = ask_guaranteed()
    target_constellation = ask_constellation()
    copies_owned = ask_non_negative_integer("Cópias do personagem já possuídas: ")

    try:
        banner_state = BannerState(
            current_pity=current_pity,
            is_guaranteed=is_guaranteed,
        )

        character_goal = CharacterGoal(
            target_constellation=target_constellation,
            copies_owned=copies_owned,
        )

        summary = calculate_pull_summary(
            primogems=primogems,
            intertwined_fates=intertwined_fates,
            banner_state=banner_state,
            character_goal=character_goal,
        )

    except ValueError as error:
        print()
        print(f"Erro: {error}")
        return

    print()
    print("=== Resultado ===")
    print(f"Pulls disponíveis: {summary.total_pulls}")
    print(f"Pity atual: {summary.current_pity}")
    print(f"Pulls até o hard pity: {summary.pulls_until_hard_pity}")
    print(f"Próximo 5★ garantido: {'Sim' if summary.is_guaranteed else 'Não'}")
    print(f"Chance estimada do próximo 5★: {summary.next_five_star_probability:.2%}")
    print()
    print(f"Meta: C{summary.target_constellation}")
    print(f"Cópias necessárias no total: {summary.total_copies_required}")
    print(f"Cópias já possuídas: {summary.copies_owned}")
    print(f"Cópias restantes: {summary.copies_needed}")
    print(f"Probabilidade estimada de atingir a meta: {summary.goal_success_probability:.2%}")


if __name__ == "__main__":
    main()
