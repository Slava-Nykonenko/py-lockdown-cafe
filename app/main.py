from app.errors import NotWearingMaskError, VaccineError
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    counter, vaccine_issue, mask_counter = 0, 0, 0
    for person in friends:
        try:
            cafe.visit_cafe(person)
        except VaccineError as error:
            vaccine_issue += 1
            print(error)
        except NotWearingMaskError as error:
            mask_counter += 1
            print(error)
        else:
            counter += 1
    if vaccine_issue != 0:
        return "All friends should be vaccinated"
    elif mask_counter != 0:
        return f"Friends should buy {mask_counter} masks"
    elif counter == len(friends):
        return f"Friends can go to {cafe.name}"
