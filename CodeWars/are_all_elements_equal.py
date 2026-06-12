def eq_all(iterable):
    iterator = iter(iterable)
    try:
        first = next(iterator)
    except StopIteration:
        return True  # Colección vacía
    
    return all(element == first for element in iterator)