from dataclasses import dataclass

from iagocava_genshin.core.currency import calculate_total_pulls
from iagocava_genshin.core.pity import MAX_CHARACTER_PITY, BannerState
from iagocava_genshin.core.probability import five_star_probability


@dataclass(frozen=True)
class PullSummary:
    total_pulls: int
    current_pity: int
    is_guaranteed: bool
    pulls_until_hard_pity: int
    next_five_star_probability: float


def calculate_pull_summary(
    primogems: int,
    intertwined_fates: int,
    banner_state: BannerState,
) -> PullSummary:
    total_pulls = calculate_total_pulls(
        primogems,
        intertwined_fates,
    )

    return PullSummary(
        total_pulls=total_pulls,
        current_pity=banner_state.current_pity,
        is_guaranteed=banner_state.is_guaranteed,
        pulls_until_hard_pity=MAX_CHARACTER_PITY - banner_state.current_pity,
        next_five_star_probability=five_star_probability(banner_state.current_pity),
    )
