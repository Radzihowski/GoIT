pay_system = {
    5: "MasterCard",
    4: "Visa",
    3: "American Express"
}

card_number = ["5375414112345678", "2346236356566475", "4168757587879876", "216875758787987d", "3345345O45879876"]

for card in card_number:
    print('Payment systeme {:<20} Is card is valid {:6}'.format(pay_system.get(int(card[0]), 'Unknown'),
                                                                str(card.isdigit() and len() == 16)))