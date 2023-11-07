"""
Метод: format
-------------
<   :  left-align text in the field
^   :  center text in the field
>   :  right-align text in the field
-------------
Перша цифра у номері пластикової картки означає, до якої платіжної системи вона належить. Усі картки Visa мають
номер, що починається на "4", Mastercard - на "5", а American Express - "3". Якщо картку видала не кредитна
організація, номер може починатися з інших цифр. "1" і "2" - це різні авіалінії, "3" - організації сфери
подорожей та розваг, «6» - мерчендайзингові компанії, «7» - паливні, «8» - підприємства у сфері
телекомунікацій, а «9» - це державні асигнації.
"""
pay_system = {
    5: "MasterCard",
    4: "Visa",
    3: "American Express"
}

card_numbers = ["5375414112345678", "4168757587879876", "216875758787987d"]


def is_valid_card(card: str) -> bool:
    return card.isdigit() and len(card) == 16

for card in card_numbers:
    string = 'Номер картки {:<8} Платіжна система: {:^16} картка валідна: {:>16}'
    print(string.format(card, pay_system.get(int(card[0]), 'Unknown'), str(is_valid_card(card))))