The teager-py package is a clean Python solution to performing a Teager operation on a raw signal in the form of a 1-Dimensional or 2-Dimensional array.

<b>To install this package on your computer, run the command:</b><br> 
<pre>
     $ pip install teager-py
     
     or
     
     $ git clone https://github.com/Delpen9/teager.git
</pre>

<b>Dependencies: </b><br>
<pre>
     (Linux/macOS)
     $ sudo apt install python3-pip
     $ sudo apt install python3-numpy
     
     or 
     
     (Windows)
     $ pip install "numpy‑1.14.2+mkl‑cp36‑cp36m‑win32.whl"
     
</pre>
  
 <b> How to use within your Python CLI: </b>
    
    // You must have numpy dependency installed and imported
    
    $ import numpy as numpy
    
    // Your input array (e.g. test_array) can be in the form of a list or numpy.ndarray
    // However, the output of the Teager operation will always be a numpy array
    
    $ test_array = numpy.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
    $ test_array = [[1,1,1], [1,1,1], [1,1,1]]
    
    $ from teager_py import Teager
    
    // There are two ways of running the Teager operation
    
    $ new_array = Teager(test_array, 'horizontal', 1)
    $ new_array = teager_py.Teager(test_array, 'horizontal', 1)
    
    // Display the output. It will be a numpy.ndarray with dtype = 'int'
    
    $ print(new_array)
    $ [[0], 
       [0], 
       [0]]
       
<b>Teager Parameters:</b>
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

<b>teager_angle_one:</b> (str) - can be any of the following options within the list:

     <b> ['horizontal', 'vertical', 'diagonal-right', 'diagonal-left'] </b>
     
     <b> horizontal </b> - the teager operation is looping through a row of the array, 
      whether it is 1-dimensional or 2-dimensional (matrix).
      
     <b> vertical </b> - the teager operation is looping through the columns of the array,
      meaning the array is 2-dimensional (matrix).
      
     <b> diagonal-right </b> - the teager operation is looping through both the columns and rows of 
      the array at an angle of 45 degrees (x<sub>t+1</sub>) and 225 degrees (x<sub>t-1</sub>) 
      about the current value in a loop.
     
     <b> diagonal-left </b> - the teager operation is looping through both the columns and rows of
      the array at an angle of 135 degrees (x<sub>t+1</sub>) and 315 degrees (x<sub>t-1</sub>) 
      about the current value in a loop.
     
<b>teager_one_spread:</b> (int) - the radius from the current number in a loop. 
The teager spread can be either 1 or 2. 

     The teager operation: 
          <b>Teager(x<sub>t</sub>) = x<sub>t</sub><sup>2</sup> + x<sub>t-1</sub> * x<sub>t+1</sub></b>
     
     The 1 within the t - 1 and t + 1 is the radius such that <em>(with r being the radius)</em>:
          <b>Teager(x<sub>t</sub>) = x<sub>t</sub><sup>2</sup> + x<sub>t-r</sub> * x<sub>t+r</sub></b>

<b>teager_angle_two:(optional) </b> (str) - can be any of the following options within the list:

     <b> [None, 'horizontal', 'vertical', 'diagonal-right', 'diagonal-left'] </b>
     
      This field can be left blank as seen within the 'How to use within your Python CLI' section.
     
<b>teager_two_spread:(should only exist when there is a teager_angle_two parameter) </b> (int) - the radius 
from the current number in a loop. The teager spread can be either 1 or 2. 

     This is the same as teager_one_spread, but instead of changing the radius of teager_angle_one, 
     it determines the radius of teager_angle_two.

</pre>

<b>Code Snippets:</b>
<pre>

# Horizontal Teager
def horizontal_teager(teager_array, teager_spread: int, teager_array_dimension: str):
    if (teager_array_dimension == '1D' or teager_array_dimension == '1d'): 
        i = teager_array[teager_spread:-teager_spread] * teager_array[teager_spread:-teager_spread]
        j = teager_array[(teager_spread - 1):(-teager_spread - 1)] * teager_array[(teager_spread + 1):None if (-teager_spread + 1) == 0 else (-teager_spread + 1)]
        return i - j

    elif (teager_array_dimension == '2D' or teager_array_dimension == '2d'): 
        temp_array = numpy.array([ [None] * (len(teager_array[0]) - 2 * teager_spread) ] * len(teager_array))
        for row in range(len(teager_array)):
            i = teager_array[row][teager_spread:-teager_spread] * teager_array[row][teager_spread:-teager_spread]
            j = teager_array[row][(teager_spread - 1):(-teager_spread - 1)] * teager_array[row][(teager_spread + 1):None if (-teager_spread + 1) == 0 else (-teager_spread + 1)]
            temp_array[row] = i - j
        return temp_array

    else:
        try:
            raise Exception("Input a valid teager_array_dimension: '1d', '1D', '2d', or '2D'.")
        except Exception:
            raise

