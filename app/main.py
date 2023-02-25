from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    count_mask_error = 0
    for people in friends:
        try:
            cafe.visit_cafe(people)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            count_mask_error += 1

    if count_mask_error > 0:
        return f"Friends should buy {count_mask_error} masks"
    return f"Friends can go to {cafe.name}"
