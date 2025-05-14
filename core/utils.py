def set_dict_key(
    data: dict[str, str], target_key: str, possible_keys: list[str]
) -> None:
    for key in possible_keys:
        if value := data.get(key):
            item = {target_key: value}
            del data[key]
    data |= item
