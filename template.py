import re

sections = ['Chain complexes',
'LES in homology',
'Chain homotopy',
'Mapping Cones and Cylinders',
'Resolutions',
'Derived functors',
'Exact functors',
'Categories, functors, and natural transformations',
'Adjunctions',
'Adjunctions and the Yoneda lemma',
'Adjunctions and exactness',
'Balancing Tor and Ext',
'Universal coefficient theorem',
'Homological dimension',
'Local rings, Koszul complexes',
'Gorenstein rings',
'Group cohomology',
'Local cohomology'
]


# https://github.com/jpvanhal/inflection/blob/master/inflection.py
def camelize(string, uppercase_first_letter=True, separator=' '):
    """
    Convert strings to CamelCase.

    Examples::

        >>> camelize("device_type")
        "DeviceType"
        >>> camelize("device_type", False)
        "deviceType"

    :func:`camelize` can be though as a inverse of :func:`underscore`, although
    there are some cases where that does not hold::

        >>> camelize(underscore("IOError"))
        "IoError"

    :param uppercase_first_letter: if set to `True` :func:`camelize` converts
        strings to UpperCamelCase. If set to `False` :func:`camelize` produces
        lowerCamelCase. Defaults to `True`.
    """
    regexpr = r"(?:^|" + separator + r")(.)"
    if uppercase_first_letter:
        return re.sub(regexpr, lambda m: m.group(1).upper(), string)
    else:
        return string[0].lower() + camelize(string)[1:]
