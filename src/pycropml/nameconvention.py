def signature1(model):
    """_summary_

    Args:
        model (ModelUnit): A Python object of a Crop2ML model Unit

    Returns:
        str: name
    """
    name = model.name
    name = name.strip()
    name = name.replace(' ', '_').lower()

    return name

def signature2(model):
    """_summary_

    Args:
        model (ModelUnit): A Python object of a Crop2ML model Unit

    Returns:
        str: name
    """
    return signature2_from_name(model.name)


def signature2_from_name(name):
    n = name.strip()
    n = n.replace(' ', '_')
    n = n[0].upper() + n[1:]
    return n


def signature(model, format):
    """_summary_

    Args:
        model (ModelUnit): A Python object of a Crop2ML model Unit

    Returns:
        str: name
    """
    if format in ("py", "r", "f90"):
        return signature1(model)
    else:
        return signature2(model)