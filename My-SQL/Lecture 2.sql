select first_name, last_name
from patients
where allergies is null;

select allergies from patients;

select first_name
from patients
where first_name like "C%";

select first_name, last_name
from patients
where weight >= 100 and weight <= 120;

select first_name, last_name
from patients
where weight between 100 and 120;

update patients
SET allergies = "NKA"
where allergies is null;

select concat(first_name, " ", last_name) as full_name
from patients;

select first_name, last_name, province_name
from patients
JOIN province_names
ON patients.province_id = province_names.province_id;


select count(patient_id) as total_patients
from patients
where birth_date like "2010%";

select birth_date from patients;


select first_name, last_name, height
from patients WHERE height = 
(select MAX(HEIGHT) FROM patients);


select * from patients where patient_id IN
(1, 45, 534, 879, 1000);

select count(patient_id) as total_admissions from admissions;

select * from admissions
where
admission_date = discharge_date;

select patient_id, count(patient_id) as total_admissions
from admissions
where patient_id = 579;

select distinct(city) as unique_cities
from patients
where province_id = 'NS';

select first_name, last_name, birth_date
from patients
where height > 160 and weight > 70;

select first_name, last_name, allergies
from patients where
allergies is not null and city = "Hamilton";

