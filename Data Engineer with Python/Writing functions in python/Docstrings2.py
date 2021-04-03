'''
Reviewing your co-worker's code
Your co-worker is asking you to review some code that they've written and give them some tips on how to get it ready for production. You know that having a docstring is considered best practice for maintainable, reusable functions, so as a sanity check you decide to run this has_docstring() function on all of their functions.
'''

def has_docstring(func):
  """Check to see if the function
  `func` has a docstring.

  Args:
    func (callable): A function.

  Returns:
    bool
  """
  return func.__doc__ is not None
