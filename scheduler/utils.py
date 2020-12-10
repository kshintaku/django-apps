from datetime import datetime, timedelta
from .models import Event
import calendar


class Calendar:
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        month_name = ["January", "February", "March", "April",
            "May", "June", "July", "August",
            "September", "October", "November", "December"]
        self.str_month = month_name[self.month-1]

    def format_month(self):
        month_header = "".join(('<div class="month-header">',
            f'<span class="month">{self.str_month} {self.year}</span>',
            '</div>'))
        return month_header
    
    day_header = "".join(('<div class="days-of-week">',
        '<span class="sun">Sunday</span>',
        '<span class="mon">Monday</span>',
        '<span class="tue">Tuesday</span>',
        '<span class="wed">Wednesday</span>',
        '<span class="thu">Thursday</span>',
        '<span class="fri">Friday</span>',
        '<span class="sat">Saturday</span>',
        '</div>'))
