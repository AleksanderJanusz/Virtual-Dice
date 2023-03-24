"""Dice simulator"""
from random import randint
from typing import Union


def _throw_inf() -> Union[list[int, int, int], bool, str]:
    """
    Factoring information into 3 parts
    :return: list of factored parts, Fals if invalid value, exit the program
    """
    num_of_throws = 0
    dice_type = 0
    extra_value = 0

    input_ = list(input("What throw you want to do?: "))
    if input_ == list("exit"):
        return "exit"
    if "D" not in input_:
        return False

    for id_, value_ in enumerate(input_):
        if value_ == "D":
            num_of_throws = input_[:id_]
            dice_type = input_[(id_ + 1):]

    if not num_of_throws:
        num_of_throws = ["1"]

    for id_, value_ in enumerate(dice_type):
        if value_ in ("+", "-"):
            extra_value = dice_type[id_:]
            dice_type = dice_type[:id_]
            try:
                extra_value = int("".join(extra_value))
            except ValueError:
                return False

    try:
        num_of_throws = int("".join(num_of_throws))
        dice_type = int("".join(dice_type))

    except ValueError:
        return False
    return [num_of_throws, dice_type, extra_value]


def main() -> None:
    """
    Instead of 'throwing' dice multiple times and adding extra value I change boundaries
    randint funktion to simulate it
    :return: None
    """
    print("Enter numbers of throws then D then type of dice and extra value. Ex 3D6+10")
    print("Types of dice: D3, D4, D6, D8, D10, D12, D20, D100, But you can use any.")
    while True:
        encoder_ = _throw_inf()
        if not encoder_:
            print("Something goes wrong. Try again")
            continue
        if encoder_ == "exit":
            return None
        throw_ = randint(encoder_[0], encoder_[0] * encoder_[1]) + encoder_[2]
        print(throw_)
        print("If you want to exit type 'exit'")


main()
