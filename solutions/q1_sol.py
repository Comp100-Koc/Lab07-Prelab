def get_value(person, field):
    # field may be nested, like 'address.zip_code'
    value = person
    for part in field.split('.'):
        if isinstance(value, dict):
            value = value.get(part)
        else:
            return None
    return value

def custom_sort(people, primary, secondary):
    def compare(a, b):
        key_a = (get_value(a, primary), get_value(a, secondary), a.get("name"))
        key_b = (get_value(b, primary), get_value(b, secondary), b.get("name"))
        if key_a < key_b:
            return -1
        elif key_a > key_b:
            return 1
        else:
            return 0

    # Implement insertion sort (stable)
    result = people[:]
    n = len(result)
    for i in range(1, n):
        cur = result[i]
        j = i - 1
        while j >= 0 and compare(cur, result[j]) < 0:
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = cur
    return result
