--List the following details of each employee: employee number, last name, first name, sex, and salary.
SELECT
	e.emp_no,
	e.first_name,
	e.last_name,
	e.sex,
	s.salary
	
FROM
	employees e
JOIN
	salaries s
ON e.emp_no = s.emp_no;


--List first name, last name, and hire date for employees who were hired in 1986.

SELECT 
	e.first_name,
	e.last_name,
	e.hire_date
	
FROM
	employees e
WHERE extract (year from e.hire_date) = 1986;
	
--List the manager of each department with the following information: department number, department name, the manager's employee number, last name, first name.
SELECT
	d.dept_no,
	d.dept_name,
	dm.emp_no,
	e.first_name,
	e.last_name
	
	
FROM dept_manager dm
INNER JOIN departments d on dm.dept_no = d.dept_no
INNER JOIN employees e on dm.emp_no=e.emp_no;
	

--List the department of each employee with the following information: employee number, last name, first name, and department name.

SELECT
	e.emp_no,
	e.first_name,
	e.last_name,
	d.dept_name
	
	
FROM employees e
INNER JOIN dept_emp de on e.emp_no = de.emp_no
INNER JOIN departments d on d.dept_no=de.dept_no;

--List first name, last name, and sex for employees whose first name is "Hercules" and last names begin with "B."

SELECT
	e.first_name,
	e.last_name,
	e.sex
FROM employees e
WHERE e.first_name = 'Hercules'
	and e.last_name like 'B%';


--List all employees in the Sales department, including their employee number, last name, first name, and department name.

SELECT
	e.emp_no,
	e.first_name,
	e.last_name,
	d.dept_name
	
	
FROM employees e
INNER JOIN dept_emp de on e.emp_no = de.emp_no
INNER JOIN departments d on d.dept_no=de.dept_no
WHERE d.dept_name = 'Sales';
	

--List all employees in the Sales and Development departments, including their employee number, last name, first name, and department name.
SELECT
	e.emp_no,
	e.first_name,
	e.last_name,
	d.dept_name
	
	
FROM employees e
INNER JOIN dept_emp de on e.emp_no = de.emp_no
INNER JOIN departments d on d.dept_no=de.dept_no
WHERE d.dept_name = 'Sales'
	or d.dept_name = 'Development';

--List the frequency count of employee last names (i.e., how many employees share each last name) in descending order.
SELECT
	e.last_name, count(*) as sum
	
FROM employees e
GROUP BY e.last_name 
ORDER BY e.last_name desc;




