class UniqueInt:
    @staticmethod
    def processFile(input_file_path, output_file_path):
        """
        Reads an input file, finds the unique integers, and writes the results to an output file.

        Args:
            input_file_path (str): The path to the input file.
            output_file_path (str): The path to the output file.
        """
        unique_integers = UniqueInt.findUniqueIntegers(input_file_path)
        UniqueInt.writeUniqueIntegers(output_file_path, unique_integers)

    @staticmethod
    def findUniqueIntegers(input_file_path):
        """
        Reads the input file and finds the unique integers.

        Args:
            input_file_path (str): The path to the input file.

        Returns:
            list: A list of unique integers.
        """
        unique_integers = []
        unique_counts = {}
        with open(input_file_path, 'r') as input_file:
            for line in input_file:
                integer = UniqueInt.readNextItemFromFile(line.strip())
                if integer is not None:
                    if integer not in unique_counts:
                        UniqueInt.addUniqueInteger(unique_integers, unique_counts, integer)
                    else:
                        unique_counts[integer] += 1
        UniqueInt.iterativeQuicksort(unique_integers, 0, len(unique_integers) - 1)
        return unique_integers

    @staticmethod
    def addUniqueInteger(unique_integers, unique_counts, integer):
        """
        Adds a unique integer to the list of unique integers in the correct position to maintain increasing order.

        Args:
            unique_integers (list): The list of unique integers.
            unique_counts (dict): A dictionary to keep track of the count of each unique integer.
            integer (int): The integer to add.
        """
        left, right = 0, len(unique_integers) - 1
        while left <= right:
            mid = (left + right) // 2
            if unique_integers[mid] == integer:
                return
            elif unique_integers[mid] < integer:
                left = mid + 1
            else:
                right = mid - 1
        unique_integers.insert(left, integer)
        unique_counts[integer] = 1

    @staticmethod
    def contains(lst, item):
        """
        Checks if an item is present in a list.

        Args:
            lst (list): The list to search.
            item: The item to search for.

        Returns:
            bool: True if the item is in the list, False otherwise.
        """
        return item in lst

    @staticmethod
    def iterativeQuicksort(lst, left, right):
        """
        Sorts a list of integers in increasing order using the Quicksort algorithm (iterative implementation).

        Args:
            lst (list): The list to sort.
            left (int): The left index of the sublist to sort.
            right (int): The right index of the sublist to sort.
        """
        stack = [(left, right)]
        while stack:
            low, high = stack.pop()
            if low < high:
                pivot = UniqueInt.partition(lst, low, high)
                stack.append((low, pivot - 1))
                stack.append((pivot + 1, high))

    @staticmethod
    def partition(lst, left, right):
        """
        Partitions a list around a pivot element for the Quicksort algorithm.

        Args:
            lst (list): The list to partition.
            left (int): The left index of the sublist to partition.
            right (int): The right index of the sublist to partition.

        Returns:
            int: The index of the pivot element.
        """
        pivot = lst[right]
        i = left - 1
        for j in range(left, right):
            if lst[j] < pivot:
                i += 1
                lst[i], lst[j] = lst[j], lst[i]
        lst[i + 1], lst[right] = lst[right], lst[i + 1]
        return i + 1

    @staticmethod
    def writeUniqueIntegers(output_file_path, unique_integers):
        """
        Writes the unique integers to the output file.

        Args:
            output_file_path (str): The path to the output file.
            unique_integers (list): A list of unique integers.
        """
        with open(output_file_path, 'w') as output_file:
            for integer in unique_integers:
                output_file.write(str(integer) + '\n')

    @staticmethod
    def readNextItemFromFile(line):
        """
        Reads the next integer from the input file line.

        Args:
            line (str): The input file line.

        Returns:
            int or None: The integer value from the line,
            or None if the line is empty or contains non-integer characters.
        """
        try:
            return int(line)
        except ValueError:
            # Skip lines with non-integer values
            return None


# Example usage
UniqueInt.processFile('hw01/sample_inputs/sample_03.txt', 'hw01/sample_results/sample_input_03.txt_results.txt')
