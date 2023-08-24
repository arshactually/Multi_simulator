def takeRGBValues():
     print("Enter the values of channels:")
     channel1 = int(input(
       "Enter the value of 1st Channel: "))
     
     channel2 = int(input(
       "Enter the value of 2nd Channel: "))
     channel3 = int(input(
       "Enter the value of 3rd Channel: "))
     return channel1, channel2, channel3 

# def takeRGBValues():
#     print("Enter the values of channels:")
#     channels = []
    
#     for i in range(3):
#         channel_value = int(input(f"Enter the value of Channel {i+1}: "))
#         channels.append(channel_value)
    
#     return tuple(channels)


def takeRGBValues():
    print("Enter the values of channels:")
    channels = []

    for i in range(3):
        channel_value = int(input(f"Enter the value of Channel {i+1}: "))
        if channel_value < 0 or channel_value > 255:
            raise ValueError("Channel values should be between 0 and 255")
        channels.append(channel_value)

    return bytes(channels)