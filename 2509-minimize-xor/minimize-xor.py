class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        target_bits = bin(num2).count('1')
        
        # Initialize result and track how many bits we've set
        x = 0
        bits_set = 0
        
        # First phase: Try to match bits with num1 from most significant to least
        # This ensures minimal XOR since matching bits will give 0 in XOR
        for i in range(31, -1, -1):  # 32-bit integer
            if bits_set < target_bits and (num1 & (1 << i)):
                # If we still need more bits and this bit is set in num1,
                # set it in our answer
                x |= (1 << i)
                bits_set += 1
        
        # Second phase: If we still need more bits, add them from right to left
        # This ensures the smallest possible number if we need additional bits
        if bits_set < target_bits:
            for i in range(32):  # Start from least significant bit
                if bits_set >= target_bits:
                    break
                if not (x & (1 << i)):  # If this bit isn't set yet
                    x |= (1 << i)  # Set it
                    bits_set += 1
        
        return x