class Solution:
    def average(salary: list[int]) -> float:
        salary.sort()
        print(f"sorted:{salary} {salary[1:-1]} {len(salary[1:-1])}")
        return sum(salary[1:-1]) / len(salary[1:-1])

salary = [4000,3000,1000,2000]
assert Solution.average(salary) == 2500.00000

salary = [1000,2000,3000]
assert Solution.average(salary) == 2000.00000