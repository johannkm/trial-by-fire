
def getMutants(id: int) -> [(str, [str])]:
    solution = [
        [  # problem 1
            ("""
  def find(self, string, target):
      c = -1
      for i in range(len(string)):
          if string[i] == target:
              c = i
      return c
        """, ["Test the case where there are duplicates of the target in the string"]),
            ("""
  def find(self, string, target):
      for i in range(len(string)):
          if string[i] == target:
              return i
      return 0
        """, ["Test the case where the target cannot be found","Test the case where the input is an empty string"]),
        ], 
        [  # problem 2

        ]
    ]

    return solution[id]

def getCanonical(id: int) -> str:
    solution = ["""
  def find(self, string, target):
      for i in range(len(string)):
          if string[i] == target:
              return i
      return -1

    """,
    """
  def product(self, a, b):
    return a * b

    """]

    return solution[id]

def getRunnable(id: int, tests: [str], algorithm: str) -> str:
    '''
    Convert a set of test cases into a runnable set of tests
    '''

    test_framework = [
        "results = {}",
        "class Test(object):",
        "  def __init__(self):",
        "    self.results = {}",
        "    for i in dir(self):",
        "      if i.startswith('test') and hasattr(getattr(self, i), '__call__'):",
        "        result = getattr(self, i)",
        "        self.results[result.__name__] = result()",
    ]

    # build runnable code
    lines: [str] = test_framework
    lines.append(algorithm)  # add algorithm
    for test in tests:  # add user tests
        lines.append(test)
    lines.append("results = Test().results")
    
    runnable: str = '\n'.join(lines)

    return runnable