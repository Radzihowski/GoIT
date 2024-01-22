# str.strip(): Видаляє всі пробіли та символи нового рядка з початку і кінця строки.

# Валідування номерів телефону

phone_storage = ["380669640547", "0637306465    ", " 420961935171", "632643973", "050832520 ", "38066964O547",
                 "00000000000", "480730283918", "597632643973", "0986223575", "37(029)7947963",
                 "+42(050)123-32-34", "38986223575", "38(950)123 32 34", "38(050)123 32 3b"]

codes_operators = {"067", "068", "096", "097", "098", "050", "066", "095", "099", "063", "073", "093", "029"}


# 38 - UA, 42 - IT,  37 - GER 48 - PL

def clean_up_phone(phone):
    return (phone.strip()
            .removeprefix('+')
            .replace('(', '')
            .replace(')', '')
            .replace('-', '')
            .replace(' ', ''))


def is_valid_phone(phone):
    if phone.isdigit():
        if len(phone) == 12:
            if phone[2] == '0':
                return phone[2:5] in codes_operators
            return False
        if len(phone) == 10:
            return phone[:3] in codes_operators
        return False

def phone_by_country(list_of_phones):
    phone_by_country_dict = dict()
    for i in range(len(list_of_phones)):
        phone = clean_up_phone(list_of_phones[i])
        if phone.startswith('38'):
            phone_by_country_dict.setdefault('UA', []).append(phone)
        if phone.startswith('32'):
            phone_by_country_dict.setdefault('IT', []).append(phone)
        if phone.startswith('37'):
            phone_by_country_dict.setdefault('GER', []).append(phone)
        if phone.startswith('48'):
            phone_by_country_dict.setdefault('PL', []).append(phone)



for phone in phone_storage:
    print(clean_up_phone(phone))
