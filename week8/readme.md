TODO: Reflect on what you learned this week and what is still unclear.
Goodreads Notes

def parseDateSafe(date):
    try:
        if (type(date) is str) and (date is not None):
            if type(date) is datetime.datetime:
            return date
            else:
                return parser.parse(date).date() 
        else:
            return dead_date.date()
    except Exception as e:
        print(date, e)
        return date

Notes:
Line 5: If a single object is passed to type(), the function returns its type.
Line 6: datetime.datetime is a combination of a date and a time. Attributes:
 year, month, day, hour, minute, second, microsecond, and tzinfo.
Line 10: This module offers a generic date/time string parser which is able to 
parse most known formats to represent a date and/or time.  
Line 13: datetime.date Class You can instantiate date objects from the date class.
 A date object represents a date (year, month and day)

 crt + / hashes out everything reuse to undo