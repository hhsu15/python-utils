from dateutil import rrule
next_leap_year_on_saturday = list(
     rrule.rrule(
         rrule.YEARLY,
         count=1,
         byweekday=rrule.SA,
         bymonthday=29,
         bymonth=2,
     )
 )

print(next_leap_year_on_saturday)