# Vertical Teager
def vertical_teager(teager_array, teager_spread: int):
    temp_array = numpy.array([ [None] * len(teager_array[0]) ] * (len(teager_array) - 2 * teager_spread))
    for row in range(len(teager_array)):
        if (row > teager_spread - 1 and row < len(teager_array) - teager_spread):
            i = teager_array[row][:] * teager_array[row][:]
            j = teager_array[row + teager_spread][:] * teager_array[row - teager_spread][:]
            temp_array[row - teager_spread] = i - j
    return temp_array

# 45/225 Degree Diagonal Teager
def diagonal_teager_right(teager_array, teager_spread: int):
    temp_array = numpy.array([ [None] * (len(teager_array[0]) - 2 * teager_spread) ] * (len(teager_array) - 2 * teager_spread))
    for row in range(len(teager_array)):
        if (row > teager_spread - 1 and row < len(teager_array) - teager_spread):
            i = teager_array[row][teager_spread:-teager_spread] * teager_array[row][teager_spread:-teager_spread]
            j = teager_array[row - teager_spread][(teager_spread - 1):(-teager_spread - 1)] * teager_array[row + teager_spread][(teager_spread + 1):None if (-teager_spread + 1) == 0 else (-teager_spread + 1)]
            temp_array[row - teager_spread] = i - j
    return temp_array

# 135/315 Degree Diagonal Teager
def diagonal_teager_left(teager_array, teager_spread: int): 
    temp_array = numpy.array([ [None] * (len(teager_array[0]) - 2 * teager_spread) ] * (len(teager_array) - 2 * teager_spread))
    for row in range(len(teager_array)):
        if (row > teager_spread - 1 and row < len(teager_array) - teager_spread):
            i = teager_array[row][teager_spread:-teager_spread] * teager_array[row][teager_spread:-teager_spread]
            j = teager_array[row + teager_spread][(teager_spread - 1):(-teager_spread - 1)] * teager_array[row - teager_spread][(teager_spread + 1):None if (-teager_spread + 1) == 0 else (-teager_spread + 1)]
            temp_array[row - teager_spread] = i - j
    return temp_array
    
</pre>

**NOTICE**: <br />
This is the updated import statement for the Teager package:<br />
**from teager_py import Teager**

1D Horizontal             |  2D Horizontal
:-------------------------:|:-------------------------:
<img src = "https://user-images.githubusercontent.com/25447440/50270913-ba119d00-03f8-11e9-9e71-254b43f41698.png" width = "500">  |  <img src = "https://user-images.githubusercontent.com/25447440/50315450-7eb6b300-0478-11e9-8704-28dbd015eaf8.png" width = "500">

2D Vertical             |  2D Horizontal and Vertical
:-------------------------:|:-------------------------:
<img src = "https://user-images.githubusercontent.com/25447440/50316686-4796d080-047d-11e9-8161-b0520e2639c0.png" width = "500">  | <img src="https://user-images.githubusercontent.com/25447440/50317339-af9ae600-0480-11e9-96ae-e3aac917a8eb.png" width = "500">

**NOTICE**: <br />
This is the updated import statement for the Teager package:<br />
**from teager_py import Teager**

2D Diagonal-Left             |  2D Diagonal-Right
:-------------------------:|:-------------------------:           
<img src = "https://user-images.githubusercontent.com/25447440/50316742-9d6b7880-047d-11e9-85e6-7baefd1521a3.png" width = "500"> | <img src = "https://user-images.githubusercontent.com/25447440/50316718-74e37e80-047d-11e9-807c-9a2a1350ed06.png" width = "500">

**NOTICE**: <br />
This is the updated import statement for the Teager package:<br />
**from teager_py import Teager**

2D Diagonal-Left and Diagonal-Right            |  Teager_One_Spread and Teager_Two_Spread = 2
:-------------------------:|:-------------------------:           
<img src = "https://user-images.githubusercontent.com/25447440/50317942-e7575d00-0483-11e9-96a0-b27f6e3f9d77.png" width = "500"> | <img src = "https://user-images.githubusercontent.com/25447440/50318085-a875d700-0484-11e9-96de-f7235b4649cf.png" width = "500">

