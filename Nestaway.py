lst_name = []


def nestaway():
    T = int(input())
    salary = 0
    booking_val = 0
    house_visit_val = 0
    total_house_visit_count = 0
    if 2 <= T <= 100:
        while T > 0:
            lst_name.append(input())
            T = T - 1
        rating = float(input())

        if 1.0 <= rating <= 5.0:

            for value in lst_name:
                details = value.split(',')

                name = details[0].strip()[1:-1]
                attribute = details[1].strip()[1:-1]
                val = int(details[2].strip())
                if name == 'Booking' and attribute in ['last bed', 'any bed'] and 1000 <= val <= 100000:
                    if attribute == 'last bed':
                        booking_val = booking_val + 0.15 * val

                    if attribute == 'any bed':
                        booking_val = booking_val + (0.1 * val)

                if name == 'House visit' and attribute in ['new lead', 'existing lead'] and 1 <= val <= 100:
                    if attribute == 'new lead':
                        total_house_visit_count = total_house_visit_count + val
                        house_visit_val = house_visit_val + (1000 * val)

                    if attribute == 'existing lead':
                        total_house_visit_count = total_house_visit_count + val
                        house_visit_val = house_visit_val + (700 * val)

            if total_house_visit_count > 0:

                if total_house_visit_count > 30:
                    house_visit_val = (1.10 * house_visit_val)
                elif 30 >= total_house_visit_count >= 10:

                    house_visit_val = (1.05 * house_visit_val)
                else:
                    house_visit_val = house_visit_val + 0

                if rating > 4.5:
                    salary = house_visit_val + booking_val + (0.50 * (house_visit_val + booking_val))
                else:

                    salary = house_visit_val + booking_val
            else:
                salary = booking_val

    print(int(round(salary)))


nestaway()
