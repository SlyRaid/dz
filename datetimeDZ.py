from datetime import datetime


class SuperDate(datetime):

    def get_season(self):
        seasons = {
            1: "Winter",
            2: "Winter",
            3: "Spring",
            4: "Spring",
            5: "Spring",
            6: "Summer",
            7: "Summer",
            8: "Summer",
            9: "Autumn",
            10: "Autumn",
            11: "Autumn",
            12: "Winter"
        }

        return seasons[self.month]

    def get_time_of_day(self):
        time_of_day = {
            0: "Night",
            1: "Night",
            2: "Night",
            3: "Night",
            4: "Night",
            5: "Night",
            6: "Morning",
            7: "Morning",
            8: "Morning",
            9: "Morning",
            10: "Morning",
            11: "Morning",
            12: "Day",
            13: "Day",
            14: "Day",
            15: "Day",
            16: "Day",
            17: "Day",
            18: "Evening",
            19: "Evening",
            20: "Evening",
            21: "Evening",
            22: "Evening",
            23: "Evening"
        }

        return time_of_day[self.hour]


a = SuperDate(2024, 3, 19, 22)
print(a.get_season())
print(a.get_time_of_day())