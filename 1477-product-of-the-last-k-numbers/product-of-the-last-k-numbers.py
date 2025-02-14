class ProductOfNumbers:
    def __init__(self):
        self.prefix_products = [1]  # Initialize with 1 to handle division

    def add(self, num: int) -> None:
        if num == 0:
            self.prefix_products = [1]  # Reset on zero
        else:
            self.prefix_products.append(self.prefix_products[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.prefix_products):  # If k exceeds available product range, means a 0 was encountered
            return 0
        return self.prefix_products[-1] // self.prefix_products[-(k + 1)]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)