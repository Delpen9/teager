To install this package on your computer, run the command: 
  <b>pip install teager-py</b>
  
The teager-py package is a clean Python solution to performing a Teager operation.

<b>Dependencies</b>
  numpy
  
 <b> How to use </b>
  Within your Python CLI:
    
    // You must have numpy dependency installed and imported
    
    $ import numpy as numpy
    
    // Your input array (e.g. test_array) can be in the form of a list or numpy.ndarray
    // However, the output of the Teager operation will always be a numpy array
    
    $ test_array = numpy.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
    $ test_array = [[1,1,1], [1,1,1], [1,1,1]]
    
    $ from teager import Teager
    
    // There are two ways of running the Teager operation
    
    $ new_array = Teager(test_array, 'horizontal', 1)
    $ new_array = teager.Teager(test_array, 'horizontal', 1)
    
    // Display the output. It will be a numpy.ndarray with dtype = 'int'
    
    $ print(new_array)
    $ [[0], 
       [0], 
       [0]]
    
def Teager(teager_array, teager_angle_one: str, teager_one_spread: int, teager_angle_two: str = None, teager_two_spread: int = None, *positional_parameters, **keyword_parameters)
       

    
