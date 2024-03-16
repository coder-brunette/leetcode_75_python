# Given an array of characters chars, compress it using the following algorithm:
# Begin with an empty string s. For each group of consecutive repeating characters in chars:

# If the group's length is 1, append the character to s.
# Otherwise, append the character followed by the group's length.
# The compressed string s should not be returned separately, but instead, be stored in the input character array chars. 
# Note that group lengths that are 10 or longer will be split into multiple characters in chars.

# After you are done modifying the input array, return the new length of the array.
# You must write an algorithm that uses only constant extra space.

class Solution:
    def compress(self, chars: List[str]) -> int:
        write_index = 0
        read_index = 0
        
        while read_index < len(chars):
            current_char = chars[read_index]
            count = 0
            
            while read_index < len(chars) and chars[read_index] == current_char:
                read_index += 1
                count += 1
            
            chars[write_index] = current_char
            write_index += 1
            
            if count > 1:
                count_str = str(count)
                for digit in count_str:
                    chars[write_index] = digit
                    write_index += 1
        
        return write_index