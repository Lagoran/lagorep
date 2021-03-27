'''
Crafting a docstring
You've decided to write the world's greatest open-source natural language processing Python package. It will revolutionize working with free-form text, the way numpy did for arrays, pandas did for tabular data, and scikit-learn did for machine learning.

The first function you write is count_letter(). It takes a string and a single letter and returns the number of times the letter appears in the string. You want the users of your open-source package to be able to understand how this function works easily, so you will need to give it a docstring. Build up a Google Style docstring for this function by following these steps.

Instructions 1/4
25 XP
Copy the following string and add it as the docstring for the function: Count the number of times `letter` appears in `content`.
'''

# Add a docstring to count_letter()
def count_letter(content, letter):
  """Count the number of times `letter` appears in `content`.

  # Add a Google style arguments
  Args:
      content (str): The string to search.
      letter (str): The letter to search for.

  # Add retruns section
  Returns:
      int

  # Add a section detailing what errors might be raised
  Raises:
    ValueError: If `letter` is not a one-character string.
  """
  if (not isinstance(letter, str)) or len(letter) != 1:
    raise ValueError('`letter` must be a single character string.')
  return len([char for char in content if char == letter])


# Get the docstring with an attribute of count_letter()
docstring = count_letter.__doc__

border = '#' * 28
print('{}\n{}\n{}'.format(border, docstring, border))


#2nd option to call for the docstring of the function
import inspect

# Get the docstring with a function from the inspect module
docstring = inspect.getdoc(count_letter)

border = '#' * 28
print('{}\n{}\n{}'.format(border, docstring, border))

#3rd option to call for docstrings
def build_tooltip(function):
    """Create a tooltip for any function that shows the
    function's docstring.

    Args:
      function (callable): The function we want a tooltip for.

    Returns:
      str
    """
    # Use 'inspect' to get the docstring
    docstring = inspect.getdoc(function)
    border = '#' * 28
    return '{}\n{}\n{}'.format(border, docstring, border)


print(build_tooltip(count_letter))
print(build_tooltip(range))
print(build_tooltip(print))
print(build_tooltip(build_tooltip))

#and another option for the last print print(build_tooltip(build_tooltip))
docstring = inspect.getdoc(build_tooltip)

border = '#' * 28
print('{}\n{}\n{}'.format(border, docstring, border))

#and the straightest way
print(build_tooltip.__doc__)