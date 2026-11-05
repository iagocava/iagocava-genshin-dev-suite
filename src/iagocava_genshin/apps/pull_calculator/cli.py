from iagocava_genshin.core.calculator import PullSummary, calculate_pull_summary
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
    return ask_integer_in_range(
        "Constelação desejada (0 a 6): ",
        0,
        6,
    )


def ask_guaranteed() -> bool:
    while True:
        answer = input("Próximo 5★ está garantido? (s/n): ").strip().lower()

        if answer == "s":
            return True

        if answer == "n":
            return False

        print("Digite apenas 's' para sim ou 'n' para não.")


def ask_integer_in_range(
    prompt: str,
    minimum: int,
    maximum: int,
) -> int:
    """Solicita um inteiro dentro de um intervalo permitido."""
    if minimum > maximum:
        raise ValueError("O limite mínimo não pode superar o máximo.")

    while True:
        raw_value = input(prompt).strip()

        try:
            value = int(raw_value)
        except ValueError:
            print("Erro: digite um número inteiro válido.")
            continue

        if minimum <= value <= maximum:
            return value

        print(f"Erro: informe um número entre {minimum} e {maximum}.")


def format_pull_summary(
    summary: PullSummary,
    primogems: int,
    intertwined_fates: int,
) -> str:
    """Formata os resultados do Pull Calculator."""

    lines = [
        "=== IAGOCAVA | RESULTADO ===",
        "",
        "--- RECURSOS DISPONÍVEIS ---",
        f"Primogemas: {primogems}",
        f"Destinos Entrelaçados: {intertwined_fates}",
        f"Total de tiros: {summary.total_pulls}",
        "",
        "--- ESTADO DO BANNER ---",
        f"Pity atual: {summary.current_pity}",
        f"Tiros até o hard pity: {summary.pulls_until_hard_pity}",
        f"Garantia ativa: {'Sim' if summary.is_guaranteed else 'Não'}",
        f"Chance de 5★ no próximo tiro: {summary.next_five_star_probability:.2%}",
        "",
        "--- OBJETIVO DO PERSONAGEM ---",
        f"Constelação desejada: C{summary.target_constellation}",
        f"Cópias necessárias no total: {summary.total_copies_required}",
        f"Cópias possuídas: {summary.copies_owned}",
        f"Cópias restantes: {summary.copies_needed}",
    ]

    if summary.copies_needed == 0:
        lines.append("Situação da meta: JÁ ALCANÇADA")
    elif summary.total_pulls == 0:
        lines.append("Situação da meta: PENDENTE (SEM TIROS DISPONÍVEIS)")
    else:
        lines.append("Situação da meta: PENDENTE")

    lines.append(
        f"Probabilidade estimada de atingir a meta: {summary.goal_success_probability:.2%}"
    )

    return "\n".join(lines)


def ask_repeat() -> bool:
    """Pergunta se o usuário deseja realizar outro cálculo."""

    while True:
        answer = input("\nDeseja realizar outro cálculo? (s/n): ").strip().lower()

        if answer == "s":
            return True

        if answer == "n":
            return False

        print("Digite apenas 's' para sim ou 'n' para não.")


def run_calculation() -> None:
    print()
    print("=== IagoCava Genshin Pull Calculator ===")
    print()

    primogems = ask_non_negative_integer("Primogemas disponíveis: ")
    intertwined_fates = ask_non_negative_integer("Destinos Entrelaçados disponíveis: ")
    current_pity = ask_integer_in_range(
        "Pity atual (0 a 89): ",
        0,
        89,
    )

    is_guaranteed = ask_guaranteed()
    target_constellation = ask_constellation()
    copies_owned = ask_integer_in_range(
        "Cópias do personagem já possuídas (0 a 7): ",
        0,
        7,
    )

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
    print(
        format_pull_summary(
            summary=summary,
            primogems=primogems,
            intertwined_fates=intertwined_fates,
        )
    )


def main() -> None:
    """Executa a calculadora até o usuário solicitar a saída."""

    while True:
        run_calculation()

        if not ask_repeat():
            print()
            print("Encerrando o Pull Calculator.")
            print("Até a próxima!")
            return


if __name__ == "__main__":
    main()
