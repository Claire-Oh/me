TODO: Reflect on what you learned this week and what is still unclear.
    the_countdown = []
    for i in range(start, stop, 1):
        response = ("message: {}".format(i))
        print(response)
        the_countdown.append(response)
        print(completion_message)
    return the_countdown