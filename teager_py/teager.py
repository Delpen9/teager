import numpy as numpy

# Crop 2D Arrays
def crop_center(teager_array, cropx, cropy):
    y,x = teager_array.shape
    startx = x//2 - cropx//2
    starty = y//2 - cropy//2
    return teager_array[starty:(starty + cropy), startx:(startx + cropx)]


# Find Minimum for Crop
def minimum_crop(temp_array_one, temp_array_two):
    one_y, one_x = temp_array_one.shape
    two_y, two_x = temp_array_two.shape
    minimum_shape_value = min(one_y, one_x, two_y, two_x)
    return minimum_shape_value

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


# The Teager Operator
def Teager(teager_array, teager_angle_one: str, teager_one_spread: int, teager_angle_two: str = None, teager_two_spread: int = None, *positional_parameters, **keyword_parameters):
    try:
        if (type(teager_array) is not list and type(teager_array) is not numpy.ndarray):
            raise Exception("Your teager array must be of type 'list' or 'numpy.ndarray'.")
    except TypeError:
	    raise

    # np.array teager_array
    else:
        if (type(teager_array) is list):
            teager_array = numpy.array(teager_array)

        # 1 dimensional np.array
        if (len(teager_array.shape) == 1):
            try: 
                if (type(teager_array[0]) != numpy.int64):
                    raise Exception("Each row in your teager array must be of equal length.")
            except Exception:
                raise

            try:
                if (len(teager_array) < teager_one_spread * 2 + 1):
                    raise Exception("The rows of your teager array are insufficiently large. Each row must be of length", teager_one_spread * 2 + 1, "or more when your teager_angle_one is horizontal with a teager_angle_spread of ", teager_one_spread, ".")
            except ValueError:
                raise
            
            try:
                if (teager_angle_one.lower() != 'horizontal'):
                    raise Exception("When your teager array is one dimensional, your teager_angle_one must be 'horizontal'.")
            except ValueError:
                raise

            try:
                if (teager_one_spread == None or teager_one_spread < 1):
                    raise Exception("The spread is outside the acceptable range of 1 or more pixels. The teager_two_spread value should be 1 or greater if you're using a teager_angle_two.")
            except ValueError:
                raise

            try:
                if (type(teager_one_spread) != int):
                    raise Exception("Your teager_one_spread is not of type: int.")
            except TypeError:
                raise
            
            try:
                if(teager_angle_two != None):
                    raise Exception("When your teager array is one dimensional, you cannot have a teager_angle_two.")
            except TypeError:
                raise

            try:
                if(teager_two_spread != None):
                    raise Exception("When your teager array is one dimensional, you cannot have a teager_spread_two.")
            except TypeError:
                raise

            temp_array = horizontal_teager(teager_array, teager_one_spread, '1D')
            return temp_array.astype('float')

        # 2 dimensional np.array
        elif (len(teager_array.shape) == 2):
            if (teager_angle_two == None):
                try:
                    if (len(teager_array[0]) < teager_one_spread * 2 + 1):
                        raise Exception("The rows of your teager array are insufficiently large. Each row must be of length", teager_one_spread * 2 + 1, "or more when your teager_angle_one is horizontal with a teager_angle_spread of", teager_one_spread, ".")
                except ValueError:
                    raise

                try:
                    if (type(teager_angle_one) != str):
                        raise Exception("Your teager_angle_one must be of type: str.")
                except:
                    raise

                try:
                    if (type(teager_one_spread) != int):
                        raise Exception("Your teager_one_spread must be of type: int.")
                except:
                    raise

                try:
                    if (teager_two_spread != None):
                        raise Exception("If you do not have a teager_angle_two then you cannot have a teager_two_spread.")
                except TypeError:
                    raise

                if (teager_angle_one.lower() == 'horizontal'):
                    temp_array = horizontal_teager(teager_array, teager_one_spread, '2D')
                    return temp_array.astype('float')

                elif (teager_angle_one.lower() == 'vertical'): 
                    temp_array = vertical_teager(teager_array, teager_one_spread)
                    return temp_array.astype('float')

                elif (teager_angle_one.lower() == 'diagonal-right'): 
                    temp_array = diagonal_teager_right(teager_array, teager_one_spread)
                    return temp_array.astype('float')

                elif (teager_angle_one.lower() == 'diagonal-left'): 
                    temp_array = diagonal_teager_left(teager_array, teager_one_spread)
                    return temp_array.astype('float')

                else:
                    try:
                        raise Exception("Your teager_angle_one must be a valid input of: 'horizontal', 'vertical', 'diagonal-right', or 'diagonal-left'.")
                    except:
                        raise

            else:
                try:
                    if (teager_angle_one == None):
                        raise Exception("If you have a teager_angle_two, then you must have a teager_angle_one.")
                except TypeError:
                    raise

                try:
                    if (type(teager_angle_one) != str):
                        raise Exception("Your teager_angle_one must be of type: str.")
                except TypeError:
                    raise

                try:
                    if (teager_angle_one.lower() not in ['horizontal', 'vertical', 'diagonal-right', 'diagonal-left']):
                        raise Exception("Your teager_angle_one must be a valid input of: 'horizontal', 'vertical', 'diagonal-right', or 'diagonal-left'.")
                except ValueError:
                    raise

                try:
                    if (teager_one_spread == None or teager_one_spread < 1):
                        raise Exception("Your teager_one_spread spread is outside the acceptable range of 1 or more pixels. The teager_one_spread value should be 1 or greater if you're using a teager_angle_one.")
                except ValueError:
                    raise

                try:
                    if (type(teager_angle_two) != str):
                        raise Exception("Your teager_angle_two must be of type: str.")
                except TypeError:
                    raise

                try:
                    if (teager_angle_two.lower() not in ['horizontal', 'vertical', 'diagonal-right', 'diagonal-left']):
                        raise Exception("Your teager_angle_two must be a valid input of: 'horizontal', 'vertical', 'diagonal-right', or 'diagonal-left'.")
                except ValueError:
                    raise

                try:
                    if (teager_two_spread == None or teager_two_spread < 1):
                        raise Exception("Your teager_two_spread is outside the acceptable range of 1 or more pixels. The teager_two_spread value should be 1 or greater if you're using a teager_angle_two.")
                except ValueError:
                    raise

                if (teager_angle_one.lower() == 'horizontal' and teager_angle_two.lower() == 'vertical' or teager_angle_one.lower() == 'vertical' and teager_angle_two.lower() == 'horizontal'):
                    temp_array_one = horizontal_teager(teager_array, teager_one_spread, '2D')
                    temp_array_two = vertical_teager(teager_array, teager_two_spread)

                    minimum_shape_value = minimum_crop(temp_array_one, temp_array_two)

                    temp_array_one = crop_center(temp_array_one, minimum_shape_value, minimum_shape_value)
                    temp_array_two = crop_center(temp_array_two, minimum_shape_value, minimum_shape_value)

                    return (temp_array_one + temp_array_two).astype('float')
                
                elif(teager_angle_one.lower() == 'horizontal' and teager_angle_two.lower() == 'diagonal-right' or teager_angle_one.lower() == 'diagonal-right' and teager_angle_two.lower() == 'horizontal'):
                    temp_array_one = horizontal_teager(teager_array, teager_one_spread, '2D')
                    temp_array_two = diagonal_teager_right(teager_array, teager_two_spread)

                    minimum_shape_value = minimum_crop(temp_array_one, temp_array_two)

                    temp_array_one = crop_center(temp_array_one, minimum_shape_value, minimum_shape_value)
                    temp_array_two = crop_center(temp_array_two, minimum_shape_value, minimum_shape_value)

                    return (temp_array_one + temp_array_two).astype('float')

                elif(teager_angle_one.lower() == 'horizontal' and teager_angle_two.lower() == 'diagonal-left' or teager_angle_one.lower() == 'diagonal-left' and teager_angle_two.lower() == 'horizontal'):
                    temp_array_one = horizontal_teager(teager_array, teager_one_spread, '2D')
                    temp_array_two = diagonal_teager_left(teager_array, teager_two_spread)

                    minimum_shape_value = minimum_crop(temp_array_one, temp_array_two)

                    temp_array_one = crop_center(temp_array_one, minimum_shape_value, minimum_shape_value)
                    temp_array_two = crop_center(temp_array_two, minimum_shape_value, minimum_shape_value)

                    return (temp_array_one + temp_array_two).astype('float')

                elif(teager_angle_one.lower() == 'vertical' and teager_angle_two.lower() == 'diagonal-right' or teager_angle_one.lower() == 'diagonal-right' and teager_angle_two.lower() == 'vertical'):
                    temp_array_one = vertical_teager(teager_array, teager_one_spread)
                    temp_array_two = diagonal_teager_right(teager_array, teager_two_spread)   

                    minimum_shape_value = minimum_crop(temp_array_one, temp_array_two)

                    temp_array_one = crop_center(temp_array_one, minimum_shape_value, minimum_shape_value)
                    temp_array_two = crop_center(temp_array_two, minimum_shape_value, minimum_shape_value)

                    return (temp_array_one + temp_array_two).astype('float')

                elif(teager_angle_one.lower() == 'vertical' and teager_angle_two.lower() == 'diagonal-left' or teager_angle_one.lower() == 'diagonal-left' and teager_angle_two.lower() == 'vertical'):
                    temp_array_one = vertical_teager(teager_array, teager_one_spread)
                    temp_array_two = diagonal_teager_left(teager_array, teager_two_spread)

                    minimum_shape_value = minimum_crop(temp_array_one, temp_array_two)

                    temp_array_one = crop_center(temp_array_one, minimum_shape_value, minimum_shape_value)
                    temp_array_two = crop_center(temp_array_two, minimum_shape_value, minimum_shape_value)

                    return (temp_array_one + temp_array_two).astype('float')

                elif(teager_angle_one.lower() == 'diagonal-right' and teager_angle_two.lower() == 'diagonal-left' or teager_angle_one.lower() == 'diagonal-left' and teager_angle_two.lower() == 'diagonal-right'):
                    temp_array_one = diagonal_teager_right(teager_array, teager_one_spread)                    
                    temp_array_two = diagonal_teager_left(teager_array, teager_two_spread)

                    minimum_shape_value = minimum_crop(temp_array_one, temp_array_two)

                    temp_array_one = crop_center(temp_array_one, minimum_shape_value, minimum_shape_value)
                    temp_array_two = crop_center(temp_array_two, minimum_shape_value, minimum_shape_value)
                    
                    return (temp_array_one + temp_array_two).astype('float')

        else:
            try:
                raise Exception("Lower the dimensions of your Teager array to be of 1 or 2 dimensions.")
            except TypeError:
                raise

    try:
        raise Exception("There was no output from your operation.")
    except IOError:
        raise
