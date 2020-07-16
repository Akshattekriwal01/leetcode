class Solution:
	def canArrange(self, arr: List[int], k: int) -> bool:
		counts = [0] * k
		for x in arr:
			counts[x % k] += 1
		if counts[0] % 2 == 1:
			return False
		for i in range(1, k // 2 + 1):
			if counts[i] != counts[k - i]:
				return False
		return True