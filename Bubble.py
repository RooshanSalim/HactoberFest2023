def bubble_sort(array):
  """Sorts an array using the bubble sort algorithm.

  Args:
    array: A list of elements to be sorted.

  Returns:
    A sorted list of elements.
  """
  # Iterate over the array multiple times, swapping adjacent elements if they are
  # in the wrong order.
  for i in range(len(array) - 1):
    for j in range(len(array) - i - 1):
      if array[j] > array[j + 1]:
        # Swap the elements.
        array[j], array[j + 1] = array[j + 1], array[j]

  # Return the sorted array.
  return array


# Example usage:

array = [5, 3, 8, 6, 7, 2]

# Sort the array using the bubble sort algorithm.
sorted_array = bubble_sort(array)

# Print the sorted array.
print(sorted_array)
