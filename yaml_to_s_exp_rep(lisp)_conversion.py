import yaml

def to_s_expression(data, prefix="yaml"):
    if isinstance(data, dict):
        result = []
        for k, v in data.items():
            tag = k.replace('$', '')
            if isinstance(v, list):
                list_items = ' '.join(to_s_expression(item, prefix) for item in v)
                result.append(f'({prefix}:{tag} {list_items})')
            else:
                result.append(f'({prefix}:{tag} {to_s_expression(v, prefix)})')
        return '\n'.join(result)
    elif isinstance(data, list):
        return ' '.join(to_s_expression(item, prefix) for item in data)
    elif isinstance(data, str):
        import re
        if re.match(r'^\d{4}-\d{2}-\d{2}$', data):
            y, m, d = data.split('-')
            return f'(make-date {int(y)} {int(m)} {int(d)})'
        return '"' + data.replace('"', '\\"') + '"'
    elif isinstance(data, bool):
        return '#t' if data else '#f'
    elif data is None:
        return 'null'
    else:
        return str(data)


def main():
    with open("clmul.yaml", "r") as f:
        yaml_obj = yaml.safe_load(f)
    print(f"({to_s_expression(yaml_obj)})")

if __name__ == '__main__':
    main()
