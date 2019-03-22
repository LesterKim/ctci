class CallCenter:
	def __init__(self, employees):
		self.employees = employees

	def list_employees(self):
		employees = self.employees

		for employee_type in employees:
			staffnums = [str(employee.staffnum) for employee in employees[employee_type]]
			staffnums = ' '.join(staffnums)
			print(employee_type + ' ' + staffnums)

	def dispatch_call(self, complexity):
		employees = self.employees
		handled = False

		for employee_type in employees:
			for employee in employees[employee_type]:
				if employee.capability < complexity:
					print("Escalating from %s" % employee_type)
					break
				elif employee.is_free:
					employee.take_call()
					handled = True
					print("Call served by %s %i" % (employee_type, employee.staffnum))
					break
				print("Moving to next employee")
			
			if handled: break

			print("All %ss unable to handle call" % employee_type)

		if not handled:
			print('Call not handled')

class Employee:
	def __init__(self, staffnum, capability, is_free=True):
		self.staffnum = staffnum
		self.capability = capability
		self.is_free = is_free

	def take_call(self):
		self.is_free = False

	def end_call(self):
		self.is_free = True


class Respondent(Employee):
	def __init__(self, staffnum):
		Employee.__init__(self, staffnum, 1)

class Manager(Employee):
	def __init__(self, staffnum):
		Employee.__init__(self, staffnum, 2)

class Director(Employee):
	def __init__(self, staffnum):
		Employee.__init__(self, staffnum, 3)

employees = {
	'respondent': [Respondent(100), Respondent(101)],
	'manager': [Manager(200), Manager(201)],
	'director': [Director(300), Director(301)]
}

call_center = CallCenter(employees)

call_center.dispatch_call(1)
call_center.dispatch_call(2)
call_center.dispatch_call(3)
call_center.dispatch_call(1)
call_center.dispatch_call(1)
call_center.dispatch_call(1)
call_center.dispatch_call(1)
call_center.dispatch_call(1)
call_center.dispatch_call(1)