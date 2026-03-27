def sms_manager(sms: str) -> str:
    """Determines the length of the message
    and returns a result that can be sent
    """

    if len(sms) <= 160:
        return sms
    else:
        return sms[:160]
