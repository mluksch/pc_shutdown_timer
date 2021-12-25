def format_time_in_sec(time_in_sec):
    secs = _time_in_sec % 60
    mins = time_in_sec // 60
    return f"{_format_digit(mins)}:{_format_digit(secs)}"


def _format_digit(digit):
    if 0 <= digit <= 9:
        return f"{digit}"
    else:
        return f"0{digit}"
