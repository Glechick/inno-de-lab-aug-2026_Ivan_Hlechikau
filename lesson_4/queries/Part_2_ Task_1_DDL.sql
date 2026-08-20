-- Create
--create table Departments (
--    DepartmentID Serial primary key,
--    DepartmentName VARCHAR(50) unique not null,
--    location VARCHAR(50)
--);

-- Alter
--alter table employees add column Email VARCHAR(50);

-- Update
--update employees
--set Email = Lower(firstname || '.' || lastname || '@company.com');

-- Alter constraint
--alter table employees
--add constraint UQ_Email unique (Email);

-- Alter rename
--alter table departments
--rename column location to OfficeLocation;

select *
from departments d;