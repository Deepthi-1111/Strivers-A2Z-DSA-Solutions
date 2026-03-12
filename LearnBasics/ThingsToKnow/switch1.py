class Solution:
    def whichWeekDay(self, day):
        if day >= 1 and day < 8:
            match day:
                case 1:
                    d = 'Monday'
                case 2:
                    d = 'Tuesday'
                case 3:
                    d = 'Wednesday'
                case 4:
                    d = 'Thursday'
                case 5:
                    d = 'Friday'
                case 6:
                    d = 'Saturday'
                case 7:
                    d = 'Sunday'
            print(d)
        else:
            print('Invalid')





