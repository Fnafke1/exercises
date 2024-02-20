def make_path(parts):
    if len(parts) == 0:
        return ""

    result = f"{parts[0]}"

    for i in range(1, len(parts)):
        result += f"/{parts[i]}"
    return result
