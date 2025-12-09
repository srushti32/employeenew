from employee import employee_details

def test_employee_details():
    expected_output = (
        "Employee Name: bhagyashree\n"
        "Employee ID: 292\n"
        "Department: IT\n"
        "Salary: 50000"
    )

    assert employee_details("bhagyashree", "292", "IT", 50000) == expected_output
