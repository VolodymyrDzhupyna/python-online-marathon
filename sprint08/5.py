import unittest


class Worker:
    
    def __init__(self, name, salary = 0.0):
        self.name = name
        self.salary = salary
        if self.salary < 0:
            raise ValueError

    def get_tax_value(self):
        if self.salary <= 1000:
            return self.salary * 0.0
        elif 1000 <= self.salary <= 3000:
            tax = 0.1 * (self.salary - 1000)
            return tax
        elif 3000 <= self.salary <= 5000:
            tax = (0.1 * (3000 - 1000)) + (0.15 * (self.salary - 3000))
            return tax
        elif 5005 <= self.salary <= 10000:
            tax = (0.1 * (3000 - 1000)) + (0.15 * (5000 - 3000)) + (0.21 * (self.salary - 5000))
            return tax
        elif 10000 <= self.salary <= 20000:
            tax = ((0.1 * (3000 - 1000)) + (0.15 * (5000 - 3000)) + (0.21 * (10000 - 5000)) 
                    + (0.3 * (self.salary - 10000)))
            return tax
        elif 20000 <= self.salary <= 50000:
            tax = ((0.1 * (3000 - 1000)) + (0.15 * (5000 - 3000)) + (0.21 * (10000 - 5000)) 
                    + (0.3 * (20000 - 10000)) + (0.4 * (self.salary - 20000)))
            return tax
        elif self.salary > 50000:
            tax = ((0.1 * (3000 - 1000)) + (0.15 * (5000 - 3000)) + (0.21 * (10000 - 5000)) 
                    + (0.3 * (20000 - 10000)) + (0.4 * (50000 - 20000)) + (0.47 * (self.salary - 50000)))
            return tax


class WorkerTest(unittest.TestCase):

    def setUp(self):
        self.worker = Worker("Natasha", 1001)
        self.worker2 = Worker("Vasia", 500)

    @unittest.expectedFailure
    def test_get_tax_value(self):
        self.assertEqual(self.worker.get_tax_value(), 0.2)
    
    def test_get_tax_value_return_zero(self):
        self.assertEqual(self.worker2.get_tax_value(), 0.0)

    def tearDown(self):
        self.worker = None
        self.worker2 = None



worker = Worker("Petia", 500)
print(worker.get_tax_value())

worker1 = Worker("Natasha", 1001)
print(worker1.get_tax_value())

worker2 = Worker("Vika", 100000)
print(worker2.get_tax_value())
