


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
    name = model.name
    name = name.strip()
    name = name.replace(' ', '_')
    name = name[0].upper()+name[1:]

    return name

def signature(model, format):
    """_summary_

    Args:
        model (ModelUnit): A Python object of a Crop2ML model Unit

    Returns:
        str: name
    """
    if format in ("py", "r", "f90"):
        return signature1(model)
    
    else: return signature2(model)