def format_time_in_sec(time_in_sec):
    secs = time_in_sec % 60
    mins = time_in_sec // 60
    return f"{_format_digit(mins)}:{_format_digit(secs)}"


def _format_digit(digit):
    if 0 <= digit <= 9:
        return f"0{digit}"
    else:
        return f"{digit}"
