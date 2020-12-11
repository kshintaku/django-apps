from datetime import date


class Calendar:
    day_name = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]
    day_name_short = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]

    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        month_name = [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December",
        ]
        self.str_month = month_name[self.month - 1]
        self.month_start = date(self.year, self.month, 1).weekday()
        self.month_header = "".join(
            (
                '<div class="month-header">',
                f'<span class="month">{self.str_month} {self.year}</span>',
                "</div>",
            )
        )
        if self.month + 1 > 12:
            self.num_days = (
                date(self.year + 1, (self.month + 1) % 12, 1)
                - date(self.year, self.month, 1)
            ).days
        else:
            self.num_days = (
                date(self.year, self.month + 1, 1) - date(self.year, self.month, 1)
            ).days

    def format_month(self):
        cal = self.month_header
        cal += self.create_header()
        num_weeks = int(((self.month_start + self.num_days) / 7) + 1)
        offset = self.month_start
        day_count = 1
        for x in range(num_weeks):
            cal += "".join((f'<div class="week week-{x+1}">'))
            for x in range(7):
                if offset != 0:
                    cal += "".join(
                        (f'<span class="day {self.day_name_short[x]}"></span>')
                    )
                    offset -= 1
                elif day_count <= self.num_days:
                    cal += "".join(
                        (
                            f'<span class="day {self.day_name_short[x]}">{day_count}</span>'
                        )
                    )
                    day_count += 1
                else:
                    cal += "".join(
                        (f'<span class="day {self.day_name_short[x]}"></span>')
                    )
            cal += "</div>"
        return cal

    def create_header(self):
        day_header = '<div class="days-of-week">'
        for x in range(len(self.day_name)):
            day_header += "".join(
                (
                    f'<span class="day {self.day_name_short[x]}">{self.day_name[x]}</span>'
                )
            )
        day_header += "</div>"
        return day_header
