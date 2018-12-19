The teager-py package is a clean Python solution to performing a Teager operation.

<b>To install this package on your computer, run the command:</b><br> 
<pre>
     pip install teager-py
</pre>

<b>Dependencies: </b><br>
<pre>
     (Linux/macOS)
     sudo apt install python3-pip
     sudo apt install python3-numpy
     
     or 
     
     (Windows)
     pip install "numpy‑1.14.2+mkl‑cp36‑cp36m‑win32.whl"
     
</pre>
  
 <b> How to use within your Python CLI: </b>
    
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
       
<b>Teager Parameters</b>
<pre>
     def Teager(
     teager_array, 
     teager_angle_one: str, 
     teager_one_spread: int, 
     teager_angle_two: str = None, 
     teager_two_spread: int = None, 
     *positional_parameters, 
     **keyword_parameters)
     
<b>teager_array:</b> (list or numpy.ndarray()) - the input array of which will be manipulated by 
the Teager operation within the program

<b>teager_angle_one:</b> (str) - the radius from the current number in a loop. 
Within the teager operation: Teager(x<sub>t</sub>) = x<sub>t</sub><sup>2</sup> + x<sub>t - 1</sub>*x<sub>t + 1</sub>

</pre>

    
