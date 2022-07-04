import random
import string


def generate_id(number_of_small_letters=4,
                number_of_capital_letters=2,
                number_of_digits=2,
                number_of_special_chars=2,
                allowed_special_chars=r"_+-!"):
    # 'T!uq6-b4Yq'
    result = []
    for item in range(number_of_small_letters):
        result.append(random.choice(list(string.ascii_lowercase)))
    for item in range(number_of_capital_letters):
        result.append(random.choice(list(string.ascii_uppercase)))
    for item in range(number_of_digits):
        result.append(random.choice(list(string.digits)))
    for item in range(number_of_special_chars):
        result.append(random.choice(list(allowed_special_chars)))
    random.shuffle(result)
    result = "".join(result)
    return result
