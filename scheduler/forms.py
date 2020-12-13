from django import forms


class AppointmentForm(forms.Form):
    AVAILABLE_TIMES = [
    ('10am', '10am'),
    ('11am', '11am'),
    ('12pm', '12pm'),
    ('1pm', '1pm'),
    ('2pm', '2pm'),
    ]

    schedule_time = forms.CharField(label="Please select desired time.", widget=forms.RadioSelect(choices=AVAILABLE_TIMES))

    def __init__(self, year=2020, month=1, day=1):
        super().__init__()
        AVAILABLE_TIMES = [
            ('10:30am', '10:30am'),
            ('12pm', '12pm'),
            ('1pm', '1pm'),
            ('2pm', '2pm'),
        ]
        self.schedule_time = forms.CharField(label="Please desired time.", widget=forms.RadioSelect(choices=AVAILABLE_TIMES))

    

