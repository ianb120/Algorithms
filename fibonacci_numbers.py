def get_fib_num_seq(n):
    """
    function uses recursion to get a fibonacci based on the param int passed in.
    """
    if n <= 1:
        return n
    else:
        return get_fib_num_seq(n - 1) + get_fib_num_seq(n - 2)

def display_fib_num_seq(n):
  """
  function returns a list of fibonacci numbers based on the param int passed in.
  """
    list = []
    for num in range(0, n):
        list = list + [get_fib_num_seq(num)]
    return list

# ask user to select the total number of fibonacci numbers and print to the screen
usr_input = input("Select the total number of Fibonacci numbers to display: ")
total_fib_num_display = int(usr_input)
list_fib_nums = display_fib_num_seq(total_fib_num_display)
print(list_fib_nums)

# assert that the fibonacci sequence is correct
for fib in range(0, len(list_fib_nums)):
    if fib > 1:
        expected_fib_num = list_fib_nums[fib - 1] + list_fib_nums[fib - 2]
        assert expected_fib_num == list_fib_nums[fib], f'Fibonacci Number is wrong, expected: {expected_fib_num} but got: {list_fib_nums[fib]}'
